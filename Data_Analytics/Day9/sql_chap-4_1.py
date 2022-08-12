# 1. Display all the customers in San Jose whose rating is above 200

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
csv_file = "customers.txt"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").load(csv_file))
df.createOrReplaceTempView("customers_table")
spark.sql("""SELECT cname, city, rating FROM customers_table WHERE rating > 200 and  city == \"San Jose\"""").show()

# Using DataFrame

df.select(['cname', 'city', 'rating']).filter((df.rating > 200) & (df.city == "San Jose")).show()