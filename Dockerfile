FROM kennethreitz/pipenv

RUN apt update && apt install firefox -y
RUN webdrivermanager firefox

COPY . /app
CMD pytest