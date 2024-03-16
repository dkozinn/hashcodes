FROM python:3.10
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
ADD . /app
EXPOSE 9090
#ENTRYPOINT ["python","app/app.py"]
#ENTRYPOINT ["python","app.py"]
#ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "app.wsgi:app"]
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]