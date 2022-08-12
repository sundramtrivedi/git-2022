import sys
from pyspark import SparkContext

sc = SparkContext()

total_Jobs_With_Balance = sc.textFile("bank.csv") \
                        .map(lambda x:(x.split(',')[1], int(x.split(',')[5])))

avg_Of_Blue_Collar = total_Jobs_With_Balance.filter(lambda x : (x[0] == "blue-collar")) \
                                            .groupByKey().mapValues(lambda x : sum(x) / len(x))

for ele in total_Jobs_With_Balance.collect():
    if(ele[1] > avg_Of_Blue_Collar.collect()[0][1]):
        print(ele)