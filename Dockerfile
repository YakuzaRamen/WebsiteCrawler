FROM python:3-alpine

#RUN apt-get update -y && \
#    apt-get install -y python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt
RUN mkdir result

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]

EXPOSE 5000

