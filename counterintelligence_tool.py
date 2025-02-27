import random
import time
from datetime import datetime, timedelta

def random_timed_routine():
    for i in range(100):
        # Get the current time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Generate a random delay in minutes (e.g., between 1 and 10 minutes)
        delay_minutes = random.randint(1, 10)
        
        # Calculate when the next task will run
        next_run_time = datetime.now() + timedelta(minutes=delay_minutes)
        next_run_time_str = next_run_time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Print the current time and the next run time
        print(f"Current time: {current_time}")
        print(f"Next routine in {delay_minutes} minutes, at {next_run_time_str}")
        
        
        # Execute the routine task
        print("Routine task executed")

if __name__ == "__main__":
    random_timed_routine()
    input("Press enter to close program")
