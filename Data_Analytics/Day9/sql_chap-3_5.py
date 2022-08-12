# 5. Display customers whose rating is 100

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
csv_file = "customers.txt"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").load(csv_file))
df.createOrReplaceTempView("customers_table")
spark.sql("""SELECT cname, rating FROM customers_table WHERE rating == 100""").show()

# Using DataFrame

df.select(['cname', 'rating']).filter(df.rating == 100).show()