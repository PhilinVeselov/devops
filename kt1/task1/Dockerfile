FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential

COPY static_files /static_files
COPY server.py /server.py

WORKDIR /

EXPOSE 8080

CMD ["python", "server.py"]
