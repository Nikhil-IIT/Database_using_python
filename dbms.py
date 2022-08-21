import psycopg2

conn=None

def L(x):
        y= 2000 + 5*x
        return y

try:
    conn= psycopg2.connect(database = "lis", user = "postgres",password = "1234567890", host = "localhost", port = "5432")
    print("connected successfully")
    curr=conn.cursor()
    curr.execute("select * from book_catalogue")
    
    rows=curr.fetchmany(2)
    print(curr.rowcount)
    curr.close()

except(Exception,psycopg2.DataError)as error:
    print(error)

finally:
    if conn is not None:
        conn.close()