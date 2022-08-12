# Fields in the input file are age, job, marital status, education, default, balance, housing loan, personal loan

# 4. average

from pyspark import SparkContext

sc = SparkContext()

output = sc.textFile("bank.csv") \
        .map(lambda x : (x.split(',')[1], x.split(',')[2], int(x.split(',')[5]), 1)) \
        .filter(lambda x : (x[0] == 'blue-collar' and x[1] == 'divorced')) 

count = output.map(lambda x : (x[0], x[3])) \
        .reduceByKey(lambda x, y : x + y)

# print(output.collect())
print(count.collect())

final = output.map(lambda x : (x[0], x[2])) \
        .reduceByKey(lambda x, y : x + y)

average = final.collect()[0][1] / count.collect()[0][1]

print(final.collect())

print("Average = %d" % average)
