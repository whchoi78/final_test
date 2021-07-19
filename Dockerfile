FROM dlalstjr28/final_project:was
EXPOSE 8000
EXPOSE 8080
WORKDIR /django
CMD python3 /django/manage.py makemigrations && python3 /django/manage.py migrate && python3 /django/manage.py runserver 0:8000 
