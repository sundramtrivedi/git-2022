import sys
from pyspark import SparkContext, SparkConf
sc = SparkContext("local", "Pair RDD Example")
marks_rdd = sc.parallelize([('Rahul', 25), ('Swati', 26), ('Shreya', 22), ('Abhay', 29), ('Rohan', 22),
                            ('Rahul', 23), ('Swati', 19), ('Shreya', 28), ('Abhay', 26), ('Rohan', 22)])
mobile_rdd = sc.parallelize([('Rahul', '9871628793'), ('Swati', '7832651749'), ('Shreya', '9927384198')])
final_rdd = marks_rdd.join(mobile_rdd)
for key, value in final_rdd.collect():
    print(key, list(value))