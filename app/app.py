from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello World!'

@app.route('/receive_form', methods=['POST'])
def receive_form():
    # Extract data from the request
    data = request.json
    print('Data received: ', data)

    

    # Process data (you can add your logic here)
    # if rccb5b3de7a4d476ba482356fcab1ec8d exists, get the vlaue
    if 'rccb5b3de7a4d476ba482356fcab1ec8d' in data:
        userId = data['rccb5b3de7a4d476ba482356fcab1ec8d']

        ## query some excel/CSV file to get rest of user information

    else:
        userId = 'No user id'

    


    # Send response back to Power Automate
    return jsonify({"status": "success", "message": "Data received", "data": data})

if __name__ == '__main__':
    app.run(
        debug=True, 
        port=5005
        )
