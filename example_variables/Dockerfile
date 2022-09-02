FROM python:alpine AS minimal-useful-python
ARG user=dau

RUN adduser -D $user
USER $user

WORKDIR /workbench
#Or use WORKDIR /home/$user ?

ENV PATH=/home/$user/.local/bin:$PATH
RUN pip install --no-cache-dir --upgrade \
    pip \
 && pip install --no-cache-dir --upgrade \
    python-decouple

ENV IMAGE_TYPE=minimal

CMD /bin/sh

# Second stage with more installed software
FROM minimal-useful-python AS python-dev

ENV IMAGE_TYPE=dev
RUN pip install --no-cache-dir --upgrade \
    ipython

# Third stage with even more software
FROM python-dev AS python-full

ENV IMAGE_TYPE=pipes_and_wistles
RUN pip install --no-cache-dir --upgrade \
    flask