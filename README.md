Aperçu du projet : Le but de ce projet est de récupérer les informations sur les produits du site Web Jumia.ci et de stocker les données 
dans une base de données SQL Server.


Bibliothèques requises : 
-requests
-BeautifulSoup
-pyodbc

Création de base de données SQL Server :

- Tags
- Categories
- Article

1. Tags:
CREATE TABLE Tags (
  id INT IDENTITY(1,1) PRIMARY KEY,
  tag_name VARCHAR(255) NOT NULL
);

2.Categories 
CREATE TABLE categories (
  id INT IDENTITY(1,1) PRIMARY KEY,
  category_name VARCHAR(255) NOT NULL
);

3.Article 
CREATE TABLE article (
  produit_id INT IDENTITY(1,1) PRIMARY KEY,
  produit_name varchar(255) NOT NULL,
  produit_prix varchar(100) NOT NULL,
  avis varchar(20) NOT NULL 
);

Résultats: Les données extraites sont ensuite insérées dans la base de données SQL Server et peuvent être interrogées pour analyse.

