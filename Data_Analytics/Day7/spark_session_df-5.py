from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
df = spark.read.csv ('appl_stock.csv', inferSchema = True, header = True)
# collect () will store the results into a Python List
filtered = df.filter (df['Low'] == 197.16).collect()
print(filtered)