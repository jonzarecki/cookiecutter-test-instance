FROM continuumio/anaconda3:2021.05

RUN mkdir /code

COPY .github/workflows/constraints.txt /tmp
RUN pip install --constraint=/tmp/constraints.txt pip
RUN pip install --constraint=/tmp/constraints.txt poetry
RUN pip install --constraint=/tmp/constraints.txt nox nox-poetry

COPY . /code
WORKDIR /code

