from flask import Flask
import numpy
from flask import redirect
from flask import request
from flask import url_for
from flask import render_template
import sha
import os
import subprocess
import sys
app = Flask(__name__)
#####################################################################################################
#                                                                                                   #
#                   NO COMMENTS I DONT GIVE A FUCK IF YOU DONT UNDERSTAND                           #
#                                                                                                   #
#                                       *LOL*                                                       #
#                                                                                                   #
#                                   PROJECT NUCLEUS                                                 #
#                                                                                                   #
#                                      pen tech                                                     #
#                                                                                                   #
#                           AUTHOR : JAIYEOLA TOSIN STEPHEN                                         #
#                               <livecity505@gmail.com>                                             #
#####################################################################################################

@app.route('/email_buster/<email>')
def email_buster(email):
    return render_template('email_buster.html', email=email_address)

@app.route('/buster/<name>')
def buster(name):
    return 'Get out of here %s' %name

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('home.html', name=username)

@app.route('/username_buster')
def username_buster():
    return render_template('username_buster.html')

@app.route('/password_buster')
def password_buster():
    return render_template('password_buster.html')


@app.route ('/register', methods=['POST'])
def validator():
    email_address = request.form.get('email_address')
    username = request.form.get("username")
    password = request.form.get("password")
    country = request.form.get("country")
    try:
        email_split = email_address.split('.')
        email_split[1] = email_split[1].lower()
        if email_split[1] == 'com':
            pass
        else:
            return render_template('email_buster.html', email=email_address)
    except IndexError:
        return render_template('email_buster.html', email=email_address)
    if len(username) == 0:
        return render_template('username_buster.html')
    if len(password) == 0:
        return render_template('password_buster.html')
    else:
        password = encrypt(password)
        with open ('/var/host/media/removable/UNTITLED/Custom/restricted/userlist.txt', 'a') as users:
            users.write('\n'+username+' : '+password)
            users.close()

        with open ('/var/host/media/removable/UNTITLED/Custom/restricted/email_list.txt', 'a') as email:
            email.write('\n'+email_address+' : '+password)
            email.close()
        

    return render_template('home.html', name=username)
    
    

def encrypt(value):
    value = sha.sha(value)
    encrypted_val = value.hexdigest()
    return encrypted_val

if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
