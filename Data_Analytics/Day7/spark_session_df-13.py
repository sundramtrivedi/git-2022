from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Missing').getOrCreate()
df = spark.read.csv('containsNull.csv', inferSchema = True, header = True)
df.show()
# drop rows that have any null values columns
df.na.drop (). show()
# a row must have at least two non-null columns to appear in the table
df.na.drop (how = 'any'). show()
# drop rows that have any null value columns
df.na.drop (how = 'all'). show()
# drop rows that have a null value in the Sales columns
df.na.drop (subset = ["Sales"]). show()
# fill null values with our own value
df.na.fill ('DUMMY INSERT'). show()
# fill null values with zeroes for numeric columns
df.na.fill (0). show()
# fill null values only for name column with our own value
df.na.fill ('No name', subset = ['Name']). show()