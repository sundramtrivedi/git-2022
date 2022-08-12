import sys
from pyspark import SparkContext

sc = SparkContext()

total_Type = sc.textFile("bank.csv") \
        .map(lambda x:(x.split(',')[1], int(x.split(',')[5]))) \
        .reduceByKey(lambda x, y : x + y).collect()

each_Total = sc.textFile("bank.csv") \
        .map(lambda x:(x.split(',')[1], 1)) \
        .reduceByKey(lambda x, y : x + y).collect()

print(total_Type)

print("\r")

for ele in range(len(each_Total)):
    print("(" + str(each_Total[ele][0]) + ", " + str(total_Type[ele][1] / each_Total[ele][1]) + ")")


####################################################################################################

selectBankFields = bankLines.map(lambda x : (x[1], int(x[5])))
grouped_sum = selectBankFields.reduceByKey(lambda a, b : a + b)

for ele in grouped_sum.collect():
    print(ele)

grouped_avg = selectBankFields.groupByKey().mapValues(lambda x : sum(x) / len(x))

for ele in grouped_avg.collect():
    print(ele)
