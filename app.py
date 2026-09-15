import os
from flask import Flask , request, render_template,jsonify
from flask_mysqldb import MySQL  # type: ignore[import-not-found]


app = Flask(__name__)


# MySQL configurations
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'password')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'devops')


mysql = MySQL(app)

@app.route('/health')
def health():
    return jsonify({"status":"healthy"})

# Home page route
@app.route('/')
def hello():

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, message FROM messages")

    messages = cur.fetchall()
    cur.close()
    return render_template('index.html' , messages=messages)


# submit message route

@app.route('/submit' , methods=['POST'])

def submit():

    new_message = request.form['new_message']

    if not new_message:
        return jsonify({"error" : "Message cannot be empty"}),400

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO messages (message) VALUES (%s)",[new_message])

    mysql.connection.commit()
    cur.close()


    return jsonify({"message" : new_message})


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug = True)


