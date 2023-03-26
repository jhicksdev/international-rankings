import json
import pathlib
import sqlite3
from typing import TypedDict

DIRNAME = pathlib.Path(__file__).parent


class JSONRecord(TypedDict):
    title: str
    version: str
    country_name: str
    rank: int
    score: float


connection = sqlite3.connect(f"{DIRNAME}/main.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM INTERNATIONAL_RANKINGS")
records: list[tuple[str, str, str, int, float]] = cursor.fetchall()
with open(f"{DIRNAME}/international_rankings.json", "w") as file:
    json_records: list[JSONRecord] = []
    for record in records:
        TITLE, VERSION, COUNTRY_NAME, RANK, SCORE = record
        json_records.append({"title": TITLE, "version": VERSION,
                            "country_name": COUNTRY_NAME, "rank": RANK, "score": SCORE})
    json.dump(json_records, file)
    file.close()
connection.close()
