FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install git

# RUN python -m pip install basic_units
RUN python -m pip install numpy
RUN python -m pip install scikit-learn
RUN python -m pip install matplotlib
RUN python -m pip install tabulate
