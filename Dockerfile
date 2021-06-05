FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /Profile-Builder
COPY requirements.txt /Profile-Builder/
RUN pip install -r requirements.txt
COPY . /Profile-Builder/
