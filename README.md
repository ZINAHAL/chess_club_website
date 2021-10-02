BEFORE EVERYTHING:
- Setup a Postgres database
- Create knights/env.py file and add the following with your database details:
```
import os

os.environ["DATABASE_NAME"] = '*******'
os.environ["DATABASE_USER"] = '*******'
os.environ["DATABASE_PASSWORD"] = '*******'
os.environ["DATABASE_HOST"] = '*******'
os.environ["DATABASE_PORT"] = '*******'
os.environ["SECRET_KEY"] = '*******'
```

DOCKER:
- Make the needed changes in the stared comments ("***********") of knights/knights/settings.py file
- (If this is being setup in a virtual machine, then add the machine's IP address in the "ALLOWED_HOSTS" list)
- Run "docker-compose -f docker-compose.yml up" in the main root folder
- Access the site @ localhost:8080 and localhost:8080/admin

LOCAL SERVER:
- Make the needed changes in the stared comments ("***********") of settings.py file
- python3 -m venv venv
- source venv/bin/activate
- pip install -r knights/requirements.txt
- python knights/manage.py runserver
- Access the site @ localhost:8000 and localhost:8080/admin
