# Используем базовый образ Python 3.8 на основе slim-buster
FROM python:3.8-slim-buster

# Меняем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем все зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы из текущей директории в директорию /app внутри образа
COPY . .

# Запускаем интерпретатор python
ENTRYPOINT ["python"]

# Добавляем список параметров к ENTRYPOINT для выполнения команды, которая запускает приложение
CMD ["main.py"]
