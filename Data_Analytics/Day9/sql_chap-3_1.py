# 1. Find all the details about salespeople

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
csv_file = "salespeople.txt"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").load(csv_file))
df.createOrReplaceTempView("sales_people")
spark.sql("""SELECT snum, city, comm FROM sales_people""").show()

# OR

from pyspark.sql import SparkSession
spark = (SparkSession.builder.appName("UnderstandingSQLChapter3").getOrCreate())
csv_file = "salespeople.txt"
schema = "`snum` INT, `sname` STRING, `city` STRING, `comm` FLOAT"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").schema(schema).load(csv_file))
df.createOrReplaceTempView("sales_people")
spark.sql("""SELECT snum, city, comm FROM sales_people""").show()