# Required imports
import os
import flask
import flickr_api as flickr
import werkzeug
from datetime import datetime

#Initialize Flickr session.
api_key = '4413f335ce82d81200ba2feeaab1aa18'
api_secret = '338e4360a6bca00b'
#user_id = '190606903@N07'

#For this part, if you don't remember, check out the Wiki page of the flickr_api library and follow the guide to authorize the app.
flickr.set_keys(api_key=api_key,
                api_secret=api_secret) # not this line if you store these details in flickr_keys.py

flickr.set_auth_handler("auth.txt") # or whatever you save your auth file as

dateTimeObj = datetime.now()
name = dateTimeObj.strftime("%H:%M:%S.%f")


app = flask.Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def handle_request():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    #upload the image using flickr_api
    flickr.upload(photo_file="androidFlask.jpg", title=name)
    return "Image Uploaded Successfully"

app.run(host="0.0.0.0", port=5000, debug=True)


