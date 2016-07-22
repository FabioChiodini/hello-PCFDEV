from __future__ import print_function
import os
import uuid
import urlparse
import json
import socket
from flask import Flask, render_template, jsonify

from cfenv import AppEnv

env = AppEnv()

app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"

COLOR = GREEN

counterK = 0

@app.route('/')

def hello():
   whoamiK = socket.gethostname()
   return """
    <html>
    <body bgcolor="{}">
    <center><h1><font color="white">Hi, I'm GUID:<br/>
	{}
	<center><h1><font color="white">My hostname is:<br/>
    {}
    </body>
    </html>
    """.format(COLOR,my_uuid,whoamiK)
	

if __name__ == "__main__":
	 app.run(debug=False,host='0.0.0.0', port=env.port)
