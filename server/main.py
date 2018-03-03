from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)




# Index HTML
@app.route("/")
def index():
    return render_template('index.html')

# Receiving messages
@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    print "Some message received"
    
    emit('my response', "Server: This is a simple response.")
    print "Emitted a message back."



# Boilerplate starts SocketIO instead of standard flask.
if __name__ == '__main__':
    socketio.run(app)