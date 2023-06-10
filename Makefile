mig:
	./manage.py makemigrations
	./manage.py migrate

admin:
	./manage.py createsuperuser --username admin --email ''