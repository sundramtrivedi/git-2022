# Use DataFrames
# You are given data indicating student grades for a teo-year (four-semester) course
# Seven students are enrolled in this courseThe 'student.txt' file depicts two year of gradedata, divided into semesters,
# for 
# Fields are : student id, year, semester 1 marks, semester 2 marks
# 1. Calculate average year-wise marks (i.e. for 2 semesters for a year) for each student (df-1.py)

from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, IntegerType, FloatType, StructType
from pyspark.sql.functions import format_number
spark = SparkSession \
        .builder \
        .appName("Python Spark data frame example") \
        .getOrCreate()
data_schema =   [
                    StructField ('student_id', StringType(), True),
                    StructField ('year', StringType(), True),
                    StructField ('sem_1', FloatType(), True),
                    StructField ('sem_2', FloatType(), True)
                ]
final_struct = StructType (fields = data_schema)
df = spark.read.csv("student.txt", header = False, schema = final_struct)
result_df = df.select ('student_id', 'year', format_number(((df['sem_1'] + df['sem_2']) / 2), 2).alias ("Avg Marks"))
result_df.show()