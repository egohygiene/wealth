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
    LC_ALL=${LANG} \
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

# Set working directory
WORKDIR /workspace

# Copy the proxy setup script
COPY .devcontainer/post_create.py /workspace/.devcontainer/post_create.py
