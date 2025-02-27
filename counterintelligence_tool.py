import random
from datetime import datetime, timedelta

def generate_random_times():
    times_list = []
    
    # Get the current time as a datetime object (not a string)
    current_time = datetime.now()
    
    for i in range(100):
        # Generate a random delay in minutes (e.g., between 1 and 10 minutes)
        delay_minutes = random.randint(1, 10)
        
        # Calculate the next run time by adding the delay to the last run time (cumulative)
        next_run_time = current_time + timedelta(minutes=delay_minutes)
        next_run_time_str = next_run_time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Store the current time and next run time in the list
        times_list.append((current_time.strftime("%Y-%m-%d %H:%M:%S"), next_run_time_str))
        
        # Update the current time to the new "next run time" for the next iteration
        current_time = next_run_time
    
    return times_list

if __name__ == "__main__":
    times = generate_random_times()
    
    # Print the list of times
    for current_time, next_run_time in times:
        print(f"Current time: {current_time} | Next routine at: {next_run_time}")
    
    input("Press enter to close program")
