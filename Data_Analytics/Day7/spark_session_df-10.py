from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, format_number
spark = SparkSession.builder.appName('Basics').getOrCreate()
df = spark.read.csv('sales_info-2.csv', inferSchema = True, header = True)
sales_avg = df.select (avg ('Sales'). alias ('tempvar'))
sales_avg.select (format_number ('tempvar', 2). alias ('Average')). show()