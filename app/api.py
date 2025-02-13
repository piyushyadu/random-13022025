from fastapi import APIRouter, Path
import sqlite3


router = APIRouter()
connection = None


def get_cursor():
    global connection
    if not connection:
        connection = sqlite3.connect('database.db')
    return connection.cursor()


@router.get('/status/{resource_id}', status_code=200)
def get_resource_status(resource_id: str = Path(min_length=1, max_length=10)):
    cursor = get_cursor()
    cursor.execute("SELECT * FROM resource_status where resource_id == ? ", (resource_id,))
    data = cursor.fetchall()[0]
    data = {"resource_id": data[0], "resource_status": data[1]}
    return data



