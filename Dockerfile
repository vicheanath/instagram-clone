### Build and install packages
FROM python:3.9 as build-python

RUN apt-get -y update \
  && apt-get install -y gettext \
  # Cleanup apt cache
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
WORKDIR /app
COPY requirements/common.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

### Final image
FROM python:3.9-slim

RUN groupadd -r instagram-clone && useradd -r -g instagram-clone instagram-clone

RUN apt-get update \
  && apt-get install -y \
  libcairo2 \
  libgdk-pixbuf2.0-0 \
  liblcms2-2 \
  libopenjp2-7 \
  libpango-1.0-0 \
  libpangocairo-1.0-0 \
  libssl3 \
  libtiff6 \
  libwebp7 \
  libxml2 \
  libpq5 \
  shared-mime-info \
  mime-support \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN echo 'image/webp webp' >> /etc/mime.types
RUN echo 'image/avif avif' >> /etc/mime.types

RUN mkdir -p /app/media /app/static \
  && chown -R instagram-clone:instagram-clone /app/

COPY --from=build-python /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/
COPY --from=build-python /usr/local/bin/ /usr/local/bin/
COPY . /app
WORKDIR /app


EXPOSE 8000
ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "--bind", ":8000", "--workers", "4", "--worker-class", "config.asgi.gunicorn_worker.UvicornWorker", "config.asgi:application"]