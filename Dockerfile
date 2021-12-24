FROM docker.io/python:3

RUN groupadd pysauce && useradd --no-log-init -g pysauce pysauce

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER pysauce

CMD ["python", "-u", "./main.py"]