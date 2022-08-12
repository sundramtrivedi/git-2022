# Calculate average age and print
# The corresponding Dataframe example is rddVersusdf-2.py

from pyspark import SparkContext

sc = SparkContext()

dataRDD = sc.parallelize ([("Sachin", 49), ("Rahul", 51), ("MSD", 40), ("Rahul", 41), ("MSD", 30), ("Sunil", 63)])

agesRDD = (dataRDD .map (lambda x : (x[0], (x[1], 1))) .reduceByKey (lambda x, y : (x[0] + y[0], x[1] + y[1]))
			.map (lambda x : (x[0], x[1][0] / x[1][1])))

print (agesRDD.collect())