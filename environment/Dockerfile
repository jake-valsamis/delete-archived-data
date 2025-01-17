# hash:sha256:457ae8e78b9fccac81b6034571530f04b7c091943ef320edc71247216428cd16
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/jupyterlab:3.6.1-miniconda4.12.0-python3.9-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive
ARG CUSTOM_KEY

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

ENV CODE_OCEAN_DOMAIN=https://codeocean.allenneuraldynamics.org/

RUN pip install -U --no-cache-dir \
    codeocean==0.3.0
