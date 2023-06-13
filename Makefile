mig:
	./manage.py makemigrations
	./manage.py migrate

admin:
	./manage.py createsuperuser --username admin --email ''

run_bot:
	./manage.py start_polling