
from flask import Flask, render_template,request
import ibm_db

app = Flask(__name__)

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=31249;PROTOCOL=TCPIP;USERNAME=tng21908;PASSWORD=vnmqInQc1vrqJrUO;SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt",'','')
print(ibm_db.active(conn))


@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/profile')
def profile():
    return render_template('/profile.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
       uname =  request.form['username']
       pword =  request.form['password']
       print(uname,pword)
    return render_template('/login.html')

if __name__ == '__main__':
    app.run(debug=True)
