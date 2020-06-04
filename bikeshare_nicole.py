import time
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
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ['chicago','new york city', 'washington','all']
    input_city = input("From which city would you like to get data? chicago, new york city, washington or all?: ").lower()
    print("Super, you chose {}.".format(input_city))
    while input_city not in city:
        print("There might be a spelling mistake, please try again!", end='')
        input_city = input("Try again: ")
        print("Now it worked! You chose {}.".format(input_city))


    # get user input for month (all, january, february, ... , june)
    month = ['january','february', 'march', 'april', 'may', 'june', 'all']
    input_month = input("You can now choose a month from january to june or all: ").lower()
    print("Your choice: {}".format(input_month))
    while input_month not in month:
        print("There might be a spelling mistake, please try again!", end='')
        input_month = input("Try again: ")
        print("Perfect, you chose {}.".format(input_month))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ['monday','tuesday', 'wednesday', 'thurday', 'friday', 'saturday', 'sunday', 'all']
    input_day = input("please choose a day of the week or all days: ").lower()
    print("Awesome, you chose {}.".format(input_day))
    while input_day not in day:
        print("You may have misspelled the day, please try again!", end='')
        input_day = input("Please enter the day again: ")
        print("Now you got it, you chose {}.".format(input_day))

    print('-'*40)
    return input_city, input_month, input_day


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

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
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
    common_month = df['month'].mode()[0]

    print('Most common month:', common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]

    print('Most common day of week:', common_day_of_week)

    # display the most common start hour
    common_start_hour = df.hour.mode()[0]

    print('Most common start hour:', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('Most common start station:', common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('Most common end station:', common_end_station)

    # display most frequent combination of start station and end station trip
    common_start_station = df['Start Station'].mode()[0]
    common_end_station = df['End Station'].mode()[0]
    common_combi = df.groupby(['Start Station', 'End Station']).size().nlargest(1)

    print('Most frequent combination of start station and end station:', common_combi)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum() / 60 / 60 /24

    print('total travel time:', total_travel_time)

    # display mean travel time
    average_travel_time = (df['Trip Duration'].mean()) / 60

    print('average travel time:', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""



    print('\nCalculating User Stats...\n')
    start_time = time.time()



    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('user types:', user_types)


    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Gender:', gender)
    else:
        print("We don't have gender information")


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print('earliest year of birth:', earliest_year)
    else:
        print("There is no information about the birth year")

    if 'Birth Year' in df.columns:
        most_recent_year = df['Birth Year'].max()
        print('most recent year of birth:', most_recent_year)
    else:
        print("There is no information about the birth year")

    if 'Birth Year' in df.columns:
        most_common_year = df['Birth Year'].mode()[0]
        print('most common year of birth:', most_common_year)
    else:
        print("There is no information about the birth year")




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



# Ask for raw data first 5 and then next 5 raw data rows
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 0
        raw = input("\n Do you wanna see the first 5 rows of raw data?; type 'yes' or 'no'?\n").lower()
        pd.set_option('display.max_columns',200)
        while True:
            if raw == 'no':
                break
            print(df[i:i+5])
            raw = input('\n Do you wanna see now the next rows of raw data?\n').lower()
            i += 5
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
