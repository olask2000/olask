import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Male', 'Male', 'Male',
               'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female',
               'Female', 'Female', 'Female', 'Female', 'Female', 'Female'],
    'Holding Duration': [60.75, 67.41, 42.19, 59.74, 52.64, 43.37, 73.27,
                         59.09, 51.15, 58.32, 22.22, 30.57, 17.47, 22.39,
                         26.90, 36.85, 27.33, 29.55, 13.87, 34.66],
    'Height': [184, 182, 180, 191, 189, 181, 180, 170, 176, 185, 175, 158,
               166, 175, 160, 165, 166, 170, 170, 172]
}

data_frame = pd.DataFrame(data)

plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.hist(data_frame['Holding Duration'], bins=10, color='teal', edgecolor='black', alpha=0.7)
plt.title('Distribution of Breath Holding Durations')
plt.xlabel('Breath Holding Duration (s)')
plt.ylabel('Count')


plt.subplot(1, 2, 2)

plt.scatter(data_frame[data_frame['Gender'] == 'Male']['Holding Duration'],
            [0] * sum(data_frame['Gender'] == 'Male'),
            color='blue', label='Male', alpha=0.6)


plt.scatter(data_frame[data_frame['Gender'] == 'Female']['Holding Duration'],
            [1] * sum(data_frame['Gender'] == 'Female'),
            color='pink', label='Female', alpha=0.6)


plt.title('Comparison of Breath Holding Durations by Gender')
plt.yticks([0, 1], ['Male', 'Female'])
plt.xlabel('Breath Holding Duration (s)')
plt.legend()


plt.tight_layout()
plt.show()