# 3. Show sorted (highest-to-lowest) average grades in the second year (df-3.py)

from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, IntegerType, FloatType, StructType
from pyspark.sql.functions import format_number
spark = SparkSession.builder.appName("Python Spark data frame example").getOrCreate()
data_schema =   [
                    StructField ('student_id', StringType(), True),
                    StructField ('year', StringType(), True),
                    StructField ('sem_1', FloatType(), True),
                    StructField ('sem_2', FloatType(), True)
                ]
final_struct = StructType (fields = data_schema)
df = spark.read.csv("student.txt", header = False, schema = final_struct)
result_df = df.select ('student_id', 'year', format_number(((df['sem_1'] + df['sem_2']) / 2), 2).alias ("Avg Marks"))
ans = result_df.filter(df['year'] == 'year2')
ans.orderBy (ans['Avg Marks'].desc()).show()