FROM python:latest

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get upgrade -y && apt-get install -y unzip

RUN pip install requests && pip install pymongo

CMD ["python","Main.py","/app/pollutionData","/app/pollution"]

