# DjangoTimeTracker
A simple way to track your time!

Steps to setup:
1) Clone
```cmd
git clone https://github.com/RoboJojo/DjangoTimeTracker.git
```
2) Download desired boostrap distribution into static folder
     * Something like this:
        * _/DjangoTimeTracker/static/boostrap-x.x.x-dist_
3) Update html includes to match boostrap version (the x.x.x value) 
     * For instance, in _/DjangoTimeTracker/templates/head.html_, the x.x.x values need to be updated to the correct version:
```html 
          <link rel="stylesheet" href="{% static 'bootstrap-x.x.x-dist/css/bootstrap.min.css' %}">
```
4) Download desired jquery distribution into static/js folder:
     * Something like this: 
        * _/DjangoTimeTracker/static/js/jquery-x.x.x.min.js_
5) Update html includes to match jquery distribution:
    * For instance, in _/DjangoTimeTracker/templates/footer.html_, the x.x.x values need to be updated to the correct version:
```html 
          <script src="{% static 'js/jquery-x.x.x.min.js' %}"></script>
```
6) Install django and django-chartjs:
```
pip install django
pip install django-chartjs
```
7) Navigate to DjangoTimeTracker folder where manage.py is located and make the database:
```    
python manage.py makemigrations timeTracking
python manage.py migrate timeTracking
```
8) Start the website (hosting it locally with Django's built in server):
```    
python manage.py runserver
```
_Note: If used in production, remove the secret key from the [settings.py](https://github.com/RoboJojo/DjangoTimeTracker/blob/master/timeTracker/settings.py) file, and do not use the development server started with the runserver command_
