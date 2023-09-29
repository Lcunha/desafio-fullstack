FROM python:3.10
RUN mkdir /code
WORKDIR /code/
ADD requeriments.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/