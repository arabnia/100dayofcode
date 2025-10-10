from flask import Flask, jsonify
import datetime

app = Flask(__name__)


@app.route('/time', methods=['GET'])
def get_time():
    # Perform a task: return the current server time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify({'current_time': current_time})


# if name == 'main':
app.run(host='0.0.0.0', port=8080)