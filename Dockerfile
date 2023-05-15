# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11.2

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
WORKDIR /app

RUN apt-get update -qq && \
    apt-get install -y git python3-pip build-essential

COPY . /app
RUN python3 -m pip install -r requirements.txt