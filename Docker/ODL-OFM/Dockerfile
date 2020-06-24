FROM ubuntu:xenial

RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -y --no-install-recommends install \
    net-tools tcpdump telnet traceroute curl iperf3 knot-host openssh-client mtr-tiny socat nano vim-tiny \
    nmap iputils-ping \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get update \
    && apt-get -y install default-jre-headless \
    && export JAVA_HOME=/usr/lib/jvm/default-java \
    && apt-get -y install wget \
    && wget https://nexus.opendaylight.org/content/repositories/public/org/opendaylight/integration/distribution-karaf/0$
    && apt-get install -y unzip \
    && unzip distribution-karaf-0.5.2-Boron-SR2.zip

VOLUME [ "/root" ]
CMD [ "sh", "-c", "cd; exec bash -i" ]

