Напишите простое приложение на Node.js, которое отдает "Hello, World!" на запросы. Создайте Dockerfile для этого Node.js приложения.

# Постройте Docker-образ:

docker build -t task2 .

# Запустите Docker-контейнер:

docker run -p 3000:3000 task2

# результат: 

http://____:3000/

<img width="599" alt="Снимок экрана 2024-06-27 в 12 59 12" src="https://github.com/PhilinVeselov/devops/assets/110721135/9e5d2b29-0627-4a1b-8b5d-720f532bdc96">

<img width="532" alt="Снимок экрана 2024-06-27 в 12 59 21" src="https://github.com/PhilinVeselov/devops/assets/110721135/28f544ad-3e21-4551-8441-a6ec5fb537cb">
