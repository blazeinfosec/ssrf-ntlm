# Proof of concept of a SSRF vulnerability, written in Python 
# using Windows's WinHTTP.WinHTTPRequest native methods
# to demonstrate how Windows will give out hashes when asked
# to authenticate using NTLM.
#
# written by Julio Cesar Fort, Wildfire Labs /// Blaze Information Security
#
# Copyright 2016-2017, Blaze Information Security
# https://www.blazeinfosec.com

from flask import Flask, Response, request
import win32com.client

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    error_msg = '''<html><title>Blaze Information Security</title>
    <p>Proof of concept of SSRF using Windows native HTTP request COM object.</p>
    <p>Navigate to http://%s/?url=http://ip to exploit the SSRF.</p>
    <p>This is a PoC to demonstrate that when HTTP requests using Windows HTTP native API are sent to Responder, NTLM hashes can be harvested.</p>
    <br>
    <p>Copyright 2016-2017, Blaze Information Security - https://www.blazeinfosec.com</p>
    ''' % request.host
    
    if request.method == 'GET':
        if request.args.get('url'):
            try:
                URL = request.args.get('url')
                COM_OBJ = win32com.client.Dispatch('WinHTTP.WinHTTPRequest.5.1')
                COM_OBJ.SetAutoLogonPolicy(0)
                COM_OBJ.Open('GET', URL, False)
                COM_OBJ.Send()    
                return COM_OBJ.ResponseText
            except Exception, err:
                return "<p>Error: %s</p>" % str(err)
        else:
            return error_msg
    else:
        return "Method not supported."

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)