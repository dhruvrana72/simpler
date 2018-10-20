from flask_cors import CORS
import json
from flask import Flask, abort, make_response, request
app = Flask(__name__)
CORS(app)


@app.route('/save_email/', methods=['POST', 'GET'])
def save_email():
	args = request.data
	args = json.loads(args)
	args = dict(args[0])
	email = args['value']
	print(email)
	with open("emails.txt", "a") as myfile:
		myfile.write(email+ "\n")
	return "test"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)