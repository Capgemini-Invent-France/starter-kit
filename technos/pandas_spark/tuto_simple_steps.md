# Tutoriel PySpark : Premiers Pas dans Jupyter Notebook

## Sommaire
- [Tutoriel PySpark : Premiers Pas dans Jupyter Notebook](#tutoriel-pyspark--premiers-pas-dans-jupyter-notebook)
  - [Sommaire](#sommaire)
  - [Prérequis](#prérequis)
  - [Installation](#installation)
    - [Installer PySpark](#installer-pyspark)
  - [Configuration de PySpark](#configuration-de-pyspark)
    - [Importer SparkSession](#importer-sparksession)
    - [Initialiser SparkSession](#initialiser-sparksession)
  - [Manipulation de Données](#manipulation-de-données)
    - [Créer un DataFrame](#créer-un-dataframe)
    - [Filtrer votre dataframe](#filtrer-votre-dataframe)
    - [Aggréger les données](#aggréger-les-données)
    - [Jointure](#jointure)
    - [Utilisation de SQL avec PySpark](#utilisation-de-sql-avec-pyspark)

## Prérequis
- Assurez-vous d'avoir une version récente de Python et Java installée sur votre machine.
- La variable d'environnement `JAVA_HOME` doit être configurée.

## Installation
### Installer PySpark
Utilisez pip pour installer PySpark:
```sh
pip install pyspark
```

## Configuration de PySpark
### Importer SparkSession
Utilisez le code suivant pour importer SparkSession dans votre notebook.

```python
from pyspark.sql import SparkSession
```

### Initialiser SparkSession
Utilisez le code suivant pour initialiser SparkSession.

```python
spark = SparkSession.builder.appName("MyApp").getOrCreate()
```

## Manipulation de Données
### Créer un DataFrame

```python
data = [
    (1, "Alice", 23, 85),
    (2, "Bob", 22, 89),
    (3, "Charlie", 24, 78),
    (4, "Daisy", 22, 92),
    (5, "Bob", 21, 91)
]

# Creer votre dataframe avec les colonnes ID, Name, Age, Grade
```

### Filtrer votre dataframe

```python
# Ne garder que les lignes où Age > 22
```

### Aggréger les données

```python
# Créer une dateframe avec max Age pour chaque Name
# La colonne doit s'appeler Age Maximum
```

### Jointure 

```python
extra_data = [
    (1, "Alice", "Computer Science"),
    (2, "Bob", "Physics"),
    (4, "Daisy", "Mathematics"),
    (6, "Eva", "Biology")
]

# Joindre ces nouvelles données à la dataframe students
# Utiliser une jointure left

```

### Utilisation de SQL avec PySpark

```python
# Création d'une vue temporaire
df.createOrReplaceTempView("people")

# Récuperer les Noms avec un grade inférieur à 85
```
