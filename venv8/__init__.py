from flask import Flask, render_template, request, redirect, url_for, session, flash
from Forms import CreateProduct, CreateCartForm, CreateSalesForm, CreateOrderForm, SignUpUser, LoginForm, PasswordForm, \
    updateUserForm, updatePasswordForm, CreateStandardReward, CreateSpecialReward, CreatePromoCode, UpdateStandardReward,\
    UpdateSpecialReward, UpdatePromoCode, CreateFeedback, UpdateFeedback, UserFeedbackForms
from flask_session import Session
import shelve, Products, cart, order, User, Login, sales, UserFeedback, Standard, Reward, PromoCode, Feedback
import os
from uuid import uuid4
from werkzeug.utils import secure_filename
from flask_mail import Mail, Message

basedir = os.getcwd()
DBDIR = f"{basedir}/notes"
app = Flask(__name__)
app.secret_key = "abc"

Upload_Folder = 'static/assets/img/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['Upload_FOLDER'] = Upload_Folder

# basedir = os.getcwd()
# DBDIR = f"{basedir}/notes"
# app = Flask(name)
# app.secret_key = "abc"
#
# Upload_Folder = 'static/assets/img/'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
# app.config['Upload_FOLDER'] = Upload_Folder

# Keith
path = "static/assets/profimg/"
APP_ROUTE = os.path.dirname(os.path.abspath(__file__))
basedir = os.getcwd()

BASEDIR = os.getcwd()
DBDIR = f"{BASEDIR}/database/standard_db"
DBDIR_2 = f"{BASEDIR}/database/special_db"
DBDIR_3 = f"{BASEDIR}/database/promoCode_db"
DBDIR_4 = f"{BASEDIR}/database/feedback_db"
DBDIR_5 = f"{BASEDIR}/database/customerFeedback_db"

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = path


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'appdevresetpw@gmail.com'
app.config['MAIL_PASSWORD'] = 'iamgay1122@@'
mail = Mail(app)
# Keith



@app.route('/')
def home():
    return render_template('home.html')


# Jia le

@app.route('/create', methods=['GET', 'POST'])
def create():
    create_form = CreateProduct(request.form)
    if request.method == 'POST' and create_form.validate():
        products_dict = {}
        db = shelve.open('products.db', 'c')
        try:
            products_dict = db['Products']
        except:
            print("Error in retrieving Products from Products.db.")

        product = Products.Products(create_form.name.data, create_form.brand.data,create_form.category.data,
                                    create_form.price.data, create_form.quantity.data, create_form.status.data,
                                    create_form.date_created,create_form.date_updated, create_form.picture.data)
        uploaded_file = CreateProduct(request.files)
        f = uploaded_file.picture.data
        if f != None:
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            product.set_picture(filename)
        products_dict[product.get_uuid()] = product
        db['Products'] = products_dict
        db.close()
        return redirect(url_for("view"))
    return render_template('createProducts.html', form=create_form)

@app.route('/view',methods=['GET', 'POST'])
def view():
    products_dict = {}
    db = shelve.open('products.db', 'r')
    products_dict = db['Products']
    db.close()

    products_list = []
    for key in products_dict:
        products = products_dict.get(key)
        products_list.append(products)

    return render_template('viewProducts.html', count=len(products_list), products_list=products_list)


@app.route('/deleteProducts/<id>', methods=['POST'])
def delete_products(id):
    while True:
        products_dict = {}
        db = shelve.open('products.db', 'w')
        products_dict = db['Products']
        products_dict.pop(id)
        db['Products'] = products_dict
        db.close()

        return redirect(url_for("view"))


@app.route('/update/<id>/', methods=['GET', 'POST'])
def update_products(id):
    update_products = CreateProduct(request.form)
    if request.method == 'POST' and update_products.validate():
        products_dict = {}
        db = shelve.open('products.db', 'w')
        products_dict = db['Products']

        product = products_dict.get(id)
        product.set_name(update_products.name.data)
        product.set_brand(update_products.brand.data)
        product.set_category(update_products.category.data)
        product.set_price(update_products.price.data)
        product.set_quantity(update_products.quantity.data)
        product.set_status(update_products.status.data)
        # product.set_picture(update_products.picture.data)

        db['Products'] = products_dict
        db.close()

        return redirect(url_for('view'))
    else:
        products_dict = {}
        db = shelve.open('products.db', 'r')
        products_dict = db['Products']
        db.close()

        product = products_dict.get(id)
        update_products.name.data = product.get_name()
        update_products.brand.data = product.get_brand()
        update_products.category.data = product.get_category()
        update_products.price.data = product.get_price()
        update_products.quantity.data = product.get_quantity()
        update_products.status.data = product.get_status()
        # update_products.picture.data = product.get_picture()

        return render_template('updateProducts.html', form=update_products)


@app.route('/charts')
def charts():
    return render_template('profp.html')


@app.route('/homeUser')
def homeUser():
    products_dict = {}
    db = shelve.open('products.db', 'r')
    products_dict = db['Products']
    db.close()

    products_list = []
    for key in products_dict:
        products = products_dict.get(key)
        products_list.append(products)

    return render_template('homeUser.html', count=len(products_list), products_list=products_list)
# Jia le


# Jing hui
@app.route('/createCart/<id>' , methods=['GET', 'POST'])
def create_cart(id):
    create_cart_form = CreateCartForm(request.form)
    products_dict = {}
    db = shelve.open('products.db', 'w')
    products_dict = db['Products']
    db.close()
    products = products_dict.get(id)
    if request.method == 'POST':
        cart_order_dict = {}
        db = shelve.open('cart.db', 'c')

        try:
            cart_order_dict = db['Cart']
        except:
            print("Error in retrieving Products from products.db")

        cart_order = cart.Cart(id,create_cart_form.name.data, create_cart_form.brand.data, create_cart_form.category.data,
                               create_cart_form.price.data, create_cart_form.quantity.data)

        print(id, cart_order)
        cart_order_dict[cart_order.get_uuid()] = cart_order
        db['Cart'] = cart_order_dict

        db.close()

        session['cart_created'] = cart_order.get_name()

        print("homeUser")
        return redirect(url_for('homeUser'))

    else:
        products_dict = {}
        db = shelve.open('products.db', 'r')
        products_dict = db['Products']
        db.close()

        product = products_dict.get(id)
        create_cart_form.name.data = product.get_name()
        create_cart_form.brand.data = product.get_brand()
        create_cart_form.category.data = product.get_category()
        create_cart_form.price.data = product.get_price()
        create_cart_form.quantity.data = product.get_quantity()
        create_cart_form.status.data = product.get_status()

        return render_template('createCart.html', form=create_cart_form, products=products)


@app.route('/updateCart/<id>', methods=['GET', 'POST'])
def update_cart(id):
    update_cart = CreateCartForm(request.form)
    if request.method == 'POST':
        cart_order_dict = {}
        db = shelve.open('cart.db', 'w')
        cart_order_dict = db['Cart']

        product = cart_order_dict.get(id)
        product.set_name(update_cart.name.data)
        product.set_brand(update_cart.brand.data)
        product.set_category(update_cart.category.data)
        product.set_price(update_cart.price.data)
        product.set_quantity(update_cart.quantity.data)

        db['Cart'] = cart_order_dict
        db.close()

        return redirect(url_for('viewCart'))
    else:
        products_dict = {}
        db = shelve.open('products.db', 'r')
        products_dict = db['Products']
        db.close()

        product = products_dict.get(id)
        update_cart.name.data = product.get_name()
        update_cart.brand.data = product.get_brand()
        update_cart.category.data = product.get_category()
        update_cart.price.data = product.get_price()
        update_cart.quantity.data = product.get_quantity()

        return render_template('updateCart.html', form=update_cart)


@app.route('/viewCart')
def viewCart():
    cart_order_dict = {}
    db = shelve.open('cart.db', 'r')
    cart_order_dict = db['Cart']
    db.close()

    view_cart_list = []
    for key in cart_order_dict:
        print("key is", key)
        products = cart_order_dict.get(key)
        view_cart_list.append(products)
        # print(int(products.get_price()))
        # total_amt = products.get_price() * products.get_quantity()

    return render_template('viewCart.html', count=len(view_cart_list), cart_list=view_cart_list)


@app.route('/deleteCart/<id>',  methods=['POST'])
def delete_cart(id):
    while True:

        cart_order_dict = {}
        db = shelve.open('cart.db', 'w')
        cart_order_dict = db['Cart']
        cart_order_dict.pop(id)
        db['Cart'] = cart_order_dict
        db.close()

        return redirect(url_for("viewCart"))

@app.route('/createOrder', methods=['GET', 'POST'])
def create_order():
    create_order_form = CreateOrderForm(request.form)
    if request.method == 'POST' and create_order_form.validate():
        create_order_dict = {}
        db = shelve.open('order.db', 'c')

        try:
            create_order_dict = db['Order']
        except:
            print("Error in retrieving order from order.db.")

        create_orders = order.Order(create_order_form.order_date.data, create_order_form.order_time.data,
                                   create_order_form.amount.data, create_order_form.email.data)

        create_order_dict[create_orders.get_uuid()] = create_orders
        db['Order'] = create_order_dict

        db.close()

        return redirect(url_for('view_order'))
    return render_template('createOrder.html', form=create_order_form)

@app.route('/viewOrder')
def view_order():
    create_order_dict = {}
    db = shelve.open('order.db', 'r')
    create_order_dict = db['Order']
    db.close()

    view_order_list = []
    for key in create_order_dict:
        orders = create_order_dict.get(key)
        view_order_list.append(orders)


    return render_template('viewOrder.html', count=len(view_order_list), view_order_list=view_order_list)


@app.route('/deleteOrder/<id>', methods=['POST'])
def delete_order(id):
    while True:
        create_order_dict = {}
        db = shelve.open('order.db', 'w')
        create_order_dict = db['Order']
        create_order_dict.pop(id)
        db['Order'] = create_order_dict
        db.close()

        return redirect(url_for("view_order"))


@app.route('/createSales', methods=['GET', 'POST'])
def create_sales():
    create_sales_form = CreateSalesForm(request.form)
    if request.method == 'POST' and create_sales_form.validate():
        create_sales_dict = {}
        db = shelve.open('sales.db', 'c')

        try:
            create_sales_dict = db['Sales']
        except:
            print("Error in retrieving sales from sales.db.")

        create_sales = sales.Sales(create_sales_form.date.data, create_sales_form.Total_amount.data,create_sales_form.name.data)

        create_sales_dict[ create_sales .get_uuid()] = create_sales
        db['Sales'] = create_sales_dict

        db.close()

        return redirect(url_for('view_sales'))
    return render_template('createSales.html', form= create_sales_form)

@app.route('/viewSales')
def view_sales():
    create_sales_dict = {}
    db = shelve.open('sales.db', 'r')
    create_sales_dict = db['Sales']
    db.close()

    view_sales_list = []
    for key in create_sales_dict:
        sales = create_sales_dict.get(key)
        view_sales_list.append(sales)


    return render_template('viewSales.html', count=len(view_sales_list), view_sales_list=view_sales_list)


@app.route('/deleteSales/<id>',  methods=['POST'])
def delete_sales(id):
    while True:
        create_sales_dict = {}
        db = shelve.open('sales.db', 'w')
        create_sales_dict = db['Sales']
        create_sales_dict.pop(id)
        db['Sales'] = create_sales_dict
        db.close()

        return redirect(url_for("view_sales"))

# Jing hui






# keith

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0
]


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"
]

# trial

# trial


@app.route('/line')
def line():
    line_labels = labels
    line_values = values

    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    db.close()

    lenVal = (len(signup_dict.keys()))
    return render_template('line.html', title='User Creation Statistics(Graph)', max=50, labels=line_labels,
                           values=line_values,
                           lenVal=lenVal)


@app.route('/forgetpass', methods = ["GET", "POST"])
def forgetpass():
    forgetpassword = PasswordForm(request.form)
    if request.method == "POST" and forgetpassword.validate():
        signup_dict = {}
        db = shelve.open('signup.db', 'r')
        signup_dict = db['SignUp']

        users_list = []
        for key in signup_dict:
            user = signup_dict.get(key)
            users_list.append(user)

        for user in users_list:
            if forgetpassword.email.data == user.get_email():
                newpassword = str(uuid4())[:8]
                user.set_password(newpassword)

                db['SignUp'] = signup_dict
                db.close()
                msg = Message('Your New Password ', sender='appdevresetpw@gmail.com',
                              recipients=[forgetpassword.email.data])

                msg.html = render_template("email.html", newpassword=newpassword)
                mail.send(msg)
                print('hello')
                print(forgetpassword.email.data)
                return redirect(url_for("login"))
    return render_template('forgetpass.html', form=forgetpassword)


@app.route('/preNavs')
def retrieveUser1():
    return render_template('preNavs.html')

#
# @app.route('/preLogin')
# def preLogin():
#     # flash('Sign Out Successful!', 'success')
#     return render_template('homeUser.html')


@app.route('/preLogin')
def preLogin():
    products_dict = {}
    db = shelve.open('products.db', 'r')
    products_dict = db['Products']
    db.close()

    products_list = []
    for key in products_dict:
        products = products_dict.get(key)
        products_list.append(products)

    return render_template('preLogin.html', count=len(products_list), products_list=products_list)


@app.route('/userAccount')
def user_account():
    return render_template('userAccount.html')


# @app.route('/viewAccount')
# def view_account():
#     return render_template('viewAccount.html')


@app.route('/userHelp')
def user_help():
    return render_template('userHelp.html')


@app.route('/UserSignUp', methods=['GET', 'POST'])
def sign_up():
    sign_up_form = SignUpUser(request.form)
    if request.method == 'POST' and sign_up_form.validate():
        signup_dict = {}
        db = shelve.open('signup.db', 'c')

        try:
            signup_dict = db['SignUp']
        except:
            print("Error in retrieving Users from User.db.")

        signup = User.User(sign_up_form.first_name.data, sign_up_form.last_name.data,
                           sign_up_form.email.data, sign_up_form.address.data, sign_up_form.phone_number.data,
                           sign_up_form.unit_number.data, sign_up_form.postal_code.data, sign_up_form.password.data,
                           sign_up_form.password_confirm.data)

        user_list = []
        for key in signup_dict:
            user = signup_dict.get(key)
            user_list.append(user)
        # dont need this part
        # uploaded_file = SignUpUser(request.files)
        # f = uploaded_file.picture.data
        #
        # if f != None:
        #     filename = secure_filename(f.filename)
        #     f.save(os.path.join(app.config['Upload_FOLDER'], filename))
        #     signup.set_picture(filename)
        # dont need this part
        signup_dict[signup.get_email()] = signup
        db['SignUp'] = signup_dict
        db.close()
        #
        # print(signup_dict.keys())
        # print(signup.get_email())


        # if signup.get_email() == signup_dict.keys():
        for x in user_list:
            print(x.get_email())
            if x.get_email() == signup.get_email():
                flash('Account Already Exists! Please try again', 'danger')
                return redirect(url_for('sign_up'))
            else:
                flash('Sign Up Successful!', 'success')
                return redirect(url_for('login'))

    return render_template('UserSignUp.html', form=sign_up_form)


@app.route('/Login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    loginUser = Login.Login(login_form.email.data, login_form.password.data)
    user_list = []
    for key in signup_dict:
        user = signup_dict.get(key)
        user_list.append(user)
    if request.method == 'POST' and login_form.validate():
        if login_form.email.data == 'admin@gmail.com' and login_form.password.data == 'password':
            # flash('Login Successful', 'success')
            return redirect(url_for('home'))
        else:
            for x in user_list:
                if request.method == 'POST' and login_form.validate():
                    if x.get_email() == loginUser.get_email():
                        if x.get_password() == loginUser.get_password():
                            email = request.form['email']
                            session['email'] = email
                            # password = request.form['password']
                            # session['password'] = password
                            flash('Log In Successful', 'success')
                            return redirect(url_for('homeUser'))
                        else:
                            flash('Login Unsuccessful, Either Email or Password is Wrong', 'warning')
                            return redirect(url_for('login'))
            else:
                flash('Invalid Credentials, Please sign up', 'danger')
                return redirect(url_for('sign_up'))
    db.close()
    # session['user_created'] = loginUser.get_email() and loginUser.get_password()
    return render_template('Login.html', form=login_form)


@app.route('/userProfile/<email>/')
def user_Profile(email):
    print("***", email)
    show_profile_form = SignUpUser(request.form)
    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    # profile_em = signup_dict.get(email=session['email'])
    profile = signup_dict.get(email)
    p_fn = profile.get_first_name()
    p_ln = profile.get_last_name()
    p_em = profile.get_email()
    p_ad = profile.get_address()
    p_ph = profile.get_phone_number()
    p_un = profile.get_unit_number()
    p_pc = profile.get_postal_code()
    print(profile.get_first_name())
    pic = signup_dict.get(email)
    pics = pic.get_picture()
    users_list = []
    for key in signup_dict:
        user = signup_dict.get(key)
        users_list.append(user)
    db.close()

    return render_template('userProfile.html', first_name=p_fn, email=profile, last_name=p_ln, pemail=p_em, address=p_ad
                           , phone=p_ph, unit=p_un, postal=p_pc, count=len(users_list), users_list=users_list, pics=pics)


@app.route('/updateProfile/<email>/', methods=['GET', 'POST'])
def update_profile(email):
    update_profile_form = updateUserForm(request.form)
    # if request.method == 'POST':
    if request.method == 'POST' and update_profile_form.validate():
        signup_dict = {}
        db = shelve.open('signup.db', 'wc')
        signup_dict = db['SignUp']

        profile = signup_dict.get(email)
        profile.set_first_name(update_profile_form.first_name.data)
        profile.set_last_name(update_profile_form.last_name.data)
        profile.set_email(update_profile_form.email.data)
        profile.set_address(update_profile_form.address.data)
        profile.set_phone_number(update_profile_form.phone_number.data)
        profile.set_unit_number(update_profile_form.unit_number.data)
        profile.set_postal_code(update_profile_form.postal_code.data)
        # Did not include the bottom two and the request.method validate because i need the
        # to change the users password as well, so perhaps if only my update user is when user calls for support,
        # then include the bottom two
        # profile.set_password(update_profile_form.password.data)
        # profile.set_password_confirm(update_profile_form.password_confirm.data)


        uploaded_file = SignUpUser(request.files)
        f = uploaded_file.picture.data

        if f != None:
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            profile.set_picture(filename)
            db['SignUp'] = signup_dict
            db.close()

        # else:
            # return send_from_directory(os.path.join('static', 'assets/img/bg.jpg'))
            # return send_from_directory(os.path.join('static', 'assets/img/bg.jpg'))
        #     pass
        # signup_dict[signup.get_picture()] = signup

        users_list = []
        db = shelve.open('signup.db', 'w')
        signup_dict = db['SignUp']

        for key in signup_dict:
            signup = signup_dict.get(key)
            users_list.append(signup)

        db['SignUp'] = signup_dict
        db.close()

        return redirect(url_for("user_Profile", email=session['email'], users_list=users_list, form=update_profile_form))
    else:
        signup_dict = {}
        db = shelve.open('signup.db', 'r')
        signup_dict = db['SignUp']
        db.close()

        profile = signup_dict.get(email)
        update_profile_form.first_name.data = profile.get_first_name()
        update_profile_form.last_name.data = profile.get_last_name()
        update_profile_form.email.data = profile.get_email()
        update_profile_form.address.data = profile.get_address()
        update_profile_form.phone_number.data = profile.get_phone_number()
        update_profile_form.unit_number.data = profile.get_unit_number()
        update_profile_form.postal_code.data = profile.get_postal_code()
        update_profile_form.picture.data = profile.get_picture()

        return render_template('updateProfile.html', form=update_profile_form, email=session['email'])



@app.route('/updatePassword/<email>/', methods=['GET', 'POST'])
def update_password(email):
    update_pass_form = updatePasswordForm(request.form)
    # if request.method == 'POST':
    if request.method == 'POST' and update_pass_form.validate():
        signup_dict = {}
        db = shelve.open('signup.db', 'w')
        signup_dict = db['SignUp']

        profile = signup_dict.get(email)
        profile.set_password(update_pass_form.password.data)
        profile.set_password_confirm(update_pass_form.password_confirm.data)

        db['SignUp'] = signup_dict
        db.close()
        return redirect(url_for("user_Password", email=session['email'], form=update_pass_form))
    else:
        signup_dict = {}
        db = shelve.open('signup.db', 'r')
        signup_dict = db['SignUp']
        db.close()

        user = signup_dict.get(email)
        update_pass_form.password.data = user.get_password()
        update_pass_form.password_confirm.data = user.get_password_confirm()

        return render_template('updatePassword.html', form=update_pass_form, email=session['email'])


@app.route('/userPassword/<email>/')
def user_Password(email):
    print("***", email)
    show_profile_form = SignUpUser(request.form)
    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    # profile_em = signup_dict.get(email=session['email'])
    profile = signup_dict.get(email)
    p_pass = profile.get_password()
    # p_passconfirm = profile.get_password_confirm()
    p_em = profile.get_email()
    # users_list = []
    # for key in signup_dict:
    #     user = signup_dict.get(key)
    #     users_list.append(user)
    db.close()

    return render_template('userPassword.html', email=profile, pemail=p_em, password=p_pass)


@app.route('/userAddress/<email>/')
def user_Address(email):
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    # profile_em = signup_dict.get(email=session['email'])
    profile = signup_dict.get(email)
    p_fn = profile.get_first_name()
    p_ln = profile.get_last_name()
    p_em = profile.get_email()
    p_ad = profile.get_address()
    p_ph = profile.get_phone_number()
    p_un = profile.get_unit_number()
    p_pc = profile.get_postal_code()
    print(profile.get_first_name())
    pic = signup_dict.get(email)
    pics = pic.get_picture()
    users_list = []
    for key in signup_dict:
        user = signup_dict.get(key)
        users_list.append(user)
    db.close()

    return render_template('userAddress.html', first_name=p_fn, email=profile, last_name=p_ln, pemail=p_em, address=p_ad
                           , phone=p_ph, unit=p_un, postal=p_pc, count=len(users_list), users_list=users_list,
                           pics=pics)



@app.route("/logout")
def logout():
    session.pop('email', None)
    session.pop('id', None)
    return redirect("/")


@app.route('/retrieveUsers')
def retrieve_users():
    signup_dict = {}
    db = shelve.open('signup.db', 'r')
    signup_dict = db['SignUp']
    db.close()

    users_list = []
    for key in signup_dict:
        user = signup_dict.get(key)
        users_list.append(user)

    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)


@app.route('/updateUser/<email>/', methods=['GET', 'POST'])
def update_user(email):
    update_user_form = updateUserForm(request.form)
    # if request.method == 'POST':
    if request.method == 'POST' and update_user_form.validate():
        signup_dict = {}
        db = shelve.open('signup.db', 'w')
        signup_dict = db['SignUp']

        user = signup_dict.get(email)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_email(update_user_form.email.data)
        user.set_address(update_user_form.address.data)
        user.set_phone_number(update_user_form.phone_number.data)
        user.set_unit_number(update_user_form.unit_number.data)
        user.set_postal_code(update_user_form.postal_code.data)
        # Did not include the bottom two and the request.method validate because i need the
        # to change the users password as well, so perhaps if only my update user is when user calls for support,
        # then include the bottom two
        # user.set_password(update_user_form.password.data)
        # user.set_password_confirm(update_user_form.password_confirm.data)
        # update_user_form.password.data = user.get_password()

        db['SignUp'] = signup_dict
        db.close()
        return redirect(url_for('retrieve_users'))
    else:
        signup_dict = {}
        db = shelve.open('signup.db', 'r')
        signup_dict = db['SignUp']
        db.close()

        user = signup_dict.get(email)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.email.data = user.get_email()
        update_user_form.address.data = user.get_address()
        update_user_form.phone_number.data = user.get_phone_number()
        update_user_form.unit_number.data = user.get_unit_number()
        update_user_form.postal_code.data = user.get_postal_code()

        return render_template('updateUser.html', form=update_user_form)


@app.route('/deleteUser/<email>/', methods=['POST'])
def delete_user(email):
    signup_dict = {}
    db = shelve.open('signup.db', 'w')
    signup_dict = db['SignUp']

    signup_dict.pop(email)

    db['SignUp'] = signup_dict
    db.close()

    return redirect(url_for('preLogin', email=email))


# Add your codes below here


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404

# keith

# jerell
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/createStandard', methods=['GET', 'POST'])
def create_standard():
    create_standard = CreateStandardReward(request.form)
    if request.method == 'POST' and create_standard.validate():
        standard_dict = {}
        db = shelve.open(DBDIR, 'c')

        try:
            standard_dict = db['Standard']
        except:
            print(f"Error in retrieving Users from {DBDIR}.")

        standard = Standard.Standard(create_standard.name.data, create_standard.value.data,
                                     create_standard.points.data, create_standard.expiryDate.data,
                                     create_standard.category.data)
        standard_dict[standard.get_standard_id()] = standard

        db['Standard'] = standard_dict

        db.close()
        flash("A Standard Reward has been Successfully Added !")
        return redirect(url_for('create_standard'))
    return render_template('createStandard.html', form=create_standard)


@app.route('/viewStandard')
def retrieve_standard():
    standard_dict = {}
    db = shelve.open(DBDIR, 'r')
    standard_dict = db['Standard']
    db.close()

    standard_list = []
    for key in standard_dict:
        standard = standard_dict.get(key)
        standard_list.append(standard)
    return render_template('viewStandard.html', count=len(standard_list), standard_list=standard_list)


@app.route('/updateStandard/<string:id>/', methods=['GET', 'POST'])
def update_standard(id):
    update_standard = UpdateStandardReward(request.form)
    if request.method == 'POST' and update_standard.validate():
        standard_dict = {}
        db = shelve.open(DBDIR, 'w')
        standard_dict = db['Standard']

        standard = standard_dict.get(id)
        standard.set_name(update_standard.name.data)
        standard.set_value(update_standard.value.data)
        standard.set_points(update_standard.points.data)
        standard.set_expiryDate(update_standard.expiryDate.data)
        standard.set_category(update_standard.category.data)

        db['Standard'] = standard_dict
        db.close()
        return redirect(url_for('retrieve_standard'))
    else:
        standard_dict = {}
        db = shelve.open(DBDIR, 'r')
        standard_dict = db['Standard']
        db.close()

        standard = standard_dict.get(id)
        update_standard.name.data = standard.get_name()
        update_standard.value.data = standard.get_value()
        update_standard.points.data = standard.get_points()
        update_standard.expiryDate.data = standard.get_expiryDate()
        update_standard.category.data = standard.get_category()

    return render_template('updateStandard.html', form=update_standard)


@app.route('/deleteStandard/<string:id>', methods=['POST'])
def delete_standard(id):
    standard_dict = {}
    db = shelve.open(DBDIR, 'w')
    standard_dict = db['Standard']

    standard_dict.pop(id)

    db['Standard'] = standard_dict
    db.close()

    return redirect(url_for('retrieve_standard'))


@app.route('/createReward', methods=['GET', 'POST'])
def create_reward():
    create_reward = CreateSpecialReward(request.form)
    if request.method == 'POST' and create_reward.validate():
        reward_dict = {}
        db = shelve.open(DBDIR_2, 'c')

        try:
            reward_dict = db['Special']
        except:
            print(f"Error in retrieving Special Rewards from {DBDIR_2}.")

        reward = Reward.Reward(create_reward.name.data, create_reward.value.data,
                               create_reward.expiryDate.data, create_reward.category.data)
        reward_dict[reward.get_special_id()] = reward
        db['Special'] = reward_dict

        db.close()
        flash("A Special Reward has been Successfully Added !")
        return redirect(url_for('create_reward'))
    return render_template('createReward.html', form=create_reward)


@app.route('/viewReward')
def retrieve_reward():
    reward_dict = {}
    db = shelve.open(DBDIR_2, 'r')
    reward_dict = db['Special']
    db.close()

    reward_list = []
    for key in reward_dict:
        reward = reward_dict.get(key)
        reward_list.append(reward)
    return render_template('viewReward.html', count=len(reward_list), reward_list=reward_list)


@app.route('/updateReward/<string:id>/', methods=['GET', 'POST'])
def update_reward(id):
    update_reward = UpdateSpecialReward(request.form)
    if request.method == 'POST' and update_reward.validate():
        reward_dict = {}
        db = shelve.open(DBDIR_2, 'w')
        reward_dict = db['Special']

        reward = reward_dict.get(id)
        reward.set_name(update_reward.name.data)
        reward.set_value(update_reward.value.data)
        reward.set_expiryDate(update_reward.expiryDate.data)
        reward.set_category(update_reward.category.data)

        db['Special'] = reward_dict
        db.close()
        return redirect(url_for('retrieve_reward'))
    else:
        reward_dict = {}
        db = shelve.open(DBDIR_2, 'r')
        reward_dict = db['Special']
        db.close()

        reward = reward_dict.get(id)
        update_reward.name.data = reward.get_name()
        update_reward.value.data = reward.get_value()
        update_reward.expiryDate.data = reward.get_expiryDate()
        update_reward.category.data = reward.get_category()

    return render_template('updateReward.html', form=update_reward)


@app.route('/deleteReward/<string:id>', methods=['POST'])
def delete_reward(id):
    reward_dict = {}
    db = shelve.open(DBDIR_2, 'w')
    reward_dict = db['Special']

    reward_dict.pop(id)

    db['Special'] = reward_dict
    db.close()

    return redirect(url_for('retrieve_reward'))


@app.route('/createPromo', methods=['GET', 'POST'])
def create_promo():
    create_promo = CreatePromoCode(request.form)
    if request.method == 'POST' and create_promo.validate():
        promo_dict = {}
        db = shelve.open(DBDIR_3, 'c')

        try:
            promo_dict = db['Promo']
        except:
            print(f"Error in retrieving Promo Code from {DBDIR_3}.")

        promo = PromoCode.PromoCode(create_promo.name.data, create_promo.value.data,
                                    create_promo.promoCode.data, create_promo.quantity.data,
                                    create_promo.expiryDate.data, create_promo.category.data,)
        promo_dict[promo.get_promo_id()] = promo
        db['Promo'] = promo_dict

        db.close()
        flash("A Promo Code has been Successfully Added !")
        return redirect(url_for('create_promo'))
    return render_template('createPromo.html', form=create_promo)


@app.route('/viewPromo')
def retrieve_promo():
    promo_dict = {}
    db = shelve.open(DBDIR_3, 'r')
    promo_dict = db['Promo']
    db.close()

    promo_list = []
    for key in promo_dict:
        promo = promo_dict.get(key)
        promo_list.append(promo)
    return render_template('viewPromo.html', count=len(promo_list), promo_list=promo_list)


@app.route('/updatePromo/<string:id>/', methods=['GET', 'POST'])
def update_promo(id):
    update_promo = UpdatePromoCode(request.form)
    if request.method == 'POST' and update_promo.validate():
        promo_dict = {}
        db = shelve.open(DBDIR_3, 'w')
        promo_dict = db['Promo']

        promo = promo_dict.get(id)
        promo.set_name(update_promo.name.data)
        promo.set_value(update_promo.value.data)
        promo.set_promoCode(update_promo.promoCode.data)
        promo.set_quantity(update_promo.quantity.data)
        promo.set_(update_promo.quantity.data)
        promo.set_(update_promo.expiryDate.data)
        promo.set_category(update_promo.category.data)

        db['Promo'] = promo_dict
        db.close()
        return redirect(url_for('retrieve_promo'))
    else:
        promo_dict = {}
        db = shelve.open(DBDIR_3, 'r')
        promo_dict = db['Promo']
        db.close()

        promo = promo_dict.get(id)
        update_promo.name.data = promo.get_name()
        update_promo.value.data = promo.get_value()
        update_promo.promoCode.data = promo.get_promoCode()
        update_promo.quantity.data = promo.get_quantity()
        update_promo.expiryDate.data = promo.get_expiryDate()
        update_promo.category.data = promo.get_category()

    return render_template('updatePromo.html', form=update_promo)


@app.route('/deletePromo/<string:id>', methods=['POST'])
def delete_promo(id):
    promo_dict = {}
    db = shelve.open(DBDIR_3, 'w')
    promo_dict = db['Promo']

    promo_dict.pop(id)

    db['Promo'] = promo_dict
    db.close()

    return redirect(url_for('retrieve_promo'))


@app.route('/delete_allPromo/<string:id>', methods=['POST'])
def delete_all_promo(id):
    promo_dict = {}
    db = shelve.open(DBDIR_3, 'w')
    promo_dict = db['Promo']

    promo_dict.clear()

    db['Promo'] = promo_dict
    db.close()

    return redirect(url_for('retrieve_promo'))


@app.route('/createFeedback',  methods=['GET', 'POST'])
def feedback():
    create_feedback = CreateFeedback(request.form)
    if request.method == 'POST' and create_feedback.validate():
        feedback_dict = {}
        db = shelve.open(DBDIR_4, 'c')

        try:
            feedback_dict = db['Feedback']
        except:
            print(f"Error in retrieving Feedback from {DBDIR_4}.")

        feedback = Feedback.Feedback(create_feedback.q1.data, create_feedback.q2.data,
                                     create_feedback.q3.data, create_feedback.q4.data,
                                     create_feedback.q5.data)
        feedback_dict[feedback.get_feedback_id()] = feedback
        db['Feedback'] = feedback_dict

        db.close()
        create_feedback.q1.data = ''
        create_feedback.q2.data = ''
        create_feedback.q3.data = ''
        create_feedback.q4.data = ''
        create_feedback.q5.data = ''
        flash("Feedback Questions have been Successfully Added !")
        return render_template('feedback_disabled.html', form=create_feedback)
    return render_template('feedback.html', form=create_feedback)


@app.route('/viewFeedback')
def retrieve_feedback_qns():
    feedback_dict = {}
    db = shelve.open(DBDIR_4, 'r')
    feedback_dict = db['Feedback']
    db.close()

    feedback_list = []
    for key in feedback_dict:
        star = feedback_dict.get(key)
        feedback_list.append(star)
    return render_template('view_feedback_qns.html', feedback_list=feedback_list)


@app.route('/updateFeedback/<string:id>/', methods=['GET', 'POST'])
def update_feedback_qns(id):
    update_feedback = UpdateFeedback(request.form)
    if request.method == 'POST' and update_feedback.validate():
        feedback_dict = {}
        db = shelve.open(DBDIR_4, 'w')
        feedback_dict = db['Feedback']

        feedback = feedback_dict.get(id)
        feedback.set_q1(update_feedback.q1.data)
        feedback.set_q2(update_feedback.q2.data)
        feedback.set_q3(update_feedback.q3.data)
        feedback.set_q4(update_feedback.q4.data)
        feedback.set_q5(update_feedback.q5.data)

        db['Feedback'] = feedback_dict
        db.close()
        return redirect(url_for('retrieve_feedback_qns'))
    else:
        feedback_dict = {}
        db = shelve.open(DBDIR_4, 'r')
        feedback_dict = db['Feedback']
        db.close()

        feedback = feedback_dict.get(id)
        update_feedback.q1.data = feedback.get_q1()
        update_feedback.q2.data = feedback.get_q2()
        update_feedback.q3.data = feedback.get_q3()
        update_feedback.q4.data = feedback.get_q4()
        update_feedback.q5.data = feedback.get_q5()

    return render_template('updateFeedback.html', form=update_feedback)


@app.route('/userFeedback', methods=["GET", "POST"])
def user_feedback():
    user_feedback = UserFeedbackForms(request.form)
    user_feedback.dropdown.choices = get_products_name()
    if request.method == 'POST' and user_feedback.validate():
        user_feedback_dict = {}
        db = shelve.open(DBDIR_5, 'c')

        try:
            user_feedback_dict = db['UserFeedback']
        except:
            print(f"Error in retrieving User Feedback from {DBDIR_5}.")

        user_feedback = UserFeedback.UserFeedback(user_feedback.q1.data, user_feedback.q2.data,
                                                  user_feedback.q3.data, user_feedback.q4.data,
                                                  user_feedback.dropdown.data)
        user_feedback_dict[user_feedback.get_user_id()] = user_feedback

        db['UserFeedback'] = user_feedback_dict

        db.close()
        flash("Your Feedback has been successfully submitted !")
        return redirect(url_for('user_feedback'))
    return render_template('UserFeedback.html', form=user_feedback)


def get_products_name():
    products_dict = {}
    db = shelve.open('products.db', 'r')
    products_dict = db['Products']
    db.close()

    products_list = []
    for key in products_dict:
        products = products_dict.get(key)
        products_list.append(products.get_name())
    return products_list


@app.route('/viewUserFeedback')
def reteive_user_feedback():
    user_feedback_dict = {}
    db = shelve.open(DBDIR_5, 'r')
    user_feedback_dict = db['UserFeedback']
    db.close()

    user_feedback_list = []
    for key in user_feedback_dict:
        user_feedback = user_feedback_dict.get(key)
        user_feedback_list.append(user_feedback)
    return render_template('viewUserFeedback.html', count=len(user_feedback_list), user_feedback_list=user_feedback_list)
# jerell


if __name__ == '__main__':
    app.run()

