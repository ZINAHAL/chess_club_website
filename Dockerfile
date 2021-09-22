FROM python:3

# Below ensures the python output is sent to the terminal rather than buffered
ENV PYTHONUNBUFFERED=1

WORKDIR /knights
COPY knights .
RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

CMD [ "uwsgi", "--ini", "uwsgi.ini" ]
