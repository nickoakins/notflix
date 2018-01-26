
FROM python:3.6
MAINTAINER nick
COPY . /NotFlix
WORKDIR /NotFlix
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["notflix.py"]

