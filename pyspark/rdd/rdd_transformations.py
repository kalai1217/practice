# Import necessary libraries
from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "RDD example")

# Create an RDD from a list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# Stop SparkContext
sc.stop()
