### golden_owl_test
## Before run this project 
Clone this repository: ```git clone https://github.com/huungociter/golden_owl_test.git```

#1 Need to install Django: 
Open terminal and run command: ```pip install django```

#2 Run project: 
Open terminal at root directory (example: golden_owl_test/)
 
Run command: ```python manage.py runserver```

Open: ```localhost:8000``` or ```http://127.0.0.1:8000``` on browser to view website\

(Note: Due to the nature of the test, there is little use of the database. So I use the sqlite database available in django to conveniently run the program. If you want to change to any other database like mysql or postgresql, just change the information in the file goldenowl_test/setting.py DATABASES)