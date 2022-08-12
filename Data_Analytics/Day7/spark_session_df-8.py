from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
df = spark.read.csv('sales_info-2.csv', inferSchema = True, header = True)
group_data = df.groupBy ('Company')
group_data.agg ({'Sales' : 'sum'}).show ()