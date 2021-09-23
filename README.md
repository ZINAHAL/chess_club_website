DOCKER:
- make the needed changes in the stared comments ("***********") of settings.py file
- run "docker-compose -f docker-compose.yml up" in the main root folder
- access the site @ localhost:8080

LOCAL SERVER:
- make the needed changes in the stared comments ("***********") of settings.py file
- python3 -m venv venv
- source venv/bit/activate
- python knights/manage.py runserver
- access the site @ localhost:8000
