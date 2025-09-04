# BUT3INFO_R505_ProgAvanc
Repository où il y aura tout mes exercises pour le module R5.05 du BUT 3 Informatique IUT Orléans

## TD/TP 1 Mise en bouche - Initialisation au framework Django
### Feuille 1 - Installation du framwork
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

### Feuille 2 - Création d'un projet Django

Pour créer un projet django voici la commande à réaliser ```django-admin startproject <nom repertoire projet>```
Pour moi ce cera TutoDjango

```bash
django-admin startproject TutoDjango
```

Une fois le projet créer, se placer dans le répertoire du projet et lancer le serveur pour la première fois

```bash
cd TutoDjango
python manage.py runserver
```
Une fois le serveur lancer il est accéssible en local [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Feuille 4 - Découverte des applications

variable INSTALLED_APPS dans `./TutoDjango/settings.py`

pour les rendre fonctionnelle ==> faire la migration 
```bash
python manage.py migrate
```
note : examine le réglage **INSTALLED_APPS** et crée les tables de base de données nécessaires en
fonction des réglages de base de données dans votre fichier **TutoDjango/settings.py**

### Feuille 5 et 6 - Création d'un application 

Création d'une app dans un projet Django commande : `startapp`

```bash
./manage.py startapp monApp
```
ajout de `monApp` dans la variable **INSTALLED_APPS** de *settings.py*

### Feuille 7 - ajout d'une Première Page

- Ajout de la première vue dans monApp/views
```py
from django.http import HttpResponse
def home(request):
    return HttpResponse("<h1>Hello Django!</h1>")
```
- Ajout d'une configuration url `urls.py` dans monApp/urls.py 
```py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
]
```
- importation de urls conf de monApp dand urls.py de TudoDjango
    - ajout de include dans `from django.urls import` dans TutoDjango/urls.py
    - ajout de `path("monApp/", include("monApp.urls")),` dans TutoDjango/urls.py


### Feuille 9 : creation d'une route et vue avec paramètre
- création d'une vue dynamique avec un paramètre
`path('home/<param>',views.home ,name='home'),` et  
```py
def home(request, param):
    return HttpResponse(f"<h1>Bonjour { param }!</h1>") 
```