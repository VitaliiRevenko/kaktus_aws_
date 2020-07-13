FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV C_FORCE_ROOT 1

ADD requirements.txt /
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin gettext python3-dev python3-setuptools
RUN pip install -U pip && pip install -r requirements.txt

WORKDIR /srv/site

EXPOSE 8000

CMD exec gunicorn mysite.wsgi:application --bind 0.0.0.0:8000 --workers 10
#CMD python manage.py runserver 127.0.0.1:8000
