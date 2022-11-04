# Using R version 4.2 causes issues when installing `pyCHNOSZ`.
FROM jupyter/r-notebook:r-4.1.3

# Grants `sudo` privledges to install TeX related packages.
ENV GRANT_SUDO yes

USER root

WORKDIR /home/notebook

RUN sudo apt update

# Disables interactive CLI when building for tzdata.
RUN DEBIAN_FRONTEND="noninteractive" TZ=Etc/UTC apt-get -y install tzdata

# Installs TeX to export notebook to pdf
# https://nbconvert.readthedocs.io/en/latest/install.html#installing-tex
RUN sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic -y

# COPY environment.yml ./
# RUN conda env update -n base --file environment.yml --verbose

COPY . .
