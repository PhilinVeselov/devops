FROM python:3.9

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y sqlite3
RUN pip install flask flask_cors

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
