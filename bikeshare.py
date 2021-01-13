import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

#*****************************************************************************

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities= ['chicago' , 'new york city' , 'washington']

    months= ['all' , 'january', 'february', 'march', 'april', 'may', 'june' ]

    days=   ['all' ,'sunday', 'monday', 'tuesday', 'wednesday',
             'thursday', 'friday', 'saturday']

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input('\n Please enter the name of the city to filter by : chicago , new york city , or washington: \n').lower()
        if city not in cities:
            print(' Sorry,invalid input. Please try again')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input("\nWhich month would you like to filter by? january, february, march, april, may, june or type 'all' \n").lower()
        if month not in months:
            print(' Sorry,invalid input. Please try again')
            continue
        else:
           break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day=input("please, select a day to fillter by, kindly enter the day as follows: sunday, monday, tuesday, wednesday, thursday, friday, Saturday or type 'all' if you do not have any preference.\n").lower()
        if day not in days :
            print('Sorry,invalid input. Please try again')
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city.lower()])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    #Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        #create a new data frame if there was filter apply
        df = df[df['month'] == month]

        # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
#*****************************************************************************

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_commom_month = df['month'].mode()[0]
    print('Most common month :' , most_commom_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day :' , most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['Start Time'].mode()[0]
    print('Most common hour :' , most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#*****************************************************************************

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('\nMost commonly start station :' , start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('\nMost commonly end station :' , end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_and_end_combine ='from:' + df['Start Station'] + '   '+ 'to:' + df['End Station']
    combination_station = start_and_end_combine.mode()[0]
    print('\nMost frequent combination of start station and end station trip:', combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#*****************************************************************************

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', int(Total_Travel_Time/(60*60*24)), " Days")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', int(mean_travel_time/60), " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#*****************************************************************************

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_users = df['User Type'].value_counts()
    print('\nCount of users type :' , count_of_users)

    # TO DO: Display counts of gender
    try:
        df['Gender'].fillna('not mentioned the gender')
        count_of_genders = df['Gender'].value_counts()
        print('\nCount of gender types\n' , count_of_genders)
    except KeyError:
        print("\nGender Types:\nNo data available for this month.")
    # TO DO: Display earliest, most recent, and most common year of birth

    #1-Earliest year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('\nEarliest Year is:' , int(earliest_year))
    except KeyError:
        print("\nEarliest year:\nNo data available for this month.")
    #2-Most recent year of birth
    try:
        most_recent_year = df['Birth Year'].max()
        print('\nMost Recent Year is:',int(most_recent_year))
    except KeyError:
        print("\nMosr resent Year:\nNo data available for this month.")
   #3-Most common year of bitrh
    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost common Year of birth is:', int(most_common_year))
    except KeyError:
        print("\nMost common Year of birth is:\nNo data available for this month.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#*************************************************************************

def raw_data(df):
    count=0
    end=0
    while end <= df.count()[0]:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        if answer.lower() == 'yes':
            end = count + 5
            print('\nThe 5 lines of raw data:\n' , df.iloc[count:end])
            count += 5
            continue
        else:
            print('Sorry, There is no more data')
            break

#*****************************************************************************

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
