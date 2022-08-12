import sys
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local", "test example")
    numbers = sc.parallelize([1, 7, 8, 9, 5, 77, 48])
    # min, max
    min = numbers.reduce(lambda a,b : min (a, b))
    max = numbers.reduce(lambda a,b : max (a, b))
    print("min is : %d" % min)
    print("max is : %d" % max)