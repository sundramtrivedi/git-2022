import sys
from pyspark import SparkContext

sc = SparkContext()

all_Data = sc.textFile("student.txt") \
            .map(lambda x : (x.split(",")[0], x.split(",")[1],(float(x.split(",")[2]) + float(x.split(",")[3])) / 2))

for ele in all_Data.collect():
    print(ele)