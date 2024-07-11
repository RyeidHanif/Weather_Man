import os
import csv








class Weather_Data:

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

    def __init__(self, parser_file_path, year, month = None):
        self.parser_file_path = parser_file_path
        self.year = year
        self.month = month
       
    def load_data(self):
        if self.month :
            return self.load_monthly_data()
        else : 
            return self.load_yearly_data

    def load_monthly_data(self):
        file_path = os.path.join(
            self.parser_file_path,
            f"Murree_weather_{self.year}_{Weather_Data.months_list[int(self.month) - 1]}.txt",
        )

        try:
            with open(file_path, "r") as csv_file:
                weather_data = self.column_cutting(csv_file)

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Invalid month or year entered: {e}")

        return weather_data

    def load_yearly_data(self):
        yearly_data = []

        for month in Weather_Data.months_list:
            file_path = os.path.join(
                self.parser_file_path, f"Murree_weather_{self.year}_{month}.txt"
            )

            try:
                with open(file_path, "r") as csv_file:
                    month_data = self.column_cutting(csv_file)
                    yearly_data.append(month_data)

            except FileNotFoundError:
                continue

        return yearly_data

    def column_cutting(self, csv_file):
        csv_reader = csv.DictReader(csv_file)
        month_data = {col: [] for col in Weather_Data.columns_to_keep}
        for row in csv_reader:
            for col in Weather_Data.columns_to_keep:
                if col in row :
                    month_data[col].append(row[col])
                else : 
                    continue
                
        return month_data
