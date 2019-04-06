# logs Analysis
the first project in full stack nanodegree
# project Overview
in this project the task is to create a reporting tool
that prints out reports (in plain text)based on the data in the database
this reporting tool  is a python program using the psycopg2  module to connect
to the Database
# Requirements
[python3] this code is using ver 3.7
[vagrant]
[virtualbox]
[git]
# how to access to this Project
1. download vagrant and virtualbox and install them
2. download the Udacity config file from this link ((https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
3. download the database (https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
4. cd to vagrant
5. use command vagrant up to launch the vm it may take time
6. once the install complete use command vagrant ssh
7. To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql
8. Once you have the data loaded into your database, connect to your database using psql -d news
9. explore the tables using the \dt and \d table commands and select statements.


# My Views
1. problem2
create view problem2 as select articles.title,articles.author,log.path from articles
join log on articles.slug=substring(log.path,10,300);



2. errors
create view errors as select cast(time as date) as days ,
 count(* ) as num from log where status like '404%' group by days ;
3. totalvisitors
select count(* ) as vistors , cast(time as date) as days from log group by days;
