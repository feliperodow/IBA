#Tells Docker to use the official python 3 image from dockerhub as a base image
FROM python:3
# Sets the container's working directory to /app
WORKDIR /app
# Copies all files from our local project into the container
ADD . /app
# Copy the requirements into the container
COPY requirements.txt /app/requirements.txt
# runs the pip install command for all packages listed in the requirements.txt file
RUN pip install -r requirements.txt