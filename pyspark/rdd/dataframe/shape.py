from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("SparkByExamples.com") \
    .getOrCreate()
data = [('csk', 50), ('rcb', 45), ('mi', 54),('kkr',34)] 
sparkDF=spark.createDataFrame(data,["name","age"]) 
sparkDF.printSchema()
sparkDF.show()

print((sparkDF.count(), len(sparkDF.columns)))

def sparkShape(dataFrame):
    return (dataFrame.count(), len(dataFrame.columns))
import pyspark
pyspark.sql.dataframe.DataFrame.shape = sparkShape
print(sparkDF.shape())

import pandas as pd    
pandasDF=sparkDF.toPandas()
print(pandasDF.shape)
