# curso-django
Repository related to Django learning

1. SETING UP PIPENV<br>
- In windows, create inside the project files a folder named `.venv`. Then, command `pip install pipenv` if your main 
Python doesn't have pipenv already installed, and finally order `pipenv install`. See that PIPENV wil install inside the
`.venv` folder (within project's files) your Virtual Environment.
- Never forget about all dependencies that the projetc may have. Thus, order the cmd `pipenv sync` and/or `pipenv sync -d`
in order to install all requerements needed.
<br><br>
2. STARTING A PROJETC WITH DJANGO-ADMIN
- Type `django-admin startproject pypro[proj_name] .[place_to_root_file_manage.py]` (_the DOT indicates projetc's rootfolder_)
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
<br><br>
- CREATE AN ALIAS:<br>
  - There's a need to implement alias to run django server anywhere. Basically, what is does is to 
  find and run `manage.py` (stored inside project's root) even if you are working in another folder, turning it simple 
  to run and test you app.<br>
  <br>
3. INSTALLING HEROKU<br>
- Install HEROKU for WIN64;<br>
- Activate through cmdlet `heroku login`
<br><br>
4. UPLOADING FIRST THING ONLINE<br>
- Change `settings.py <from> ALLOWED_HOSTS = [] <to> ALLOWED_HOSTS = ['0']`. This way, every HOST is allowed<br>
- Create `Procfile` in main root. Edit it: `web: gunicorn pypro.wsgi --log-file -`. It serves to indicate heroku the WSGI to use `<br>
- Install GUNICORN with PIPENV to make it a basic requerement: `pipenv install gunicorn`, that's part of WISG mentioned above<br>
- Create an APP with heroku: `heroku apps: create [app_name]ramos-rr-django`. Notice that heroku will return as 
followed:<br>
```
 (curso-django) PS C:\Users\rafae\PycharmProjects\curso-django> heroku apps:create ramos-rr-django
 Creating ⬢ ramos-rr-django... done
 https://ramos-rr-django.herokuapp.com/ | https://git.heroku.com/ramos-rr-django.git
```
<br>

<strong>ATTENTION: It is possible that an error occurs regarding COLLECTSTATIC. Thus, simply type what heroku tells
you to:</strong> `DISABLE_COLLECTSTATIC=1`. IT SHOULD FIX IT

- After that, you can investigate Git by using `git remote -v`, and you'll see a new repository that has just been 
created inside heroku's github:<br>
```
 (curso-django) PS C:\Users\rafae\PycharmProjects\curso-django> git remote -v
 heroku  https://git.heroku.com/ramos-rr-django.git (fetch)
 heroku  https://git.heroku.com/ramos-rr-django.git (push)
 origin  https://github.com/ramos-rr/curso-django.git (fetch)
 origin  https://github.com/ramos-rr/curso-django.git (push)
```
<br>

- COMMIT all changes, but not push them yet;<br>
- PUSH the app from heroku to master: `git push heroku[heroku_origin] master[main_remote]`<br>
- TEST if the deploy has been successful by clicking on the link provided:<br>
```
remote:        https://ramos-rr-django.herokuapp.com/ deployed to Heroku
```
<br>

5. AUTOMATIC DEPLOY<br>
<strong>Comments: The idea here is to avoid different versions of the same application, mostly when it comes to be developed by two or
more team member.</strong><br>
5.1. First, login to [heroko website](https://id.heroku.com/);<br>
5.2. Then, access you application and go to " Deploy " window;<br>
5.3. Certify to pick Github as main connection, indicanting your repository address;<br>
5.4. Enable <i>AUTOMATIC DEPLOY</i><br>
<br><br>
6. RUN DJANGO SERVER IN PYCHARM<br>
<b>Comments: By doing this, you can debug an executing code.</b><br>
6.1. At the top of the screen, there's a litle box, with the Python logo inside, appointing to the actual server that 
is being used. Click edit, and inside RUN/DEBUG CONFIGURATION, Add a new one, by selecting Python as MAIN, then rename
the unknown to DJANGO (or as desired). Continue by indicating the path (select MANAGE.PY from your project). Finally, as 
<i>PARAMETER</i> type "_runserver_". Apply the changes.<br>
<br>
<b>Note that this new settings will appear above as a RUN OPTION</b><br>
<br><br>
7. UPLOAD FIRST HOME TO DJANGO SERVER<br>
- FIRST: in the terminal, go to the app_folder (Created in Item 2.), then run `manage.py startapp base[app_name]`.
Attention! You need to create inside the project that you've set up with DJANGO!.<br>
<br>
<strong> Don't forget to use alias to call `manage.py` from root files</strong><br>
<br>

- EDIT `view.py` inside this brandnew app's folder. The VIEW.PY is responsable to answer all requests coming from 
   browsers:
<br>

```
<local> view.py
from django.http import HttpResponse
   
def home(request):
    return HttpResponse('Helo Django!')
```
<br>

- EDIT `apps.py` in app's files, to change its name:<br>
```
   class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name = 'base' # OLD NAME
    name = 'pypro.base'
```
- TELL `settings.py` (stored in django-project's files) ~~that you have an APP READY to go 
online:<br>
APPEND IN `INSTALLED_APPS = []` your app's path, e.g., `INSTALLED_APPS = [..., 'pypro.base']`<br>
- MAP in `urls.py` (stored in django-project's files) that function created inside view.py file: 
`urlpatterns = [path('', home),]`. Because `home` is a function, you have to rightly import: `from pypro.base.views import home`<br>
- RUN IT<br>
<br>
8. PYTEST-DJANGO<br>
<b>Comments: Once of the most important enhencement one can provide is to make sure everything is testable. So, lets 
implement <i>pytest-django</i> plugin using pipenv in the terminal: `$ pipenv install 'pytest-django'`.<br></b>
- SET UP PYTEST by creating a file named `pytest.ini` inside the project main root files:
```
<file> pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = pypro.settings  # Necessary indicate where setings.py is locatede 
```
<br><b>
- CREATE TEST FOLDER INSIDE THE APP FOLDER</b>: `~/curso-django/pypro/base/tests`
- DEFINE A TEST (Read all commentaries below):

```
from django.test import Client


# client is a fixture provided by django.test. It emulates HTTP requests so it is not necessary to use real requests
def test_status_code(client: Client):
    # Now, we use a call of GET type to call our VIEW.PY, which is based inside app root folder
    # use '/' to address ROOT
    resp = client.get('/')
    return resp.status_code == 200  # Code 200 refers to a successful result
```
<br>

9. IMPLEMENT GITHUB ACTION TO RUN AUTOTESTS<br>
<b>Comments: Since TRAVIS has not been used due to its fees, CI was implemented using GITHUB ACTIONS<br></b>
<br> 

10. DECOUPLE<br>
<b>Comments: To avoid your website giving more information than necessary to outsiders, it worth it to use the library 
PYTHON-DECOUPLE</b>. Therefore, locally you can leave DEBUG=True to help you track down any error during the development
process<br>
- IMPORT the library: `$ pipenv install 'python-decouple'`;<br>
- EDIT `settings.py` from project, and create a variable to informe whether DEBUG is True or False.<br>
<b>NOTE: it is necessary to give 2 parameters for the function " _config(name: str; cast=boll)_ " to work!</b><br>
```
from decouple import config

DEBUG = config('DEBUG', cast=bool)  # First parameter = <name: Str> / Second parameter = <cast=bool> to transform to bool
```
- CREATE `.env` file in localroot, because in case of not having a BOOLEAN indicated for DEBUG, it will search for this
`.env` file looking for a valid boolean value;<br>
- TYPE `DEBUG=False`
- HIDE the file `.env` from GIT repository (for security reasons) using `.gitignore`;<br>
- Cast a sample instead: `/config/env-sample` (a copy). This way, in order for CI to test, there will be an obligation 
to add a new STEP transforming this sample in an online temporary `.env` file:<br>
````<example>
step:
    name: Create .env
    run: cp contrib/env-sample .env
````
- PUSH changes, and expect:<br>
````
<from django server>
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/foo
Using the URLconf defined in pypro.urls, Django tried these URL patterns, in this order:

admin/
The current path, foo, didn’t match any of these.

You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.

<from heroku server>
Not Found
The requested resource was not found on this server.
````
<br>

11. SECRET KEY SETTING<br>
COMMENT: A secret key serves as a cryptograph value for sign in sessions, messages, password reset, and on;<br>
- EDIT: `setings.py >> SECRET_KEY = config('SECRET_KEY')`;<br>
- EDIT: `.env >> (+ line) SECRET_KEY=CHAVE SECRETA`;<br>
- EDIT: `/contib/env-sample >> SECRET_KEY=defina sua chave secreta`;<br>
- RUN Terminal to generate a random secret_key:<br>
```
<terminal> pipenv shell
<terminal_venv> python
<terminal_python> from django.core.management.utils import get_random_secret_key
<terminal_python> get_random_secret_key()
```
- COPY secret key generated by django;<br>
- SET SECRET KEY TO HEROKU ALSO: `$ heroku config:set SECRET_KEY='<your_key_generated>'`
- CHECK all environment variables in heroku to make sure everything is ok: `$ heroku config`
```
=== ramos-rr-django Config Vars
DEBUG:                 False
DISABLE_COLLECTSTATIC: 1
SECRET_KEY:            <secret_key>
```
<br>

