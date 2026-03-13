import mysql.connector
from datetime import date

# connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ranjith123",
    database="standup"
)

cursor = db.cursor()

print("DAILY STAND-UP REPORTER\n")

name = input("Enter your name: ")
yesterday = input("What did you do yesterday? ")
today = input("What will you do today? ")
blockers = input("Any blockers? ")

today_date = date.today()

sql = "INSERT INTO reports (name, yesterday, today, blockers, report_date) VALUES (%s,%s,%s,%s,%s)"
values = (name, yesterday, today, blockers, today_date)

cursor.execute(sql, values)
db.commit()

print("\n✅ Report saved successfully!")