import csv
from datetime import datetime 
DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    
    date = datetime.fromisoformat(iso_string)
    return date.strftime('%A %d %B %Y')
        

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    change_to_float = float(temp_in_fahrenheit)
    celsius = (change_to_float - 32) * 5 / 9
    return round(celsius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    # check the number of item in a list
    length=len(weather_data)
    total=0
    #loop and add all value
    for degree in weather_data:
        total=total+float(degree)
    mean=total/length
    # return mean
    return mean

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    new_data_list=[]
  
    with open(csv_file,mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
    #  skip the header
        next(csv_reader)
        for row in csv_reader:
    #get rid of empty row
           if(row !=[]):
            new_data_list.append(row)
    #  change string into int      
        for i in range(len(new_data_list)):
            new_data_list[i][1] = int(new_data_list[i][1])
            new_data_list[i][2] = int(new_data_list[i][2])
    return new_data_list

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # check a list is empty or not 
    if weather_data !=[]:
        min_value=weather_data[0]
        min_index=0
        for i in range(1,len(weather_data)):
        # compare 1st element and 2nd element. set range from 1 
        # if weather[i] is smaller than min_value
        # it becomes min_value
        # and give the position

            if(weather_data[i]<=min_value):
                min_value=weather_data[i]
                min_index=i
        return (float(min_value),min_index)
    else:
        return()
   




def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if(weather_data !=[]):
        max_value=weather_data[0]
        max_index=0
        for i in range(1,len(weather_data)):
            if(weather_data[i]>=max_value):
                max_value=weather_data[i]
                max_index=i
        return (float(max_value),max_index)
    else:
        return ()
    
# print(find_max([49, 57, 56, 55, 57, 53, 49]))


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

  
    min_f_data=[]
    max_f_data=[]
    dates_data=[]
    # check the length of the array ->8 Day Overview
    days=len(weather_data)

    for data in weather_data:
       dates_data.append(data[0])
       min_f_data.append(data[1])
       max_f_data.append(data[2])


    #  find min F
    (min_f_deg_final,min_index)=find_min(min_f_data)
    (max_f_deg_final,max_index)=find_max(max_f_data)

    # # covert to min F deg to  Cel
    min_c_deg=format_temperature(convert_f_to_c(min_f_deg_final))
    max_c_deg=format_temperature(convert_f_to_c(max_f_deg_final))
    # get dates using index of temp(it has original index)
    min_date=convert_date(dates_data[min_index])
    max_date=convert_date(dates_data[max_index])
  

    # get min temp mean
    min_mean=calculate_mean(min_f_data)
    min_mean_deg=format_temperature(convert_f_to_c(min_mean))
    max_mean=calculate_mean(max_f_data)
    max_mean_deg=format_temperature(convert_f_to_c(max_mean))

    
    return f'{days} Day Overview\n  The lowest temperature will be {min_c_deg}, and will occur on {min_date}.\n  The highest temperature will be {max_c_deg}, and will occur on {max_date}.\n  The average low this week is {min_mean_deg}.\n  The average high this week is {max_mean_deg}.\n'





def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary=""

    for data in weather_data:
    
        date_format=convert_date(data[0])
        min_deg_format=format_temperature(convert_f_to_c(data[1]))
        max_deg_format=format_temperature(convert_f_to_c(data[2]))

        summary+=f'---- {date_format} ----\n  Minimum Temperature: {min_deg_format}\n  Maximum Temperature: {max_deg_format}\n\n'
    return summary   
  

