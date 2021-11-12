# 🦾 Exercise Results

Awesome Inc is proud to deliver and install high-quality products at customer's location. As part of the Analytics team, your current job is to help us with the following topics.

# 🐱‍🏍 Getting started

The repository contains a `docker-compose` file that starts a Postgres database containing Awesome Inc data, PgAdmin in order to manage the Postgres instance. 
* By default, the interface of PgAdmin with Postgres is accessible at `http://localhost:8080`.
* The API is accessible at `http://localhost:8000`

There is also the dbt-IBA directory which contains all the dbt models, that generate views in the database. To generate this views:
  * In the command line go to the directory of `dbt-IBA` of the `awesome-inc` repository
  * As it say in the `README.md` of the dbt-IBA directory, run the command `dbt run` to generate the views in the database.
  * Go to the database to see the generated views.

## 📈 Data Warehouse

We would like to report on the number of installations that the company is doing every month in order to see if the business is growing.

* The report is available in the database views under the name: `monthly_num_installations`.

We would also like to see which product category brings us more revenues, and which region of the world is our best market.

* One report showing the product category with most revenues, also in the database views under the name: `best_product_category_revenue`.
* Other report showing the best market region depending on the revenues is under the name of: `best_market_region`.

## 📃Data API

API to access Awesome Inc data.

### 👓 Usages
With `http://localhost:8000` shows you how to navigate to the different table names of the database.
* In order to Create and List the different values of the tables navigate to `http://localhost:8000/<table_name>/`
* In order to Retrieve, Delete and Update use a specific `id` from a table `http://localhost:8000/<table_name>/<id>/`


