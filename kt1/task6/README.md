Напишите простое приложение на Go, например, программа, которая выводит "Hello, World!". Создайте Dockerfile для этого приложения на Go.

# Постройте Docker-образ:

docker build -t task6 .

# Запустите Docker-контейнер:

docker run -p 8080:80 task6

# результат: 

<img width="429" alt="Снимок экрана 2024-06-27 в 13 16 45" src="https://github.com/PhilinVeselov/devops/assets/110721135/98cd14cf-d08c-468b-92f3-b9136c95f179">
