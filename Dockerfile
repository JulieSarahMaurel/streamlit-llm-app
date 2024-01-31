FROM python:3.8

EXPOSE 8080
WORKDIR /app

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY ./app.py ./
COPY ./src ./

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
