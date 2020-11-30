FROM python:latest

COPY requirements.txt /requeriments.txt

RUN pip install -r requeriments.txt
#RUN export FLASK_APP=main.py /Esto no funciona?/

COPY app app

WORKDIR /app

#ENTRYPOINT ["python3", "main.py"]
CMD ["python3", "main.py"]

#CMD ["flask", "run", "--host=0.0.0.0"]
