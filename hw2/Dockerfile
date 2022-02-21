FROM debian:stretch

# Latex packages
RUN apt-get update && \
    apt update && \
    apt install -y graphviz && \
    apt-get install -y libgraphviz-dev wget build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev && \
    wget https://www.python.org/ftp/python/3.9.1/Python-3.9.1.tgz && \
    tar -xf Python-3.9.1.tgz && \
    cd Python-3.9.1 && \
    ./configure --enable-optimizations && \
    make -j 2 && \
    make altinstall && \
    apt-get install -y --no-install-recommends texlive-latex-recommended texlive-fonts-recommended && \
    apt-get install -y --no-install-recommends texlive-latex-extra texlive-fonts-extra texlive-lang-all && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /root
ADD . /proj

RUN  cd /proj && \
    pip3.9 install -r requirements.txt && \
    python3.9 main.py

# Default command
CMD ["bash"]