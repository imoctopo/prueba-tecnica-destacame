FROM python:3.9 as build-stage
ENV PYTHONUNBUFFERED 1
WORKDIR /src
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ .
RUN python manage.py migrate
RUN python manage.py collectstatic --no-input --clear
EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--workers", "4", "--bind", ":8000"]
