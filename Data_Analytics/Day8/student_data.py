# 1. Calculate average year-wise marks (i.e. for 2 semesters for a year) for each student. Example : ['si1', 'year1', 43.2323]['si1', 'year2', 3423.3433]

import sys 

from pyspark import SparkContext, SparkConf

sc = SparkContext()

data = sc.textFile("student.txt")

dataLine = data.map(lambda l : l.split(','))

calculateYear = dataLine.map(lambda x : ([x[0], x[1], (float(x[2]) + float(x[3]))/2]))

# Convert into a Python list and print
for i in calculateYear.collect():
	print(i)

#print(calculateYear.collect())

# 2. Display all the averages only for the second year.

avg_second_year = dataLine.map(lambda x : ([x[0], x[1], (float(x[2]) + float(x[3]))/2])).filter(lambda x : x[1] != 'year1')

print(avg_second_year.collect())

# 3. Show sorted (highsest-to-lowest) average grades in the second year

sort_Year2_data = avg_second_year.sortBy(lambda x: x[2], ascending = False ).filter(lambda x : x[1] != 'year1').collect()

#sort_Year2_data = avg_second_year.sortBy(lambda x: -x[2]).filter(lambda x : x[1] != 'year1').collect()

print(sort_Year2_data)

# 4. Top three students who have the highest average grades in the second year.

top_three_student =  avg_second_year.takeOrdered(3,lambda x: -x[2])

print(top_three_student)

# 5. List of students who have higher average grade in the first year than their second year grade.



# 6. list of students who have consistently improved their scores (second higher than first, third higher than second, fourth higher than third).
