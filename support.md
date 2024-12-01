### **Structure du Dépôt GitHub : dockerhadoop**

Ce dépôt contient un ensemble de configurations pour mettre en place un environnement Hadoop distribué en utilisant Docker. Voici les composants principaux et comment ils sont configurés :

---

### **1. Docker et Docker Compose**
#### **Description**
Dans ce dépôt, Docker est utilisé pour conteneuriser chaque service Hadoop (comme le NameNode et le DataNode), ce qui permet de créer un environnement distribué facilement. Docker Compose est un outil qui permet de définir et de gérer des applications multi-conteneurs en utilisant un fichier `docker-compose.yml`.

#### **Comment le mettre en place :**
1. **Installation de Docker** : Assurez-vous que Docker et Docker Compose sont installés sur votre machine. Vous pouvez les installer via :
   - **Linux** : Utilisez `apt-get` pour installer Docker (`sudo apt-get install docker docker-compose`).
   - **Windows / Mac** : Téléchargez Docker Desktop.

2. **Cloner le dépôt** : Clonez le dépôt sur votre machine en utilisant :
   ```bash
   git clone https://github.com/WORFLOW-EM-ENGINER-DATA01/dockerhadoop.git
   cd dockerhadoop
   ```

3. **Configurer Docker Compose** : Le fichier `docker-compose.yml` contient toutes les instructions nécessaires pour lancer les conteneurs. Il définit des services comme `namenode`, `datanode`, et peut inclure d'autres services comme `resourcemanager` pour YARN.
   
4. **Lancer le cluster** : Pour démarrer tous les conteneurs, exécutez :
   ```bash
   docker-compose up -d
   ```
   Cette commande lancera tous les services définis dans le fichier `docker-compose.yml`.

### **2. Hadoop (HDFS)**
#### **Description**
Le dépôt configure un cluster Hadoop avec HDFS pour le stockage distribué. HDFS est la base du système de fichiers distribué dans Hadoop.

#### **Comment le mettre en place :**
1. **Configuration du NameNode et des DataNodes** : Dans le dépôt, le fichier `docker-compose.yml` spécifie un conteneur pour le NameNode (gestion des métadonnées HDFS) et un ou plusieurs conteneurs pour les DataNodes (stockage des blocs de données).
   
2. **Fichiers de configuration Hadoop** : Vous trouverez probablement des fichiers de configuration spécifiques dans un dossier comme `config/` ou `hadoop/` qui contiennent les réglages pour le cluster. Les fichiers critiques incluent :
   - **`core-site.xml`** : Configuration du système de fichiers distribué.
   - **`hdfs-site.xml`** : Configuration spécifique à HDFS, comme la taille des blocs et le facteur de réplication.

3. **Accès à HDFS** : Une fois le cluster démarré, HDFS est accessible via l'interface web d'Hadoop, généralement sur le port 9870 pour le NameNode.

### **3. YARN (Yet Another Resource Negotiator)**
#### **Description**
YARN est configuré pour gérer les ressources et orchestrer les tâches dans le cluster Hadoop.

#### **Comment le mettre en place :**
1. **Service YARN dans Docker** : Dans le fichier `docker-compose.yml`, il peut y avoir une section dédiée pour le ResourceManager et le NodeManager de YARN, ce qui gère les tâches et les ressources du cluster.
   
2. **Configurer les fichiers pour YARN** : Les fichiers de configuration, souvent trouvés dans le dépôt, incluent :
   - **`yarn-site.xml`** : Pour configurer les détails de YARN, comme le scheduler et la gestion des ressources.
   - **`mapred-site.xml`** : Pour définir les configurations de MapReduce.

3. **Vérification de YARN** : Après le démarrage, vous pouvez vérifier que YARN fonctionne via l'interface web, généralement accessible sur le port 8088.

### **4. MapReduce**
#### **Description**
MapReduce est le framework de traitement par défaut dans Hadoop, et il est configuré pour s'exécuter sur le cluster via YARN.

#### **Comment le mettre en place :**
1. **Configuration de MapReduce** : Dans les fichiers de configuration `mapred-site.xml`, assurez-vous que le mode de soumission des tâches est bien configuré pour utiliser YARN comme gestionnaire de ressources.

2. **Exécution des tâches** : Vous pouvez lancer des tâches MapReduce sur le cluster Hadoop une fois qu'il est configuré. Cela se fait via des commandes dans le conteneur NameNode, par exemple :
   ```bash
   hadoop jar [chemin_du_jar] [classe_principale] [arguments]
   ```

### **5. Apache Hive (si présent dans le dépôt)**
#### **Description**
Hive est souvent utilisé pour effectuer des requêtes sur les données stockées dans HDFS en utilisant un langage SQL (HiveQL).

#### **Comment le mettre en place :**
1. **Configurer le métastore Hive** : Il peut y avoir un conteneur dédié pour Hive qui gère le métastore et interagit avec HDFS.
2. **Connexion à HDFS** : Assurez-vous que Hive est configuré pour accéder aux données stockées dans HDFS.

### **6. Spark (si présent dans le dépôt)**
#### **Description**
Apache Spark est un moteur de traitement distribué qui peut fonctionner avec Hadoop pour des traitements en mémoire plus rapides.

#### **Comment le mettre en place :**
1. **Déploiement de Spark avec Docker** : Si le dépôt inclut des fichiers pour Spark, il y aura un conteneur dédié avec un fichier de configuration pour interagir avec Hadoop et YARN.
2. **Accéder à l'interface Spark** : Une fois lancé, Spark peut avoir son propre UI accessible sur un port spécifique (comme 4040).

### **Conclusion**

Le dépôt `dockerhadoop` fournit une infrastructure pour déployer rapidement un environnement Hadoop distribué avec Docker. Chaque composant (NameNode, DataNode, YARN, etc.) est conteneurisé, facilitant la gestion et le déploiement du cluster. Pour des détails spécifiques sur la configuration, il est crucial de vérifier chaque fichier de configuration présent dans le dépôt (comme `docker-compose.yml`, `core-site.xml`, `hdfs-site.xml`, `yarn-site.xml`) pour voir comment ils sont configurés et personnalisés pour l'environnement cible.
