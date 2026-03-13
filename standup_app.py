import streamlit as st
import mysql.connector
import pandas as pd
from datetime import date

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Standup Reporter",
    page_icon="🤖",
    layout="wide"
)

# ---------------- DATABASE ----------------

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ranjith123",
    database="standup"
)

cursor = db.cursor()

# ---------------- TITLE ----------------

st.markdown("""
<h1 style='text-align:center; 
color:white;
background:linear-gradient(90deg,#4CAF50,#00BCD4);
padding:15px;
border-radius:10px;'>
🤖 AI Daily Standup Reporter
</h1>
""", unsafe_allow_html=True)

st.write("")

# ---------------- DASHBOARD ----------------

cursor.execute("SELECT COUNT(*) FROM reports")
total_reports = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM reports WHERE blockers != 'None'")
total_blockers = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(DISTINCT name) FROM reports")
team_members = cursor.fetchone()[0]

col1, col2, col3 = st.columns(3)

col1.metric("📄 Total Reports", total_reports)
col2.metric("⚠ Blockers", total_blockers)
col3.metric("👥 Team Members", team_members)

st.write("---")

# ---------------- FORM ----------------

st.subheader("📝 Submit Standup Report")

with st.form("report_form"):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Name")
        yesterday = st.text_area("📌 Yesterday Work")

    with col2:
        today = st.text_area("📅 Today Plan")
        blockers = st.text_input("⚠ Blockers")

    submit = st.form_submit_button("Submit Report")

if submit:

    sql = """INSERT INTO reports
    (name,yesterday,today,blockers,report_date)
    VALUES (%s,%s,%s,%s,%s)"""

    values = (name, yesterday, today, blockers, date.today())

    cursor.execute(sql, values)
    db.commit()

    st.success("✅ Report Submitted Successfully!")

# ---------------- TABLE ----------------

st.subheader("📊 Team Reports")

cursor.execute("SELECT name,yesterday,today,blockers FROM reports")
reports = cursor.fetchall()

df = pd.DataFrame(
    reports,
    columns=["Name", "Yesterday Work", "Today Plan", "Blockers"]
)

st.dataframe(df, use_container_width=True)

# ---------------- SUMMARY ----------------

st.subheader("🤖 AI Generated Summary")

for r in reports:

    name = r[0]
    yesterday = r[1]
    today = r[2]
    blockers = r[3]

    st.write(f"**{name}** completed *{yesterday}* yesterday and will work on *{today}* today.")

    if blockers.lower() != "none":
        st.warning(f"⚠ Blocker detected: {blockers}")
    else:
        st.success("No blockers reported")

    st.write("---")