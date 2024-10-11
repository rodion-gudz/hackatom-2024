FROM python:3.12.1-alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN pip install  -r requirements.txt

COPY . .

EXPOSE 6969

CMD ["python3", "app.py"]
