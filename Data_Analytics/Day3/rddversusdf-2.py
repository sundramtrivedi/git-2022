# Calculate average age and print
# The corresponding RDD example is rddVersusdf-1.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = (SparkSession .builder .appName ("AuthorsAge") .getOrCreate())

data_df = spark.createDataFrame([("Sachin", 49), ("Rahul", 51), ("MSD", 40), ("Sunil", 73), ("Sachin", 39), ("Rahul", 41), ("MSD", 30), ("Sunil", 63)], ["name", "age"])

avg_df = data_df.groupBy ("name") .agg (avg ("age"))

avg_df.show ()