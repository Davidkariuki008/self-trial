from service import *
from app import app

@app.route("/")
def home ():
    liquors=[]
    x=read_records()
    for 
    return render_templete(home.html)


def obj_dict(alcohol):
    return{
        "name":alcohol.name,
        "pic":alcohol.pic,
        "price":alcohol.price
    }
