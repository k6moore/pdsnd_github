import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington). 
    valid_city = True
    while valid_city:
            city = input("What city are you interested in? \n(Chicago, New York City or Washington): \n").lower()

            if city not in ('chicago', 'new york city', 'washington'):
                print("Oops! Looks like you entered an invalid city. Please try again\n")
            else:
                valid_city = False
        
    # Get user input for month (all, january, february, ... , june)
    valid_month = True
    while valid_month:
        month = input("\nWhat month would you like data for? \n(all, January, February, March, April, May or June): \n").lower()
        
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Oops! Looks like you entered an invalid month. Please try again\n")
        else:
            valid_month = False

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    valid_day = True
    while valid_day:
        day = input("\nWhat day of the week would you like data for? \n(all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or SUnday): \n").lower()
        
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Oops! Looks like you enteres an invalid day. Please try again\n")
        else:
            valid_day = False

        
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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('\nMost Common Month: \n', calendar.month_name[popular_month])

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('\nMost Common Day of the Week: \n', popular_day_of_week)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour: \n', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    #print(df['Start Station'].value_counts())
    print('\nMost Used Start Station: \n',popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    #print(df['End Station'].value_counts())
    print('\nMost Used End Station: \n',popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Start_End Station'] = df['Start Station'] + ' -- ' + df['End Station']
    #print(df['Start_End Station'].value_counts())
    popular_start_end_station = df['Start_End Station'].mode()[0]
    print('\nMost Frequent combination of Start End Station: \n',popular_start_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal Travel Time: \n',total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nMean Travel Time: \n',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCount of User Types:\n')
    print(user_types)

    # Display counts of gender (if applicable)
    try:
        gender = df['Gender'].value_counts()
        print('\nCount of Genders:\n')
        print(gender)
    except KeyError:
        print('\nCount of Genders:\n')
        print('\nNo Gender data for this city\n')
        


    # Display earliest, most recent, and most common year of birth (if applicable)
    try:
        earliest_year = df['Birth Year'].min()
        latest_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('\nYear of Birth Statistics: \n')
        print('\nEarliest Year of Birth: \n',earliest_year)
        print('\nMost Recent Year of Birth: \n',latest_year)
        print('\nMost Common Year of Birth: \n',common_year)
    except KeyError:
        print('\nYear of Birth Statistics: \n')
        print('\nNo Year of Birth Data for this city\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data_index = 5
        raw_data = 'yes'
        while True:
            raw_data = input('\nWould you like to see raw data? Enter yes or no.\n')
            if raw_data == 'yes':
                print(df.head(raw_data_index))
                raw_data_index += 5
            elif raw_data == 'no':
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
