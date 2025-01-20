# Databricks notebook source
# MAGIC %fs ls dbfs:/databricks-datasets/bikeSharing/data-001/

# COMMAND ----------

df = spark.read.csv(path= "dbfs:/databricks-datasets/bikeSharing/data-001/day.csv", header=True)
display(df)

# COMMAND ----------

df = spark.read \
.format("csv") \
.option("header", True) \
.option("inferSchema", True) \
.load("dbfs:/databricks-datasets/bikeSharing/data-001/day.csv")
display(df)

# COMMAND ----------

df.printSchema()

# COMMAND ----------

help(df.select)

# COMMAND ----------

display(df)

# COMMAND ----------

from pyspark.sql.functions import col
df1 = df.select(col("instant").alias("Instant"), df.dteday.alias("Date"), df["season"].alias("Season"))
display(df1)

# COMMAND ----------

display(df1.describe())

# COMMAND ----------

help(df.describe)

# COMMAND ----------

display(df1.describe(["Season"]))

# COMMAND ----------

# MAGIC %sql
# MAGIC
