# logs Analysis
the first project in full stack nanodegree
# project Overview
in this project the task is to create a reporting tool
that prints out reports (in plain text)based on the data in the database
this reporting tool  is a python program using the psycopg2  module to connect
to the Database.
# instructions for how to run the program
1. download vagrant and virtualbox and install them
2. download the Udacity [Configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
3. download the [Database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
4. cd to vagrant
5. use command `vagrant up` to launch the vm it may take time
6. once the install complete use command `vagrant ssh`
7. To load the data, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`
8. Once you have the data loaded into your database, connect to your database using `psql -d news`
9. explore the tables using the `\dt` and `\d`   table commands and select statements.
[GitHub](http://github.com)
#  Functions
1. `getdata` --> connect the database and execute & fetch query
2. `print_data`--> print the result of `getdata`
3. `SUBSTR(string, start, length)`--> extracts a substring from a string
4. `to_char(date, 'Mon-dd-YYYY')`--> convert the date format
5. `cast(time as date)`--> for casting to date type
# My Views
1. artics
`create view artics as select articles.title,articles.author,log.path from articles
join log on articles.slug=substr(log.path,10);``



2. errors
`create view errors as select cast(time as date) as days ,
 count(* ) as num from log where status like '404%' group by days ;``
3. totalvisitors
`select count(* ) as vistors , cast(time as date) as days from log group by days;`
