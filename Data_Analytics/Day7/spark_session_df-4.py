from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
df = spark.read.csv ('appl_stock.csv', inferSchema = True, header = True)
df.filter ((df ['Close'] < 500) & (df['Open'] > 200)).select(['Open', 'Close']).show(10000)