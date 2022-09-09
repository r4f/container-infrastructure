# Helloworld example

### Serve via docker

To run this example, we don't build a customized image, but instead simply use an official `python` image from a repository such as `hub.docker.com`.
Using the `docker-compose.yml` is optional, as the setup is simple enough to run via
```
docker run --rm --publish 8000:8000 \
--volume $PWD/server:/server \
python:alpine python /server/hello.py
```

- Using the `python:alpine` images instead of the standard `python` image just saves a bit of time and disk space, and does in this case not behave differently.

The docker-compose equivalent of the line above is:

```
version: "3"
services:
  helloworld:
    image: python:alpine
    ports:
      - "8000:8000"
    volumes:
      - "$PWD/server:/server"
    command: ["python", "server/hello.py"]
```

and can be invoked via the following command:

```
docker-compose up
```