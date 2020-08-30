FROM frolvlad/alpine-glibc

RUN apk add socat

COPY flag.txt  /home/user/flag.txt
COPY challenge /home/user/challenge
RUN chmod 0001 /home/user/challenge

RUN adduser -D user
USER user

WORKDIR /home/user
CMD socat TCP-LISTEN:8080,reuseaddr,fork EXEC:"./challenge"
