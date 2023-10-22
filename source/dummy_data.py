from tools.logging import logger
from db_con import get_db_instance
import random

import json

def generate_dummy_brainwave_data(data):
    data_json = json.dumps(data)  # convert the list to JSON string
    db, cur = get_db_instance()
    cur.execute("INSERT INTO brain (movieID, data) VALUES (?, ?)", (random.randint(1, 100), data_json))
    db.commit()
    return [random.randint(0, 100) for _ in range(10)]

# When retrieving the data later, will deserialize it back to a list
def get_brainwave_data_from_db():
    db, cur = get_db_instance()
    cur.execute("SELECT * FROM brain")
    rows = cur.fetchall()
    result = []
    for row in rows:
        movieID, data_json = row[1], row[2]
        data = json.loads(data_json)  # Deserialize JSON string back to a list
        result.append((movieID, data))
    return result
