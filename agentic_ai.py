import mysql.connector
from datetime import date

# connect to mysql
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ranjith123",
    database="standup"
)

cursor = db.cursor()

print("\n===== DAILY STAND-UP REPORTER =====\n")

# get user input
name = input("Enter your name: ")
yesterday = input("What did you do yesterday? ")
today = input("What will you do today? ")
blockers = input("Any blockers? ")

today_date = date.today()

# insert into database
sql = "INSERT INTO reports (name, yesterday, today, blockers, report_date) VALUES (%s,%s,%s,%s,%s)"

values = (name, yesterday, today, blockers, today_date)

cursor.execute(sql, values)

db.commit()

print("\n✅ Report saved successfully!")

# ---------------------------
# AGENTIC AI SUMMARY
# ---------------------------

print("\n===== AI GENERATED DAILY SUMMARY =====\n")

cursor.execute("SELECT name, yesterday, today, blockers FROM reports")

reports = cursor.fetchall()

for r in reports:

    name = r[0]
    yesterday = r[1]
    today = r[2]
    blockers = r[3]

    print(f"👤 {name}")
    print(f"Yesterday: {yesterday}")
    print(f"Today: {today}")

    if blockers.lower() != "none":
        print(f"⚠ Blocker detected: {blockers}")
    else:
        print("No blockers")

    print("--------------------------------")

print("\n✅ Standup analysis completed by AI agent.")
