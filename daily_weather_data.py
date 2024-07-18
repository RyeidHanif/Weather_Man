"""Module for a class whose objects contain values for the weather and are added into a list to be computed and Visualized """

import datetime


class WeatherDataRow:
    def __init__(self, pkt, max_temp, mean_temp, min_temp, max_humidity, mean_humidity):
        self.pkt = pkt
        self.max_temp = self.validate_value(max_temp, -100, 100, "temperature")
        self.mean_temp = self.validate_value(mean_temp, -100, 100, "temperature")
        self.min_temp = self.validate_value(min_temp, -100, 100, "temperature")
        self.max_humidity = self.validate_value(max_humidity, 0, 100, "humidity")
        self.mean_humidity = self.validate_value(mean_humidity, 0, 100, "humidity")

    def strip_date(self):
        """Strips the date into correct format and returns the day, month, and year."""

        if self.pkt is not None:
            date_refined = datetime.datetime.strptime(self.pkt , "%Y-%m-%d")
            date_day = date_refined.strftime("%d")
            date_month = date_refined.strftime("%B")
            date_year = date_refined.strftime("%Y")
            return date_day, date_month, date_year
        else:
            return None, None, None
    
    def validate_value(self, value, min_range, max_range, value_type):
        """
        This Internal function is to validatte the data for humidity and temperature 
        it checks whether the data is present , whether it is None and whether it is within the ranges specified in the parameters 
        The parameters include ranges and type to combine humidity and temperature validation 
        Returns the an integer value if Validated , otherwise will return None.
        """
        if value is None or value == "":
            return None
        try:
            value = int(value)
            if min_range <= value <= max_range:
                return value
            else:
                print(f" value {value} is out of range.")
                return None
        except ValueError:
            print(f"Invalid {value_type} value: {value}")
            return None
        