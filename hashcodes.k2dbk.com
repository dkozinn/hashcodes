server {
    listen 80;
    server_name hashcodes.k2dbk.com;

    location / {
        include uwsgi_params;
        uwsgi_pass unix://home/ubuntu/hashcodes/hashcodes.socket;
    }
}