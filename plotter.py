import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("iris.txt", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
dataset_list = dataset.dropna().values.tolist()
i = 0
j = 0
new_dataset_list = []
while i < len(dataset_list):
    temp = []
    while j <= 3:
        temp.append(dataset_list[i][j])
        j += 1
    new_dataset_list.append(temp)
    j = 0
    i += 1
first_list = []
second_list = []
third_list = []
forth_list = []
i = 0
while j <= 3:
    temp = []
    i = 0
    while i < len(new_dataset_list):
        temp.append(new_dataset_list[i][j])
        i += 1
    if j == 0:
        for i in temp:
            first_list.append(i)
    if j == 1:
        for i in temp:
            second_list.append(i)
    if j == 2:
        for i in temp:
            third_list.append(i)
    if j == 3:
        for i in temp:
            forth_list.append(i)
    j += 1




# Creating plot
plt.boxplot(first_list)
# plt.boxplot(second_list)
# plt.boxplot(third_list)
# plt.boxplot(forth_list)

# show plot
plt.show()
















