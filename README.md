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
<br>

- ! Problems found !<br>
a. There's a need to implement alias, since the file `.bash_profile` couldn't be located. So, I got to manually set up
a file named `mng.bat` inside `.venv/Scripts`.<br>
<br>
3. INSTALLING HEROKU
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
<br>
6. RUN DJANGO SERVER IN PYCHARM<br>
<b>Comments:</b> By doing this, you can debug an executing code.<br>
   1. At the top of the screen, there's a litle box, with the Python logo inside, appointing to the actual server that 
   is being used. Click edit, and inside RUN/DEBUG CONFIGURATION, Add a new one, by selectin Python as MAIN, then rename
   the unknown to DJANGO. Continue by indicating the path (selec MANAGE.PY from your project). Finally, as 
   <i>PARAMETER</i> type "_runserver_". Apply the changes.<br>
      1. <b>Note that this new settings will appear above as a RUN OPTION</b><br>
<br>
7. 