python3 -m venv .venv
CMD-SHIFT-P
input 'interpreter'
select local env
open a new terminal by '+'
or 
python3 activate env
pip3 install flask

app.py

>flask run

create Dockerfile 

>docker build -t rest-apis-flask-project . 

>docker run -dp 5000:5000 rest-apis-flask-project

pip3 install -r requirements.txt

Dockerfile update

>docker build -t flask-smorest-api . 
>docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api  // for debug

>docker run -dp 5005:5000 flask-smorest-api // for deployment

http://localhost:5005/swagger-ui

flask==2.2.2
flask-smorest==0.40.0

docker container ls -a
docker stop <Container_ID>
docker rm -f < Container_ID>
docker rmi -f <Image_name>

https://jwt.io/

pip3 install flask-migrate
flask db init
# delete ./instance/data.db

flask db migrate
# apply table to database instance/data.db
flask db upgrade 

# add new 'description' field into items table and call migrate again
flask db migrate
flask db upgrade

git init
ls -la
git status
create .gitignore
git add .
git rm --cached schemas.py
git add schemas.py

git checkout -- app.py 
# same as
git restore app.py

# unstage app.py
gir reset HEAD app.py
# or
git restore --staged app.py

# commit and add the message
git commit -am "readme changes"
