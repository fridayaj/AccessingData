# main.py

import pyodbc
try:
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                          'Database=IS4010;'
                          'uid=IS4010Login;'
                          'pwd=P@ssword2;')
    # submit a quiery
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tAmericanAthleticConference')
except:
    # I'd like to know more
    print("Error accessing database")
    print(e)
    exit() # give up

# we have conncted and logged in to the db server
# we have a connection called conn
# we have a cursor that has been populated with a query result

print("We are connected and have a populated cursor")

total_enrollment = 0
# Step through all the rows in the results set
for row in cursor:
    print(row); # All columns in the row
    print (row[1]); # Second column
    print (row[2]); # Third column
    print (row[3]); # Third column
    total_enrollment = total_enrollment + int(row[2]) # running sum of enrollments

print ("Total enrollment = " + str(total_enrollment))
