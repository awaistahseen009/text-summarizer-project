import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO,format= '[%(asctime)s]: %(message)s:')
project_name="text_summarizer"
file_paths=[
    '.github/workflows/.iam',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "DockerFile",
    "requirements.txt",
    "setup.py",
    "experiment/exp.ipynb"
]

for fp in file_paths:
    filepath=Path(fp)
    filedir,filename=os.path.split(filepath)
    if filedir!="" and  not os.path.exists(filedir):
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Directory successfully created !: {filedir}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0) :
        with open(filepath,'w') as f:
            f.write("")
        logging.info(f"File created with path: {filepath}")
    else:
        logging.info(f"File {filename} already exits !")

