FROM python:3.6
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "API2.py" ]
RUN python3 Model/download_model.py 117M
RUN python3 Model/download_model.py 345M
