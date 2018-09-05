FROM alpine:3.8

RUN apk add --update \
    python \
    py-pip \
  && pip install prometheus-client \
  && pip install speedtest-cli \
  && rm -rf /var/cache/apk/*

RUN mkdir /app
COPY speedtest-exporter.py /app/

EXPOSE 9104

ENTRYPOINT ["/usr/bin/python", "-u", "/app/speedtest-exporter.py"]

