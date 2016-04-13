from app import app
from flask import render_template, request, jsonify

@app.route('/')
@app.route('/write')
def write():
    return render_template('write.html', text="WRITE")

@app.route('/read')
def read():
    return render_template('read.html', text="READ")

@app.route('/settings')
def settings():
    return render_template('settings.html', text="SETTINGS")

