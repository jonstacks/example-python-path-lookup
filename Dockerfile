FROM python:3

WORKDIR /usr/src/app
COPY test.py test.txt com.example.my.jar ./

CMD ["python", "test.py"]