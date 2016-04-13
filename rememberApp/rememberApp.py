from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


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




if __name__ == '__main__':
    app.run()
