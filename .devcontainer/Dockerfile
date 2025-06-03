# syntax=docker/dockerfile:1.4

FROM mcr.microsoft.com/devcontainers/base@sha256:cdff177dd5755c0ba2afea60cdc0ab07d933c60d50c6c90dccbcc42b4b4ab76d

# Proxy Environment Variables
# https://docs.docker.com/reference/dockerfile/#predefined-args

# Override the temporary directory if needed
ARG TMPDIR=/tmp

# Locale and timezone settings
ARG LANG=en_US.UTF-8
ARG LANGUAGE=en_US:en
ARG TZ=UTC
ARG LC_ALL=en_US.UTF-8

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive \
    DEBCONF_NONINTERACTIVE_SEEN=true \
    DEBIAN_PRIORITY=critical \
    DEBCONF_NOWARNINGS=yes \
    TERM=xterm-256color \
    APT_LISTCHANGES_FRONTEND=none \
    APT_LISTBUGS_FRONTEND=none \
    TMPDIR=${TMPDIR} \
    LANG=${LANG} \
    LANGUAGE=${LANGUAGE} \
    TZ=${TZ} \
    LC_ALL=${LC_ALL} \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=1 \
    PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# Install system dependencies required for building Python + Python packages
RUN apt-get update -qq && \
    apt-get install --no-install-recommends --yes \
        build-essential \
        ca-certificates \
        ccache \
        clang \
        clang-format \
        clang-tidy \
        cmake \
        curl \
        dnsutils \
        git \
        gnupg \
        htop \
        iputils-ping \
        jq \
        less \
        libblosc-dev \
        libboost-all-dev \
        libbz2-dev \
        libcurl4-openssl-dev \
        libdb-dev \
        libffi-dev \
        libgdbm-dev \
        liblz4-dev \
        liblzma-dev \
        libncursesw5-dev \
        libnss3-dev \
        libreadline-dev \
        libsqlite3-dev \
        libssl-dev \
        libxi-dev \
        libxml2-dev \
        libxmlsec1-dev \
        libxslt1-dev \
        libzstd-dev \
        llvm \
        net-tools \
        ninja-build \
        pkg-config \
        python3 \
        python3-dev \
        python3-pip \
        python3-venv \
        ripgrep \
        sudo \
        tar \
        tk-dev \
        unzip \
        uuid-dev \
        vim \
        wget \
        xz-utils \
        zlib1g-dev \
        zsh \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* /var/tmp/* /tmp/*

RUN apt-get update -qq && apt-get install --no-install-recommends --yes \
    locales \
    tzdata \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* /var/tmp/* /tmp/*

RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment \
    && echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \
    && echo "LANG=en_US.UTF-8" > /etc/locale.conf \
    && locale-gen en_US.UTF-8 \
    && update-locale LANG=en_US.UTF-8 \
    && dpkg-reconfigure locales

# Ensure SYS_UID_MAX and SYS_GID_MAX are set to high values, uncommented or inserted
RUN sed -i '/^#\?SYS_UID_MAX/ d' /etc/login.defs && echo 'SYS_UID_MAX 99999' >> /etc/login.defs && \
    sed -i '/^#\?SYS_GID_MAX/ d' /etc/login.defs && echo 'SYS_GID_MAX 99999' >> /etc/login.defs

RUN mkdir -p /devtools

# Set working directory
WORKDIR /workspace

# Copy the proxy setup script
COPY .devcontainer/post_create.py /workspace/.devcontainer/post_create.py

ENV NIX_CONF_DIR=/devtools/nix

# Ensure the Nix configuration directory exists
RUN mkdir -p ${NIX_CONF_DIR}

# Copy the Nix configuration file
COPY --chown=vscode:vscode .devcontainer/nix/nix.conf ${NIX_CONF_DIR}/nix.conf
