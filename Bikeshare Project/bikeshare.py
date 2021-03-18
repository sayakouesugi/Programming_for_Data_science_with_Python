import time
import pandas as pd
import numpy as np


#Bikeshare Project

CITY_DATA = { 'chicago': 'chicago.csv', 'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv', 'New york city': 'new_york_city.csv',
              'new york city': 'new_york_city.csv', 'washington': 'washington.csv',
             'Washington': 'washington.csv' }

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print("Please write a city name: Chicago, New York City or Washington!")
        city = input().lower()
        if city not in CITY_DATA:
            print("\nThis answer is invalid\n")
            continue
        else:
            break
    MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    """ Made the List to output
    specified data
    """

    while True:
         print("January, Feburary, March, April, May, June or all?")
         month = input("Please Enter Month\n").lower()
         if month not in MONTH_LIST:
            print("\nThis answer is invalid\n")
            continue
         else:
            break

    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    """ Made the List to output
    specified data
    """

    while True:
         print("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?")
         day = input("Please Enter day\n").lower()
         if day not in DAY_LIST:
            print("\nThis answer is invalid\n")
            continue
         else:
            break


    print(city)
    print(month)
    print(day)
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month

    popular_month = df['month'].mode()[0]
    print(popular_month)


    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print(popular_day_of_week)


    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(common_end)

    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print(total_travel)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print(mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    if  'Gender' in df:
       gender = df['Gender'].value_counts()
       print(gender)
    else:
       print('There are no gender information')


    # Display earliest, most recent, and most common year of birth
    if  'Birth_Year' in df:
        earliest = df['Birth_Year'].min()
        print(earliest)
        recent = df['Birth_Year'].max()
        print(recent)
        common = df['Birth_Year'].mode()
        print(common)
    else:
        print('There are no birth year information')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def data(df):


    """
    Display more specified data,
    after ask user.
    """
    raw_data = 0
    while True:
        answer = input("Do you want to see the raw data? Yes or No").lower()
        if answer not in ['yes', 'no']:
            answer = input("Please type Yes or No.").lower()
        elif answer == 'yes':
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            again = input("Do you want to see more? Yes or No").lower()
            if again == 'no':
                break
        elif answer == 'no':
            return



def main():
    city = ""
    month = ""
    day = ""
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nDo you want to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("You can see all data always, Thanks")
            break


if __name__ == "__main__":
	main()
