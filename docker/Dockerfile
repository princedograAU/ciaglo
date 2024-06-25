FROM python:3.12-slim

# Ensure that Python outputs everything that's printed inside
# the application rather than buffering it.
ENV PYTHONUNBUFFERED 1

ENV DEBIAN_FRONTEND noninteractive

# Install OS dependencies
RUN apt-get update \
  && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    sudo \
    socat \
    gdebi \
    build-essential \
    libpq-dev \
    libpq5 \
    xorg \
    libssl-dev \
    libxrender-dev \
    xmlsec1 \
  && rm -rf /var/lib/apt/lists/*

# Create the application directory
RUN mkdir \
  /opt/ciaglo \
  /opt/ciaglo/static \
  /opt/ciaglo/media_root \
  /opt/storage

VOLUME '/opt/static'
VOLUME '/opt/storage'

WORKDIR /opt/ciaglo

# Copy pip requirements
COPY requirements requirements
ARG REQUIREMENTS_NAME=local
RUN pip install --upgrade pip
RUN pip install -r requirements/${REQUIREMENTS_NAME}.txt

# Add the rest of the app files
COPY . .

EXPOSE 8000

ENTRYPOINT ["docker/entrypoint.sh"]
CMD ["docker/start.sh"]
