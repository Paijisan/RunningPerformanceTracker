# Initialize an empty list to store runs
running_log = []

# Create a function that takes the date, distance, and time as inputs, calculates the pace, and stores the data in the structure
def add_run(running_log):
    date = input("Please input the date (YYYY-MM-DD): ")
    distance = float(input("Please enter the distance (in miles): "))  # Convert distance to float
    time = input("Please enter the time duration of the run (in HH:MM:SS format): ")

    # Calculate pace (with HH:MM:SS format)
    hours, minutes, seconds = map(int, time.split(':'))  # Properly split the time string
    total_minutes = (hours * 60) + minutes + (seconds / 60)  # Calculate the total minutes
    pace = total_minutes / distance

    # Format the pace as MM:SS
    pace_minutes = int(pace)
    pace_seconds = int((pace - pace_minutes) * 60)
    pace_formatted = f'{pace_minutes:02d}:{pace_seconds:02d}'

    # Store the run data
    run = {"Date": date, "Distance": distance, "Time": time, "Pace": pace_formatted}

    # Append the run to the running log list
    running_log.append(run)
    print(f"Run added: {run}")

# Create a function that allows you to see all runs logged so far
def view_runs(running_log):
    for run in running_log:
        print(f"Date: {run['Date']}, Distance: {run['Distance']} miles, Time: {run['Time']}, Pace: {run['Pace']} per mile")


##save the running log to a file

# Example usage:
# add_run(running_log)
# view_runs(running_log)
