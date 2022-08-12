# 1. Find salespeople located either in Barcelona or London

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
csv_file = "salespeople.txt"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").load(csv_file))
df.createOrReplaceTempView("salespeople_table")
spark.sql("""SELECT sname, city FROM salespeople_table WHERE city == \"Barcelona\" or city == \"London\"""").show()

# Using DataFrame

df.select(['sname', 'city']).filter((df.city == "Barcelona") | (df.city == "London")).show()