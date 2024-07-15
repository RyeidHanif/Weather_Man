"""Contains the main code where all the classes in various modules are instantiated 
   ArgParser is used to parse various command line arguments from the user .
   the parsed data is provided to instances / objects of the respective classes and their methods called . 

   """

import argparse
from get_data import WeatherData
from computation import Compute
from visualizer import Bar_chart
from termcolor import colored


def process_data(parser_file_path, year, month=None, chart=False):
    """Contains a Series for checks for whether the User asks for Barcharts , Monthly or yearly data
    Accordingly Returns the appropriate datastructure or value after instantiation of the computation and visualization class
    """

    weather_data = WeatherData(parser_file_path, year, month)
    data = weather_data.load_data(month)
    if chart:
        side_bar_chart = Bar_chart(data)
        side_bar_chart.visu()

    else:
        compute = Compute(data)
        if month:
            max_temp_monthly, min_temp_monthly, mean_hum = (
                compute.compute_monthly_data()
            )
            return max_temp_monthly, min_temp_monthly, mean_hum

        else:
            max_temp_overall, min_temp_overall, max_humidity_overall = (
                compute.compute_yearly_data(data)
            )
            return max_temp_overall, min_temp_overall, max_humidity_overall


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "parser_file_path", help="Enter the directory path to the weather files"
    )
    parser.add_argument(
        "-a",
        metavar=("YYYY/MM"),
        help="Monthly data in the format: YYYY/MM",
        action="append",
    )
    parser.add_argument(
        "-e", metavar=("YYYY"), help="Yearly data in the format: YYYY", action="append"
    )
    parser.add_argument(
        "-c",
        metavar=("YYYY/MM"),
        help="Monthly bar chart data in the format: YYYY/MM",
        action="append",
    )

    args = parser.parse_args()

    if not (args.a or args.e or args.c):
        parser.error("At least one of the arguments -a, -e, or -c is required.")

    if args.a:

        for entry in args.a:
            year, month = map(
                int, entry.split("/")
            )  # split the Year and month given separately by the user
            max_temp_monthly, min_temp_monthly, mean_hum = process_data(
                args.parser_file_path, year, month
            )
            print(
                colored(
                    f"\n ----------------- {max_temp_monthly['month']} , {max_temp_monthly['year']}--------------- \n",
                    "green",
                )
            )
            print(
                colored(
                    f"Highest Average Temperature: {max_temp_monthly['temperature']} on {max_temp_monthly['month']} {max_temp_monthly['day']}",
                    "red",
                )
            )
            print(
                colored(
                    f"lowest Average Temperature: {min_temp_monthly['temperature']} on {min_temp_monthly['month']} {min_temp_monthly['day']}",
                    "blue",
                )
            )
            print(f"Average Mean Humidity : {mean_hum}")

    if args.e:

        for entry in args.e:
            year = int(entry)
            max_temp_overall, min_temp_overall, max_humidity_overall = process_data(
                args.parser_file_path, year
            )
            print(
                colored(
                    f"\n  --------------- {max_temp_overall['year']}-------------------- \n",
                    "green",
                )
            )
            print(
                colored(
                    f"Highest temperature  : {max_temp_overall['temperature']}C on the {max_temp_overall['day']}th of {max_temp_overall['month']}",
                    "red",
                )
            )
            print(
                colored(
                    f"Lowest Temperature : {min_temp_overall['temperature']}C on the {min_temp_overall['day']}th of {min_temp_overall['month']}",
                    "blue",
                )
            )
            print(
                f"Highest humidity  : {max_humidity_overall['humidity']}% on the {max_humidity_overall['day']}th of {max_humidity_overall['month']}"
            )

    if args.c:

        for entry in args.c:
            year, month = map(int, entry.split("/"))
            process_data(args.parser_file_path, year, month, chart=True)
