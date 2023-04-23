from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome from Docker! This is updated file!!' 

@app.route('/app')
def hello_world():
    return 'This is from APP.......' 

 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)