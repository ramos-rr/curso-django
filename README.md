# curso-django
Repository related to Django learning, base on DevPro classes.

## I. CONTINUOUS COMMITMENT
### 1. SETING UP PIPENV<br>
- In windows, create inside the project files a folder named `.venv`. Then, command `pip install pipenv` if your main 
Python doesn't have pipenv already installed, and finally order `pipenv install`. See that PIPENV wil install inside the
`.venv` folder (within project's files) your Virtual Environment.
- Never forget about all dependencies that the projetc may have. Thus, order the cmd `pipenv sync` and/or `pipenv sync -d`
in order to install all requerements needed.
<br><br>

### 2. STARTING A PROJETC WITH DJANGO-ADMIN
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

- CREATE AN ALIAS:<br>
  - There's a need to implement alias to run django server anywhere. Basically, what is does is to 
  find and run `manage.py` (stored inside project's root) even if you are working in another folder, turning it simple 
  to run and test you app.<br>
  <br>

### 3. INSTALLING HEROKU<br>
- Install HEROKU for WIN64;<br>
- Activate through cmdlet `heroku login`
<br><br>

### 4. UPLOADING FIRST THING ONLINE<br>
- Change `settings.py <from> ALLOWED_HOSTS = [] <to> ALLOWED_HOSTS = ['0']`. This way, every HOST is allowed<br>
- Create `Procfile` in main root. Edit it: `web: gunicorn pypro.wsgi --log-file -`. It serves to indicate heroku the WSGI to use `<br>
- Install GUNICORN with PIPENV to make it a basic requerement: `pipenv install gunicorn`, that's part of WISG mentioned above<br>
- Create an APP with heroku: `heroku apps: create [app_name]ramos-rr-django`. Notice that heroku will return as 
followed:<br>
```
 (curso-django) PS C:\Users\rafae\PycharmProjects\curso-django> heroku apps:create ramos-rr-django
 Creating ??? ramos-rr-django... done
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

### 5. AUTOMATIC DEPLOY<br>
<strong>Comments: The idea here is to avoid different versions of the same application, mostly when it comes to be developed by two or
more team member.</strong><br>
5.1. First, login to [heroko website](https://id.heroku.com/);<br>
5.2. Then, access you application and go to " Deploy " window;<br>
5.3. Certify to pick Github as main connection, indicanting your repository address;<br>
5.4. Enable <i>AUTOMATIC DEPLOY</i><br>
<br><br>

### 6. RUN DJANGO SERVER IN PYCHARM<br>
<b>Comments: By doing this, you can debug an executing code.</b><br>
6.1. At the top of the screen, there's a litle box, with the Python logo inside, appointing to the actual server that 
is being used. Click edit, and inside RUN/DEBUG CONFIGURATION, Add a new one, by selecting Python as MAIN, then rename
the unknown to DJANGO (or as desired). Continue by indicating the path (select MANAGE.PY from your project). Finally, as 
<i>PARAMETER</i> type "_runserver_". Apply the changes.<br>
<br>
<b>Note that this new settings will appear above as a RUN OPTION</b><br>
<br><br>

### 7. UPLOAD FIRST HOME TO DJANGO SERVER<br>
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

### 8. PYTEST-DJANGO<br>
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

### 9. IMPLEMENT GITHUB ACTION TO RUN AUTOTESTS<br>
<b>Comments: Since TRAVIS has not been used due to its fees, CI was implemented using GITHUB ACTIONS<br></b>
<br> 

## II. PROJECT SET UP
### 10. DECOUPLE<br>
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
The current path, foo, didn???t match any of these.

You???re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.

<from heroku server>
Not Found
The requested resource was not found on this server.
````
<br>

### 11. SECRET KEY SETTING<br>
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

### 12. DOMAIN AND ALLOWED HOSTS<br>
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
        ??? Configure your app's DNS provider to point to the DNS Target xxxxxxxxxxxxxxxx.herokudns.com,
        ??? For help, see https:/devcenter.heroku.com/articles/custom-domains
        
        The domain django.pythonpro.com.br has been enqueued for addition
        ??? Run heroku domain:wait 'django.pythonpro.com.br' to wait for completion
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
>> Setting ALLOWED_HOSTS and restarting ??? ramos-rr-django... done, v50
>> ALLOWED_HOSTS: ramos-rr-django.herokuapp.com
```

- RUN BOTH SERVIDORS to test<br>
<br>
- ### 13. SET DATABASE ADDRESS IN SETTINGS<br>
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

### 14. MANAGE POSTGRESS DATABASE<br>
- INSTALL the library PSYCOPG2: `pipenv install psycopg2-binary`<br>
<br>

## III. STATIC FILES AND FILES UPLOAD
### 15. STATIC FILE AND UPLOAD DIRECTORY IN DJANGO<br>
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

# configura????o de ambiente de desenvolvimento
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR / 'statcfiles')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR / 'mediafiles')
```
<br>

### 16. CREATE AN ACCOUNT AT AWS<br>
COMMENT: Heroku is a server that process requests. Due to this, and to security issues, it doesn???t allow that you write 
new files in its server.<br>
Django has also the attribution to treat requests until it reaches the `view.py` file, and a lot of processes is done 
in this path. It would be a waste of resources to process all these layers over and over just to deliver you the 
same statics files (that never change).<br>
Therefore, Django does not provide static files if you are not running as <b>DEBUG=True</b>. In other words, it 
only provides static files in your local environment, so you don???t have to put these files elsewhere during the
development.<br>
Connecting these two points, it???s a good practice to set up your files inside a dedicated place that optimizes the 
deliverance of those static files. This is the so called CDN service (Content Delivery Network).<br>
Thus, _S3_, from AWS, is a nice place and a great example of CDN.<br>
(Renzo Nutiteli, 2020.)<br>
<br>
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

### 17. CREATE AND CONFIG S3 AT AWS<br>
<b>COMMENT: It's a bucket to store all files to be uploaded</b><br>
- Create a type S3 (Scalable Storage in the Cloud);<br>
- Name it;<br>
- Apply a new POLICY. <b>TAKE A LOOK AT A BUCKET POLICY EDITOR ARN.</b> To make a new policy, go to [AWS Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html)<br>
a. Select S3_Bucket_Policy type;<br>
b. Select ALLOW as effect;<br>
c. Copy ARN from the USER and paste it as the PRINCIPAL. You need to go back in AWS > USER and find it;<br>
d. Select ALL ACTIONS;<br>
e. Copy and Paste ARN from s3_Bucket;<br>
f. Submit it and COPY yhe JSON code generate automatically;<br>
g. Paste this code in AWS as a new POLICY (make sure that the first caracter is `{` instead of a blank space, otherwise
it will return an error).<br>

### 18. CONFIG LIB DJANGO_S3_FOLDER_STORAGE
<b>COMMENT: This library is to help upload your files to AWS.</b><br>
- Install: `pipenv install django-s3-folder-storage`
- Now, lets config our connection between LOCAL and AWS:
a. In `settings.py`, create an IF to certify that we have a valid AWS_ACCESS_KEY_ID;<br>
b. IF POSITIVE, add the other AWS parameters to make it right. It should look like the followed:<br>

```
<file> settings.py
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')  # a.
# STORAGE CONFIGURATION IN S3 AWS
if AWS_ACCESS_KEY_ID:  # b. IF THERE'S AN KEY_ID, THEN WE HAVE TO UPLOAD OUR FILES
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400', }
    AWS_PRELOAD_METADATA = True
    AWS_AUTO_CREATE_BUCKET = False
    AWS_QUERYSTRING_AUTH = True
    AWS_S3_CUSTOM_DOMAIN = None
    AWS_DEFAULT_ACL = 'private'

    # Static Assets
    # ----------------------------------------------------------------------------------
    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    STATIC_S3_PATH = 'static'
    STATIC_ROOT = f'/{STATIC_S3_PATH}'
    STATIC_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{STATIC_S3_PATH}'
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

    # Upload Media Folder
    # ----------------------------------------------------------------------------------
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
    DEFAULT_S3_PATH = 'media'
    MEDIA_ROOT = f'/{DEFAULT_S3_PATH}'
    MEDIA_URL = f'//s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/{DEFAULT_S3_PATH}'

    INSTALLED_APPS.append('s3_folder_storage')
    INSTALLED_APPS.append('storages')
```

c. SHELL PIPENV: `$ pipenv shell`<br>
d. TELL DJANGO NOT TO ASK TO UPLOAD FILES, leting to allways upload as default: 
`$ python manage.py collectstatic --no-input`. Submit!<br>
e. Recieve the answer `130 static files copied.`. Well done!<br>
<br>

### 19. OPTIMIZE UPLOADS WITH COLLECTFAST
- HEROKU must remove DISABLE_COLLECTSTATIC;<br>
- HEROKU must get all AWS key to access it:<br>
```
<terminal> $ heroku config:unset DISABLE_COLLECTSTATIC
<terminal> $ heroku config:set AWS_ACCESS_KEY_ID=<your_key>
<terminal> $ heroku config:set AWS_SECRET_ACCESS_KEY=<your_key>
<terminal> $ heroku config:set AWS_STORAGE_BUCKET_NAME=<your_bucket_name>
```

- Install COLLECTFAST to upload only those files that have been modified, avoiding delays in deployments:
`$ pipenv install Collectfast`;<br>
- EDIT `settings.py` to Add `collectfast` as one of the INSTALLED_APPS BEFORE `django.contrib.staticfiles`, OTHERWISE 
an error will occur;<br>
- EDIT `settings.py` again, adding:<br>
````<file> settings.py

COLLECTFAST_ENABLED = False
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
COLLECTFAST_STRATEGY = 'collectfast.strategies.boto3.Boto3Strategy

# STORAGE CONFIGURATION IN S3 AWS
# ----------------------------------------------------------------------------------
if AWS_ACCESS_KEY_ID:  # IF THERE'S AN KEY_ID, THEN WE HAVE TO UPLOAD OUR FILES
    ...
    COLLECTFAST_ENABLED = True
````
<br>

## IV. MIGRATIONS AND USER CUSTOMIZATION
### 20. OVERWRITING AN USER CLASS
<b>COMMENT:</b> Django documentation highly recommend that you set up a new User Model, even though it already provides 
a standard user to use. That's because when managing with migrations (next subject), these standard users will be 
more difficult to integrate with outer systems, and even harder to change in the midle of the project.<br>
- CREATE `models.py` module in app base (heroku created app): `C:\Users\rafae\PycharmProjects\curso-django\pypro\base\models`;<br>
- Look for the `class AbstractUser(AbstractBaseUser, PermissionsMixin):` in `auth\models.py` from django intern modules;<br>
- Apply the changes as desired.<br>
a. Change class name to User;<br>
b. Import AbstractBaseUser from django.contrib.auth.base_user and PermissionsMixin from django.contrib.auth.models;<br>
c. Change the Docstring;<br>
d. Delete username_validator and all related files, since your user will be an email;<br>
e. Import models from django.db;<br>
f. Import gettext_lazy as _ from django.utils.translation;<br>
g. Remove `last_name` line, since your user will be an email;<br>
h. switch `email = models.EmailField(_("email address"), blank=True)` to `email = models.EmailField(_("email address"), unique=True)`
to tell system that it must accept unique emails only;<br>
i. Import timezone from django.utils;<br>
j. Switch off objects = UserManager() for now (add it as commentary);<br>
k. Alter `USERNAME_FIELD = 'username'` to `USERNAME_FIELD = 'email'`, since your user will be an email;<br>
l. remove `abstract = True` from `class Meta`:
- followed file model:<br>

```
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    """
    App base User class

    Email and password are required. Other fields are optional.
    """

    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    # is_staff if to iddentify users able to accesse django-adimn settings
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    # is_active deffine Users that can login the system
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    # date_joined deffines when User joined the system
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    # objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s' % self.first_name
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

```
<br>

### 21. CREATING A MANAGER FOR USERS<br>
<b>COMMENT: Django documentation says that if you have created a USER using fields from the system, it is possible
to simply use UserManager to manage all users</b><br>
- Create a `classe UserManager` to handle all incoming users, enheriting `BaseUserManager`;<br>
- Create functions to create new user and create new superuser(for special authorizations);<br>
- Is should look like this:<br>

```
class UserManager(BaseUserManager):
    use_in_migrratios = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates ans servs a User with the given email and password.
        :param email: User email that will be user for login
        :param password: Key to be used at he login
        :param extra_fields: Any other information retaleted to the User
        :return: User()
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.sale(using=self._db)
        return user

    def create_user(self, useremail: str, password=None, **extra_fields: any):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(useremail, password, **extra_fields)

    def create_superuser(self, useremail: str, password=None, **extra_fields: any):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        return self._create_user(useremail, password, **extra_fields)
```

- Switch on `objects = UserManager()` in `class User` below to make the connection between User and Manager;<br>
<br>

### 22. MAKEMIGRATION COMMAND<br>
<b>COMMENT: It's time to makemigration. You should migrate `base` app now to get ready for launch</b><br>
- RUN `$ pipenv shell` / `$ python manage.py makemigration`. It must return the follwed message:<br>

````
Migrations for 'base':
  pypro\base\migrations\0001_initial.py
    - Create model User
````

- IF AN ERROR OCCUR, it may be fixed by following the hints from the terminal;
- IF Nothing happens, instead, is because django hasn't used the right APP path. You can see which contents django is
using typing `$ python manage.py showmigrations`:<br>

```
<terminal> $ python manage.py showmigrations
admin
 [ ] ...
auth
 [ ] ...
contenttypes
 [ ] ...
sessions
 [ ] ...
```

- See that the APP name is not there! Thus, to fix it, type `python manage.py makemigrations base[<APP_name.>]`:<br>
- It should work, and if you ask for showmigrations again, you must get:<br>

```
<terminal> $ python manage.py showmigrations
admin
 [ ] ...
auth
 [ ] ...
base
 [ ] ...
contenttypes
 [ ] ...
sessions
 [ ] ...
```

- FINALLY, check inside `/migrations/` for the first migration created `0001_initial.py`. Reading it, you are going to 
notice that all fields for your database have been created!
<br><br>

### 23. DATABASE CONNECTIONS AND MIGRATIONS
<b>COMMENT: </b><br>
- RUN `$ pipenv shell` / `$ python manage.py createsuperuser` to create a superuser required to manage other users;<br>
- See in DB if it has been createde!
<br><br>

### 24. USER ADMIN<br>
- Run django-server and access local/server;<br>
- entre a slash "/" `admin` at the end of address or [click here](http://127.0.0.1:8000/admin)<br>
- Entre with superuser account (created in the previous topic);<br>
- SEE that the dashboard only shows GROUP to manage, but it should bring USERS as well. This has happened because we 
changed the default user. Therefore, lets do some ajustments;<br>
a. First, search for the builtin `class UserAdmin` inside django: `django.contrib.auth.admin`;<br>
b. COPY the whole module and paste it inside the APP `admin.py`;<br>
c. Time to Overwrite the standard class by fixing those fields that have been changed, such as `username` and `email`. 
In the end, it should look as below:<br>

```
<file> pypro/base/admin.py
import...

csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())


@admin.register(User)  # OBS1
class UserAdmin(admin.ModelAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("first_name", "email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "email", "password1", "password2"),
            },
        ),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ("email", "first_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("first_name", "email")
    ordering = ("first_name",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )
```

#### OBS1: To make sure that the @admin.register(User) don't take the AbstractClass as model, it is necessary to:<br>
i. ELIMINATE `from django.contrib.auth.models import Group, User`;<br>
ii. ADD `from pypro.base.models import User`, that is your model from your app!<br>
- REFRESH the server and accesse ADMIN again: [click here](http://127.0.0.1:8000/admin)<br>
<br>
### 25. SET UP AUTOMATIC DATABASE UPLOAD FROM LOCAL TO HEROKU'S POSTGRES
- EDIT `Pocfile`, and add in the first line: `release: python manage.py migrate --noinput`
