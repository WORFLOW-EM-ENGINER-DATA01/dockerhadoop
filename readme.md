# Installation du cluster hadoop / spark 

1) Lancez : ``` docker build ``` 
2) Lancez : ``` docker compose up -d ``` 
3) Vérifiez les différents ports mappés. 

## Problèmes courants :

### Le port 7077 est inaccessible : 

Assurez-vous que le port est correctement mappé dans docker-compose.yml.
Vérifiez que le Master écoute bien sur ce port en utilisant :

```netstat -tuln | grep 7077```

### Les Workers ne s'enregistrent pas :

Vérifiez que l'URL du Master dans SPARK_MASTER_URL est correcte.
Consultez les logs du Worker :

```docker logs spark-master```

### Erreur dans le fichier entrypoint.sh :

Assurez-vous que le fichier est exécutable :

```chmod +x entrypoint.sh```

### Dépendances manquantes (par exemple, jps) :

Vérifiez que le package Java est bien installé.