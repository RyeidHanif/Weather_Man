"""Module for a class whose objects contain values for the weather and are added into a list to be computed and Visualized """

import datetime


class WeatherDataRow:
    def __init__(self, pkt, max_temp, mean_temp, min_temp, max_humidity, mean_humidity):
        self.pkt = pkt
        self.max_temp = (
            int(max_temp) if max_temp is not None and max_temp != "" else None
        )
        self.mean_temp = (
            int(mean_temp) if mean_temp is not None and mean_temp != "" else None
        )
        self.min_temp = (
            int(min_temp) if min_temp is not None and min_temp != "" else None
        )
        self.max_humidity = int(max_humidity) if max_humidity else None
        self.mean_humidity = int(mean_humidity) if mean_humidity else None

    def strip_date(self, date):
        """Strips the date into correct format and returns the day, month, and year."""

        if date is not None:
            date_refined = datetime.datetime.strptime(date, "%Y-%m-%d")
            date_day = date_refined.strftime("%d")
            date_month = date_refined.strftime("%B")
            date_year = date_refined.strftime("%Y")
            return date_day, date_month, date_year
        else:
            return None, None, None
