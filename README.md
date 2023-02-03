# fyr_pricing_module

## How to run the project:
1. Clone the project in your local using `git clone https://github.com/OneGithubforMe/fyr_pricing_module`
2. After enabling the python virtual environment in the project repo, install all the dependencies by running `pip install -r requirements.txt`.
3. For now,this project run with `SQLite` database so no need to install/configure any external database because SQlite is created by Django automatically.
4. Run `python manage.py makemigrations` and `python manage.py migrate` to create the tables in the database.
5. Run `python manage.py createsuperuser` and project the superuser details so that superuser can login to the admin panel.
6. Run `python manage.py runserver` to run the server.
7. Go to admin panel and put pricing calculation data which required to calculate the pricing in the respecitive tables(Distance additional prices, Time multiplier factors, Distance base pricings).
8. Use the GET request on url  `127.0.0.1:8000/pricing/calculate?hour=[hour]&distance=[distance]` to get the calculated price.
