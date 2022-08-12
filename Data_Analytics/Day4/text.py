import sys
print("Hello")
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    # create spark context with spark configuration
    conf = SparkContext(). setAppName("Read Text to RDD - Python")
    sc = SparkContext(conf=conf)

    # read input text file to RDD
    numbers = sc.parallelize([1, 2, 4, 5, 5, 5, 6, 7, 9, 10])

    # filtered data
    filteredData = numbers.filter(lambda x : x != 5).collect()

    # now distinct data
    for num in filterData:
        print('%i '% (num))