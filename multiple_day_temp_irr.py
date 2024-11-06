import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt

def generate_smooth_temperature(hour, minute):
    """Generate smooth temperature using a sinusoidal function based on time of day."""
    time_decimal = hour + minute / 60.0
    day_temp_peak = 32  # Peak daytime temperature
    night_temp_min = 24  # Minimum nighttime temperature
    temp_amplitude = (day_temp_peak - night_temp_min) / 2
    temperature = night_temp_min + temp_amplitude + temp_amplitude * np.sin((time_decimal - 6) * (np.pi / 12))
    return round(temperature, 2)

def generate_smooth_irradiance(hour, minute):
    """Generate smooth irradiance based on a Gaussian curve centered at noon."""
    time_decimal = hour + minute / 60.0
    peak_irradiance = 1000  # Max irradiance at noon
    std_dev = 3.5  # Standard deviation to control spread around noon
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
end_date = "2020-01-05"  # Multiple days for visualization

# Generate daily timestamps
date_stamp = pd.date_range(start=start_date, end=end_date, freq='D')

# Initialize empty DataFrame to store all data
df_temp_irradiance_data = pd.DataFrame(columns=['Date', 'Time', 'Temp C', 'Irradiance W/m²'])

# Generate temperature and irradiance data for each day
df_list = []
for day in date_stamp:
    df_list.append(generate_temperature_irradiance_data_smooth(day))
df_temp_irradiance_data = pd.concat(df_list, ignore_index=True)

df_temp_data = df_temp_irradiance_data[['Date', 'Time', 'Temp C']]
df_irr_data = df_temp_irradiance_data[['Date', 'Time', 'Irradiance W/m²']]

print(df_temp_data.head(10))
print(df_irr_data.head(10))

df_temp_data.to_csv('temp_data.csv', index=False)
df_irr_data.to_csv('irradiance.csv', index=False)

'''
# Example plot for multiple days to visualize the smooth temperature and irradiance pattern
df_example_days = df_temp_irradiance_data[(df_temp_irradiance_data['Date'] >= '2020-01-01') & (df_temp_irradiance_data['Date'] <= '2020-01-05')]

fig, ax1 = plt.subplots(figsize=(12, 8))

# Plot temperature for each day
for date in df_example_days['Date'].unique():
    daily_data = df_example_days[df_example_days['Date'] == date]
    ax1.plot(daily_data['Time'], daily_data['Temp C'], label=f'Temperature ({date.strftime("%Y-%m-%d")})', alpha=0.7)

ax1.set_xlabel("Time")
ax1.set_ylabel("Temperature (°C)", color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Plot irradiance on secondary y-axis for the same days
ax2 = ax1.twinx()
for date in df_example_days['Date'].unique():
    daily_data = df_example_days[df_example_days['Date'] == date]
    ax2.plot(daily_data['Time'], daily_data['Irradiance W/m²'], linestyle='--', label=f'Irradiance ({date.strftime("%Y-%m-%d")})', alpha=0.5)

ax2.set_ylabel("Irradiance (W/m²)", color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Show legends and plot
fig.tight_layout()
plt.title("Smooth Temperature and Irradiance from January 1 to January 5, 2020")
plt.xticks(rotation=45)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.grid()
plt.show()
'''