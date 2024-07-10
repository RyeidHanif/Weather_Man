from termcolor import colored


class Bar_chart:
    def __init__(self, monthly_data):
        self.monthly_data = monthly_data

    def visu(self):

        max_temperatures = self.monthly_data["Max TemperatureC"]
        min_temperatures = self.monthly_data["Min TemperatureC"]

        max_temperatures = [
            int(temp) if temp.isdigit() else None for temp in max_temperatures
        ]
        min_temperatures = [
            int(temp) if temp.isdigit() else None for temp in min_temperatures
        ]

        # Finding the maximum temperature for scaling the chart
        max_temp_value = max(temp for temp in max_temperatures if temp is not None)

        for day in range(len(max_temperatures)):
            max_temp = max_temperatures[day]
            min_temp = min_temperatures[day]

            if max_temp is None or min_temp is None:
                continue

            max_temp_bar = "+" * max_temp
            min_temp_bar = "-" * min_temp

            # Print day number and bars
            print(
                colored(f"Day {day + 1} | Max: {max_temp_bar} ({max_temp}°C)", "blue")
            )
            print(
                colored(f"Day {day + 1} | Min: {min_temp_bar} ({min_temp}°C)\n", "red")
            )
