# website_portfolio

create virtual env
python -m venv venv

cd /c/Users/Emachines/PycharmProjects/Portfolio_website
source venv/Scripts/activate
pip freeze > requirements.txt
git init
git add .
git commit -am "second commit"
git push heroku master
