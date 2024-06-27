# Используем базовый образ Python
FROM python:3.9-slim

# Установка зависимостей
RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential

# Копирование статических файлов в контейнер
COPY static_files /static_files

# Копирование кода сервера в контейнер
COPY server.py /server.py

# Определение рабочей директории
WORKDIR /

# Открытие порта
EXPOSE 8080

# Запуск сервера при старте контейнера
CMD ["python", "/server.py"]

