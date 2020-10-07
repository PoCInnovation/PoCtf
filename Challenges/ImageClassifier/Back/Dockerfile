FROM python:3

COPY . /app

WORKDIR /app

EXPOSE 5000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --use-feature=2020-resolver
CMD ["flask", "run"]
