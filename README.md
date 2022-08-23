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
- Type `django-admin startproject pypro[proj_name] .[place_to_root_file_manage.py]` (_the DOT indicates projetc's rootfolder_)<br>
- See that the django project must have been created where it was supposed to with the followed structure:<br>

```
<python_project_root>/<django_project_root>:
1. __init__.py
2. asgi.py
3. settings.py
4. urls.py
5. wsgi.py
```

- To get MANAGE.PY, type in terminal `python manage.py --help`:<br>

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
<strong> Don't forget to use alias to call `manage.py` from root files</strong>
<br>
- See that the application folder will be created as followed:<br>

```
<python_project_root>/<django_project_root>/<app_name>:
1. /migrations
2. __init__.py
3. admin.py
4. apps.py
5. models.py
6. views.py
```

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

12. DOMAIN AND ALLOWED HOSTS<br>
- DOMAIN is you website address. Allways check up before cast a domain to avoid an already existing domain: [REGISTRO.BR](https://registro.br).
Remember that DOMAIN is just the final part of an web address, e.g. `pythonpro.com.br`.
- IF AVALIABLE, you can purchase it directly from a HOST that is going to manage this DOMAIN. Hosts example: [DreamHost](https://www.dreamhost.com/),
[Hostinger](https://www.hostinger.com.br/).
- SUBDOMAIN: `www` is the most famous subdomain. It allways comes first than the DOMAIN. Generally, you can pick your own
subdomain;<br>
- DNS means _Domain Name Server_ that each domain has. You can set a subdomain for your domain by telling SERVER which new
DNS you created:
```
DNS TYPE CNAME - You copy/paste a Subdomain DNS providor to the domain DNS provider. This way, the main domain provider correctly points
to the subdomain in order to reach it:
    Example:
        >>> Input
        <using_heroku_to_add_new_subdomai> $ heroku domains:add django.pythonpro.com.br
        
        >>> Output
        Adding django.pythonpro.com.br to ...<old domain>...
        ► Configure your app's DNS provider to point to the DNS Target xxxxxxxxxxxxxxxx.herokudns.com,
        ► For help, see https:/devcenter.heroku.com/articles/custom-domains
        
        The domain django.pythonpro.com.br has been enqueued for addition
        ► Run heroku domain:wait 'django.pythonpro.com.br' to wait for completion
```
- Now, paste `xxxxxxxxxxxxxxxx.herokudns.com` inside host.
- EDIT `settings.py` and `.env`, ALLOWED HOSTS to limit which hosts are allowed to access it. Use decouple plugin to indicate the list
of allowed hosts for your website. <strong> THIS PROCEDURE IS TO ALLOW WORK LOCALLY</strong>:
```
<file> settings.py
from decouple import config, Csv

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

<file> .env
ALLOWED_HOSTS=localholst, 127.0.0.1:8000/
```

- FINALLY, UPDATE HEROKU LIST OF ALLOWED_HOSTS, otherwise, it will return BAD REQUEST:<br>

```
<terminal> $ heroku domains
>> === ramos-rr-django Heroku Domain
>> ramos-rr-django.herokuapp.com  # COPY
<terminal> $ heroku config:set ALLOWED_HOSTS='ramos-rr-django.herokuapp.com'
>> Setting ALLOWED_HOSTS and restarting ⬢ ramos-rr-django... done, v50
>> ALLOWED_HOSTS: ramos-rr-django.herokuapp.com
```

- RUN BOTH SERVIDORS to test<br>
<br>
13. SET DATABASE ADDRESS IN SETTINGS<br>
<b>COMMENT1: Django reads a DATABASE as a dictionary with the followed keys:</b><br>

````
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': '',
    'PORT': '',
    'CONN_MAX_AGE': 0
    'ENGINE': ''}
````

<b>COMMENT2: LETS CONNECT WITH DB PROVIDED BY HEROKU</b><br>
- RUN `$ heroku config` to check up if a postgress db has been provided. If not, run `$ heroku addons:docs heroku-postgresql`
to tell heroku to create a db for your account.<br>
- It should appear like this:<br>

```
(curso-django) PS C:\Users\rafae\PycharmProjects\curso-django> heroku config
=== ramos-rr-django Config Vars
ALLOWED_HOSTS:         ramos-rr-django.herokuapp.com
DATABASE_URL:          postgres://....
DISABLE_COLLECTSTATIC: 1
SECRET_KEY:            <secret_key>
```

- Go to `settings.py` in your django-project, and begin to switch DATABASES default values to indicate your new database:<br>
```
<file> settings.py
[ORIGINAL DATABASE SETTINGS]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

[NEW DATABASE SETTINGS]
default_db_url = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')  # See OBS1
parse_database = partial(default_db_url.parse, conn_max_age=600)  # See OBS2 and OBS3
DATABASES = {
    'default': config('DATABASE_URL', default=default_db_url, cast=parse_database)
}  # See OBS4
```

OBS1: `default_db_url` is where the local db is located;<br>
OBS2: `parse_databse` is to add a value to the KEY `[CONN_MAX_AGE]`;<br>
OBS3: `[CONN_MAX_AGE]` serves to indicate (in seconds) the connection duration with database. If the value is not provided,
it will take a 0 as default. If `None` value is provided, the duration will be limitless.<br>
OBS4: The fist parameter `'DATABASE_URL` is to tell Django to search in `.env` file for a valid database url, transform 
the String into a dictionary. If any valid url is found, the system will take the `default` parameter (`default_base_url`) as a database, and is goint to transform it 
in a dictionary as well. Finally, the last parameter `cast` is to add the KEY`[CONN_MAX_AGE]` in database dictionary,
even if it hasn't found any external db.url.<br>
<br>

14. MANAGE POSTGRESS DATABASE<br>
- INSTALL the library PSYCOPG2: `pipenv install psycopg2-binary`<br>
<br>
15. STATIC FILE AND UPLOAD DIRECTORY IN DJANGO<br>
<b>COMMENT: Static files are those that don't change. Basically, HTTP has a structure that needs to repeat everytime. 
Thus, django-server have to go collect these staticfiles within its own system to be able to fill all requests</b><br>
NOTE: Django provides basic staticfiles so that you don't have to depend on external servers to begin your development.<br>

- EDIT `settings.py` to add STATIC_ROOT right below STATIC_URL: `STATIC_ROOT = os.path.join(BASE_DIR / 'statcfiles')`
- RUN `$pipenv shell / $ python manage.py collectstatic`. Check if it worked like written below:<br>

```
PS C:\Users\rafae\PycharmProjects\curso-django> python manage.py collectstatic

130 static files copied to 'C:\Users\rafae\PycharmProjects\curso-django\statcfiles'.
PS C:\Users\rafae\PycharmProjects\curso-django> 
```

- IN ORDER TO UPLOAD STUFS, you need to set up two more path in `settings.py`: `MEDIA_URL = 'media/'` and
`MEDIA_ROOT = os.path.join(BASE_DIR / 'mediafiles')`<br>
- Everything shoul look like this:<br>
 
```
<file> settings.py

# configuração de ambiente de desenvolvimento
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'statcfiles')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'mediafiles')
```
<br>

16. CREATE AN ACCOUNT AT AWS<br>
<b>COMMENT: Heroku é um servidor cujo objetivo é processar requisições. Por conta disso, e tb de segurança, ele não 
permite que vc escreva arquivos no servidor.<br>
Django tb tem objetivo de tratar requisições e até ela chegar em sua view, muito processamento é feito. Seria um 
desperdicio de recurso processar todas camadas para sempre entregar arquivos que não mudam, ou seja, são estáticos.
Por conta disso, o Django não serve arquivos estáticos se vc não está em modo debug True. Ou seja, ele só serve 
estático no seu ambiente local para não ter o trabalho de colocar os estáticos em algum outro lugar quando estiver 
desenvolvendo localmente.<br>
Juntando os dois pontos, a boa prática é vc colocar seus arquivos em um serviço otimizado para sempre entregar arquivos
estáticos. Esse serviço se chama CDN (Content Delivery Network). O S3, da AWS, é um exemplo desse CDN.
</b><br>
- Create an account at [AmazonWebServices](https://aws.amazon.com/pt/)<br>
- GO to _Identity and Access Management_ (IAM) service<br>
- Create a USER using `AmazonS3FullAccess` policy
- COPY the secret_key_id to `.env` file:<br>

```
<file> .env
DEBUG=True
SECRET_KEY='CHAVE SECRETA'
ALLOWED_HOSTS='127.0.0.1'
AWS_ACCESS_KEY_ID=AK.....742
AWS_SECRET_ACCESS_KEY=Tr....Pxj
```
<br>

17. CREATE AND CONFIG S3 AT AWS<br>
<b>COMMENT: It's a bucket to store all files to be uploaded</b><br>
- 