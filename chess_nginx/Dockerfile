FROM nginx

COPY default.conf /etc/nginx/conf.d/
COPY uwsgi_params /etc/nginx/
RUN mkdir -p /chess_site/static
RUN mkdir /chess_site/media
RUN mkdir /unix_sockets
