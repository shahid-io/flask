from flask import *
from database import *

public = Blueprint('public',__name__)

@public.route("/")
def home():
    return render_template("home.html")

@public.route("/login",methods=['get','post'])
def login():
    if 'submit' in request.form:
        uname = request.form['uname']
        passw = request.form['passwd']

        q="select * from login where username='%s' and password='%s'"%(uname,passw)
        res=select(q)
        # print(res)
        if res:
            if res[0]['user_type'] == 'admin':
                return redirect(url_for("admin.adminhome"))
            elif res[0]['user_type'] == 'user':
                return redirect(url_for("user.userhome"))
            
    return render_template("login.html")

@public.route("/register", methods=['get','post'])
def register():
    if 'submit' in request.form:
        fname = request.form['fname']
        lname = request.form['lname']
        dob = request.form['dob']
        contact = request.form['contact']
        address = request.form['address']
        gender = request.form['gen']
        email = request.form['email']
        password = request.form['password']

        quali = request.form['quali']
        hobb = request.form['hobb']

        q="insert into login values (null,'%s','%s','user')"%(email,password)

        lid=insert(q)
        print(lid)
        query = "insert into user values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(lid,fname,lname,dob,contact,address,gender,email,quali,hobb)
        insert(query)
        return redirect(url_for("public.login"))
    return render_template("registration.html")
