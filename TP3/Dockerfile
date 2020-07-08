FROM ubuntu
RUN apt-get update 
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get install -y bash-completion software-properties-common curl ssh git iputils-ping net-tools
RUN apt-get install -y npm openjdk-8-jre-headless
RUN curl -O https://nexus.opendaylight.org/content/groups/public/org/opendaylight/integration/distribution-karaf/0.3.0-Lithium/distribution-karaf-0.3.0-Lithium.tar.gz
RUN tar -xvzf distribution-karaf-0.3.0-Lithium.tar.gz
RUN git clone https://github.com/CiscoDevNet/OpenDaylight-Openflow-App.git
RUN sed -i 's/localhost/192.168.3.2/g' ./OpenDaylight-Openflow-App/ofm/src/common/config/env.module.js
RUN npm install -g grunt-cli
