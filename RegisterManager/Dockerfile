FROM python:3.9.5-slim-buster
RUN mkdir /app /tmp/wheels
RUN addgroup --system app && adduser --system --group app
WORKDIR /app
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /tmp/wheels -r requirements.txt
RUN pip install --no-cache /tmp/wheels/*
RUN rm -rf /tmp/wheels/*
COPY . .
ENV PYTHONPATH /app
USER app
EXPOSE 5005
CMD ["gunicorn", "-b", "0.0.0.0:5005", "main:app"]
