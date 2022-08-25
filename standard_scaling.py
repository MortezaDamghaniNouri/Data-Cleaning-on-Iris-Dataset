import pandas as pd
from sklearn import preprocessing
import math

# This function prints the elements of the input dataset
def dataset_printer(input_dataset):
    for item in input_dataset:
        print(item)



dataset = pd.read_csv("iris.txt", names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'target'])
dataset_list = dataset.dropna().values.tolist()
i = 0
while i < 150:
    if dataset_list[i][4] == "Iris-setosa":
        dataset_list[i][4] = 0
    if dataset_list[i][4] == "Iris-versicolor":
        dataset_list[i][4] = 1
    if dataset_list[i][4] == "Iris-virginica":
        dataset_list[i][4] = 2
    i += 1

scaled_dataset = preprocessing.StandardScaler().fit_transform(dataset_list)
# print(scaler)
i = 0
j = 0
first_mean = 0
second_mean = 0
third_mean = 0
forth_mean = 0
fifth_mean = 0
main_sum = 0
first_variance = 0
second_variance = 0
third_variance = 0
forth_variance = 0
fifth_variance = 0
while j <= 4:
    while i < len(dataset_list):
        main_sum += dataset_list[i][j]
        i += 1
    i = 0
    if j == 0:
        first_mean = main_sum / len(dataset_list)
    if j == 1:
        second_mean = main_sum / len(dataset_list)
    if j == 2:
        third_mean = main_sum / len(dataset_list)
    if j == 3:
        forth_mean = main_sum / len(dataset_list)
    if j == 4:
        fifth_mean = main_sum / len(dataset_list)
    main_sum = 0
    j += 1

j = 0
while j <= 4:
    while i < len(dataset_list):
        if j == 0:
            main_sum += math.pow((first_mean - dataset_list[i][j]), 2)
        if j == 1:
            main_sum += math.pow((second_mean - dataset_list[i][j]), 2)
        if j == 2:
            main_sum += math.pow((third_mean - dataset_list[i][j]), 2)
        if j == 3:
            main_sum += math.pow((forth_mean - dataset_list[i][j]), 2)
        if j == 4:
            main_sum += math.pow((fifth_mean - dataset_list[i][j]), 2)
        i += 1
    i = 0
    if j == 0:
        first_variance = main_sum / len(dataset_list)
    if j == 1:
        second_variance = main_sum / len(dataset_list)
    if j == 2:
        third_variance = main_sum / len(dataset_list)
    if j == 3:
        forth_variance = main_sum / len(dataset_list)
    if j == 4:
        fifth_variance = main_sum / len(dataset_list)
    main_sum = 0
    j += 1

print("First mean: " + str(first_mean))
print("Second mean: " + str(second_mean))
print("Third mean: " + str(third_mean))
print("Forth mean: " + str(forth_mean))
print("Fifth mean: " + str(fifth_mean))
print("First variance: " + str(first_variance))
print("Second variance: " + str(second_variance))
print("Third variance: " + str(third_variance))
print("Forth variance: " + str(forth_variance))
print("Fifth variance: " + str(fifth_variance))
j = 0
first_new_mean = 0
second_new_mean = 0
third_new_mean = 0
forth_new_mean = 0
fifth_new_mean = 0
first_new_variance = 0
second_new_variance = 0
third_new_variance = 0
forth_new_variance = 0
fifth_new_variance = 0
while j <= 4:
    while i < len(scaled_dataset):
        main_sum += scaled_dataset[i][j]
        i += 1
    i = 0
    if j == 0:
        first_new_mean = main_sum / len(scaled_dataset)
    if j == 1:
        second_new_mean = main_sum / len(scaled_dataset)
    if j == 2:
        third_new_mean = main_sum / len(scaled_dataset)
    if j == 3:
        forth_new_mean = main_sum / len(scaled_dataset)
    if j == 4:
        fifth_new_mean = main_sum / len(scaled_dataset)
    main_sum = 0
    j += 1
j = 0
while j <= 4:
    while i < len(scaled_dataset):
        if j == 0:
            main_sum += math.pow((first_new_mean - scaled_dataset[i][j]), 2)
        if j == 1:
            main_sum += math.pow((second_new_mean - scaled_dataset[i][j]), 2)
        if j == 2:
            main_sum += math.pow((third_new_mean - scaled_dataset[i][j]), 2)
        if j == 3:
            main_sum += math.pow((forth_new_mean - scaled_dataset[i][j]), 2)
        if j == 4:
            main_sum += math.pow((fifth_new_mean - scaled_dataset[i][j]), 2)
        i += 1
    i = 0
    if j == 0:
        first_new_variance = main_sum / len(scaled_dataset)
    if j == 1:
        second_new_variance = main_sum / len(scaled_dataset)
    if j == 2:
        third_new_variance = main_sum / len(scaled_dataset)
    if j == 3:
        forth_new_variance = main_sum / len(scaled_dataset)
    if j == 4:
        fifth_new_variance = main_sum / len(scaled_dataset)
    main_sum = 0
    j += 1
print("======================================================")
print("First new mean: " + str(first_new_mean))
print("Second new mean: " + str(second_new_mean))
print("Third new mean: " + str(third_new_mean))
print("Forth new mean: " + str(forth_new_mean))
print("Fifth new mean: " + str(fifth_new_mean))
print("First new variance: " + str(first_new_variance))
print("Second new variance: " + str(second_new_variance))
print("Third new variance: " + str(third_new_variance))
print("Forth new variance: " + str(forth_new_variance))
print("Fifth new variance: " + str(fifth_new_variance))



