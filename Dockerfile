# Use an official Python runtime based on Debian 10 "bullseye" as a parent image
FROM python:3.12.12-bullseye as base

# Set the working directory to /app
WORKDIR /app

RUN apt update && \
    apt upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip setuptools wheel
#    pip install --no-cache-dir --force-reinstall -r requirements.txt -r requirements_test.txt

# Copy the current directory contents into the container at /app
COPY . /app
