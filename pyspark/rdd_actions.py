# Import necessary libraries
from pyspark import SparkContext
from operator import add

# Create a SparkContext
sc = SparkContext("local", "RDD actions")

# Create an RDD from a list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)

# collect() action
collected_data = rdd.collect()

# take() action
taken_data = rdd.take(3)

# top() action
top_data = rdd.top(3)

# count() action
count = rdd.count()

# min() action
min_value = rdd.min()

# max() action
max_value = rdd.max()

# mean() action
mean_value = rdd.mean()

# reduce() action
sum_result = rdd.reduce(add)

# countByKey() action
key_value_rdd = sc.parallelize([('a', 1), ('b', 2), ('a', 3), ('c', 4), ('b', 5)])
count_by_key = key_value_rdd.countByKey()

# countByValue() action
count_by_value = rdd.countByValue()

# fold() action
fold_result = rdd.fold(0, add)

# Stop SparkContext
sc.stop()
