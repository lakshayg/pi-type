from bottle import route, run, template
import rainbow
import subprocess
import time

# Global state
WORDFILE = 'words.txt'
WORDS = set([line.strip() for line in open(WORDFILE)])
INDEX = 0

def savewords():
    with open(WORDFILE, 'w') as f:
        f.write('\n'.join(WORDS))

def random_choice(s):
    global INDEX
    l = len(s)
    INDEX = (INDEX + 1) % l
    i = INDEX
    for word in s:
        if i == 0:
            return word
        i -= 1
    raise Exception

@route('/rainbow')
def play_rainbow():
    subprocess.Popen(['python3 ./rainbow.py'],
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE,
                 shell=True)

@route('/shutdown')
def shutdown():
    rainbow.show()
    time.sleep(0.1)
    subprocess.Popen(['shutdown now'],
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE,
                 shell=True)

@route('/words')
def words():
    return {"words": list(WORDS)}

@route('/delete/<word>')
def delete(word):
    if word not in WORDS:
        return "Word does not exist"
    WORDS.remove(word.lower())
    savewords()
    return "Done"

@route('/add/<word>')
def add(word):
    if word in WORDS:
        return "Word already exists"
    WORDS.add(word.lower())
    savewords()
    return "Done"

@route('/')
def index():
    random_word = random_choice(WORDS)
    return template('index', word=random_word)

rainbow.show()
run(port=80, host='0.0.0.0')
