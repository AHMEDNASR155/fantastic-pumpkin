import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}
Months = ['all', 'january', 'february', 'march', 'april', 'may',
          'june']

Days = ['all', 'monday', 'tuesday', 'wednesday',
        'thursday', 'friday', 'saturday', 'sunday']


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
    city_name = input("would you like to see data for Chicago, New York City, or washington ?\n").lower().strip()    
    while city_name.lower() not in CITY_DATA:
        print("just input one of chicago,new york, or washington")
        city_name = input("would you like to see data for Chicago, New York, or Washington ?\n").lower().split()
    if city_name.lower() in CITY_DATA:
        city = CITY_DATA.get(city_name)
    else:
        print("Sorry,choose one of chicago, new york city or washington")

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = input(
        "would you like to filter by month or day? input a month name or 'all' if you do not want month filter .\n").lower().split()
    while month_name.lower() not in Months:
        print("sorry, wrong choice")
        month_name = input(
            "which month do you want ?input a correct month name or 'all' if you do not want month filter.\n").lower().split()
    if month_name.lower() in Months:
        month = month_name.lower()
    else:
        print("Sorry,type one of the months or 'all' if you do not want month filter")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = input("which day you want to filter? input a day or 'all' if you do not want filter day.\n").lower().split()
    while day_name.lower() not in Days:
        print("sorry,wrong choice which day do you mean?.")
        day_name = input("which day do you want to filter?input a correct day name or type 'all' if you do not day filter.\n").lower().split()
    if day_name.lower() in Days:
        day = day_name.lower()
    else:
        print("Sorry,type a day like monday,tuesday,..or type 'all' if you do not want day filter")

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
    df = pd.read_csv(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_of_week
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month = Months.index(month) + 1
        df = df[df['month'] == month]

        if day != 'all':

           df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month

    most_common_month = df['month'].mode()[0]
    print(f"the most common month is :{most_common_month}")

    # TO DO: display the most common day of week

    most_common_day = df['day_of_week'].mode()[0]
    print(f"the most common day is :{most_common_day}")

    # TO DO: display the most common start hour

    most_common_start_hour = df['hour'].mode()[0]
    print(f"the most common start hour is :{most_common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print(f"the most common start station is :{most_common_start_station}")

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print(f"the most common end station is :{most_common_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print(f"the most common used start station and end station is :{most_common_start_end_station[0]},{most_common_start_end_station[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print(f"Total travel time is : {total_time}")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time is : {mean_travel_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(f"the count of user types is: {str(user_types)}")

    # TO DO: Display counts of gender
    counts_of_gender = df['Gender'].value_counts()
    print(f"the count of user gender is: {str(counts_of_gender)}")

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    most_recent_birth = df['Birth Year'].max()
    most_common_birth = df['Birth Year'].mode()[0]
    print(f'earliest birth is:{earliest_birth}')
    print(f'Most recent birth is: {most_recent_birth}')
    print(f'Most common birth is: {most_common_birth}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """display raw data on user request."""
    print('\nCalculating Display Data...\n')
    start_time = time.time()
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no\n").lower().split()

    start_loc = 0
    keep_adding = True
    if view_data == 'no':
        keep_adding = False
    while (keep_adding):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        more_display = input("Do you want to continue? ").lower()
        if more_display == 'no':
            keep_adding = False

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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
