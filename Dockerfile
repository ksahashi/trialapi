FROM python:3.10-slim

RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config python3-dev curl
WORKDIR /app

COPY src/requirements/requirements.txt /app/requirements.txt

# Add this line to upgrade pip
RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./src/ .
COPY ./db/ ../db

COPY ./script/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# Specify the command to run on container start
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
