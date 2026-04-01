from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Hello from DevSecOps API!"})

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
flask==2.0.1
werkzeug==2.0.1
requests==2.20.0
pyyaml==5.3.1
