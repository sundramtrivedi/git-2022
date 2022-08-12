
# run on the terminal pyspark 

strings = spark.read.text("test.txt")

filtered = strings.filter(strings.value.contains("Spark"))

filtered.count()