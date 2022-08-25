import pandas as pd

dataset = pd.read_csv("iris.txt", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
dataset_list = dataset.values.tolist()
first_att_nan_counter = 0
second_att_nan_counter = 0
third_att_nan_counter = 0
forth_att_nan_counter = 0
fifth_att_nan_counter = 0
i = 0
j = 0
while i < 159:
    if j == 0:
        if pd.isna(dataset_list[i][j]):
            first_att_nan_counter += 1
    if j == 1:
        if pd.isna(dataset_list[i][j]):
            second_att_nan_counter += 1
    if j == 2:
        if pd.isna(dataset_list[i][j]):
            third_att_nan_counter += 1
    if j == 3:
        if pd.isna(dataset_list[i][j]):
            forth_att_nan_counter += 1
    if j == 4:
        if pd.isna(dataset_list[i][j]):
            fifth_att_nan_counter += 1
    if i == 158:
        if j != 4:
            i = 0
            j += 1
        else:
            i += 1
    else:
        i += 1


print("First attribute nan counter: " + str(first_att_nan_counter))
print("Second attribute nan counter: " + str(second_att_nan_counter))
print("Third attribute nan counter: " + str(third_att_nan_counter))
print("Forth attribute nan counter: " + str(forth_att_nan_counter))
print("Fifth attribute nan counter: " + str(fifth_att_nan_counter))
