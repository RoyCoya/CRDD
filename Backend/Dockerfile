FROM python:3.11

ENV MYSQL_PSW=520Syner^Coya

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
