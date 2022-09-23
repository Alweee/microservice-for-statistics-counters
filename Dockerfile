FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

WORKDIR /app/statistics_counter

CMD ["python3", "manage.py", "runserver", "0:8000"]
