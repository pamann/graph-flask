FROM python:3.8
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD ["app.py"]