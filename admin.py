from flask import *
from database import *
import uuid
admin=Blueprint('admin',__name__)

@admin.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")


@admin.route("/product", methods=['post','get'])
def product():
    if 'submit' in request.form:
        p_name = request.form['p_name']
        p_image = request.files['p_image']
        path="static/uploads/"+str(uuid.uuid4())+p_image.filename
        p_image.save(path)
        p_quantity = request.form['p_quantity']
        p_price = request.form['p_price']

        query = "insert into product values(null,'%s','%s','%s','%s')"%(p_name, path, p_quantity, p_price)
        insert(query)
        return redirect(url_for("admin.product"))
        # print(p_name,path, p_quantity, p_price)



    data={}
    q='select * from product'
    res=select(q)
    data['res']=res


    if 'action' in request.args:
        action=request.args['action']
        pid=request.args['pid']
    else:
        action=None

    if action == 'delete':
        q="delete from product where product_id='%s'"%(pid)
        delete(q)
        return redirect(url_for("admin.product"))

    if action == 'update':
        query = "select * from product where product_id ='%s'"%(pid)
        print(query)
        data['updateProduct'] = select(query)

    if 'update' in request.form:
        p_name = request.form['p_name']
        p_price = request.form['p_price']
        p_quantity = request.form['p_quantity']
        if request.files['p_image']:
            p_image = request.files['p_image']
            path="static/uploads/"+str(uuid.uuid4())+p_image.filename
            p_image.save(path)
            q = "update product set product_name = '%s', product_image= '%s', product_quantity = '%s', product_price = '%s' where product_id = '%s'"%(p_name,path,p_quantity, p_price,pid)
        else:
            q = "update product set product_name = '%s',  product_quantity = '%s', product_price = '%s' where product_id = '%s'"%(p_name,p_quantity, p_price,pid)
        update(q)
        return redirect(url_for("admin.product"))
    return render_template("product.html",data=data)



# employee

@admin.route("/employee", methods=['post','get'])
def employee():
    emp = {}
    que='select * from employees'
    res=select(que)
    print(res)
    emp['res']=res

    if 'submit' in request.form:
        e_name = request.form['e_name']
        e_contact = request.form['e_contact']
        e_dept = request.form['e_dept']
        e_address = request.form['e_address']
        e_work = request.form['e_work']

        query = "insert into employees values(null,'%s','%s','%s','%s','%s')"%(e_name,e_contact,e_dept,e_address,e_work)
        # print(e_name, e_contact,e_dept,e_work)
        insert(query)

        return redirect(url_for("admin.employee"))

    if 'action' in request.args:
        action=request.args['action']
        e_id=request.args['e_id']
    else:
        action=None

    if action == 'delete':
        q="delete from employees where e_id='%s'"%(e_id)
        delete(q)
        return redirect(url_for("admin.employee"))

    if action == 'update':
        query = "select * from employees where e_id ='%s'"%(e_id)
        print(query)
        res = select(query)
        emp['updateEmployee']=res


    if 'update' in request.form:
        e_name = request.form['e_name']
        e_contact = request.form['e_phone']
        e_dept = request.form['e_department']
        e_address = request.form['e_address']
        e_work = request.form['e_work']
        q = "update employee set e_name = '%s', e_phone = '%s', e_department = '%s', e_address = '%s', e_work = '%s' where e_id = '%s'"%(e_name,e_contact,e_dept,e_address,e_work,e_id)
        update(q)
        return redirect(url_for("admin.employee"))

    return render_template("employee.html",emp=emp)


@admin.route("/newemployee", methods=['post','get'])
def new_employee():
    if 'submit' in request.form:
        e_name = request.form['e_name']
        e_contact = request.form['e_contact']
        e_dept = request.form['e_dept']
        e_address = request.form['e_address']
        e_work = request.form['e_work']

        query = "insert into employees values(null,'%s','%s','%s','%s','%s')"%(e_name,e_contact,e_dept,e_address,e_work)
        print(e_name, e_contact,e_dept,e_work)
        insert(query)

        return redirect(url_for("admin.new_employee"))

    return render_template("newemployee.html")
