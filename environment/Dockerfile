# hash:sha256:88aaf1bdcc4cfe0d9d752c83b6c9a6ee999a27ca4b1f26b08ced0df4d0db9d5f
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/jupyterlab:3.6.1-miniconda4.12.0-python3.9-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive
ARG CUSTOM_KEY

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip install -U --no-cache-dir \
    aind-codeocean-utils==0.1.4
