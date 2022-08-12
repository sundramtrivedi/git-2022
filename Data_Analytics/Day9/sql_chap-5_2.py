# 2. Find salespeople who earn commission in the range of .10 and .12

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
csv_file = "salespeople.txt"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").load(csv_file))
df.createOrReplaceTempView("salespeople_table")
spark.sql("""SELECT sname, comm FROM salespeople_table WHERE comm > .10 and comm < .12""").show()

# Using DataFrame

df.select(['sname', 'comm']).filter((df.comm > .10) & (df.comm < .12)).show()