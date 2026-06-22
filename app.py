from flask import Flask, render_template
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="task_tracker_db"
)

@app.route("/")
def dashboard():

    df = pd.read_sql("SELECT * FROM tasks", db)

    total_tasks = len(df)

    status_count = df["status"].value_counts()

    os.makedirs("static", exist_ok=True)

    plt.figure(figsize=(6,4))
    status_count.plot(kind="bar")
    plt.title("Tasks By Status")
    plt.tight_layout()
    plt.savefig("static/chart.png")
    plt.close()

    return render_template(
        "dashboard.html",
        total_tasks=total_tasks
    )

if __name__ == "__main__":
    app.run(debug=True)