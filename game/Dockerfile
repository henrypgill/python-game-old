FROM python as base

WORKDIR /app

COPY . .
RUN python3 -m pip install -r requirements.txt

EXPOSE 8000

CMD python3 main.py