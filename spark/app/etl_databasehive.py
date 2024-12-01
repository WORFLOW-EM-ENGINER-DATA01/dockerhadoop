from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower

def clean_data_etl_with_sql():
    try:
        # Créer une session Spark avec le support Hive
        spark = SparkSession.builder \
            .appName("Clean NOAA Data") \
            .config("spark.hadoop.fs.defaultFS", "hdfs://namenode:9000") \
            .enableHiveSupport() \
            .getOrCreate()

        # Créer la table Hive si elle n'existe pas
        spark.sql("""
            CREATE TABLE IF NOT EXISTS weather_data (
                STATION STRING,
                DATE STRING,
                LATITUDE DOUBLE,
                ...
                FRSHTT STRING
            )
            ROW FORMAT DELIMITED
            FIELDS TERMINATED BY ','
            STORED AS TEXTFILE
            LOCATION 'hdfs://namenode:9000/data/weather_data'
        """)

        # Lire les données depuis HDFS
        file_path = "hdfs://namenode:9000/data/sample.csv"
        raw_data = spark.read.csv(file_path, header=True, inferSchema=True)

        # Nettoyage des données
        cleaned_data = raw_data.withColumn("TEMP", (col("TEMP") - 32) * 5 / 9) \
                               .withColumn("NAME", trim(lower(col("NAME")))) \
                               .dropna()  # Suppression des lignes avec des valeurs manquantes
        
        # Insérer les données nettoyées dans la table Hive
        cleaned_data.write.mode("overwrite").insertInto("weather_data")

        cleaned_data.show(5)  # Afficher les 5 premières lignes

        # Arrêter Spark
        spark.stop()

        return {"status": "success", "message": "Cleaned data saved to Hive"}

    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    clean_data_etl_with_sql()
