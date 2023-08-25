#!flask/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, session, render_template_string

app = Flask(__name__, static_url_path='/static')
app.secret_key = "super secret key"

@app.after_request
def after_request(response):
   response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
   response.headers["Expires"] = 0
   response.headers["Pragma"] = "no-cache"
   return response

def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))
root = root_dir() + '/'



if __name__ == '__main__':
    app.run(debug=True)
