import os
from etlam.utils.jobs import process_file


def run_etl(folder):
    # We assume that there are only relevant files in the folder
    files = [f for f in os.listdir(folder)
             if os.path.isfile(os.path.join(folder, f))]

    for f in files:
        file_path = os.path.join(folder, f)

        if os.path.exists(file_path):
            process_file.delay(file_path)
        else:
            print("Path {} does not exist".format(file_path))
