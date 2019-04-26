# Logs Analysis Project
This project is part of Udacity's full stack nanodegree program. Here we have been tasked to build an **internal reporting tool** that will use information from the database to discover what kind of articles the site's readers like.

## Project Overview
This project is aimed to stretch and practice our SQL database skills. The [database for the project](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) contains newspaper articles, as well as the web server log for the site.

The goal is to create a reporting tool that prints out reports in plain text based on the data in the database. The reporting tool should answer questions such as:

* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

## Running The Project
**Optional:** You may also choose to run the project using a Virtual Machine. For instructions, [click here](https://github.com/udacity/fullstack-nanodegree-vm) (Note, they use vagrant to configure and boot your VM).

#### Requirements
* PostgreSQL

    `sudo apt-get install postgresql postgresql-contrib`
* Python 3
* psycopg2

    `pip3 install psycopg2-binary`

**Note:** If you are using a VM along with the Vagrant file mentioned above, you do not have to install any of the above requirements. The VM is configured with the requirements.

#### Loading the dataset
* Download the dataset (Link is provided above)
* `cd` into the directory where you downloaded the dataset and run
    `psql -d news -f newsdata.sql`

#### Create View
Create the below view to help with effecient SQL processing


   ` CREATE VIEW proc as SELECT RIGHT(path, -9) AS
     WHERE status = '200 OK' and path != '/'
     GROUP BY log_slug
     ORDER BY count DESC;`

#### Running the script
* Clone this repository and `cd` into it

    `git clone https://github.com/doctor-entropy/log-analysis.git`

    `cd log-analysis`
* Create views

    `bash create_views.sh` (Ensure you have the necessary permissions)

* Run the script

    `python3 run.py`

* Delete views

    `bash delete_views.sh`
