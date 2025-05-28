from python_files.Model import Tasks

def get_tasks():
    return Tasks.query.order_by(Tasks.task_id.asc()).all() 