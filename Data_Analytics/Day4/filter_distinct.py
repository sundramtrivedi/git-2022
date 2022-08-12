import sys
from pyspark import SparkContext, SparkConf
sc = SparkContext("local", "Filter Example")
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 4, 2, 8, 9, 12, 1, 2, 3, 4, 5, 1, 2, 4, 5, 7, 8, 2, 3, "Hello", "Hi", "Hello", "Welcome", "Hi", "hello", "hi"]) 
output = rdd.distinct().collect()
print(output)