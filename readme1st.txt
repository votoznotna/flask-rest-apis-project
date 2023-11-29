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
#### delete ./instance/data.db

flask db migrate
#### apply table to database instance/data.db
flask db upgrade 

#### add new 'description' field into items table and call migrate again
flask db migrate
flask db upgrade

## Git usage
'''
git init
ls -la
git status
create .gitignore
git add .
git rm --cached schemas.py
git add schemas.py
''' 
### same:
'''
git checkout -- app.py 
git restore app.py
'''

### unstage app.py
'''
gir reset HEAD app.py
git restore --staged app.py
'''

#### commit and add the message
'''
git commit -am "readme changes"
'''


# Deployement

https://dashboard.render.com/web/new
testing with Insomnia: https://flask-rest-apis-project-mxl8.onrender.com

https://dashboard.render.com/web/srv-clj4vfl8td7s73bvvj40


https://customer.elephantsql.com/instance/create
https://api.elephantsql.com/console/2d81378b-6578-4143-b9e7-2a56b88813e7/details
copy postgres://.... to .env

Stores REST API (recording)


# remove migrations folder 
flask db init
flask db migrate
flask db upgrade

tables in ElephantSQL should be created

# run "flask db migrate" after any models changes 

# add  compare_type=True to migration's env.py
   context.configure(
        url=url, 
        target_metadata=get_metadata(), 
        compare_type=True,
        literal_binds=True
    )

$ and do 
flask db migration
flask db upgrade