from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
df = spark.read.csv('sales_info-2.csv', inferSchema = True, header = True)
df.orderBy("Sales").show()
# better syntax
df.orderBy (df["Sales"].asc ()).show()
df.orderBy (df["Sales"].desc ()).show()