# 8. List of students whose second year aggregate is higher than that of the first year ...

import sys

from pyspark import SparkContext, SparkConf

sc = SparkContext()

data = sc.textFile("student.txt")

dataLine = data.map(lambda l : l.split(','))

first_year_marks = dataLine.filter(lambda x : x[1] == 'year1')

first_year_marks_mean = first_year_marks.map(lambda x : [x[0], x[1], (float(x[2]) + float(x[3])) / 2])

first_year_marks_mean_list = first_year_marks_mean.collect()

second_year_marks = dataLine.filter(lambda x : [x[0], x[1], (float (x[2]) + float(x[3])) / 2])

second_year_marks_mean = second_year_marks.map(lambda x : [x[0], x[1], (float(x[2]) + float(x[3])) / 2])

second_year_marks_mean_list = second_year_marks_mean.collect()

i = 0

print("List of students whose second year aggregate is higher than that of the first year ...")

for first_list_element in first_year_marks_mean_list:

    second_list_element = second_year_marks_mean_list [i]

    if (second_list_element [2] > first_list_element [2]):

        print("Student : %s, Second Year Aggregate : %f, First Year Aggregate : %f" % (first_list_element [0], second_list_element [2], first_list_element [2]))

        i += 1

# OR

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

ans1 = result_df.filter(df['year'] == 'year1')

first_year = ans1.orderBy (ans1['Avg Marks'].desc()).collect()

ans2 = result_df.filter(df['year'] == 'year2')

second_year = ans2.orderBy (ans2['Avg Marks'].desc()).collect()

i = 0

print("List of students whose second year aggregate is higher than that of the first year ...")

for first_list_element in first_year:

    second_list_element = second_year [i]

    if (second_list_element [2] > first_list_element [2]):

        print("Student : %s, Second Year Aggregate : %f, First Year Aggregate : %f" % (first_list_element [0], second_list_element [2], first_list_element [2]))

        i += 1
