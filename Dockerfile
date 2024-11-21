FROM python:3.10-alpine

ENV GOOGLE_API_KEY=test

WORKDIR /AIML

COPY . /AIML/

RUN pip install -r requirements.txt


EXPOSE 5000

CMD [ "python3","server.py" ]