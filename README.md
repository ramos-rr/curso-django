# curso-django
Repository related to Django learning

1. SETING UP PIPENV<br>
- In windows, create inside the project files a folder named `.venv`. Then, command `pip install pipenv` if your main 
Python doesn't have pipenv already installed, and finally order `pipenv install`. See that PIPENV wil install inside the
`.venv` folder (within project's files) your Virtual Environment.
- Never forget about all dependencies that the projetc may have. Thus, order the cmd `pipenv sync` and/or `pipenv sync -d`
in order to install all requerements needed.

2. STARTING A PROJETC WITH DJANGO-ADMIN
- Type `django-admin startproject pypro[proj_name] .[place_to_root_file_manage.py]` (_the DOT indicates projetc root 
folder_)
- To get MANAGE.PY, type in terminal `python manage.py --help`:
````
Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
````
<br>

- ! Problems found !<br>
a. There's a need to implement alias, since the file `.bash_profile` couldn't be located. So, I got to manually set up
a file named `mng.bat` inside `.venv/Scripts`.<br>
<br>
3. INSTALLING HEROKU
- Install HEROKU for WIN64;
- Activate through cmdlet `heroku login`
<br><br>
4. UPLOADING FIRST THING ONLINE
- Change `settings.py <from> ALLOWED_HOSTS = [] <to> ALLOWED_HOSTS = ['0']`
- Create `Procfile` in main root. Edit it: `web: gunicorn pypro.wsgi --log-file -`
- Install GUNICORN with PIPENV to make it a basic requerement: `pipenv install gunicorn`
- Create an APP with heroku: `heroku apps: create [app_name]ramos-rr-django`. Notice that heroku will return as 
followed:
```
    (curso-django) PS C:\Users\rafae\PycharmProjects\curso-django> heroku apps:create ramos-rr-django
    Creating ⬢ ramos-rr-django... done
    https://ramos-rr-django.herokuapp.com/ | https://git.heroku.com/ramos-rr-django.git
```
- After that, you can investigate git by using `git remote -v`, and you'll see a new repository that has just been 
created:
```
    (curso-django) PS C:\Users\rafae\PycharmProjects\curso-django> git remote -v
    heroku  https://git.heroku.com/ramos-rr-django.git (fetch)
    heroku  https://git.heroku.com/ramos-rr-django.git (push)
    origin  https://github.com/ramos-rr/curso-django.git (fetch)
    origin  https://github.com/ramos-rr/curso-django.git (push)
```
- COMMIT all changes, but not push them;
- PUSH the app from heroku to master: `git push heroku[destiny] master[local_from]`
- TEST if the deploy has been successful by clicking on the link provided:
```
remote:        https://ramos-rr-django.herokuapp.com/ deployed to Heroku
```
<br>

5.