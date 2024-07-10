import datetime


class Compute:

    def __init__(self, monthly_data):
        self.monthly_data = monthly_data

    def compute_monthly_data(self):
        max_temperatures = self.monthly_data["Max TemperatureC"]
        max_temperatures = [
            int(temp) if temp.isdigit() else None for temp in max_temperatures
        ]
        max_temperatures = [temp for temp in max_temperatures if temp is not None]
        max_temp = max(max_temperatures)
        max_temp_index = max_temperatures.index(max_temp)

        min_temperatures = self.monthly_data["Min TemperatureC"]
        min_temperatures = [
            int(temp2) if temp2.isdigit() else None for temp2 in min_temperatures
        ]
        min_temperatures = [temp2 for temp2 in min_temperatures if temp2 is not None]
        min_temp = min(min_temperatures)
        min_temp_index = min_temperatures.index(min_temp)

        mean_humidity_list = self.monthly_data[" Mean Humidity"]
        total_humidity = 0
        humi_count = 0
        for humi in mean_humidity_list:

            if humi != "":
                total_humidity += int(humi)
                humi_count += 1

            else:
                humi = None
        mean_humidity = total_humidity / humi_count

        # finding date and time

        date_max_temp_raw = self.monthly_data["PKT"][max_temp_index]
        date_max_temp_refined = datetime.datetime.strptime(
            date_max_temp_raw, "%Y-%m-%d"
        )
        max_temp_day = date_max_temp_refined.strftime("%d")
        max_temp_month = date_max_temp_refined.strftime("%B")
        max_temp_year = date_max_temp_refined.strftime("%Y")

        date_min_temp_raw = self.monthly_data["PKT"][min_temp_index]
        date_min_temp_refined = datetime.datetime.strptime(
            date_min_temp_raw, "%Y-%m-%d"
        )
        min_temp_day = date_min_temp_refined.strftime("%d")
        min_temp_month = date_min_temp_refined.strftime("%B")
        min_temp_year = date_min_temp_refined.strftime("%Y")

        max_temp_dict = {
            "max_temp": max_temp,
            "day": max_temp_day,
            "month": max_temp_month,
            "year": max_temp_year,
        }

        min_temp_dict = {
            "min_temp": min_temp,
            "day": min_temp_day,
            "month": min_temp_month,
            "year": min_temp_year,
        }

        return max_temp_dict, min_temp_dict, mean_humidity

    def compute_yearly_data(self, yearly_data_dicts):

        max_temp_details_list = []
        min_temp_details_list = []
        max_humidity_details_list = []

        for dict in yearly_data_dicts:

            # maximum temperature handling for every month of the year

            max_temperatures = dict["Max TemperatureC"]
            max_temperatures = [
                int(temp) if temp.isdigit() else None for temp in max_temperatures
            ]
            max_temperatures = [temp for temp in max_temperatures if temp is not None]
            max_temp = max(max_temperatures)
            max_temp_index = max_temperatures.index(max_temp)

            date_max_temp_raw = dict["PKT"][max_temp_index]
            date_max_temp_refined = datetime.datetime.strptime(
                date_max_temp_raw, "%Y-%m-%d"
            )
            max_temp_day = date_max_temp_refined.strftime("%d")
            max_temp_month = date_max_temp_refined.strftime("%B")

            max_temp_sub_array = [max_temp, max_temp_day, max_temp_month]
            max_temp_details_list.append(max_temp_sub_array)

            # minimum temperature handlind for every month of the year

            min_temperatures = dict["Min TemperatureC"]
            min_temperatures = [
                int(temp2) if temp2.isdigit() else None for temp2 in min_temperatures
            ]
            min_temperatures = [
                temp2 for temp2 in min_temperatures if temp2 is not None
            ]
            min_temp = min(min_temperatures)
            min_temp_index = min_temperatures.index(min_temp)

            date_min_temp_raw = dict["PKT"][min_temp_index]
            date_min_temp_refined = datetime.datetime.strptime(
                date_min_temp_raw, "%Y-%m-%d"
            )
            min_temp_day = date_min_temp_refined.strftime("%d")
            min_temp_month = date_min_temp_refined.strftime("%B")

            min_temp_sub_array = [min_temp, min_temp_day, min_temp_month]
            min_temp_details_list.append(min_temp_sub_array)

            # handling humiditiy for every month of the year

            max_humidities = dict["Max Humidity"]
            max_humidities = [
                int(humi) if humi.isdigit() else None for humi in max_humidities
            ]
            max_humidities = [humi for humi in max_humidities if humi is not None]
            max_humi = max(max_humidities)
            max_humi_index = max_humidities.index(max_humi)

            date_max_humi_raw = dict["PKT"][max_humi_index]
            date_max_humi_refined = datetime.datetime.strptime(
                date_max_humi_raw, "%Y-%m-%d"
            )
            max_humi_day = date_max_humi_refined.strftime("%d")
            max_humi_month = date_max_humi_refined.strftime("%B")

            max_humi_sub_array = [max_humi, max_humi_day, max_humi_month]
            max_humidity_details_list.append(max_humi_sub_array)

        max_temp_overall = -100
        min_temp_overall = 200
        max_humidity_overall = -1

        max_temp_overall_det = []
        min1_temp_overall_det = []
        max_humidity_overall_det = []

        for x in range(len(max_temp_details_list)):
            if max_temp_details_list[x][0] > max_temp_overall:
                max_temp_overall = max_temp_details_list[x][0]
                max_temp_overall_det = max_temp_details_list[x]

            if min_temp_details_list[x][0] < min_temp_overall:
                min_temp_overall = min_temp_details_list[x][0]
                min1_temp_overall_det = min_temp_details_list[x]

            if max_humidity_details_list[x][0] > max_humidity_overall:
                max_humidity_overall = max_humidity_details_list[x][0]
                max_humidity_overall_det = max_humidity_details_list[x]

        return max_temp_overall_det, min1_temp_overall_det, max_humidity_overall_det
