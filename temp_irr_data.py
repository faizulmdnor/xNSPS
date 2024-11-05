import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

def generate_smooth_temperature(hour, minute):
    """
    Generate smooth temperature using a sinusoidal function based on time of day.
    """
    # Convert hour and minute to decimal hours for smoother transition
    time_decimal = hour + minute / 60.0

    # Define temperature pattern: cooler at night, warmer during the day
    day_temp_peak = 32  # Peak daytime temperature (around midday)
    night_temp_min = 24  # Minimum nighttime temperature
    temp_amplitude = (day_temp_peak - night_temp_min) / 2

    # Smooth temperature variation using a sine wave
    temperature = night_temp_min + temp_amplitude + temp_amplitude * np.sin((time_decimal - 6) * (np.pi / 12))
    return round(temperature, 2)

def generate_smooth_irradiance(hour, minute):
    """
    Generate smooth irradiance based on a Gaussian curve centered at noon.
    """
    # Convert hour and minute to decimal hours for smoother transition
    time_decimal = hour + minute / 60.0

    # Peak irradiance parameters
    peak_irradiance = 1000  # Max irradiance at noon
    std_dev = 3.5  # Standard deviation to control spread around noon

    # Smooth irradiance pattern
    irradiance = peak_irradiance * np.exp(-((time_decimal - 12) ** 2) / (2 * std_dev ** 2))
    return round(irradiance, 2)

def generate_temperature_irradiance_data_smooth(date_stamp):
    # Start at midnight
    current_time = datetime.strptime("00:00", "%H:%M")
    end_time = current_time + timedelta(days=1)

    # Store temperature and irradiance data
    temperature_data = []
    irradiance_data = []
    time_data = []

    while current_time < end_time:
        hour = current_time.hour
        minute = current_time.minute

        # Generate smooth temperature and irradiance
        temperature = generate_smooth_temperature(hour, minute)
        irradiance = generate_smooth_irradiance(hour, minute)

        # Append data to list
        time_data.append(current_time.strftime("%H:%M"))
        temperature_data.append(temperature)
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
end_date = "2020-12-31"  # Full year of data

# Generate daily timestamps
date_stamp = pd.date_range(start=start_date, end=end_date, freq='D')

# Initialize empty DataFrame to store all data
df_temp_irradiance_data = pd.DataFrame(columns=['Date', 'Time', 'Temp C', 'Irradiance W/m²'])

# Generate temperature and irradiance data for each day
df_list = []
for day in date_stamp:
    df_list.append(generate_temperature_irradiance_data_smooth(day))
df_temp_irradiance_data = pd.concat(df_list, ignore_index=True)

# Example plot for a single day to visualize the smooth temperature and irradiance pattern
example_day = '2020-01-03'  # Specify a single day
df_example_day = df_temp_irradiance_data[df_temp_irradiance_data['Date'] == example_day]

fig, ax1 = plt.subplots(figsize=(12, 6))

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
plt.title(f"Smooth Temperature and Irradiance for {example_day}")
plt.xticks(rotation=45)
plt.grid()
plt.show()
