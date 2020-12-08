-----------------------
Развертывание проекта
-----------------------

mysql> CREATE DATABASE `povary` CHARACTER SET utf8 COLLATE utf8_general_ci;

```
cd povary & virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

python manage.py syncdb (пропускам создание юзера)
python manage.py migrate
python manage.py migrate recipes
python manage.py migrate seo_v2
x manage.py migrate regions
...
python manage.py createsuperuser
```


------------------
Другое
------------------
Media (MC & ARTICLES) - https://www.dropbox.com/s/cfj6xn4ib0ew3gx/media.zip


-----------------
OSX settings
-----------------
```
brew install geoip
brew install xapian --with-python
brew install mongodb
```

Configuration for Xapian & MySQL
```
export PYTHONPATH=/usr/local/Cellar/xapian/1.2.15/lib/python2.7/site-packages:$PYTHONPATH
export PATH=/usr/local/bin:/usr/local/mysql/bin/:$PATH
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/usr/local/mysql/lib/"
```

django-setman require:
```
export DJANGO_SETTINGS_MODULE=povary.settings
```

test