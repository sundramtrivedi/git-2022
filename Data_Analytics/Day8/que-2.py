# 2. Display all the averages only for the second year (df-2.py)

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
result_df.filter(df['year'] == 'year2').show()

# OR

from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, IntegerType, FloatType, StructType
from pyspark.sql.functions import format_number, col
spark = SparkSession.builder.appName("Python Spark data frame example").getOrCreate()
data_schema =   [
                    StructField ('student_id', StringType(), True),
                    StructField ('year', StringType(), True),
                    StructField ('sem_1', FloatType(), True),
                    StructField ('sem_2', FloatType(), True)
                ]
final_struct = StructType (fields = data_schema)
df = spark.read.csv("student.txt", header = False, schema = final_struct)
filter_df = df.filter(col('year') == 'year2')
result_df = filter_df.select ('student_id', 'year', format_number(((df['sem_1'] + df['sem_2']) / 2), 2).alias ("Avg Marks"))
result_df.show()