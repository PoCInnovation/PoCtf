FROM frolvlad/alpine-glibc

RUN apk add socat

COPY challenge /home/user/
RUN chmod 0001 /home/user/challenge
COPY .*part /home/user/

RUN adduser -D user
USER user

WORKDIR /home/user
CMD socat TCP-LISTEN:8080,reuseaddr,fork EXEC:"./challenge"
