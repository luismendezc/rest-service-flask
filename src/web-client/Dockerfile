FROM python:alpine

ADD app.py .
ADD requirements.txt .
ADD templates/index.html templates/index.html

WORKDIR .

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]
