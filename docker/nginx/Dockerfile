from nginx:1.23.0-alpine

COPY ./nginx/* /etc/nginx/
COPY ./run.sh /run.sh


ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000


USER root
RUN apk add --no-cache openssl bash && \
    mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    mkdir -p /vol/www && \
    chmod 755 /vol/www && \
    chmod +x /run.sh
    

VOLUME /vol/static
VOLUME /vol/www

CMD ["/run.sh"]