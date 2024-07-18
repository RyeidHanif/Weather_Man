"""Module to Store Data From the CSV files into data Structures and Handle the Parsed Commands"""

import os
import csv
from daily_weather_data import WeatherDataRow


class WeatherData:
    """
    Class containing 1 class variable (list) to use  for months of the year
    Contains attributes for file path , year to display and the month for each object
    Contains a method to load monthly and yearly data
    Contains an internal function which cuts out useless columns from the Monthly_weather dictionary and yearly_weather dictionaries
    """

    months_of_the_year = [
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

    def load_data(self, month):
        """
        Load data for a specific month or all months if month is None.
        Returns a List of objects according to input of a month 
        If a month has been inputted the total data wil be of 30 to 31 objects 
        Otherwise for a yearly data , the total data will be 365 or 366 objects in a list
        """
        total_data = []
        months_to_load = self.months_of_the_year if month is None else [self.months_of_the_year[month - 1]]

        for month_name in months_to_load:
            file_path = os.path.join(
                self.parser_file_path,
                f"Murree_weather_{self.year}_{month_name}.txt"
            )
            try:
                total_data.extend(self.load_data_from_file(file_path))
            except FileNotFoundError as fe:
                continue

        return total_data

    def load_data_from_file(self, file_path):
        """Internal method to load data from a file."""

        try:
            with open(file_path, "r") as csv_file:
                return self.handle_parsed(csv_file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Invalid month or year entered: {e}")

    def handle_parsed(self, csv_file):
        """
        Returns an array of objects of month data by instantiating an instance of tthe WeatherDataRow class.
        Provides the new instance (my_obj) with values from the dictionary created by Dictreader
        """

        csv_reader = csv.DictReader(csv_file)
        month_data = []
        for row in csv_reader:
            my_obj = WeatherDataRow(
                pkt=row.get("PKT"),
                max_temp=row.get("Max TemperatureC"),
                mean_temp=row.get("Mean TemperatureC"),
                min_temp=row.get("Min TemperatureC"),
                max_humidity=row.get("Max Humidity"),
                mean_humidity=row.get(" Mean Humidity"),
            )
            month_data.append(my_obj)

        return month_data
