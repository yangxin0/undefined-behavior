FROM python:3.10-slim as chatgpt-server

RUN apt update \
    && apt install -y --no-install-recommends python3-dev default-libmysqlclient-dev build-essential libpq-dev dos2unix \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -i https://mirrors.cloud.tencent.com/pypi/simple -r requirements.txt

WORKDIR /app

COPY . .

RUN python manage.py check --deploy && python manage.py collectstatic --no-input

FROM nginx:1.22-alpine as nginx-server

WORKDIR /app

COPY --from=chatgpt-server /app/static /app/static

COPY nginx.conf /etc/nginx/templates/default.conf.template
