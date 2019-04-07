import psycopg2

DBNAME = 'news'
# first we create function to get the query from the Database


def getdata(query):
    try:
        DB = psycopg2.connect(database = DBNAME)
        c = DB.cursor()
        c.execute(query)
        data = c.fetchall()
        DB.close()
        return(data)
    except:
        print("error in fetching database ")
# next we need to print this data so we create a function to print


def print_data(data):
    try:
        for d in data:
            print(str(d[0])+"-->"+str(d[1])+" views \n")
    except:
        print("error,can't print the data ")

# now it's time for queries
# 'substr' is a fucntion Extracting a substring from a string
# in this query we can use  log.path like concat('%',articles.slug,'%') but
# it will take more time to execute


query1 = '''select title, count(*) as num
from articles join log on
articles.slug = substr(log.path,10)
GROUP BY title
ORDER by num DESC limit 3 ;'''
# we need 2 joins in this query
# we will use a view for the first join
# create view artics as select articles.title,articles.author,log.path from
# articles join log on articles.slug=substr(log.path,10);


query2 = ''' select authors.name,count(*) as num
  from artics join authors
  on artics.author=authors.id GROUP BY authors.name
 ORDER BY num DESC limit 3; '''

# mathematically  the percentage equal (error (visitors/allvisitors)*100)
# we will create view for error and view for total visitors
# the status for error is 404
# create view errors as select cast(time as date) as days ,
# count(* ) as num from log where status like '404%' group by days
# select count(*) as vistors,cast(time as date) as days from log group by days;


query3 = '''Select to_char(errors.days, 'Mon-dd-YYYY'),
 round((errors.errors*100.0)/totalvisitors.visitors,3) as precent
  from errors join totalvisitors on errors.days=totalvisitors.days
   order by precent DESC limit 1; '''
data_1 = getdata(query1)
data_2 = getdata(query2)
data_3 = getdata(query3)
print('What are the most popular three articles of all time?')
print_data(data_1)
print("Who are the most popular article authors of all time?")
print_data(data_2)
print("On which days did more than 1% of requests lead to errors? ")
print(data_3[0][0] + "--" + str(data_3[0][1]) + " % \n")
