FROM python:3.7-alpine
WORKDIR /app
RUN apk update && apk add --no-cache postgresql-dev gcc musl-dev linux-headers python3-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 9090
# CMD ["python", "manage.py", "runserver", "0.0.0.0:9090"]
