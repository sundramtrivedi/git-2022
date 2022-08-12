# 3. Show only the salepeople names and commissions

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
csv_file = "salespeople.txt"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").load(csv_file))
df.createOrReplaceTempView("sales_people")
spark.sql("""SELECT sname, comm FROM sales_people""").show()

# Using DataFrame

df.select(['sname', 'comm']).show()