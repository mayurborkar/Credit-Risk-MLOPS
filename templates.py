
import os

dirs = [
    os.path.join('data', 'raw'),
    os.path.join('data', 'processed'),
    'notebooks',
    'data_given',
    'saved_models',
    'src'
]

for dirs_ in dirs:
    os.makedirs(dirs_, exist_ok=True)
    with open(os.path.join(dirs_, '.gitkeep'), 'w') as f:
        pass

files = [
    'dvc.yaml',
    'params.yaml',
    '.gitignore',
    os.path.join('src', '__init__.py')
]

for files_ in files:
    with open(files_, 'w') as f:
        pass