# Stage 1: Use the official Selenium image with Chrome
FROM selenium/standalone-chrome:latest AS selenium


FROM python:latest


# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    build-essential \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libbz2-dev \
    libsqlite3-dev \
    libpq-dev \
    libreadline-dev \
    libncursesw5-dev \
    tk-dev \
    liblzma-dev \
    xz-utils \
    libblas-dev \
    liblapack-dev \
    gfortran \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY --from=selenium /opt/google/chrome /opt/google/chrome
COPY --from=selenium /usr/bin/chromedriver /usr/bin/chromedriver
COPY --from=selenium /opt/selenium /opt/selenium

ENV PATH="/opt/google/chrome:/usr/bin/chromedriver:${PATH}"
ENV CHROME_DRIVER_PATH="/usr/bin/chromedriver"
ENV DISPLAY=:99


COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR app
COPY . /app

