# Initialize an empty list to store runs
running_log = []

# create a function that takes the date, distance, and time as inputs, calculates the pace, and stores the in data structure
def add_run(running_log):
    date = input("Please input the date (YYY-MM-DD): ")
    distance = input("Please enter the distance (in miles): ")
    time = input("Please enter the time duration of the run (in HH:MM:SS format): ")

    ##calculate pace(with HH:MM:SS format)
    hours, minutes, seconds = map(int(time.split))
    total_minutes  = (hours * 60) + minutes + (seconds/60) ##calculate the total minutes 
    pace = total_minutes / distance
    ##format the pace as MM:SS
    pace_minutes = int(pace)
    pace_seconds = int((pace - pace_minutes) * 60)
    pace_formatted = f'{pace_minutes:02d}:{pace_seconds:02d}'

    ##store the run data
    