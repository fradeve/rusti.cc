FROM        nginx:latest
MAINTAINER  Francesco de Virgilio <fradeve@inventati.org>

RUN         apt-get -y update && apt-get -y install supervisor

COPY        supervisord.conf /etc/supervisor/supervisord.conf
COPY        nginx.conf /etc/nginx/nginx.conf
COPY        output /usr/share/nginx/html/rusti.cc

RUN         chown -R www-data:www-data /usr/share/nginx/html/rusti.cc

# Expose HTTP port
EXPOSE      80

# Last but least, unleach the daemon!
ENTRYPOINT  ["/usr/bin/supervisord"]
