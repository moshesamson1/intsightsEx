FROM python:3

ADD ./src /src

RUN pip install twisted  requests lxml arrow

CMD [ "python", "./src/pcrawler.py" ]