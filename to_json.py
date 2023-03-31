import json
import pathlib
import sqlite3

DIRNAME = pathlib.Path(__file__).parent

connection = sqlite3.connect(f"{DIRNAME}/main.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM INTERNATIONAL_RANKINGS")
records = cursor.fetchall()
with open(f"{DIRNAME}/records.json", "w") as file:
    json_records = []
    for record in records:
        TITLE, VERSION, COUNTRY_NAME, RANK, SCORE = record
        json_records.append({
            "title": TITLE,
            "version": VERSION,
            "country_name": COUNTRY_NAME,
            "rank": RANK,
            "score": SCORE
        })
    json.dump(json_records, file)
    file.close()
connection.close()
