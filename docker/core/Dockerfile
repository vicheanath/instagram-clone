FROM python:3.12.0-alpine3.12

ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"

RUN pip install --upgrade pip


COPY ./requirements/local.txt /requirements.txt
RUN pip install -r /requirements.txt


RUN mkdir /app
WORKDIR /app
COPY . /app

COPY ./scripts/ /scripts/
RUN chmod +x /scripts/*


VOLUME /vol/web

CMD ["entrypoint.sh"]