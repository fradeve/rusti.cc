FROM        nginx:latest
MAINTAINER  Francesco de Virgilio <fradeve@inventati.org>

ENV         PELICAN_PLUGIN_PATH /usr/share/nginx/html/rusti.cc/plugins
RUN         apt-get -y update && apt-get -y install supervisor python-pip python-dev libffi-dev libssl-dev

COPY        supervisord.conf /etc/supervisor/supervisord.conf
COPY        nginx.conf /etc/nginx/nginx.conf
COPY        . /usr/share/nginx/html/rusti.cc

RUN         chown -R www-data:www-data /usr/share/nginx/html/rusti.cc

WORKDIR     /usr/share/nginx/html/rusti.cc

RUN         pip install -r requirements.txt
RUN         fab build

# Expose HTTP port
EXPOSE      80

# Last but least, unleach the daemon!
ENTRYPOINT  ["/usr/bin/supervisord"]
