# stardustWebsiteBackend
Backend for Stardust Website


create a virtual env for django
for that:
$conda create -n <yourenvname>
  to activate:
$conda activate <yourenvname>
  
  then go to directory where the projects is and:

$pip install Django

to run the server:
$python manage.py runserver

if making changes to any model make sure to run :
$python manage.py makemigrations 
then 
$python manage.py migrate

