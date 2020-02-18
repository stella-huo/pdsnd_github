import time
import pandas as pd
import numpy as np

#Three cities files used for analysis: Chicago, New York City, and Washington D.C
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data in Chicago, New York City or Washington? ").lower()
    while city not in ("chicago", "new york city", "washington"):
        city = input("Please enter a valid input. \nWould you like to see data in Chicago, New York City or Washington? ").lower()



    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month? January, February, March, April, May, June or all? Please type out the full month name. ").lower()
    while month not in ("january", "february", "march", "april", "may", "june", "all"):
        month = input("Please enter a valid input. \nWhich month? January, February, March, April, May, June or all? Please type out the full month name. ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all? Please type out the full day of week name. ").lower()
    while day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"):
        day = input("Please enter a vaild input. \nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all? Please type out the full day of week name. ").lower()


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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common month: ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common day of week: ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most common start hour: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:')
    print(popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost commonly used end station:')
    print(popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('\nMost frequent combination of start station and end station trip:')
    print(popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    seconds = df['Trip Duration'].sum()
    days = seconds //(24 * 3600)
    seconds = seconds % (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds //60
    seconds %= 60
    print('The total travel time from the given information is: ')
    print("%d days %d:%d:%d" % (days, hours, minutes, seconds))

    # TO DO: display mean travel time
    seconds = df['Trip Duration'].mean()
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds //60
    seconds %= 60
    print('\nThe average travel time is: ')
    print("%d:%d:%d" % (hours, minutes, seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The counts of user types:')
    print(user_type)
    print()
<<<<<<< HEAD

    # TO DO: Display counts of gender
||||||| merged common ancestors
    
    # TO DO: Display counts of gender   
=======

    # TO DO: Display counts of gender, exclude the city has no gender info
>>>>>>> refactoring
    if 'Gender' not in df:
        print('No gender information for this city.\n')
    else:
        gender_count = df['Gender'].value_counts()
        print('\nThe counts of gender:')
        print(gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('No year of birth information for this city.\n')
    else:
        early_birth = df['Birth Year'].min()
        print('\nThe earliest year of birth:\n', int(early_birth))
        recent_birth = df['Birth Year'].max()
        print('\nThe most recent year of birth:\n', int(recent_birth))
        common_birth = df['Birth Year'].mode()[0]
        print('\nThe most common year of birth:\n', int(common_birth))

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
<<<<<<< HEAD


        #ask the users if they want to see 5 lines of raw data, display that data if the answer is 'yes',
||||||| merged common ancestors
        
        
        #ask the users if they want to see 5 lines of raw data, display that data if the answer is 'yes', 
=======


        #ask the users if they want to see 5 lines of raw data, display that
        #data if the answer is 'yes',
>>>>>>> refactoring
        #and continue these prompts and displays until the user says 'no'.
        i = 0
        raw = input("\nWould you like to see first 5 rows of raw data; type 'yes' or 'no'?\n").lower()
        pd.set_option('display.max_columns', 200)

        while True:
            if raw == 'no':
                break
            print(df[i:i+5])
            raw = input('\nWould you like to see next rows of raw data?\n').lower()
            i += 5


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
