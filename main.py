import argparse
from get_data import Weather_data
from computation import Compute
from visualizer import Bar_chart


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "parser_file_path", help="Enter the directory path to the weather files"
    )
    parser.add_argument(
        "option",
        choices=["year", "bar_chart", "month"],
        help="Choose the operation: year for yearly, month for monthly data, bar_chart for monthly bar chart",
    )
    parser.add_argument("year", type=int, help="Enter the year")
    parser.add_argument(
        "month",
        type=int,
        nargs="?",
        choices=range(1, 13),
        help="Enter the month number (1-12) for monthly data or bar chart",
        default=None,
    )
    args = parser.parse_args()

    if args.option == "month":

        if args.month == None:
            parser.error("the following arguments are required: month")

        weather_data = Weather_data(args.parser_file_path, args.year, args.month)
        monthly_data = weather_data.load_monthly_data()

        computational_monthly = Compute(monthly_data)
        max_temp_dict, min_temp_dict, mean_hum = (
            computational_monthly.compute_monthly_data()
        )

        print(f"Max Temperature: {max_temp_dict}")
        print(f"Min Temperature: {min_temp_dict}")
        print(f"Mean Humidity: {mean_hum}")

    elif args.option == "year":

        yearly_data = Weather_data(args.parser_file_path, args.year, args.month)
        yearly_data_dicts = yearly_data.load_yearly_data()
        compute_yearly = Compute(yearly_data_dicts)

        max_temp_overall_det, min_temp_overall_det, max_humidity_overall_det = (
            compute_yearly.compute_yearly_data(yearly_data_dicts)
        )

        print(f"Max Temperature Overall: {max_temp_overall_det}")
        print(f"Min Temperature Overall: {min_temp_overall_det}")
        print(f"Max Humidity Overall: {max_humidity_overall_det}")

    elif args.option == "bar_chart":

        monthly_data_b = Weather_data(args.parser_file_path, args.year, args.month)
        monthly_chart = monthly_data_b.load_monthly_data()
        side_bar_chart = Bar_chart(monthly_chart)
        side_bar_chart.visu()
