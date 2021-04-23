FROM joyzoursky/python-chromedriver:3.7

ADD ./ /app
WORKDIR /app

RUN pip3.7 install -r ./requirements.txt
ENV PYTHONPATH /app

CMD [ "behave" ]