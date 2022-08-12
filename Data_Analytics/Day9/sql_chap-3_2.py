# 2. Do the same thing by using the * syntax

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
csv_file = "salespeople.txt"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").load(csv_file))
df.createOrReplaceTempView("sales_people")
spark.sql("""SELECT * FROM sales_people""").show()