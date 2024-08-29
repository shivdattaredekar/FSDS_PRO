"""
Install below dependencies
pip3 install gunicorn
sudo apt install nginx

lets assume our application name is app.py

test running your application with Gunicorn before integrating it with Nginx
cd /path/to/your/my_flask_app
waitress-serve --port=8000 app:app

Add a new server block to handle requests for your Flask application

http {
    ...
    server {
        listen 80;
        server_name localhost;  # Use your domain or IP if applicable

        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        location /static/ {
            alias C:/path/to/your/my_flask_app/static/;
        }
    }
}

start nginx
nginx -s reload


"""













