Напишите простое веб-приложение на PHP, которое отображает "Hello, World!" в браузере. Создайте Dockerfile для этого веб-приложения.


# Постройте Docker-образ:

docker build -t task4 .

# Запустите Docker-контейнер:

docker run -p 8080:80 task4

# результат: 

http://____:8080/

<img width="545" alt="Снимок экрана 2024-06-27 в 13 11 58" src="https://github.com/PhilinVeselov/devops/assets/110721135/4546a74b-59a4-42f1-80d1-35729acdc03b">
<img width="922" alt="Снимок экрана 2024-06-27 в 13 12 07" src="https://github.com/PhilinVeselov/devops/assets/110721135/2aa86263-6d24-4700-801f-42b8f1b58bd9">
