FROM python:3.12-slim
WORKDIR /src
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]