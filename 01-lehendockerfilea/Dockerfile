#Komentarioa 

FROM ubuntu:24.04

COPY fitxategia.txt /home/fitxategia.txt

RUN cat /home/fitxategia.txt

RUN apt update && apt install -y nginx

ENV IZENA="Pablo"

RUN echo $IZENA

EXPOSE 80

ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]

