# Import necessary libraries
from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "range RDD example")

# Create an RDD with range() transformation
range_rdd = sc.range(1, 10, 2)

# Print range RDD
print("Range RDD:", range_rdd.collect())

# Stop SparkContext
sc.stop()
