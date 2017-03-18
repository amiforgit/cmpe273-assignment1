from flask import Flask
import sys
import yaml
import json
import argparse
from github3 import login
from github3 import GitHub
import base64

app = Flask(__name__)
f=sys.argv[1]
g=GitHub()

urlcon=f.split('/')
l=len(urlcon)
print(urlcon[l-1])
print(urlcon[l-2])

amiforgit=g.user('amiforgit')

@app.route("/v1/<name>")
def hello1(name):
    if name.endswith('.yml'):
        retval=base64.b64decode(g.repository(urlcon[l-2],urlcon[l-1]).contents(name).content)
        return retval
    if name.endswith('.yaml'):
        name=name[:-5]+".yml"
        retval=base64.b64decode(g.repository(urlcon[l-2],urlcon[l-1]).contents(name).content)
        return retval
    if name.endswith('.json'):
        name=name[:-5]+".yml"
        print(name)
        retval=base64.b64decode(g.repository(urlcon[l-2],urlcon[l-1]).contents(name).content)
        retvalf=(json.dumps(yaml.load(retval), sort_keys=False, indent=2))
        return retvalf
@app.route("/")
def hello2():
   return "Hello from Dockerized Flask App!!"
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
