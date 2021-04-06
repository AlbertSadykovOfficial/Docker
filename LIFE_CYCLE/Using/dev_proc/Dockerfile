FROM python:3.4  # Выбираем версию языка

RUN pip install Flask==0.10.1 uWSGI==2.0.8 	# Устанавливае Flask И uWSGI
WORKDIR /app																# Устанавливаем рабочий каталог
COPY app /app																# Копируем содержимое каталога 
																						# app в каталог контейнера /app

CMD ["uwsgi", "--http", "0.0.0.0:9090", "--wsgi-file", "/app/identidock.py", "--callable", "app", "--stats", "0.0.0.0:9191"]
#CMD ["python", "identidock.py"] # Зпаустить код файла/