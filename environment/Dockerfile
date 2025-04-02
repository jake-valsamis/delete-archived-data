# hash:sha256:eedfbf8862ff7a36a7c26000abaf4ced5a8c7e0345e23257cff7aa16d43f22dd
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/jupyterlab:3.6.1-miniconda4.12.0-python3.9-ubuntu20.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

ENV CODE_OCEAN_DOMAIN=https://acmecorp-cfn-demo.codeocean.com/

RUN pip install -U --no-cache-dir \
    codeocean==0.3.0
