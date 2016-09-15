FROM postgres:9.4
MAINTAINER maxibaezpy@gmail.com
RUN mkdir -p /docker-entrypoint-initdb.d
ADD ./agenda_web.sql /docker-entrypoint-initdb.d/schema.sql

ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]