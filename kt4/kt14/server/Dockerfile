# Базовый образ
FROM python:3.9

# Рабочая директория
WORKDIR /app

# Копируем файлы
COPY . .

# Установка sqlite3 через системные пакеты
RUN apt-get update && apt-get install -y sqlite3
RUN pip install flask flask_cors

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска вашего приложения с использованием Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
