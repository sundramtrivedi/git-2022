# Fields in the input file are age, job, marital status, education, default, balance, housing loan, personal loan

# 1. count number of users for every age

from pyspark import SparkContext
sc = SparkContext()
output = sc.textFile("bank.csv") \
        .map(lambda x : (x.split(',')[0], 1)) \
        .reduceByKey(lambda x, y : x + y)
print(output.collect())