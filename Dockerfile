FROM python:3.10.13-bookworm 
# setup environment variable  
ENV DockerHOME=/home/app/webapp  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# set work directory
WORKDIR /currency_converter

# install dependencies  
COPY /currency_converter/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy project
COPY . .

# port where the Django app runs  
EXPOSE 8000  
