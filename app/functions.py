from Controler import db, App, connect

def get_tasks():
    conn = connect()
    with conn.cursor() as cur:
        sql = f'SELECT task_id, task_name, task_assignee FROM new_schema."Tasks"'
        cur.execute(sql)
        return cur.fetchall()