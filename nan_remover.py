import pandas as pd

dataset = pd.read_csv("iris.txt", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
print(len(dataset.dropna()))
dataset_list = dataset.dropna().values.tolist()
print(len(dataset_list))
for i in dataset_list:
    print(i)

































