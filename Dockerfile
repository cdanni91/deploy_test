
FROM python:3.9-slim


WORKDIR /


COPY requirements.txt requirements.txt


RUN pip install --no-cache-dir -r requirements.txt


COPY . .


ENV PORT=5000
EXPOSE $PORT


CMD ["python", "wiki_script.py"]
