from __future__ import print_function
import os
import uuid
import urlparse
import json
import socket
from flask import Flask, render_template, jsonify





app = Flask(__name__)
my_uuid = str(uuid.uuid1())
BLUE = "#0099FF"
GREEN = "#33CC33"

COLOR = GREEN

@app.route('/')
def hello():
        global counterK 
	global connectionsvarK
        global whoareyouK
        global ipK
        ipK = request.user_agent
        counterK = counterK +1
        r.incr ('connectionsK')
        connectionsvarK = r.get('connectionsK')
        whoamiK = socket.gethostname()
        return """
	<html>
	<body bgcolor="{}">
#       <center><h1><font color="white">I am demoing deploying CODE<br/>
	<center><h1><font color="white">Hi, I'm GUID:<br/>
	{}
        <center><h1><font color="white">Page Hits for this deploy:<br/>
        {}
	</center>
        <center><h1><font color="white">GLOBAL Page Hits:<br/>
        {}
       <center><h2><small><font color="white">My hostname is:<br/>
        {}
      <center><h2><small><font color="white">YOUR Browser is:<br/>
        {}
	</body>
	</html>
	""".format(COLOR,my_uuid, counterK,connectionsvarK,whoamiK,ipK)

if __name__ == "__main__":
app.run(debug=False,host='0.0.0.0', port=env.port)
