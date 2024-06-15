import hashlib, base64, requests
from github import Github

PREFIX = 'https://raw.githubusercontent.com/cd-public/books/main/'

with open('books.tsv', 'w') as f:
    f.write('TsvHttpData-1.0\n')
    g = Github()
    repo = g.get_repo("cd-public/books")
    for file in repo.get_contents(""):
        contents = requests.get(PREFIX + file.name)
        content = contents.content
        base64hash = base64.b64encode(hashlib.md5(content).digest())
        f.write(PREFIX + file.name + "\t" + str(len(content)) + "\t" + base64hash.decode('utf-8') + "\n")
    f.close()
