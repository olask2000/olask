import pandas as pd
import matplotlib.pyplot as plt


growth_data = {
    'With Music': [304, 317, 332, 299, 0, 257, 387, 308, 206, 0, 174,  47, 317, 278, 0,
                   214,  157, 286, 188, 0, 69, 0, 236, 43, 0],
    'Without Music': [292, 292, 282, 3, 94, 270, 364, 149, 324, 164, 47, 316, 274, 2, 0,
                      288, 287, 319, 128, 0, 324, 75, 213, 219, 0,]
}


data_frame = pd.DataFrame(growth_data)


plt.figure(figsize=(12, 6))


plt.subplot(1, 2, 1)
plt.hist(data_frame['With Music'], bins=10, color='orange', alpha=0.6, edgecolor='black')
plt.title('Growth Histogram with Music')
plt.xlabel('Growth Measurement')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.7)


plt.subplot(1, 2, 2)
plt.hist(data_frame['Without Music'], bins=10, color='green', alpha=0.6, edgecolor='black')
plt.title('Growth Histogram without Music')
plt.xlabel('Growth Measurement')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.7)


plt.tight_layout()
plt.show()


plt.figure(figsize=(11, 5))


plt.subplot(1, 2, 1)
plt.scatter(data_frame['With Music'], [0] * len(data_frame['With Music']), color='orange', alpha=0.6)
plt.title('Dot Plot of Growth with Music')
plt.yticks([])
plt.xlabel('Growth Measurement')
plt.axhline(0, color='black', lw=0.5)


plt.subplot(1, 2, 2)
plt.scatter(data_frame['Without Music'], [0] * len(data_frame['Without Music']), color='green', alpha=0.6)
plt.title('Dot Plot of Growth without Music')
plt.yticks([])
plt.xlabel('Growth Measurement')
plt.axhline(0, color='black', lw=0.5)

plt.tight_layout()
plt.show()