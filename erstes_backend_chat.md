## Download Python
https://www.python.org/downloads/


## Create Project
In Terminal `mkdir backend` then `cd backend` and in there `mkdir sample-chat`

## HTML Template
In chat/views.py hinzufügenIn chat/views.py hinzufügen
```
def index(request):
return render(request, 'chat/index.html')
```
Datei chat/templates/chat/index.html erstellenDatei chat/templates/chat/index.html erstellen
```
//in urls.py
from . import views
```

## Create virtual environment
Erstelle mit `python -m venv myvenv` Dein virtuelles Environment.
Dann führe auf Windows in cmd `"myvenv/Scripts/activate"` aus oder in Powershell `".\myvenv\Scripts\activate"` oder auf Linux/Mac `source myvenv/bin/activate`, um das virtuelle Environment zu starten.

***Note: Manchmal musst Du auf Windows in den Ordner "myvenv/Scripts" gehen und dort die Datei "Activate.ps1" löschen, wenn Du das venv in Windows Powershell starten möchtest.***

## Install Django
Wenn Du Dich im laufenden virtuellen Environment befindets:
Run `python -m pip install Django` um Django zu installieren. 
Eventuell kannst du `python -m pip install --upgrade pip` um den Package Manager zu aktualisieren.

## Starte ein Projekt und den Server
Run `django-admin startproject chatappproject .` Der Punkt sorgt dafür, dass wir die Projekt-App nicht in zwei gleichnamigen Ordnern verschachteln, sonder auf diese Weise gleich im Root Verzeichnis bleiben und mit `python manage.py runserver` der Server einfach starten können.

## Erstelle Deine erste App im Projekt
Run `python manage.py startapp chat` um eine App namens **chat** zu erstellen. Und füge 'app' in settings.py bei **INSTALLED_APPS** hinzu

## Erstelle Deine Datenbank
Run `python manage.py migrate` um Diene Sqlite DB mit Feldern zu erstellen.

## Installiere in VSC einen Sqlite Viewer
Unter Extensions kannst Du einen Sqlite Viewer wie z. B. Sqlite Viewer installieren, damit Du Deine DB anschauen kannst.

## Create Superuser
Run `python manage.py createsuperuser`. Erstelle Namen, E-mail and Passwort. 
Wenn Du den Server startes, kannst Du Dich nun via http://127.0.0.1:8000/admin als SuperUser in das Admin-UI einloggen.

## Synchronisiere mit einem Github Repository
Setze Dein Repo bei Git auf und bevor Du synchronisierst musst Du noch Deine **.gitignore** Datei in ROOT erstellen. 

## Lege eine .env Datei an
Kreiere eine Datei in Root namens .env um alle Deine globalen Variablen abzuspeichern.

## Erstelle die requirements.txt
Speichere mit `pip freeze > requirements.txt` alle Deine aktuellen Dependencies in die requirements.txt Datei.
Diese Datei sorgt später immer dafür, dass mit `pip install -r requirements.txt` alle Dependencies installiert werden. 



## Lege ein Template index.html an
In dem Ordner der Chat-App namens "chat" lege folgenden Ordner und File an:**templates/chat/index.html**. Schreibe dort etwas HTML, was dann angezeigt werden soll z. B. `<h1>Hallo Welt.</h1>`

## Konfiguriere settings.py
In settings.py füge die 'chat' App den INSTALLED_APPS hinzu. Kreiere einen view für die index.html und eine Route in urls.py.

## Füge Authentication hinzu
Mit dem Standard Property **is_authenticated** kannst Du abfragen, ob ein User authentifiziert ist.
```
if request.user.is_authenticated:
    # The user is authenticated
    ...
else:
    # The user is not authenticated
    ...
```

## Kreiere Deine erste Login Annotation
Mit dem sog. **View Decorator** kannst Du einem View ein Bedingung hinzufügen, wie z. B., dass ein User eingelogged sein muss.

```
//views.py

# Authguard importieren:
from django.contrib.auth.decorators import login_required

# Authguard hinzufügen:
@login_required(login_url='/login/')
def index(request):
    .......
    .......
```

## Füge ein Master Template hinzu
Wichtig, füge das templates Verzeichnis in settings.py hinzu
```
//settings.py

'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

Lege die Datei base.html in dem templates folder in root an:
```
//templates/base.html
{% extends "base.html" %} {% block content %}
<!-- Dein HTML Code -->
{% endblock %}
Copyright © 2022 Developer Akademie GmbH
```


## Static file einbinden mit dem Static Folder
Füge Dein Static Verzeichnis in settings.py hinzu: Einmal in templates und einmal als Directory:
```
//settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

...
...

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

```

In der base.html müssen noch die static files geladen werden, ganz so, als würdest Du ein stylesheet einbinden:
```
{% load static %} 

<link rel="stylesheet" href="{% static 'css/style.css' %}" />
```


## Kreiere Views und Pfade:
Zunächste die Custom Views:
' ',
'chat/',
'login/', 
'logout',
'register',

Dann nutze die Django Default Views für Password Reset:
'password_reset/', 
'password_reset/done/', 
'reset/<uidb64>/<token>/', 
'reset/done/', 


## Erstelle ein Docker Image und Run Docker
Build: `docker build --tag django-chatapp .`
Run: `docker run --publish 8000:8000 django-chatapp`

## For Local Development, mount your DEV Dir in Docker 
Im CMD Terminal:
`docker run --publish 8000:8000 -it -v "$(pwd)/source_dir:/usr/src/app" <app-name> bash`

oder besser verständlich:

`docker run --publish 8000:8000 -it --mount "type=bind,source=$(pwd)/source_dir,target=/app/target_dir" <app-name> bash`

Wenn der Container im Terminal gestartet ist, solltest Du im Docker Prozess sein und Dein CLI sollte z. B. so aussehen:
```
//terminal
root@a99226b5e552:/usr/src/app#
```

Du bist nun in Deinem Container der gerade läuft. Starte jetzt Deine App mit: `python manage.py runserver 0.0.0.0:8000`
```
//terminal
root@a99226b5e552:/usr/src/app# python manage.py runserver 0.0.0.0:8000
```

Die Adresse 0.0.0.0:8000 bedeutet, dass der Server auf Anfragen an Port 8000 von allen IP-Adressen akzeptiert, die auf das Gerät zugreifen können.

**Kurzum:** Der Server akzeptiert Verbindungen auf Port 8000 von allen IP-Adressen.

## Weitere wichtiger Docker Befehle:
`docker ps` zeigt alle Docker images an

`docker exec -it <mycontainer> bash` öffnet das Terminal eines Docker-Containers