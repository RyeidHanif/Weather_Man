import os
import csv


class Weather_data:

    def __init__(self, parser_file_path, year, month):
        self.parser_file_path = parser_file_path
        self.year = year
        self.month = month
        self.columns_to_keep = [
            "PKT",
            "Max TemperatureC",
            "Mean TemperatureC",
            "Min TemperatureC",
            "Max Humidity",
            " Mean Humidity",
        ]
        self.months_list = [
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

    def load_monthly_data(self):
        file_path = os.path.join(
            self.parser_file_path,
            f"Murree_weather_{self.year}_{self.months_list[int(self.month) - 1]}.txt",
        )

        try:
            with open(file_path, "r") as csv_file:
                weather_data = self.column_cutting(csv_file)

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Invalid month or year entered: {e}")

        return weather_data

    def load_yearly_data(self):
        yearly_data_dicts = []

        for month in self.months_list:
            file_path = os.path.join(
                self.parser_file_path, f"Murree_weather_{self.year}_{month}.txt"
            )

            try:
                with open(file_path, "r") as csv_file:
                    month_data = self.column_cutting(csv_file)
                    yearly_data_dicts.append(month_data)

            except FileNotFoundError:
                continue

        return yearly_data_dicts

    def column_cutting(self, csv_file):
        csv_reader = csv.DictReader(csv_file)
        month_data = {col: [] for col in self.columns_to_keep}
        for row in csv_reader:
            for col in self.columns_to_keep:
                month_data[col].append(row[col])
        return month_data
