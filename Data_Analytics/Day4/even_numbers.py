import sys
from pyspark import SparkContext, SparkConf
sc = SparkContext("local", "Even numbers")
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
myOutput = rdd.filter(lambda x : (x % 2 == 0))
myDisplay = myOutput.collect()
print(myDisplay)
