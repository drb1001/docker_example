FROM python:3.7-alpine
# See: https://hub.docker.com/_/python

# no-cache-dir to reduce image size
COPY requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ /src/

ENTRYPOINT ["python"]
CMD ["src/app.py"]
