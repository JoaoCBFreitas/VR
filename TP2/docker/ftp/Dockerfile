FROM stilliard/pure-ftpd
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y apt-utils
RUN apt-get install -y iputils-ping 
RUN apt-get install -y net-tools
RUN apt-get install -y nginx git python-setuptools python-dev
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install httpserver
RUN pip3 install flask
RUN pip3 install requests
RUN mkdir /home/code
WORKDIR /home/code
RUN mkdir /home/code/src
RUN mkdir /home/code/Templates
COPY /src/*.* /home/code/src/
COPY /Templates/*.* /home/code/Templates/
COPY script.sh ./
RUN chmod +x script.sh
ENTRYPOINT ["/home/code/script.sh"]
