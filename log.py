import psycopg2

DBNAME='news'
# first we create function to get the query from the Database
def getdata(query):
    try:
        DB=psycopg2.connect(database = DBNAME)
        c=DB.cursor()
        c.execute(query)
        data=c.fetchall()
        DB.close()
        return(data)
    except:
        print("error in fetching database ")
# next we need to print this data so we create a function to print

def print_data(data):
    try:
        for d in data:
            print(str(r[0])+"-->"+str(r[1])+" views \n")
    except:
        print("error,can't print the data ")

# now it's time for queries
query1='''select title, count(*) as num
from articles join  on log articles.slug= substr(log.path,10)
GROUP BY title
ORDER by num DESC limit 3 ;
 '''


        
