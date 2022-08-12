from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
df = spark.read.json('people.json')
df.show()
# df.printSchema()
# print(df.describe())
# df.describe().show()