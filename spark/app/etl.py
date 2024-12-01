from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, lower

def clean_data_etl():
    try:
        # Créer une session Spark
        spark = SparkSession.builder \
            .appName("Clean NOAA Data") \
            .config("spark.hadoop.fs.defaultFS", "hdfs://namenode:9000") \
            .getOrCreate()

        # Lire les données depuis HDFS
        file_path = "hdfs://namenode:9000/data/sample.csv"
        raw_data = spark.read.csv(file_path, header=True, inferSchema=True)

        # Nettoyage des données
        cleaned_data = raw_data.withColumn("TEMP", (col("TEMP") - 32) * 5 / 9).withColumn("NAME", trim(lower(col("NAME")))).dropna()  # Suppression des lignes avec des valeurs manquantes
        
        # Sauvegarder les données nettoyées dans HDFS
        output_path = "hdfs://namenode:9000/data/cleaned_sample.csv"
        cleaned_data.write.csv(output_path, header=True)
        
        cleaned_data.show(5)  # Afficher les 5 premières lignes

        # Arrêter Spark
        spark.stop()

        return {"status": "success", "message": f"Cleaned data saved to {output_path}"} 

    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    clean_data_etl()
