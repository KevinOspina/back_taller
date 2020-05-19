FROM python:3.7
# Send output to the terminal
ENV PYTHONBUFFERED 1

RUN mkdir /meejel_service

WORKDIR /meejel_service

ADD . /meejel_service

RUN pip install -r requirements.txt

RUN python manage.py makemigrations && python manage.py migrate
