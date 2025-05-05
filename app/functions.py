from Model import Tasks

def get_tasks():
    return Tasks.query.all() 