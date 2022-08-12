# Fields in the input file are age, job, marital status, education, default, balance, housing loan, personal loan

# 3. Find the average balance of blue-collar divorced people

from pyspark import SparkContext

sc = SparkContext()

output = sc.textFile("bank.csv") \
        .map(lambda x : (x.split(',')[1], x.split(',')[2], 1)) \
        .filter(lambda x : (x[0] == 'blue-collar' and x[1] == 'divorced')) 

final = output.map(lambda x : (x[0], x[2])) \
        .reduceByKey(lambda x, y : x + y)

print(final.collect())