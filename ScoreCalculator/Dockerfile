FROM python:3.9.5-slim-buster
RUN apt-get update -y && apt-get install iputils-ping -y
RUN mkdir /app /tmp/wheels
RUN addgroup --system app && adduser --system --group app
WORKDIR /app
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /tmp/wheels -r requirements.txt
RUN pip install --no-cache /tmp/wheels/*
RUN rm -rf /tmp/wheels/*
COPY . .
USER app
EXPOSE 5003
CMD ["gunicorn", "-b", "0.0.0.0:5003", "main:app"]
