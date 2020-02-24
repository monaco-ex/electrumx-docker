FROM ubuntu:18.04
MAINTAINER Cryptcoin Junkey "cryptcoin.junkey@gmail.com"

RUN apt-get update \
    && apt-get install -y wget git python3.7 python3.7-dev python3.7-distutils libleveldb-dev \
    && wget https://bootstrap.pypa.io/get-pip.py \
    && python3.7 get-pip.py \
    && pip3 install setuptools --upgrade \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  \
    && mkdir /log /db /env \
    && groupadd -r electrumx \
    && useradd -s /bin/bash -m -g electrumx electrumx \
    && cd /home/electrumx \
    && git clone https://github.com/kyuupichan/electrumx.git  -b 1.14.0 \
    && chown -R electrumx:electrumx electrumx && cd electrumx \
    && chown -R electrumx:electrumx /log /db /env \
    && python3.7 setup.py install
    
USER electrumx

VOLUME /db /log /env

COPY env/* /env/

RUN cd ~ \
    && mkdir -p ~/service ~/scripts/electrumx ~/electrumx/lib \
    && cp -R ~/electrumx/contrib/daemontools/* ~/scripts/electrumx \
    && chmod +x ~/scripts/electrumx/run \
    && chmod +x ~/scripts/electrumx/log/run \
    && sed -i '$d' ~/scripts/electrumx/log/run \
    && sed -i '$a\exec multilog t s500000 n10 /log' ~/scripts/electrumx/log/run  \
    && cp /env/* /home/electrumx/scripts/electrumx/env/ \
    && cat ~/scripts/electrumx/env/coins.py >> ~/electrumx/lib/coins.py \
    && ln -s ~/scripts/electrumx  ~/service/electrumx

CMD ["bash","-c","cp /env/* /home/electrumx/scripts/electrumx/env/ && svscan /home/electrumx/service"]
