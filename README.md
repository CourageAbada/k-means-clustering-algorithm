# k-means-clustering-algorithm
This code is a k-means clustering algorithm implementation that uses birthrate and life expectancy data of countries to group them into clusters. The data is read from a CSV file, and the number of clusters and iterations are user-inputted. The code uses the Euclidean distance formula to calculate the distance between data points and the centroids of the clusters, and the mean of the data points in a cluster is calculated to be the new centroid. The clusters are then plotted on a graph with different colors, and the countries in each cluster are also printed out.

Dependencies

csv
matplotlib
numpy
random

Input

Name of the CSV file containing the data
Number of clusters to generate
Number of iterations to run the algorithm

Output

A graph displaying the clusters of countries based on birthrate and life expectancy
A list of countries in each cluster, along with the cluster's color and mean

Usage

Run the script in a python environment
Input the required values when prompted
The graph and lists of countries in each cluster will be displayed

Note

Make sure to have the dependencies installed in your environment
The CSV file should contain the following columns: 'Country', 'Birthrate', 'Life Expectancy'
The code uses the first line of the CSV file as the header and skips it while reading the data
The sample function used in this script randomly choose the centroid points, so the result may change every time the script runs


