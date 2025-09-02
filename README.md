# BUT3INFO_R505_ProgAvanc
Repository où il y aura tout mes exercises pour le module R5.05 du BUT 3 Informatique IUT Orléans

## TD/TP 1 Mise en bouche - Initialisation au framework Django
Pour commencer tout projet en Django il faut d'abord creer la projet à la racine. 
Voici les différentes commandes à executer pour commencer

Création de l'environnement virtuel venv, initialisation, installation, vérification
```bash
virtualenv ./venv
source ./venv/bin/activate
pip install django
django-admin --version
```
Une fois l'installation fait et vérifié on sauvegarde une trace des packages installé

```bash 
pip freeze > requirements.txt
```