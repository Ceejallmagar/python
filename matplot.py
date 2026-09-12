import matplotlib.pyplot as plt
import numpy as np

# x=[4,3,1,4,7,783,]
# y=[433,123,6,74,6,1]
# plt.plot(x,y, color="blue", marker="o",linestyle="--")
# plt.title("company growth")
# plt.xlabel("hell")
# plt.ylabel("heven")
# plt.show()
# x_data=np.random.rand(50)
# y_data=np.random.rand(50)

# plt.scatter(x_data,y_data)
# plt.title("scattered data")
# plt.show()


#bar diagram

# data=["c","python","js","rust","ruby"]
# point=[10,50,45,29,43]
# plt.bar(data,point, color="green",alpha=0.1)
# plt.xlabel("hell")
# plt.show()

# ages = np.random.normal(30, 5, 200) # Mean age 30, deviation 5

# plt.hist(ages, bins=15, color='orange', edgecolor='white')
# plt.title("Age Distribution")
# # plt.show()

# print(ages)
# point=[10,50,45,29,43]

# plt.hist(point)
# plt.show()

sizes = [40, 30, 20, 10]
labels = ['Rent', 'Food', 'Utilities', 'Savings']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Monthly Budget Breakdown")
plt.show()
