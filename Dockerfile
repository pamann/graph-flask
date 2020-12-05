FROM python:3.8

# setup app
WORKDIR /app
ADD . /app
RUN pip3 install -r requirements.txt

# expose container port
EXPOSE 8080

# setup entrypoint
ENTRYPOINT [ "bash", "./gu_start.sh" ]
