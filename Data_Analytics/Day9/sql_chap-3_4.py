# 4. Display names and commissions of all the salespeople in London

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Basics').getOrCreate()
csv_file = "salespeople.txt"
df = (spark.read.format("csv").option("inferschema", "true").option("header", "true").load(csv_file))
df.createOrReplaceTempView("sales_people")
spark.sql("""SELECT sname, comm, city FROM sales_people WHERE city = \"London\"""").show()

# Using DataFrame

df.select(['sname', 'comm', 'city']).filter("city like '%London%'").show()

df.select(['sname', 'comm', 'city']).filter(df.city == "London").show()