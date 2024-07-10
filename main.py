import csv
import datetime
from termcolor import colored
import argparse
import os

parser = argparse.ArgumentParser()

months_list = ["jan", "feb" , "mar" , "apr" , "may" , "jun" , 'jul' , "aug", 'sep' , 'oct', 'nov' , 'dec']


def column_cutting(columns_to_keep, csv_file):
                csv_reader = csv.DictReader(csv_file)
                month_data = {col: [] for col in columns_to_keep}
                for row in csv_reader:
                    for col in columns_to_keep:
                        month_data[col].append(row[col])
                return month_data



def monthly_data_storage(parser_file_path, year , month):
    """Returns a Dictionary of Weather Values for the month Specified"""

    file_path = os.path.join(parser_file_path, f"Murree_weather_{year}_{months_list[month - 1]}.txt")

    columns_to_keep = ['PKT' ,'Max TemperatureC', 'Mean TemperatureC', 'Min TemperatureC', 'Max Humidity', ' Mean Humidity']
    
    # Initialize a dictionary to store all filtered data
    weather_data = {col: [] for col in columns_to_keep}

    try :
        with open(file_path, 'r') as csv_file:
            
            weather_data = column_cutting(columns_to_keep , csv_file)
            
    except FileNotFoundError as e :
        raise FileNotFoundError (f"Invalid month or year entered : {e}")
    
    return weather_data


    
def monthly_data_barcharts(weather_data):
    """Returns a Bar Chart in the Console for a month of Data"""
    
    max_temperatures = weather_data['Max TemperatureC']
    min_temperatures = weather_data['Min TemperatureC']

    max_temperatures = [int(temp) if temp.isdigit() else None for temp in max_temperatures]
    min_temperatures = [int(temp) if temp.isdigit() else None for temp in min_temperatures]
    
    # Finding the maximum temperature for scaling the chart
    max_temp_value = max(temp for temp in max_temperatures if temp is not None)

    for day in range(len(max_temperatures)):
        max_temp = max_temperatures[day]
        min_temp = min_temperatures[day]

        if max_temp is None or min_temp is None :
            continue


        max_temp_bar = '+' * max_temp
        min_temp_bar = '-' * min_temp
        
        # Print day number and bars
        print(colored(f"Day {day + 1} | Max: {max_temp_bar} ({max_temp}°C)", 'blue'))
        print(colored(f"Day {day + 1} | Min: {min_temp_bar} ({min_temp}°C)\n" , 'red'))





def monthly_data_computation(weather_data):
    """Computers the maximum , minimum Temperature and average humidity for that month 
    Returns the Value and its corresponding Date """
    
    max_temperatures = weather_data['Max TemperatureC']
    max_temperatures = [int(temp) if temp.isdigit() else None for temp in max_temperatures]
    max_temperatures = [temp for temp in max_temperatures if temp is not None]
    max_temp = max(max_temperatures)
    max_temp_index = max_temperatures.index(max_temp)

    min_temperatures = weather_data['Min TemperatureC']
    min_temperatures = [int(temp2) if temp2.isdigit() else None for temp2 in min_temperatures]
    min_temperatures = [temp2 for temp2 in min_temperatures if temp2 is not None]
    min_temp = min(min_temperatures)
    min_temp_index = min_temperatures.index(min_temp)

    mean_humidity_list = weather_data[" Mean Humidity"]
    total_humidity = 0
    humi_count = 0
    for humi in mean_humidity_list :
        
        if  humi != '' :
            total_humidity += int(humi)
            humi_count +=1

        else: 
            humi = None
    mean_humidity = total_humidity / humi_count

    #finding date and time

    date_max_temp_raw = weather_data['PKT'][max_temp_index]
    date_max_temp_refined = datetime.datetime.strptime(date_max_temp_raw, '%Y-%m-%d')
    max_temp_day = date_max_temp_refined.strftime('%d')
    max_temp_month = date_max_temp_refined.strftime('%B')
    max_temp_year = date_max_temp_refined.strftime('%Y')


    date_min_temp_raw = weather_data['PKT'][min_temp_index]
    date_min_temp_refined = datetime.datetime.strptime(date_min_temp_raw, '%Y-%m-%d')
    min_temp_day = date_min_temp_refined.strftime('%d')
    min_temp_month = date_min_temp_refined.strftime('%B')
    min_temp_year = date_min_temp_refined.strftime('%Y')

    max_temp_dict = {
        "max_temp" : max_temp, 
        "day" : max_temp_day ,
        "month": max_temp_month ,
        "year": max_temp_year 
    }

    min_temp_dict = {
        "min_temp" : min_temp, 
        "day" : min_temp_day ,
        "month": min_temp_month ,
        "year": min_temp_year 
    }

    return max_temp_dict , min_temp_dict, mean_humidity
    



def yearly_data_storage(parser_file_path , year):
    """Returns an Array of Dictionaries containing data of all 12 months of the year"""



    columns_to_keep = ['PKT', 'Max TemperatureC', 'Mean TemperatureC', 'Min TemperatureC', 'Max Humidity', ' Mean Humidity']
    yearly_data_dicts = []

    for month in months_list:
        file_path =os.path.join(parser_file_path, f"Murree_weather_{year}_{month}.txt")
        
        try:
            with open(file_path, 'r') as csv_file:
                month_data = column_cutting(columns_to_keep ,csv_file )
                yearly_data_dicts.append(month_data)

        except FileNotFoundError:
            continue
    
    
    return yearly_data_dicts

        
    
          


def yearly_data_computation(yearly_data_dicts):
    """Computes and Returns 3 lists 
    Maximum Temperature of the year and its corresponding date
    Minimum Temperature of the year and its corresponsing date 
    Maximum humidity of the year and its corresponsding date ."""

    max_temp_details_list = []
    min_temp_details_list = []
    max_humidity_details_list = []

    for dict in yearly_data_dicts:

        #maximum temperature handling for every month of the year 

        max_temperatures = dict['Max TemperatureC']
        max_temperatures = [int(temp) if temp.isdigit() else None for temp in max_temperatures]
        max_temperatures = [temp for temp in max_temperatures if temp is not None]
        max_temp = max(max_temperatures)
        max_temp_index = max_temperatures.index(max_temp)

        date_max_temp_raw = dict['PKT'][max_temp_index]
        date_max_temp_refined = datetime.datetime.strptime(date_max_temp_raw, '%Y-%m-%d')
        max_temp_day = date_max_temp_refined.strftime('%d')
        max_temp_month = date_max_temp_refined.strftime('%B')

        max_temp_sub_array = [max_temp , max_temp_day , max_temp_month]
        max_temp_details_list.append(max_temp_sub_array)


        #minimum temperature handlind for every month of the year

        min_temperatures = dict['Min TemperatureC']
        min_temperatures = [int(temp2) if temp2.isdigit() else None for temp2 in min_temperatures]
        min_temperatures = [temp2 for temp2 in min_temperatures if temp2 is not None]
        min_temp = min(min_temperatures)
        min_temp_index = min_temperatures.index(min_temp)

        date_min_temp_raw = dict['PKT'][min_temp_index]
        date_min_temp_refined = datetime.datetime.strptime(date_min_temp_raw, '%Y-%m-%d')
        min_temp_day = date_min_temp_refined.strftime('%d')
        min_temp_month = date_min_temp_refined.strftime('%B')

        min_temp_sub_array = [min_temp , min_temp_day , min_temp_month]
        min_temp_details_list.append(min_temp_sub_array)

        
        #handling humiditiy for every month of the year 

        max_humidities = dict['Max Humidity']
        max_humidities = [int(humi) if humi.isdigit() else None for humi in max_humidities]
        max_humidities = [humi for humi in max_humidities if humi is not None]
        max_humi = max(max_humidities)
        max_humi_index = max_humidities.index(max_humi)

        date_max_humi_raw = dict['PKT'][max_humi_index]
        date_max_humi_refined = datetime.datetime.strptime(date_max_humi_raw ,'%Y-%m-%d' )
        max_humi_day = date_max_humi_refined.strftime('%d')
        max_humi_month = date_max_humi_refined.strftime('%B')

        max_humi_sub_array = [max_humi , max_humi_day, max_humi_month ]
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
        


parser.add_argument('parser_file_path', help="Enter the directory path to the weather files")
parser.add_argument('option', choices=['year', 'bar_chart', 'month'], help="Choose the operation: year for yearly, month for monthly data, bar_chart for monthly bar chart")
parser.add_argument('year', type=int, help="Enter the year")
parser.add_argument('month', type=int, nargs='?', choices=range(1, 13), help="Enter the month number (1-12) for monthly data or bar chart", default=None)
args  =parser.parse_args()
#arg parse will give me the 1. file path 
# user will also give me whether he wants month , year or month bar chart
# year is the flag for yearly 
# month is the flag for monthly 
# bar_chart s the flag for monthly bar chart 
# start with allowing only one arguments 





if args.option == 'month':
    if args.month is None:
        parser.error("the following arguments are required: month")
    weather_data = monthly_data_storage(args.parser_file_path, args.year, args.month)
    max_temp_dict, min_temp_dict, mean_humidity = monthly_data_computation(weather_data)

    print("Weather Data for", months_list[args.month - 1], args.year)
    print(f"Maximum Temperature: {max_temp_dict['max_temp']}°C on {max_temp_dict['day']} {max_temp_dict['month']} {max_temp_dict['year']}")
    print(f"Minimum Temperature: {min_temp_dict['min_temp']}°C on {min_temp_dict['day']} {min_temp_dict['month']} {min_temp_dict['year']}")
    print(f"Mean Humidity: {mean_humidity}%")

    if args.option == 'bar_chart':

     monthly_data_barcharts(weather_data)

elif args.option == 'year':
    yearly_data_dicts = yearly_data_storage(args.parser_file_path, args.year)
    max_temp_overall_det, min1_temp_overall_det, max_humidity_overall_det = yearly_data_computation(yearly_data_dicts)
    print(f"Highest temperature: {max_temp_overall_det[0]}°C on {max_temp_overall_det[1]} {max_temp_overall_det[2]}")
    print(f"Lowest temperature: {min1_temp_overall_det[0]}°C on {min1_temp_overall_det[1]} {min1_temp_overall_det[2]}")
    print(f"Highest humidity: {max_humidity_overall_det[0]}% on {max_humidity_overall_det[1]} {max_humidity_overall_det[2]}")