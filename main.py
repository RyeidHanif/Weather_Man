import argparse
from get_data import Weather_Data
from computation import Compute
from visualizer import Bar_chart

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "parser_file_path", help="Enter the directory path to the weather files"
    )
    parser.add_argument(
        "-a", nargs="*", metavar=("YYYY/MM"), help="Monthly data in the format: YYYY/MM"
    )
    parser.add_argument(
        "-e", nargs="*", metavar=("YYYY"), help="Yearly data in the format: YYYY"
    )
    parser.add_argument(
        "-c",
        nargs="*",
        metavar=("YYYY/MM"),
        help="Monthly bar chart data in the format: YYYY/MM",
    )

    args = parser.parse_args()

    if args.a:
        try:
            for entry in args.a:
                year, month = map(int, entry.split("/"))
                weather_data = Weather_Data(args.parser_file_path, year, month)
                monthly_data = weather_data.load_data(month)

                computational_monthly = Compute(monthly_data)
                max_temp_dict, min_temp_dict, mean_hum = (
                    computational_monthly.compute_monthly_data()
                )

                print(f"Max Temperature: {max_temp_dict}")
                print(f"Min Temperature: {min_temp_dict}")
                print(f"Mean Humidity: {mean_hum}")
        except Exception as e:
            print("error occures", e)

    if args.e:
        try:
            for entry2 in args.e:
                year = int(entry2)
                yearly_data = Weather_Data(args.parser_file_path, year, None)
                yearly_data_dicts = yearly_data.load_data()
                compute_yearly = Compute(yearly_data_dicts)

                max_temp_overall_det, min_temp_overall_det, max_humidity_overall_det = (
                    compute_yearly.compute_yearly_data(yearly_data_dicts)
                )

                print(f"Max Temperature Overall: {max_temp_overall_det}")
                print(f"Min Temperature Overall: {min_temp_overall_det}")
                print(f"Max Humidity Overall: {max_humidity_overall_det}")
        except Exception as e:
            print("error occurred", e)

    if args.c:
        try:
            for entry3 in args.c:
                year, month = map(int, entry3.split("/"))
                monthly_data_b = Weather_Data(args.parser_file_path, year, month)
                monthly_chart = monthly_data_b.load_data()
                side_bar_chart = Bar_chart(monthly_chart)
                side_bar_chart.visu()
        except Exception as e:
            print("Error occured", e)
