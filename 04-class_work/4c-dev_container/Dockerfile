# base image

FROM python:3.12 

# setup working directory in container
WORKDIR /app  #layer2

# copy all files to app directory
COPY ./main.py /app/   

# command to run on container start
CMD ["python", "main.py"]  
