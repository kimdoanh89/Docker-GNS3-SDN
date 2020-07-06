FROM ubuntu:16.04

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y --no-install-recommends install \
    net-tools tcpdump telnet traceroute curl iperf3 knot-host openssh-client mtr-tiny socat nano vim-tiny \
    nmap iputils-ping wget unzip iproute openssh-server \
    bash-completion software-properties-common python-software-properties sudo ssh git \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get update \
    && apt-get -y install default-jre-headless \
    && cd /root \
    && wget https://nexus.opendaylight.org/content/repositories/public/org/opendaylight/integration/distribution-karaf/0.5.2-Boron-SR2/distribution-karaf-0.5.2-Boron-SR2.zip \
    && unzip distribution-karaf-0.5.2-Boron-SR2.zip \
    && curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - \
    && apt-get -y install nodejs \
    && git clone https://github.com/CiscoDevNet/OpenDaylight-Openflow-App.git \
    && npm install -g grunt-cli

RUN echo "export JAVA_HOME=/usr/lib/jvm/default-java" >> /root/.bashrc

RUN mkdir /var/run/sshd
RUN echo 'root:root' |chpasswd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN mkdir /root/.ssh
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 22

VOLUME [ "/root", "/usr", "/etc"]
CMD [ "sh", "-c", "cd; exec bash -i" ]

