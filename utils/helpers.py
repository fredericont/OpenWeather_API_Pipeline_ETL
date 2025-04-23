# Funções

def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius

def get_wind_direction(degrees):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = round(degrees / (360 / 8))
    return directions[index % 8]

def meter_per_second_to_kilometer_per_hour(mps):
    kph = mps * 3.6
    return kph

def load_config(config_file):
    import json
    with open(config_file) as f:
        return json.load(f) 