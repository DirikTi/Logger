import os
from dotenv import load_dotenv
from models.RequestLog import RequestLog
from flask import Flask, request, jsonify
import json
import sys

app = Flask(__name__)

load_dotenv()

WHICH_SYSTEM_ENUM = { 1, 2, 3 }
METHODS_ENUM = { 'GET', 'POST', 'PUT', 'DELETE', 'HEAD' }

@app.route('/logs/request', methods=['POST'])
def logs_request():
    data = request.json
    
    if(data == None):
        return '', 400
    
    request_token, request_body, request_query, which_system, base_url, headers, method, response_body, sender_ip_address, user_id, is_error, status = jsonify(data)

    if(which_system in WHICH_SYSTEM_ENUM or request_token == None or request_body == None or request_query == None or base_url == None 
       or headers == None or method == None or response_body == None or sender_ip_address == None or user_id == None or is_error == None
        or status == None ):
        return '', 400
    
    _requestLog = RequestLog(request_token, request_body, request_query, which_system, base_url, headers, method, 
            response_body, sender_ip_address, user_id, is_error, status)
    

    _requestLog.insert_data()
    


@app.route('/logs/mobile', methods=['POST'])
def logs_mobile():
    
    pass



print(sys.argv)
port = 3333

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port, debug=True)