# PYTHONFILES/Client/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY client.py client.py

CMD ["python", "client.py"]
