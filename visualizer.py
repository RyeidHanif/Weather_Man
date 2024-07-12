"""Module to display a sideways bar chart on the console for every day of the month """

from termcolor import colored
import datetime


class Bar_chart:
    """Class containing attributes for monthly data and a method for the visualization of max and Min temperature of every day ."""

    def __init__(self, monthly_data):
        """stores attribtues for instantiation of the class"""

        self.monthly_data = monthly_data

    def visu(self):
        """Returns a bar chart consisting of differently colored + or - signs for max and in temperature for every day of the month respectively"""

        max_temperatures = []
        min_temperatures = []

        for row in self.monthly_data:
            max_temperatures.append(row.max_temp)
            min_temperatures.append(row.min_temp)

        date_refined = datetime.datetime.strptime(self.monthly_data[0].pkt, "%Y-%m-%d")
        month = date_refined.strftime("%B")
        year = date_refined.strftime("%Y")

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
