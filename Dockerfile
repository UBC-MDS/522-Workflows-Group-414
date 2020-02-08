
# Authors: Tejas Phaterpekar, Thomas Pin, Matthew Connell
# Date: February 6, 2020
# Summary: This file makes a container with libraries necessary to run analysis on ASD Screening Analysis
# More info on the analysis here: https://github.com/UBC-MDS/522-Workflows-Group-414

# Use rocker's tidy verse as the base package
FROM rocker/tidyverse

# Install packages that weren't already in the Rocker/tidyverse image
RUN Rscript -e "install.packages('caret')"
RUN Rscript -e "install.packages('kableExtra')"


# install the anaconda distribution of python
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy && \
    /opt/conda/bin/conda update -n base -c defaults conda

# install docopt python package
RUN /opt/conda/bin/conda install -y -c anaconda docopt

# Install chromedriver
RUN wget -q "https://chromedriver.storage.googleapis.com/79.0.3945.36/chromedriver_linux64.zip" -O /tmp/chromedriver.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin/ \
    && rm /tmp/chromedriver.zip && chown root:root /usr/bin/chromedriver && chmod +x /usr/bin/chromedriver

# install Altair and selenium to produce plots
RUN /opt/conda/bin/conda install -y -c conda-forge altair 
RUN /opt/conda/bin/conda install -y selenium
RUN apt-get update && apt install -y chromium && apt-get install -y libnss3 && apt-get install unzip

# install the R package e1071 for the caret package to run
RUN Rscript -e "install.packages('e1071')"

# Put anaconda python in path
ENV PATH="/opt/conda/bin:${PATH}"