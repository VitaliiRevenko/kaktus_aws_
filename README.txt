1. Edit nginx/mysite.conf replace svyat.pp.ua to YOUR DOCMAIN NAME.
2. Edit .env and set your domain name, your secret and other settings
3. On MAIN NGINX in server set config to pipe data to dockerized site:
edit   /etc/nginx/sites-available/default 

location / {
	     if ($request_uri ~* ".(ico|css|js|gif|jpe?g|png|woff|woff2|svg)$") {
                                        expires 360d;
                                        access_log off;
                                        add_header Pragma public;
                                        add_header Cache-Control "public";
                                        break;
                                }
	     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;                                                                                             
         proxy_redirect off;
	     proxy_pass http://127.0.0.1:9079/;
	}


4. If required add celery start config to docker-compose.yml

 celery:
        build: ./www
        env_file:
            - ".env"
        environment:
            - TZ=${TZ}
            - C_FORCE_ROOT=1
        depends_on:
            - redis
            - postgres
            - nginx
        tty: true
        volumes:
            - "./www:/srv/site:Z"
        command: celery -A mysite worker -E -B --scheduler django -l info --autoscale=20,5
