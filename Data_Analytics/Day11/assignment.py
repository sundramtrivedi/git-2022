# Use the Customers, Salespeople, and Orders datasets used in the class to solve the following:
# For each of the following, your code should be for data frame as well as Spark SQL.


from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("Datafram with 100% SQL").getOrCreate()

salespeople_file = "salespeople.txt"
df_salespeople = spark.read.format("csv").option("inferSchema", "true").option("header", "true").load(salespeople_file)

customers_file = "customers.txt"
df_customers = spark.read.format("csv").option("inferSchema", "true").option("header", "true").load(customers_file)

orders_file = "orders.txt"
df_orders = spark.read.format("csv").option("inferSchema", "true").option("header", "true").load(orders_file)

df_salespeople.createOrReplaceTempView("salespeople_tbl")
df_customers.createOrReplaceTempView("customers_tbl")
df_orders.createOrReplaceTempView("orders_tbl")


# 1. Find all the customers and salespeople who share a city (i.e. have common city).
spark.sql("""SELECT salespeople_tbl.sname, salespeople_tbl.city, salespeople_tbl.comm, customers_tbl.cnum, customers_tbl.cname, customers_tbl.city, customers_tbl.rating
                FROM salespeople_tbl
                INNER JOIN customers_tbl
                ON (salespeople_tbl.snum = customers_tbl.snum)
                WHERE salespeople_tbl.city = customers_tbl.city""").show()

df_salespeople.join(df_customers, df_salespeople.snum == df_customers.snum, "inner")\
                .filter(df_salespeople.city == df_customers.city).show()

# +------+--------+----+----+-------+--------+------+
# | sname|    city|comm|cnum|  cname|    city|rating|
# +------+--------+----+----+-------+--------+------+
# |  Peel|  London|0.12|2001|Hoffman|  London|   100|
# |Serres|San Jose|0.13|2003|    Liu|San Jose|   200|
# |  Peel|  London|0.12|2006|Clemens|  London|   100|
# +------+--------+----+----+-------+--------+------+


# 2. Find which customer is served by which salesperson. Display the customer name and salesperson name for all matching cases.
spark.sql("""SELECT customers_tbl.cname, salespeople_tbl.sname 
                FROM customers_tbl
                INNER JOIN salespeople_tbl
                ON (salespeople_tbl.snum = customers_tbl.snum)""").show()

df_salespeople.join(df_customers, df_salespeople.snum == df_customers.snum, "inner")\
                .select(df_customers.cname, df_salespeople.sname).show()

# +--------+-------+
# |   cname|  sname|
# +--------+-------+
# | Hoffman|   Peel|
# |Giovanni|Axelrod|
# |     Liu| Serres|
# |   Grass| Serres|
# | Clemens|   Peel|
# | Pereira| Motika|
# |Cisneros| Rifkin|
# +--------+-------+


# 3. Display all the order numbers along with the name of the customer who placed that order.
spark.sql("""SELECT orders_tbl.onum, customers_tbl.cname
                FROM orders_tbl
                INNER JOIN customers_tbl
                ON (orders_tbl.cnum = customers_tbl.cnum)""").show()

df_orders.join(df_customers, df_orders.cnum == df_customers.cnum, "inner")\
                .select(df_orders.onum, df_customers.cname).show()

# +----+--------+
# |onum|   cname|
# +----+--------+
# |3001|Cisneros|
# |3003| Hoffman|
# |3002| Pereira|
# |3005|     Liu|
# |3006|Cisneros|
# |3009|Giovanni|
# |3007|   Grass|
# |3008| Clemens|
# |3010|   Grass|
# |3011| Clemens|
# +----+--------+


# 4. Find how many orders have been brought by each salesperson. Display the salesperson number, name, and the number of orders in the descending sequence of orders. 
spark.sql("""SELECT salespeople_tbl.sname, COUNT(orders_tbl.onum) Total_Order
                FROM salespeople_tbl
                INNER JOIN orders_tbl
                ON (salespeople_tbl.snum = orders_tbl.snum)
                GROUP BY salespeople_tbl.sname
                ORDER BY Total_Order DESC""").show()

df_salespeople.join(df_orders, df_salespeople.snum == df_orders.snum, "inner")\
                .select(df_salespeople.sname)\
                .groupBy(df_salespeople.sname).count()\
                .orderBy(col("count").desc()).show()

# +-------+-----+
# |  sname|count|
# +-------+-----+
# | Serres|    3|
# |   Peel|    3|
# | Rifkin|    2|
# | Motika|    1|
# |Axelrod|    1|
# +-------+-----+


# 5. For every salesperson, find out the maximum order amount for each date.
spark.sql("""SELECT salespeople_tbl.sname, orders_tbl.odate, MAX(orders_tbl.amount)
                FROM orders_tbl
                INNER JOIN salespeople_tbl
                ON (salespeople_tbl.snum = orders_tbl.snum)
                GROUP BY salespeople_tbl.sname, orders_tbl.odate
                ORDER BY orders_tbl.odate""").show()

df_salespeople.join(df_orders, df_salespeople.snum == df_orders.snum, "inner")\
            .select(df_salespeople.sname, df_orders.odate)\
            .groupBy(df_salespeople.sname, df_orders.odate).max(df_orders.amount).show()

# +-------+-------------------+-----------+
# |  sname|              odate|max(amount)|
# +-------+-------------------+-----------+
# | Motika|1990-10-03 00:00:00|     1900.1|
# |   Peel|1990-10-03 00:00:00|     767.19|
# | Serres|1990-10-03 00:00:00|    5160.45|
# | Rifkin|1990-10-03 00:00:00|    1098.16|
# | Serres|1990-10-04 00:00:00|      75.75|
# |Axelrod|1990-10-04 00:00:00|    1713.23|
# |   Peel|1990-10-05 00:00:00|     4723.0|
# | Serres|1990-10-06 00:00:00|    1309.95|
# |   Peel|1990-10-06 00:00:00|    9891.88|
# +-------+-------------------+-----------+
