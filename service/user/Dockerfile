FROM python:3.7-slim
RUN pip install --no-cache-dir --upgrade pip
WORKDIR ./app
COPY . .
RUN python -m pip install -r requirements.txt
CMD ["python", "run.py"]