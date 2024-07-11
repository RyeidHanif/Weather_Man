"""Module to compute the following : 
    1. Maximum and Minimum Temperature in a month
    2. Mean humidity in a month and max humidity in a year 
    3. The corresponsing dates for every value"""

import datetime


class Compute:
    """Class containing Attributes for monthly data.
    Contains a method for computing the monthly data dictionary values .
    Contains a method for computing the yearly data values from the list of dictionaries
    """

    def __init__(self, monthly_data):
        '"Initialize function , instantiation of object"'

        self.monthly_data = monthly_data

    def compute_monthly_data(self):
        """Computes and Returns 2 dictionaries for max temp , min temp and a value for the mean monthly humidity """
        max_temp_month = -100
        min_temp_month = 100
        total_monthly_humi = 0
        humi_count = 0
        for row in self.monthly_data:

            if row.max_temp is not None:

                if  row.max_temp is not None and row.max_temp > max_temp_month:
                    max_temp_month = row.max_temp
                    max_temp_month_date = row.pkt
            
            if row.min_temp is not None :

                if row.min_temp < min_temp_month:
                    min_temp_month = row.min_temp
                    min_temp_month_date = row.pkt

            if row.mean_humidity is not None :
                row.mean_humidity = int(row.mean_humidity)
                total_monthly_humi += row.mean_humidity
                humi_count +=1

        mean_humidity_month = total_monthly_humi / humi_count if humi_count > 0  else  1

        max_temp_month_day, max_temp_month_month, max_temp_month_year = self.strip_date(
            max_temp_month_date
        )
        min_temp_month_day, min_temp_month_month, min_temp_month_year = self.strip_date(
            min_temp_month_date
        )

        max_monthly = {
            "day": max_temp_month_day,
            "month": max_temp_month_month,
            "year": max_temp_month_year,
        }

        min_monthly = {
            "day": min_temp_month_day,
            "month": min_temp_month_month,
            "year": min_temp_month_year,
        }

        return max_monthly, min_monthly, mean_humidity_month

    def strip_date(self, date):
        """strips the date into correct format and returns the day , month and year ."""
        if date is not None :
            date_refined = datetime.datetime.strptime(date, "%Y-%m-%d")
            date_day = date_refined.strftime("%d")
            date_month = date_refined.strftime("%B")
            date_year = date_refined.strftime("%y")
            return date_day, date_month, date_year

    def compute_yearly_data(self, yearly_data):
        max_temp = float("-inf")
        min_temp = float("inf")
        max_humidity = float("-inf")
        max_temp_date = None
        min_temp_date = None
        max_humidity_date = None

        for monthly_data in yearly_data:
            for row in monthly_data:
                if row.max_temp is not None and isinstance(row.max_temp, (int, float)):
                    if row.max_temp > max_temp:
                        max_temp = row.max_temp
                        max_temp_date = row.pkt

                if row.min_temp is not None and isinstance(row.min_temp, (int, float)):
                    if row.min_temp < min_temp:
                        min_temp = row.min_temp
                        min_temp_date = row.pkt

                if row.mean_humidity is not None and isinstance(row.mean_humidity, (int, float)):
                    if row.mean_humidity > max_humidity:
                        max_humidity = row.mean_humidity
                        max_humidity_date = row.pkt

        max_temp_day, max_temp_month, max_temp_year = self.strip_date(max_temp_date)
        min_temp_day, min_temp_month, min_temp_year = self.strip_date(min_temp_date)
        max_humidity_day, max_humidity_month, max_humidity_year = self.strip_date(max_humidity_date)

        max_temp_overall = {
            "temperature": max_temp,
            "day": max_temp_day,
            "month": max_temp_month,
            "year": max_temp_year,
        }

        min_temp_overall = {
            "temperature": min_temp,
            "day": min_temp_day,
            "month": min_temp_month,
            "year": min_temp_year,
        }

        max_humidity_overall = {
            "humidity": max_humidity,
            "day": max_humidity_day,
            "month": max_humidity_month,
            "year": max_humidity_year,
        }

        return max_temp_overall, min_temp_overall, max_humidity_overall