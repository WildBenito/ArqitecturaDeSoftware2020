FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="xoxb-1443017183584-1412480381062-xtxE50QXPJaM2FQcS1S8dl4v"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN pip install wikipedia -r /requirements.txt

WORKDIR /nestor

COPY ./nestorbot.py /nestorbot.py
COPY ./nestorbot_app.py /nestorbot_app.py

CMD [ "python", "/nestorbot_app.py" ]
