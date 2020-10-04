FROM python:3.7

RUN mkdir -p /app
WORKDIR /app

COPY . /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

EXPOSE 8800

CMD ["gunicorn", "--chdir", "/app", "--bind", ":8800", "--workers", "6", "task_manager.wsgi:application"]