# DjangoTimeTracker
A simple way to track your time!

Steps to setup:
1) Clone :
     git clone https://github.com/RoboJojo/DjangoTimeTracker.git
2) Download desired boostrap distribution into static folder :
     Something like this -> DjangoTimeTracker/static/boostrap-x.x.x-dist
3) Update html includes to match boostrap version (the x.x.x value): 
    For instance, in DjangoTimeTracker/templates/head.html, the x.x.x values need to be updated to the correct version
    <link rel="stylesheet" href="{% static 'bootstrap-x.x.x-dist/css/bootstrap.min.css' %}">
4) Download desired jquery distribution into static/js folder:
     Something like this -> DjangoTimeTracker/static/js/jquery-x.x.x.min.js
5) Update html includes to match jquery distribution :
    For instance, in DjangoTimeTracker/templates/footer.html, the x.x.x values need to be updated to the correct version
    <script src="{% static 'js/jquery-x.x.x.min.js' %}"></script>
6) Install django-chartjs:
    pip install django-chartjs
7) Navigate to DjangoTimeTracker folder where manage.py is located and make the database :
    python manage.py makemigrations
    python manage.py migrate