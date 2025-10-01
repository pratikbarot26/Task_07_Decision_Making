import pandas as pd
import matplotlib.pyplot as plt

# Task_05 verified data
data = {
    'Year': ['2021', '2024'],
    'Yards_Per_Game': [366.5, 467.6],
    'Points_Per_Game': [24.9, 34.1],
    'Plays_Per_Game': [64.8, 76.9],
    'Attendance': [32461, 39130]
}

df = pd.DataFrame(data)

# Plot Attendance with legend for both years
fig, ax = plt.subplots()
bars = ax.bar(df['Year'], df['Attendance'], color=['orange','blue'])
ax.set_title('Average Attendance')
ax.set_ylabel('Attendance')
ax.set_xlabel('Year')
ax.legend(bars, ['2021', '2024'], title='Year')  # Legend now correctly shows both years
plt.xticks(rotation=0)
plt.savefig('../appendices/Visualizations/Attendance.png')
plt.close()