```
python -m venv venv
```
```
source venv/bin/activate
```
```
deactivate
```
```
pip3 install 'django<4'
```
```
pip3 show django
```
```
export PATH=$PATH:/Users/sergeykostanets/Library/Python/3.11/bin
```
```
django-admin --version
```
```
django-admin startproject boutique_ado .
```
```
python3 manage.py runserver
```
```
python3 manage.py migrate
```
```
python3 manage.py createsuperuser
```
```
pip3 install django-allauth==0.41.0
```
```
python3 manage.py migrate
```
```
python3 manage.py runserver
```
```
pip3 freeze > requirements.txt
```
```
cp -r /Users/sergeykostanets/Projects/codeinstitute-boutique-ado/venv/lib/python3.11/site-packages/allauth/templates/* ./templates/allauth 
```
```
python3 manage.py startapp home
```
```
mkdir -p home/templates/home
```
```
mkdir static
```
```
mkdir media
```
```
mkdir static/css
```
```
mkdir templates/includes
```
```
python3 manage.py startapp products
```
```
mkdir products/fixtures
```
```
python3 manage.py makemigrations --dry-run
```
```
pip3 install pillow
```
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate --plan
```
```
python3 manage.py migrate
```
```
python3 manage.py loaddata categories
```
```
python3 manage.py loaddata products
```
```
mkdir -p products/templates/products
```
```
python3 manage.py startapp bag
```
```
python3 manage.py makemigrations --dry-run
```
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate --plan
```
```
python3 manage.py migrate
```
```
python3 manage.py shell
```
```
python3 manage.py startapp checkout
```
```
python3 manage.py makemigrations --dry-run
```
```
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate --plan
```
```
python3 manage.py migrate
```
```
pip3 install django-crispy-forms==1.14.0
```
```
pip3 freeze > requirements.txt
```
```

```
