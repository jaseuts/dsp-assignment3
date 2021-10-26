# To be filled by students
FROM python:3.8.2-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD ["streamlit", "run", "app/streamlit_app.py"]