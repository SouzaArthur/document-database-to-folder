import cursor as cursor
import mysql.connector

# Connecting to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="GGrfefRW$$2242",
    database="system"
)

binaryDocument = []

cursor = mydb.cursor()

# Executing Query
cursor.execute("SELECT DOCUMENT_BLOB FROM DATABASE_NAME.DOCUMENT_IMG WHERE ID_DOCUMENT = 42")

# Looping over lines of query's return
for line in cursor:
    binaryDocument.append(line)

# Writing each binary contained in binaryDocument variable in a PDF file
i = 0
for binary in binaryDocument:
    file = open("./documents/doc%s.pdf" % str(i + 1), "+wb")
    file.write(binary[0])
    file.close()
    i = i + 1
