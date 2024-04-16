import os

IN_FOLDER = 'G:\\My Drive\\Study\\UNIX\\md'
OUT_FOLDER = 'G:\\My Drive\\Study\\UNIX'

files = [f for f in os.listdir(IN_FOLDER)]

questions = ''

for file in files:
    with open(os.path.join(IN_FOLDER, file)) as f:
        questions += f'# {file[:-3]}\n\n{f.read()}\n\n'

with open(os.path.join(OUT_FOLDER, 'combined.md'), 'w') as f:
    f.write(questions)
