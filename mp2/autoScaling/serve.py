from flask import Flask, request, jsonify
import socket

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_ip_address():
    # return the private IP address of the EC2 instance
    return socket.gethostname()

@app.route('/', methods=['POST'])
def subprocess_open():
    subprocess.Popen(['python3', 'stress_cpu.py'])
    return 'run stress_cpu.py file'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)