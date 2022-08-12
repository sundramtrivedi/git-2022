# Fields in the input file are age, job, marital status, education, default, balance, housing loan, personal loan

# 2. Find the total number of married, single and divorced people

from pyspark import SparkContext
sc = SparkContext()
output = sc.textFile("bank.csv") \
        .map(lambda x : (x.split(',')[2], 1)) \
        .reduceByKey(lambda x, y : x + y)
print(output.collect())

# Fields in the input file are age, job, marital status, education, default, balance, housing loan, personal loan

# 2. Find the total number of married and divorced people

# from pyspark import SparkContext
# sc = SparkContext()
# output = sc.textFile("bank.csv") \
#         .map(lambda x : (x.split(',')[2], 1)) \
#         .filter(lambda x : x[0] != 'single') \
#         .reduceByKey(lambda x, y : x + y)
# print(output.collect())