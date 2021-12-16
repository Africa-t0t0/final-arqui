FROM python:3.8.3-slim
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
COPY requirements.txt /tmp/
WORKDIR /app
COPY app2.py /app/.
COPY pinguino.jpg /app/.
EXPOSE 5001
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
CMD ["python", "/app/app2.py"]
