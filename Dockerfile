FROM python:3-alpine
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py","--host=0.0.0.0"]
