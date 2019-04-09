import os
from celery import Celery

from etlam.db import start_session
from etlam.utils.registry import FileRegistryModel


app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def process_file(file_path):

    session = start_session()

    rec = session.query(FileRegistryModel).filter(
        FileRegistryModel.file == os.path.basename(file_path)).first()

    if not rec or rec.to_be_processed():
        return

    register_entry = FileRegistryModel(file=os.path.basename(file_path),
                                       version=version,
                                       completed=False,
                                       in_progress=True)

    return True
