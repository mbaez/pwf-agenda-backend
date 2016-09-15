FROM library/ubuntu:15.10
MAINTAINER maxibaezpy@gmail.com

RUN apt-get update && apt-get upgrade
RUN apt-get install -y apache2 build-essential libapache2-mod-wsgi libxml2-dev python-psycopg2

#SE habilitan los módulos del apache
RUN a2enmod proxy proxy_http rewrite deflate headers proxy_balancer proxy_connect proxy_html wsgi

COPY ./src /var/www/ws-server/
ADD resources/ws.conf /etc/apache2/conf-enabled/ws.conf
RUN chmod 777 /etc/apache2/conf-enabled/ws.conf

RUN apt-get install -y vim
RUN   chown -R www-data:www-data /var/www/ws-server
EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
