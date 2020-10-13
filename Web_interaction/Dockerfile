FROM python:3.6
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "API2.py" ]
CMD start_app_command -p $PORT
