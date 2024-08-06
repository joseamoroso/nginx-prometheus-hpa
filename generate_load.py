import math
import random
import time
import requests
import sys

from typing import List

"""
Function to generate inter-arrival times using Poisson 
distribution with exponential decay.
"""
def generate_inter_arrival_times(arrival_rate: int, 
                                 decay_rate: float, 
                                 duration: int) -> List[float]:
    inter_arrival_times = []
    time = 0

    while time < duration:
        # Calculate the arrival rate at the current time using exponential decay
        current_rate = arrival_rate * math.exp(-decay_rate * time)

        # Generate the inter-arrival time using the Poisson distribution
        inter_arrival_time = random.expovariate(current_rate)
        
        # Ensure larger values don't pollute the set. 
        if inter_arrival_time >= duration:
            break
        
        inter_arrival_times.append(inter_arrival_time)
        time += inter_arrival_time

    return inter_arrival_times

# Set up API calls...

# Configure inter arrival time and arrival rate semantics.
arrival_rate = 80  # Average arrival rate of 20 requests per second
decay_rate = 0.001  # Decay rate of 0.2 requests per second
duration = 500  # Duration of the load test in seconds

host, port, path = ('localhost', 80, 'heavywork')

# Override defaults if command-line arguments are provided
if len(sys.argv) > 3:
    host, port, path = sys.argv[1], sys.argv[2], sys.argv[3]

inter_arrival_times = generate_inter_arrival_times(arrival_rate, 
                                                   decay_rate, 
                                                   duration)

for i, inter_arrival_time in enumerate(inter_arrival_times):
    time.sleep(inter_arrival_time)
    x = requests.post(f"http://{str(host)}:{str(port)}/{str(path)}")
    print(x.status_code, x.text)

