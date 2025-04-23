import json
import requests
import pandas as pd
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helpers import (
    kelvin_to_celcius,
    get_wind_direction,
    meter_per_second_to_kilometer_per_hour,
    load_config
)
from database.db_connection import execute_query

def extract_weather_data():
    secrets = load_config('../config/secrets.json')
    api_key = secrets["WEATHER_API_KEY"]

    # Coordenadas: Natal-RN
    lat = '-5.79'
    lon = '-35.21'

    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API error: {response.status_code}")

def transform_weather_data(data):
    weather_data = []
    
    for item in data['list']:
        weather = {
            'DateTime': datetime.fromtimestamp(item['dt']),
            'Temperature (ºC)': round(kelvin_to_celcius(item['main']['temp'])),
            'Feels Like (ºC)': round(kelvin_to_celcius(item['main']['feels_like'])),
            'Humidity (%)': item['main']['humidity'],
            'Weather Main': item['weather'][0]['main'],
            'Weather Description': item['weather'][0]['description'],
            'Wind Speed (km/h)': round(meter_per_second_to_kilometer_per_hour(item['wind']['speed'])),
            'Wind Direction': get_wind_direction(item['wind']['deg']),
            'Cloudiness (%)': item['clouds']['all'],
            'Rain Volume (mm)': item.get('rain', {}).get('3h', 0.00)
        }
        weather_data.append(weather)
    
    return pd.DataFrame(weather_data)

def load_weather_data(df):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather_data (
        id SERIAL PRIMARY KEY,
        datetime TIMESTAMP,
        temperature FLOAT,
        feels_like FLOAT,
        humidity INTEGER,
        weather_main VARCHAR(50),
        weather_description VARCHAR(100),
        wind_speed FLOAT,
        wind_direction VARCHAR(2),
        cloudiness INTEGER,
        rain_volume FLOAT
    );
    """
    execute_query(create_table_query)
    
    for _, row in df.iterrows():
        insert_query = """
        INSERT INTO weather_data (
            datetime, temperature, feels_like, humidity,
            weather_main, weather_description, wind_speed,
            wind_direction, cloudiness, rain_volume
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        );
        """
        params = (
            row['DateTime'], row['Temperature (ºC)'], row['Feels Like (ºC)'],
            row['Humidity (%)'], row['Weather Main'], row['Weather Description'],
            row['Wind Speed (km/h)'], row['Wind Direction'],
            row['Cloudiness (%)'], row['Rain Volume (mm)']
        )
        execute_query(insert_query, params)

def main():
    try:
        print("- Starting ETL process...")
        
        # Extract
        print("- Extracting data...")
        raw_data = extract_weather_data()
        
        # Transform
        print("- Transforming data...")
        df = transform_weather_data(raw_data)
        
        # Load
        print("- Loading data into the database...")
        load_weather_data(df)
        
        print("- ETL process completed successfully!")
        
    except Exception as e:
        print(f"Error during ETL process: {e}")

if __name__ == "__main__":
    main() 