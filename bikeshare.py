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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('please choose a city name (chicago, new york city, washington) :').lower()
        if city in cities:
            break
        else:
            print('please write ccorect name of a city from list : (chicago, new york city, washington)')

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('please choose a month :(all, january, february, march, april, may, june) :').lower()
        if month in months :
            break
        else:
            print('please enter a correct  month from the list of months: (all, january, february, march, april, may, june)')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday','friday','saturday','sunday']
    while True:
        day = input('choose a day :(all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)').lower()
        if day in days :
            break
        else:
            print('please enter a correct day from the list of days :(all, monday, tuesday, wednesday, thursday, friday, saturday, sunday)')

    
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
    
    df['Start Time']  = pd.to_datetime(df['Start Time'])  
    
    df['month']       = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['start hour']  = df['Start Time'].dt.hour
    
    if month != 'all': 
        months=['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all': 
        days = ['monday', 'tuesday', 'wednesday', 'thursday','friday','saturday','sunday']
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is : {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print('The most common day of week is : {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('The most common start hour is : {}'.format(df['start hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station is : {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most common end station is : {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+','+df['End Station']
    print('The most common frequent combination is : {}'.format(df['combination'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time : ',(df['Trip Duration'].sum()).round(1), 'seconds')

    # TO DO: display mean travel time
    print('Average travel time : ',(df['Trip Duration'].mean()).round(1), 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('The counts of gender is: ',df['Gender'].value_counts())   
    else:
        print('There is no data to this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df :
        print('The most earliest year of birth is : ',int(df["Birth Year"].min()))
        print('The most recent year of birth is : ',int(df["Birth Year"].max()))
        print('The most comman year of birth is : ',int(df["Birth Year"].mode()[0]))
    else:
        print('There is no data to this city')   

    #print("\nThis took %s seconds." % (time.time() - start_time))
    #print('-'*40)
   
def display_raw_data(df):
    
    """Display 5 raw from data if user wants , and display next 5 raws from data if user want."""
    pd.set_option('display.max_columns',200)
    print('Raw data is available to see  if you want....')
    
    x=0
    raw = input('\nWould you like to display the frist five raw from data? Enter yes or no.\n').lower()
    while True:
        if raw.lower()  == 'yes':
            print(df[x:x+5])
            raw = input('\nWould you like to display the frist five raw from data? Enter yes or no.\n').lower()
            x+=5
        elif raw.lower() not in ['yes', 'no']:
             print('This is invalid , please choose yes or no ')
             raw = input('\nWould you like to display the frist five raw from data? Enter yes or no.\n').lower()
            
        else:
            print('Thank you')
            break
                    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
          
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
               
                
       
            
       

if __name__ == "__main__":
	main()
