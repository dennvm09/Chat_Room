#render_template plantillas, helps in rendering the HTML page which are so called the templates
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
#socketio variable which enables us to use socketio instead of app in running the application
socketio = SocketIO(app)

@app.route('/') #la ruta a la que va a responder
def sessions():
    return render_template('session.html') #el nombre de mi html

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)



#The run() method takes optional host and port arguments
#by default it will listen on localhost:5000 like Flask’s development web server. 
#debug=True enables to sort out the errors with ease.
if __name__ == '__main__':
    socketio.run(app, debug=True)
