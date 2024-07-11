"""Module to Store Data From the CSV files into data Structures and Handle the Parsed Commands"""

import os
import csv
from daily_weather_data import WeatherDataRow


class WeatherData:
    """Class containing 2 class variables (lists) to use .
    Contains attributes for file path , year to display and the month for each object
    Contains a method to load monthly and yearly data
    Contains an internal function which cuts out useless columns from the Monthly_weather dictionary and yearly_weather dictionaries
    """

    columns_to_keep = [
        "PKT",
        "Max TemperatureC",
        "Mean TemperatureC",
        "Min TemperatureC",
        "Max Humidity",
        " Mean Humidity",
    ]
    months_list = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec",
    ]

    def __init__(self, parser_file_path, year, month):
        """initialize function to store attributes affter instantiation of a class"""

        self.parser_file_path = parser_file_path
        self.year = year
        self.month = month

    def load_data(self, month=None):
        """Load data for a specific month or all months if month is None."""
        if month is not None:
            # Load data for a specific month
            if month < 1 or month > 12:
                raise ValueError("Invalid month value. Month must be between 1 and 12.")
            file_path = os.path.join(
                self.parser_file_path,
                f"Murree_weather_{self.year}_{WeatherData.months_list[month - 1]}.txt",
            )
            return self.load_data_from_file(file_path)
        else:
            # Load data for all months in the year
            yearly_data = []
            for month_index in range(1, 13):
                file_path = os.path.join(
                    self.parser_file_path,
                    f"Murree_weather_{self.year}_{WeatherData.months_list[month_index - 1]}.txt",
                )
                try:
                    monthly_data = self.load_data_from_file(file_path)
                    yearly_data.append(monthly_data)
                except FileNotFoundError as e:
                    print(f"Error loading data for month {month_index}: {e}")

            return yearly_data
        
        
    def load_data_from_file(self, file_path):
        """Internal method to load data from a file."""
        try:
            with open(file_path, "r") as csv_file:
                return self.column_cutting(csv_file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Invalid month or year entered: {e}")




    def column_cutting(self, csv_file):

        csv_reader = csv.DictReader(csv_file)
        month_data = []
        for row in csv_reader:
            my_obj = WeatherDataRow(
                pkt=row.get("PKT"),
                max_temp=row.get("Max TemperatureC"),
                mean_temp=row.get("Mean TemperatureC"),
                min_temp=row.get("Min TemperatureC"),
                max_humidity=row.get("Max Humidity"),
                mean_humidity=row.get("Mean Humidity")

            )
            month_data.append(my_obj)

        return month_data
