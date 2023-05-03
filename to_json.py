from datetime import date
import json
import pathlib

DIRNAME = pathlib.Path(__file__).parent.resolve()

rankings = None


def isfloat(x):
    try:
        float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def isint(x):
    try:
        a = float(x)
        b = int(a)
    except (TypeError, ValueError):
        return False
    else:
        return a == b


def convert_to_number(x):
    return int(x) if isint(x) else float(x) if isfloat(x) else x


def get_ranking(title):
    return list(filter(lambda x: x["title"] == title, rankings))[0]


with open(f"{DIRNAME}/rankings.tsv") as file:
    rows = list(map(lambda x: x.split("\t"), file.read().split("\n")[1:]))
    rankings = list(
        map(
            lambda x: {
                "title": x[0],
                "version": convert_to_number(x[1]),
                "records": [],
            },
            sorted(set(map(lambda x: (x[0], x[1]), rows))),
        )
    )
    for row in rows:
        title, _, country, rank, score = row
        get_ranking(title)["records"].append(
            {
                "country": country,
                "rank": convert_to_number(rank),
                "score": convert_to_number(score),
            }
        )
    file.close()

json_data = {"version": date.today().strftime("%Y.%m.%d").replace(".0", "."), "rankings": rankings}

with open(f"{DIRNAME}/rankings.json", "w") as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
    file.close()

with open(f"{DIRNAME}/rankings.min.json", "w") as file:
    json.dump(json_data, file, separators=(",", ":"), ensure_ascii=False)
    file.close()
