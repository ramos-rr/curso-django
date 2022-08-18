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
- Change `settings.py <from> ALLOWED_HOSTS = [] <to> ALLOWED_HOSTS = ['0']`<br>
- Create `Procfile` in main root. Edit it: `web: gunicorn pypro.wsgi --log-file -`<br>
- Install GUNICORN with PIPENV to make it a basic requerement: `pipenv install gunicorn`<br>
- Create an APP with heroku: `heroku apps: create [app_name]ramos-rr-django`. Notice that heroku will return as 
followed:<br>
```
 (curso-django) PS C:\Users\rafae\PycharmProjects\curso-django> heroku apps:create ramos-rr-django
 Creating ⬢ ramos-rr-django... done
 https://ramos-rr-django.herokuapp.com/ | https://git.heroku.com/ramos-rr-django.git
```
<br>

- After that, you can investigate Git by using `git remote -v`, and you'll see a new repository that has just been 
created:<br>
```
 (curso-django) PS C:\Users\rafae\PycharmProjects\curso-django> git remote -v
 heroku  https://git.heroku.com/ramos-rr-django.git (fetch)
 heroku  https://git.heroku.com/ramos-rr-django.git (push)
 origin  https://github.com/ramos-rr/curso-django.git (fetch)
 origin  https://github.com/ramos-rr/curso-django.git (push)
```
<br>

- COMMIT all changes, but not push them;<br>
- PUSH the app from heroku to master: `git push heroku[destiny] master[local_from]`<br>
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
the unknown to DJANGO. Continue by indicating the path (selec MANAGE.PY from your project). Finally, as 
<i>PARAMETER</i> type "_runserver_". Apply the changes.<br>
<br>
<b>Note that this new settings will appear above as a RUN OPTION</b><br>
<br><br>
7. UPLOAD FIRST HOME TO DJANGO SERVER<br>
7.1. FIRST: in the terminal, go to the app_folder (Created in Item 2.), then run `manage.py startapp base[app_name]`.
Attention! You need to create inside the project that you've set up with DJANGO!.<br>
<br>
<strong> Don't forget to use alias to call `manage.py` from the rootfolder</strong><br>
<br>
7.2. EDIT `view.py` inside this brandnew app's folder. The VIEW.PY is responsable to answer all requests coming from 
   browsers:<br>
```
   <local> view.py
   from django.http import HttpResponse
   
   def home(request):
       return HttpResponse('Helo Django!')
   
```
<br>

7.3. EDIT `apps.py` in app's files, to change its name:<br>
```
   class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name = 'base' # OLD NAME
    name = 'pypro.base'
```
7.4. TELL `settings.py` (stored in django-project's files) ~~that you have an APP READY to go 
online:<br>
APPEND IN `INSTALLED_APPS = []` your app's path, e.g., `INSTALLED_APPS = [..., 'pypro.base']`<br>
7.5. MAP in `urls.py` (stored in django-project's files) that function created inside view.py file: 
`urlpatterns = [path('', home),]`. Because `home` is a function, you get to import it this way: `from pypro.base.views import home`<br>
7.6. RUN IT<br>
<br>
8. PYTEST-DJANGO<br>
Comments: Once of the most important enhencement one can provide is to make sure everything is testable. So, lets 
implement <i>pytest-django</i> plugin using pipenv in the terminal: `$ pipenv install 'pytest-django'`.<br>
- SET UP PYTEST by creating a file named `pytest.ini` inside the project main root files:
```
<file> pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = pypro.settings  # Necessary indicate where setings.py is locatede 
```
<br>
<b>
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
   

