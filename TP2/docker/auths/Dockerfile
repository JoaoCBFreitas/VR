FROM python:latest


RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install psycopg2

WORKDIR /home/mail_app

COPY create_DB.py postgres.py auth_server.py database.ini config.py authentication.py /home/mail_app/
RUN ls -la && pwd
EXPOSE 5000/tcp
CMD ["sh","-c","python3 create_DB.py && python3 auth_server.py" ]

