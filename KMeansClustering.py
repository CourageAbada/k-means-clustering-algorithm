import csv                              # reading the data file
import matplotlib.pyplot as plt         # will help to plot the graph 
import numpy as np                      # will help to do the math from the data
from random import sample               # will help to find and initialize the clusters that we need to calculate the distance of the values

# opening and reading the csv file
def read_csv(path):
    csv_content = csv.reader(open(path, "r"))
    next(csv_content)
    country_names_list = []
    data_point_list = []

    for record in csv_content:
        country_names_list.append(record[0])
        data_point_list.append([float(record[1]), float(record[2])])

    return country_names_list, data_point_list

# using the euclidean distance function to calculate the distance between two points
# the numpy version in python will calculate the square value
def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# using the two x and y values to calculate the square root of the value
def x_and_y(data):
    return [data_point[0] for data_point in data], [data_point[1] for data_point in data]

# calculating the mean of the two x and y values
def calculate_mean(cluster):
    x_data, y_data = x_and_y(cluster)
    return [sum(x_data) / len(cluster), sum(y_data) / len(cluster)]


if __name__ == "__main__":

    # ask user for input of values
    filename = input("Name Of CSV File: ")
    sample_clusters = int(input("How many clusters would you like to generate? "))
    iteration_end = int(input("How many iterations would you like? "))

    # defining the variables
    country_names, data = read_csv(filename)
    iteration_index = 0
    clusters = []
    colors = ["Red", "Green", "Purple", "Yellow", "Blue"]
    centroids = sample(data, sample_clusters)

    while iteration_index != iteration_end:

        clusters = [[] for i in range(sample_clusters)]

        for data_point_index, data_point in enumerate(data):
            # print(f"{data_point_index}) {data_point}, center points = {centroids}, iteration = {iteration_index}")
            data_point_centroid_distance = [euclidean_distance(data_point, centroid) for centroid in centroids]
            clusters[data_point_centroid_distance.index(min(data_point_centroid_distance))].append(data_point)

        centroids = [calculate_mean(clusters[i]) for i in range(sample_clusters)]

        iteration_index += 1

    # displaying the birthrate and life expectancy clusters in the graph form
    plt.xlabel("Birthrate")
    plt.ylabel("Life Expectancy")

    # initializing the clusters from the user input
    for i in range(sample_clusters):
        x, y = x_and_y(clusters[i])
        plt.scatter(x, y, c=colors[i], label="#")
        print(f"\n\t\tCountries for Cluster {i + 1} with a Colour of {colors[i]} and a Mean of {centroids[i]}:")
        for dp in clusters[i]:
            index_val = data.index(dp)
            print(country_names[index_val])

    # displaying the data from the countries in a graph format
    plt.show()