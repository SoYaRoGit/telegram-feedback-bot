# Используем официальный образ Python
FROM python:3.12

# Обновляем pip
RUN pip install --upgrade pip

# Устанавливаем Poetry
RUN pip install poetry

# Устанавливаем рабочую директорию для приложения
WORKDIR /usr/src/app

# Копируем файлы проекта в контейнер
COPY . .

# Устанавливаем зависимости через Poetry
RUN poetry install

# Устанавливаем команду по умолчанию для запуска приложения
CMD ["poetry", "run", "python", "src/main.py"]
