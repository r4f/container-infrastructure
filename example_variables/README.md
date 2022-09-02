#

## Small example with env variables

- alpine based images are light-weight
- not being root inside the container is good security practice
- `ARG` can set variables from inside or outside of the `Dockerfile`.
- `ENV` sets environment variables for the environment inside the container.

```
FROM python:alpine
ARG user=dau

RUN adduser -D $user
USER $user

RUN pip install --upgrade pip \
 && pip install python-decouple

ENV BUILT_FROM=python_alpine

CMD /bin/sh
```

One-liner to build the image and run a container based in it. (Probably won't run with the docker file above, as the script expects some more env variables to be set.)

```
docker run --env-file=.env -it --rm -v $PWD/scripts:/home/d2/scripts $(docker build -t py-alpine -q .) python scripts/show_env.py
```

- `-v [--volume]` requires absolute path. `$PWD` comes handy here.


## Security

There are many more advices how to build more secure containers. E.g.,
  - virtual networks only permitting the necessary access
  - drop capabilities
  - minimal images: [docker-slim](dockersl.im)
  - Video on docker and security (german, 2022-09): [Docker Container und Security](https://media.ccc.de/v/cccs-docker-container-und-security#t=4096)

## Questions

- How does one uninstall a busybox-installed tool, e.g., wget?