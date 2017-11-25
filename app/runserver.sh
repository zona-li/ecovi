cd /app

python ./homestarter/manage.py makemigrations 
python ./homestarter/manage.py migrate 
mod_wsgi-express start-server --working-directory /app/homestarter/ /app/homestarter/homestarter/wsgi.py