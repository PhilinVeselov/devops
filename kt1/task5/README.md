Напишите простое приложение на Ruby, например, программа, которая выводит "Hello, World!". Создайте Dockerfile для этого приложения на Ruby.

# Постройте Docker-образ:

docker build -t task5 .

# Запустите Docker-контейнер:

docker run -p 8080:80 task5

# результат: 

<img width="427" alt="Снимок экрана 2024-06-27 в 13 14 34" src="https://github.com/PhilinVeselov/devops/assets/110721135/6db91ee7-970f-476f-822f-bc7880504e3a">
