from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
csv_file = "sales_info-2.csv"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").load(csv_file))
df.createOrReplaceTempView("sales_info_table")
spark.sql("""SELECT Company, AVG(Sales) AS Mean FROM sales_info_table GROUP BY Company""").show()