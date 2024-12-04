import matplotlib.pyplot as plt

toppings = ['Mushroom', 'Pineapple', 'Prawns', 'Sausage', 'Spinach']
proportions = [0.17, 0.3, 0.0867, 0.187, 0.3]

plt.barh(toppings, proportions, color='purple')

plt.title('Toppings Proportion Bar Chart')
plt.xlabel('Proportion of Total')

plt.show()