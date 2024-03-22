# Import necessary libraries
from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "RDD transformations")

# Create an RDD from a list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# map() transformation
rdd_map = rdd.map(lambda x: x * 2)

# flatMap() transformation
rdd_flatmap = rdd.flatMap(lambda x: (x, x * 2))

# filter() transformation
rdd_filter = rdd.filter(lambda x: x % 2 == 0)

# Stop SparkContext
sc.stop()
