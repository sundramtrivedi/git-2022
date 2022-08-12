import sys
from pyspark import SparkContext

sc = SparkContext()

all_Data = sc.textFile("student.txt") \
            .map(lambda x : (x.split(",")[0], x.split(",")[1], \
                (float(x.split(",")[2]) +float(x.split(",")[3]) / 2)))

second_Year_Only = all_Data.filter(lambda x : (x[1] == "year2"))

for ele in second_Year_Only.collect():
    print(ele)