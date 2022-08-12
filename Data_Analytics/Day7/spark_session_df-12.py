from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName('Basics').getOrCreate()
df = spark.read.csv('sales_info-2.csv', inferSchema = True, header = True)
# only asc
df.orderBy("Sales"). show()
# another syntax - asc and desc
df.orderBy (col('Sales').asc()).show ()
df.orderBy (col('Sales').desc()).show ()
# yet another syntax 
df.orderBy (df['Sales'].asc()).show ()
df.orderBy (df['Sales'].desc()).show ()