#!/user/bin/env python3
import psycopg2
DBNAME = "news"
# connect Database and fetch result


def get_result(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


# as the result of the query is a list we need to function to iterate it
def print_result(results):
    for i in results:
        title = i[0]
        times = i[1]
        print(str(title) + "-->" + str(times)+" Views")
        print("\n")

query_1 = '''select title,count(*) as times
 from articles join log
 on articles.slug=substring(log.path,10,300)
  group by title order by times DESC limit 3;'''

query_2 = '''SELECT authors.name ,count(*) as times
from problem2 join authors on problem2.author=authors.id
 GROUP BY authors.name ORDER BY times DESC limit 3;'''

query_3 = '''select to_char(errors.days,'Mon DD, YYYY'),
 round((errors.errors*100.0)/totalvistors.visitors,3) as precent
  from errors join totalvistors on errors.days=totalvistors.days
   order by precent DESC limit 1 '''


result_1 = get_result(query_1)
result_2 = get_result(query_2)
result_3 = get_result(query_3)
print("What are the most popular three articles of all time?\n")
print_result(result_1)
print("Who are the most popular article authors of all time?\n")
print_result(result_2)
print(" On which days did more than 1% of requests lead to errors?\n")
print(result_3[0][0] + "--" + str(result_3[0][1]) + "% \n")
