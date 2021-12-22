FROM python:3.8-slim-buster
ARG WAVE_VERSION=0.19.0
RUN apt-get update
RUN apt-get install -y ca-certificates supervisor wget
RUN wget https://github.com/h2oai/wave/releases/download/v$WAVE_VERSION/wave-$WAVE_VERSION-linux-amd64.tar.gz
RUN tar -xzf wave-$WAVE_VERSION-linux-amd64.tar.gz
RUN mv wave-$WAVE_VERSION-linux-amd64 /root/wave_server
RUN ln -s /root/wave_server/www /www
COPY ./app /app
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY requirements.txt requirements.txt 
RUN pip3 --no-cache-dir install -r requirements.txt
ENTRYPOINT ["/usr/bin/supervisord"]
EXPOSE 10101