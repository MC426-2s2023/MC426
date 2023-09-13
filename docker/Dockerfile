FROM python:3.8

WORKDIR /usr/src/app

COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY .. .

ENV DJANGO_SETTINGS_MODULE projeto_mc426.projeto_mc426.settings

CMD ["gunicorn", "projeto_mc426.projeto_mc426.wsgi:application", "--bind", "0.0.0.0:8000"]