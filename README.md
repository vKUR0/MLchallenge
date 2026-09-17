Créer un environnement virtuel à la racine du projet avec la commande uv venv, puis l'activer via source .venv/bin/activate sous Linux ou macOS, ou .venv\\Scripts\\activate sous Windows.Installer l'ensemble des bibliothèques requises en lançant la commande uv pip install torch torchvision numpy scikit-image pillow matplotlib jupyterlab.



Placer le jeu de données d'images dans un dossier situé au même niveau que le notebook, et indiquer son nom dans la seconde cellule de celui ci.



Démarrer le serveur Jupyter en exécutant jupyter lab depuis le terminal, ouvrir le fichier main.ipynb et sélectionner le noyau Python associé à l'environnement virtuel .venv.



Exécuter la première cellule pour charger les modules.



Lancer la cellule suivante pour charger le dataset, traiter et normaliser les images.



Exécuter les blocs suivant, définissant les architectures neuronales, comprenant la structure UNet de base, la variante Resnet avec encodeur ResNet-18, ainsi que le discriminateur.



Lancer la cellule d'entraînement choisie.



Exécuter la cellule d'évaluation pour calculer l'erreur chromatique moyenne Delta ab ainsi que la dispersion chromatique des canaux a et b sur l'ensemble de test.  



Lancer enfin la dernière cellule pour générer la grille de visualisation comparative des images de test, affichant côte à côte l'entrée en niveaux de gris, la prédiction de couleur et l'image réelle.   

