from flask import *
from database import *

user=Blueprint('user',__name__)


@user.route("/user")
def userhome():
    return render_template("userhome.html")


