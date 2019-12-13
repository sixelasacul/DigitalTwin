# DigitalTwin

Maître et Esclave du Workshop 1 de l'option Data Science du CESI.

## Installation

Après avoir cloné le projet, il faut :

- Créer un environnement virtuel : `virtualenv venv`
- Activer l'environnement créé : `source venv/bin/activate`
- Installer les packages depuis le fichier requirements.txt : `pip install -r requirements.txt`
- Vérifier les packages installés : `pip list`

## Démarrage

Il faut lancer le serveur/esclave en premier. Il simule des capteurs de température en retournant des informations de la base de données (`dtdb`) toutes les 5 secondes.

`python server.py`

Ensuite, le client/maître peut être lancé. Il va écouter via le protocole Modbus les températures envoyées par l'esclave et les publier sur un topic via mQTT.

`python client.py`