django-run:
	gunicorn --bind 0.0.0.0:8000 config.wsgi

update-source:
	git pull git@portfolio-app:wrawka/portfolio-app.git
	sudo systemctl restart gunicorn
