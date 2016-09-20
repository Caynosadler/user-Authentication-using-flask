from flask import Flask, redirect, url_for, request, render_template
import numpy
import sha

app = Flask(__name__)

@app.route('/buster/<name>')
def buster(name):
    return 'Get out of here %s' %name
@app.route('/login', methods=['POST'])
def validator():
    user = request.form.get("login_name")
    password_value= request.form.get("login_password")
    hex_password = onsite_encrypt(password_value)
    user_list = numpy.genfromtxt('/var/host/media/removable/UNTITLED/Custom/restricted/userlist.txt', dtype=str, skiprows=0)
    count = 0
    for i in range (len(user_list)):
        if user == user_list[i][0] and hex_password == user_list[i][2]:
            return render_template('home.html', name=user)
    else:
        return redirect(url_for('buster', name=user))

def onsite_encrypt(value):
    raw_value = sha.sha(value)
    final_val = raw_value.hexdigest()
    return final_val

if __name__ == '__main__':
    app.run(debug=True, port=5000)
