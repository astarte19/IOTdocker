#Use the official image as a parent image
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pycryptodome

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define the command to run the application
#CMD ["python", "temperature.py"]
