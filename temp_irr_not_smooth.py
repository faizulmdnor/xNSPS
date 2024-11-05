import pandas as pd
import random
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
import numpy as np


def generate_irradiance_data_minute(hour, minute):
    """
    Generate irradiance based on time of day (hour and minute).
    Peak irradiance around midday, low at dawn/dusk, zero at night.
    """
    # Define irradiance pattern based on time of day
    if 6 <= hour < 18:
        # Midday peak at 1000 W/m² with Gaussian distribution
        peak_irradiance = 1000
        std_dev = 4  # Controls the spread around noon
        time_factor = hour + minute / 60.0  # Convert to decimal hours
        irradiance = peak_irradiance * np.exp(-((time_factor - 12) ** 2) / (2 * std_dev ** 2))

        # Add random variability to simulate clouds
        irradiance *= random.uniform(0.8, 1.2)
    else:
        # Nighttime irradiance is zero
        irradiance = 0

    return round(max(0, irradiance), 2)  # Ensure irradiance is not negative


def generate_temperature_irradiance_data_minute(date_stamp):
    # Define temperature ranges and initialize variables
    day_temp_min, day_temp_max = 30, 34  # Daytime temperature range
    night_temp_min, night_temp_max = 23, 26  # Nighttime temperature range

    # Start at midnight
    current_time = datetime.strptime("00:00", "%H:%M")
    end_time = current_time + timedelta(days=1)

    # Store temperature and irradiance data
    temperature_data = []
    irradiance_data = []
    time_data = []

    # Set initial temperature
    current_temperature = random.uniform(night_temp_min, night_temp_max)

    while current_time < end_time:
        hour = current_time.hour
        minute = current_time.minute

        # Determine if it's day or night for temperature, with minor fluctuations
        if 7 <= hour < 19:
            # Daytime temperature with minor random variation every minute
            base_temp = random.uniform(day_temp_min, day_temp_max)
        else:
            # Nighttime temperature with minor random variation every minute
            base_temp = random.uniform(night_temp_min, night_temp_max)

        # Apply slight variation to simulate gradual change minute-by-minute
        current_temperature = base_temp + random.uniform(-0.1, 0.1)

        # Generate irradiance based on time of day
        irradiance = generate_irradiance_data_minute(hour, minute)

        # Append data to list
        time_data.append(current_time.strftime("%H:%M"))
        temperature_data.append(round(current_temperature, 2))
        irradiance_data.append(irradiance)

        # Increment time by one minute
        current_time += timedelta(minutes=1)

    # Create DataFrame for the day
    df_temp_irradiance = pd.DataFrame({
        'Date': date_stamp,
        'Time': time_data,
        'Temp C': temperature_data,
        'Irradiance W/m²': irradiance_data
    })
    return df_temp_irradiance


# Define start and end dates
start_date = "2020-01-01"
end_date = "2020-01-01"  # Set a single day for testing

# Generate daily timestamps
date_stamp = pd.date_range(start=start_date, end=start_date, freq='D')

# Initialize empty DataFrame to store all data
df_temp_irradiance_data = pd.DataFrame(columns=['Date', 'Time', 'Temp C', 'Irradiance W/m²'])

# Generate temperature and irradiance data for each day
df_list = []
for day in date_stamp:
    df_list.append(generate_temperature_irradiance_data_minute(day))
df_temp_irradiance_data = pd.concat(df_list, ignore_index=True)

# Example plot for one day to visualize the temperature and irradiance pattern
example_day = '2020-01-01'
df_example_day = df_temp_irradiance_data[df_temp_irradiance_data['Date'] == example_day]
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot temperature
ax1.plot(df_example_day['Time'], df_example_day['Temp C'], color='tab:blue', label='Temperature (°C)')
ax1.set_xlabel("Time")
ax1.set_ylabel("Temperature (°C)", color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Plot irradiance on secondary y-axis
ax2 = ax1.twinx()
ax2.plot(df_example_day['Time'], df_example_day['Irradiance W/m²'], color='tab:orange', label='Irradiance (W/m²)')
ax2.set_ylabel("Irradiance (W/m²)", color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Show legend and plot
fig.tight_layout()
plt.title(f"Minute-by-Minute Temperature and Irradiance for {example_day}")
plt.show()
