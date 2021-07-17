FROM python:3.7-slim

ENV QUICKPOLLS=/home/QuickPolls

RUN mkdir -p $QUICKPOLLS
RUN mkdir -p $QUICKPOLLS/static

WORKDIR $QUICKPOLLS

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install netcat -y

RUN pip install --upgrade pip
COPY . /home/QuickPolls
RUN pip install -r requirements.txt

ENTRYPOINT ["/home/QuickPolls/entrypoint.sh"]