# Используем официальный образ OpenJDK
FROM openjdk:11-jdk-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app

# Копируем исходный код Java внутрь контейнера
COPY . /usr/src/app

# Компилируем Java приложение
RUN javac HelloWorld.java

# Команда для запуска приложения
CMD ["java", "HelloWorld"]

