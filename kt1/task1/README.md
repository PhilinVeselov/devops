Создайте простой веб-сервер на Python, который будет отдавать статические файлы. Создайте Dockerfile для этого веб-сервера.


# Постройте Docker-образ:

docker build -t task1 .

# Запустите Docker-контейнер:

docker run -p 8080:8080 task1

# результат: 

http://____:8080/

<img width="719" alt="Снимок экрана 2024-06-27 в 12 54 20" src="https://github.com/PhilinVeselov/devops/assets/110721135/a31b8b91-f090-4f83-befc-0c28ef284d0e">

<img width="532" alt="Снимок экрана 2024-06-27 в 12 54 27" src="https://github.com/PhilinVeselov/devops/assets/110721135/9566c13d-db2b-42ca-83f0-662c7fb9f333">
