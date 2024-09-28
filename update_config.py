import json
from datetime import datetime

def get_current_season():
    # Get the current date
    current_date = datetime.utcnow().date()

    # Define date ranges for each season
    spring_start = datetime(current_date.year, 3, 21).date()
    summer_start = datetime(current_date.year, 6, 21).date()
    fall_start = datetime(current_date.year, 9, 23).date()
    winter_start = datetime(current_date.year, 12, 21).date()

    # Determine the season based on the current date
    if current_date >= summer_start or current_date < spring_start:
        return 'summer'
    elif spring_start <= current_date < summer_start:
        return 'spring'
    elif summer_start <= current_date < fall_start:
        return 'fall'
    elif fall_start <= current_date < winter_start:
        return 'winter'
    else:
        return 'unknown'

def update_config_file(config_file):
    # Load the configuration from the file
    with open(config_file, 'r') as file:
        config = json.load(file)

    current_season = get_current_season()

    # Define thresholds for each season
    spring_thresholds = {
        "heatwave_threshold": 18,
        "coldwave_threshold": 0
    }
    summer_thresholds = {
        "heatwave_threshold": 26,
        "coldwave_threshold": 12
    }
    fall_thresholds = {
        "heatwave_threshold": 18,
        "coldwave_threshold": 8
    }
    winter_thresholds = {
        "heatwave_threshold": 13,
        "coldwave_threshold": -3
    }

    # Update thresholds based on the current season
    if current_season == 'spring':
        thresholds = spring_thresholds
    elif current_season == 'summer':
        thresholds = summer_thresholds
    elif current_season == 'fall':
        thresholds = fall_thresholds
    elif current_season == 'winter':
        thresholds = winter_thresholds
    else:
        thresholds = {}

    # Update thresholds for each city
    for city, city_data in config['city_coordinates'].items():
        city_data['thresholds'].update(thresholds)

    # Print what is updated
    print(f"Updated config file with seasonal thresholds for {current_season}:")
    print(json.dumps(thresholds, indent=4))

    # Write the updated configuration back to the file
    with open(config_file, 'w') as file:
        json.dump(config, file, indent=4)

def main():
    config_file = 'config.json'  # Update with your actual config file path
    update_config_file(config_file)
    print("Config file updated.")

if __name__ == "__main__":
    main()
