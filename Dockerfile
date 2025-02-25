# Use an official lightweight Python image.
FROM python:3.10-slim

RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config python3-dev curl
# Set the working directory in docker
WORKDIR /app

# Copy the dependencies file to the working directory
COPY src/requirements/requirements.txt /app/requirements.txt

# Install any dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the content of the local src directory to the working directory
COPY ./src/ .

# Specify the command to run on container start
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
