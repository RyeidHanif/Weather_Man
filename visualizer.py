"""Module to display a sideways bar chart on the console for every day of the month """

from termcolor import colored
import datetime
from daily_weather_data import WeatherDataRow


class Visualize:
    """Class containing attributes for monthly data and a method for the visualization of max and Min temperature of every day ."""

    def __init__(self, monthly_data):
        """stores attribtues for instantiation of the class"""

        self.monthly_data = monthly_data

    def bar_chart(self):
        """Returns a bar chart consisting of differently colored + or - signs for max and in temperature for every day of the month respectively"""

        max_temperatures = []
        min_temperatures = []

        for row in self.monthly_data:
            max_temperatures.append(row.max_temp)
            min_temperatures.append(row.min_temp)

        
        day , month , year = WeatherDataRow.strip_date(self.monthly_data[0])


        # Finding the maximum temperature for scaling the chart
        print("\n", month, year, "\n")
        for day in range(len(max_temperatures)):
            max_temp = max_temperatures[day]
            min_temp = min_temperatures[day]

            if max_temp is None or min_temp is None:
                continue

            max_temp_bar = "+" * max_temp
            min_temp_bar = "+" * min_temp

            # Print day number and bars
            print(
                colored(f"{day + 1} ", "white")
                + colored(min_temp_bar, "blue")
                + colored(f" {max_temp_bar}", "red")
                + f" ({min_temp}C - {max_temp}C)"
            )

    def print_val( max_temp , min_temp , mean_humidity ,year , month = None):
        """
        Responsible for outputting the values for max , min temperature and mean humidity 
        This was added as a function to reduce repetition and be reusable in the main code for years and months 
        if the month is given , then it will be printed out in the terminal , otherwise only the year will be 
        """

        max_temp_day, max_temp_month, max_temp_year = max_temp.strip_date()
        min_temp_day, min_temp_month, min_temp_year = min_temp.strip_date()

        print(
                colored(
                    f"\n ----------------- {month if month else "yearly data of "} , {year}--------------- \n", "green"
                )
            )
        print(
                colored(
                    f"Highest Average Temperature: {max_temp.max_temp}C on {max_temp_day} {max_temp_month}",
                    "red",
                )
            )
        print(
                colored(
                    f"Lowest Average Temperature: {min_temp.min_temp}C on {min_temp_day} {min_temp_month}",
                    "blue",
                )
            )

        print(f"Average Mean Humidity : {mean_humidity}")
        

