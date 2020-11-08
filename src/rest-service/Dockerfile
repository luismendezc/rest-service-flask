FROM python:alpine

ADD app.py .
ADD requirements.txt .

WORKDIR .

RUN pip3 install -r requirements.txt

EXPOSE 2000

CMD ["python3", "app.py"]
