# Используйте официальный образ Ubuntu
FROM ubuntu:22.04

# Обновите пакеты и установите Apache
RUN apt-get update && apt-get install -y apache2

# Копируйте ваш файл index.html в каталог Apache
COPY index.html /var/www/html/

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
# Определите порт, который будет прослушивать контейнер
EXPOSE 80

# Запустите Apache при старте контейнера
CMD ["apache2ctl", "-D", "FOREGROUND"]
