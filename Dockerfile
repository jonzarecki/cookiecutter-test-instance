FROM continuumio/anaconda3:2020-02
# last version with python3.7 (i'm lazy to create an environment)

RUN mkdir /code

COPY .github/workflows/constraints.txt /tmp
RUN pip install --constraint=/tmp/constraints.txt pip
RUN pip install --constraint=/tmp/constraints.txt poetry
RUN pip install --constraint=/tmp/constraints.txt nox nox-poetry

COPY . /code
WORKDIR /code

