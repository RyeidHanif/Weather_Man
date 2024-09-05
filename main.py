"""
Contains the main code where all the classes in various modules are instantiated 
ArgParser is used to parse various command line arguments from the user .
the parsed data is provided to instances / objects of the respective classes and their methods called . 
"""

import argparse
from get_data import WeatherData
from computation import Compute
from visualizer import Visualize
from termcolor import colored


def process_data(parser_file_path, year, month=None, chart=False):
    """
    Contains a Series for checks for whether the User asks for Barcharts , Monthly or yearly data
    Accordingly Returns the appropriate datastructure or value after instantiation of the computation and visualization class
    According to the Parameters , if the chart is set to True , weather data for that specific month will be loaded and the visualization function called
    Otherwise the choice will be between displaying yearly or monthly data
    In This case , if the month has been specified in the Command line arguments , monthly data is stored and the Monthly Computation function called
    Otherwise  The yearly function is used
    """

    weather_data = WeatherData(parser_file_path, year, month)
    total_data = weather_data.load_data(month)

    if chart:
        side_bar_chart = Visualize(total_data)
        side_bar_chart.bar_chart()
    else:
        compute = Compute(total_data)
        max_temp, min_temp, mean_humidity = compute.compute_data()

        return max_temp, min_temp, mean_humidity


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
            year, month = map(int, entry.split("/"))
            max_temp, min_temp, mean_humidity = process_data(
                args.parser_file_path, year, month
            )

            Visualize.print_val(max_temp, min_temp, mean_humidity, year, month)

    if args.e:
        for entry in args.e:
            year = int(entry)
            max_temp, min_temp, mean_humidity = process_data(
                args.parser_file_path, year
            )

            Visualize.print_val(max_temp, min_temp, mean_humidity, year)

    if args.c:
        for entry in args.c:
            year, month = map(int, entry.split("/"))
            process_data(args.parser_file_path, year, month, chart=True)
