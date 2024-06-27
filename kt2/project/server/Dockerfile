FROM php:latest

COPY ./index.php /var/www/html/
COPY ./text.txt /var/www/html/

CMD ["php", "-S", "0.0.0.0:80", "-t", "/var/www/html/"]
