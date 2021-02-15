# from flask import Flask,render_template,request
# from flask_wtf,file import FileField

import os
import random
import logging
# from flask_socketio import SocketIO, send, emit
from flask import *
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# from chatterbot.trainers import ListTrainer
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename


def Content():
    TOPIC_DICT = {"Basics": [["Introduction to Python", "/introduction-to-python-programming/"],
                             ["Print functions and Strings", "/python-tutorial-print-function-strings/"],
                             ["Math basics with Python 3", "/math-basics-python-3-beginner-tutorial/"]],
                  "Web Dev": []}

    return TOPIC_DICT


TOPIC_DICT = Content()
print(__file__)
import os
import sqlite3

project_dir = os.path.dirname(os.path.abspath(__file__))
myApp = Flask(__name__)

# ///////////////////////chat bot confuration

# //////////////Email configuration
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'ah.schoolsmail@gmail.com',
    "MAIL_PASSWORD": 'Networks1.'
}
myApp.config.update(mail_settings)
mail = Mail(myApp)
# /////////////////////////////
print(project_dir)
myApp.config['SECRET_KEY'] = 'jsbcfsbfjefebw237u3gdbdc'
# socketio = SocketIO(myApp)
from flask_sqlalchemy import SQLAlchemy

TOPIC_DICT = Content
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bstirc.db"))
myApp.config["SQLALCHEMY_DATABASE_URI"] = database_file
myApp.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(myApp)
 
# exit()
# userLoginName = ''
# idNum = 0

class adminFreeDay(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    freeDay1=db.Column(db.String(40), unique=False, nullable=True)
    freeDay2=db.Column(db.String(40), unique=False, nullable=True)
    freeDay3=db.Column(db.String(40), unique=False, nullable=True)
    freeDay4=db.Column(db.String(40), unique=False, nullable=True)
    freeTime1=db.Column(db.String(40), unique=False, nullable=True)
    freeTime2=db.Column(db.String(40), unique=False, nullable=True)
    freeTime3=db.Column(db.String(40), unique=False, nullable=True)
    freeTime4=db.Column(db.String(40), unique=False, nullable=True)
class admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False, primary_key=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    phone = db.Column(db.String(40), unique=False, nullable=True)
    picture = db.Column(db.String(40), unique=False, nullable=True)
    appointment=db.Column(db.String(40), unique=False, nullable=True)
    # picture=db.Column(db.String(40),unique=False,nullable=True)
    password = db.Column(db.String(40), unique=False, nullable=False)
    
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    projectType = db.Column(db.String(40), nullable=True, primary_key=False)
    userName = db.Column(db.String(40), unique=True, nullable=True, primary_key=False)
    pasword = db.Column(db.String(40), unique=False, nullable=True)
    email = db.Column(db.String(40), unique=False, nullable=True)
    picture = db.Column(db.String(40), unique=False, nullable=True)
    phone = db.Column(db.String(40), unique=False, nullable=True)
    appointment=db.Column(db.String(40), unique=False, nullable=True)
    loginAs=db.Column(db.String(40), unique=False, nullable=True)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ProjectTitle = db.Column(db.String(40), unique=False, nullable=True)
    ProjectDecs = db.Column(db.String(40), unique=False, nullable=True)
    ProjectPics = db.Column(db.String(40), unique=False, nullable=True)
    ProjectStatus = db.Column(db.String(80), unique=False, nullable=True)
    ProjectCategory=db.Column(db.String(40), unique=False, nullable=True)
    Client=db.Column(db.String(40), unique=False, nullable=True)
    ProjectDate=db.Column(db.String(40), unique=False, nullable=True)
    ProjectURL=db.Column(db.String(40), unique=False, nullable=True)
    ProjectCompDate=db.Column(db.String(40), unique=False, nullable=True)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clientPicture = db.Column(db.String(40), unique=False, nullable=True)
    clientName=db.Column(db.String(40), unique=False, nullable=True)
    clientComment=db.Column(db.String(40), unique=False, nullable=True)
    
class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clients = db.Column(db.String(40), unique=False, nullable=True)
    Projects=db.Column(db.String(40), unique=False, nullable=True)
    HourseOfSupport=db.Column(db.String(40), unique=False, nullable=True)
    HardWorkers=db.Column(db.String(40), unique=False, nullable=True)
    
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    clientName = db.Column(db.String(40), unique=False, nullable=True)
    clientEmail = db.Column(db.String(40), unique=False, nullable=True)
    clientProjectType = db.Column(db.String(40), unique=False, nullable=True)
    clientProjectDesc = db.Column(db.String(40), unique=False, nullable=True)    
    clientAppointment1 = db.Column(db.String(40), unique=False, nullable=True)



# db.create_all()



 

@myApp.route('/')
def home():
    onGoing = Project.query.filter_by(ProjectStatus="Under-Development")    
    Completed = Project.query.filter_by(ProjectStatus="Completed")
    clients = Client.query.all()
    PortfolioData = Portfolio.query.filter_by(id=3).first()
    freeAppointmentTime=adminFreeDay.query.filter_by(id=1).first()
    return render_template("index.html",freeTime=freeAppointmentTime,portFolioData=PortfolioData,clientsData=clients, onGoingProjects=onGoing,completedProjects=Completed)

# @myApp.route('/')
# def myHome():
#     return render_template("index.html")

@myApp.route('/adminLogin')
def adminLogin():
    return render_template("loginAdmin.html")

@myApp.route('/AdminAppointment', methods=["GET", "POST"])
def farighTime():
    freeTime = adminFreeDay.query.filter_by(id=1).first()
    freeTime.freeDay1 = request.form['appointmentDate1']
    freeTime.freeDay2 = request.form['appointmentDate2']
    freeTime.freeDay3 = request.form['appointmentDate3']
    freeTime.freeDay4 = request.form['appointmentDate4']
    freeTime.freeTime1 = request.form['appointmentTime1']
    freeTime.freeTime2 = request.form['appointmentTime2']
    freeTime.freeTime3 = request.form['appointmentTime3']
    freeTime.freeTime4 = request.form['appointmentTime4']
    db.session.add(freeTime)
    db.session.commit()
    
    adminName=admin.query.all()
    return render_template('/NiceAdmin/form_component.html',admin=adminName)

    db.session.add(freeTime)
    db.session.commit()
    return render_template("/NiceAdmin/form_component.html")

@myApp.route('/appointment', methods=["GET", "POST"])
def contactForm():

    try:
         if request.method=="POST":
            user1=Appointment()
            user1.clientName=request.form['name']
            name=user1.clientName
            name=name.replace(" ","")
            user1.clientName=name
            user1.clientEmail=request.form['email']
            user1.clientProjectType=request.form['projectType']
            user1.clientProjectDesc = request.form['message']
            user1.clientAppointment1=request.form['skill']
            print(request.form['skill'])
            # userName1 = user1.userName
            # userName1 = userName1.replace(" ", "")
            # user1.userName = userName1
            # msg = Message(subject="Welcome To Ah-Schools",
            #               sender="ah.schoolsmail@gmail.com",
            #               recipients=[user1.email],  # replace with your email for testing
            #               body="Your userName :"+user1.userName+"\n Your Password :"+str(user1.pasword)+"\n \n Please Use these Credential to login to your User Account \n\n Thanku!\n\nFollow https://ah-schools.herokuapp.com/userLogin to Login"
            #               )
            # mail.send(msg)
            db.session.add(user1)
            db.session.commit()
            print(request.form.get('email'))
            print(request.form.get('name'))
            getUser = user.query.all()
            getUserName = admin.query.all()
            onGoing = Project.query.filter_by(ProjectStatus="Under-Development")    
            Completed = Project.query.filter_by(ProjectStatus="Completed")
            clients = Client.query.all()
            PortfolioData = Portfolio.query.filter_by(id=3).first()
            freeAppointmentTime=adminFreeDay.query.filter_by(id=1).first()
            return render_template("index.html",freeTime=freeAppointmentTime,portFolioData=PortfolioData,clientsData=clients, onGoingProjects=onGoing,completedProjects=Completed)


    except OSError as error:
        print(error)
        print("exception")

@myApp.route('/Adminregister', methods=["POST", "GET"])
def registerAdmin():
    UserReg1 = admin()
    UserReg1.name = request.form['Adminusernamesignup']
    # UserReg1.phone=request.form['AdminPhone']
    userName1 = UserReg1.name
    userName1 = userName1.replace(" ", "")
    UserReg1.name = userName1
    UserReg1.email = request.form['Adminemailsignup']
    UserReg1.phone="Not-Given"
    UserReg1.password = request.form['Adminpasswordsignup']
    folderName = os.path.dirname(os.path.abspath(__file__)) + '//static//adminPhoto'
    filename = secure_filename(request.files['Adminfile'].filename)
    request.files['Adminfile'].save(os.path.join(folderName, filename))
    UserReg1.picture = filename
    print(UserReg1.picture)
    # confirmPass=request.form['confirmReg']
    db.session.add(UserReg1)
    db.session.commit()
    return render_template("loginAdmin.html")

@myApp.route('/AdminregisterByAdmin', methods=["POST", "GET"])
def registerAdminByAdmi():
    UserReg1 = admin()
    UserReg1.name = request.form['Adminusernamesignup']
    UserReg1.phone=request.form['AdminPhone']
    userName1 = UserReg1.name
    userName1 = userName1.replace(" ", "")
    UserReg1.name = userName1
    UserReg1.email = request.form['Adminemailsignup']
    # UserReg1.password = request.form['Adminpasswordsignup']
    UserReg1.password=random.randint(1001,1000000)
    folderName = os.path.dirname(os.path.abspath(__file__)) + '//static//adminPhoto'
    filename = secure_filename(request.files['Adminfile'].filename)
    request.files['Adminfile'].save(os.path.join(folderName, filename))
    UserReg1.picture = filename
    print(UserReg1.picture)
    # confirmPass=request.form['confirmReg']
    db.session.add(UserReg1)
    db.session.commit()
    return render_template("/NiceAdmin/form_component.html")

@myApp.route('/index.html')
def adminHome():
    return render_template("/NiceAdmin/index.html")

@myApp.route('/form_component.html')
def insertCourse():
    return render_template("/NiceAdmin/form_component.html")
#     
@myApp.route('/insertPortfolio', methods=["POST", "GET"])
def CleintForm12():  
    if request.method == "POST":
        user1 = Portfolio.query.filter_by(id=3).first()
        # user1 = Portfolio()
        user1.clients = request.form['clientsNumber']       
        user1.Projects = request.form['Projects']
        user1.HourseOfSupport = request.form['hours']
        user1.HardWorkers  = request.form['workers']
        
        # db.session.add(user1)
        db.session.commit()
     
        adminName=admin.query.all()
        return render_template('/NiceAdmin/form_component.html',admin=adminName)

@myApp.route('/insertClient', methods=["POST", "GET"])
def CleintForm():  
    if request.method == "POST":
        user1 = Client()
        user1.clientName = request.form['ClientName']
        name = user1.clientName
        name = name.replace(" ", "")
        user1.clientName = name
        user1.clientComment = request.form['clientComment']
        Client1 = user1.clientName
        clientLen = len(Client1)
        if clientLen == 0:
            Client1 = "Client Name is not Given"
        user1.clientName=Client1
        folderName = os.path.dirname(os.path.abspath(__file__)) + '//static//ProjectPhoto'
        filename = secure_filename(request.files['ClientLogo'].filename)
        request.files['ClientLogo'].save(os.path.join(folderName, filename))
        user1.clientPicture = filename
        # print(user1.uploadPic1)
        userName1 = user1.clientName
        # userName1 = userName1.replace(" ", "")
        user1.clientName = userName1
        # msg = Message(subject="Welcome To Ah-Schools",
        #               sender="ah.schoolsmail@gmail.com",
        #               recipients=[user1.email],  # replace with your email for testing
        #               body="Your userName :" + user1.userName + "\n Your Password :" + str(
        #                   user1.pasword) + "\n \n Please Use these Credential to login to your User Account \n\n Thanku!\n\nFollow https://ah-schools.herokuapp.com/userLogin to Login"
        #               )
        # mail.send(msg)
        db.session.add(user1)
        db.session.commit()
        # print(request.form.get('cor'))
        # print(request.form.get('name'))
        # getUser = course.query.all()
        # getUserName = admin.query.all()
        adminName=admin.query.all()
        return render_template('/NiceAdmin/form_component.html',admin=adminName)


@myApp.route('/insertProject', methods=["POST", "GET"])
def insertProjectForm():  
    if request.method == "POST":
        user1 = Project()
        user1.ProjectTitle = request.form['ProjectTitle']
        name = user1.ProjectTitle
        name = name.replace(" ", "")
        user1.ProjectTitle = name
        user1.ProjectDecs = request.form['ProjectDescription']
        user1.ProjectDate = request.form['ProjectStarting']
        user1.ProjectCompDate = request.form['ProjectDue']
        user1.Client = request.form['ProjectClient']
        Client = user1.Client
        clientLen = len(Client)
        if clientLen == 0:
            Client = "Client Name is not Given"
        user1.Client=Client
        user1.ProjectStatus = request.form['ProjectStatus']
        user1.ProjectCategory = request.form['ProjectCategory']
        user1.ProjectURL=request.form['ProjectUrl']
        # user1.pasword = random.randint(1001, 1000000)
        # files save kerne kac ode
        
        folderName = os.path.dirname(os.path.abspath(__file__)) + '//static//ProjectPhoto'
        filename = secure_filename(request.files['ProjectFile'].filename)
        request.files['ProjectFile'].save(os.path.join(folderName, filename))
        user1.ProjectPics = filename
        # print(user1.uploadPic1)
        userName1 = user1.ProjectTitle
        # userName1 = userName1.replace(" ", "")
        user1.CourseName = userName1
        # msg = Message(subject="Welcome To Ah-Schools",
        #               sender="ah.schoolsmail@gmail.com",
        #               recipients=[user1.email],  # replace with your email for testing
        #               body="Your userName :" + user1.userName + "\n Your Password :" + str(
        #                   user1.pasword) + "\n \n Please Use these Credential to login to your User Account \n\n Thanku!\n\nFollow https://ah-schools.herokuapp.com/userLogin to Login"
        #               )
        # mail.send(msg)
        db.session.add(user1)
        db.session.commit()
        # print(request.form.get('cor'))
        # print(request.form.get('name'))
        # getUser = course.query.all()
        # getUserName = admin.query.all()
        return render_template('/NiceAdmin/form_component.html')

@myApp.route('/adminLoginOK1',methods=["POST", "GET"])
def AdminloginWala():
    userFound = admin.query.all()
    appointmentData = Appointment.query.all()
    appointementsLen = len(appointmentData)
    projectData=Project.query.all()
    appointementsLen = len(appointmentData)
    ongoing = 0
    complete = 0
    print("421")
    for count in projectData:
        print("423")
        if count.ProjectStatus == "Completed":
            print("425")
            complete = complete + 1
            print("425")
        else:
            ongoing = ongoing + 1
    print(ongoing)
    print(complete)      
    return render_template('/NiceAdmin/index.html',completeProject=complete,onGoing=ongoing,AppointmentLength=appointementsLen, appointments=appointmentData,data=userFound)

# @myApp.route('/')
@myApp.route('/adminLoginOK',methods=["POST", "GET"])
def AdminloginAuth():
    if request.method == "POST":
        loginUser = admin()
        # vid=Video()
        try:
            user1 = request.form['AdminUsername']
            userLoginName = user1
            userFound = loginUser.query.filter_by(email=user1).first()
            userPass = request.form['AdminPassword']
            try:
                if user1 == userFound.email:
                    print(user1)
                    print("{}".format(userFound.email))
                    
                    print("found")
                    if user1==userFound.email and userPass == userFound.password:
                        print("email ander")
                        print(userFound.password)
                        # myUserName = userFound.email
                        appointmentData = Appointment.query.all()
                        projectData=Project.query.all()
                        appointementsLen = len(appointmentData)
                        ongoing = 0
                        complete = 0
                        print("421")
                        for count in projectData:
                            print("423")
                            if count.ProjectStatus == "Completed":
                               print("425")
                               complete = complete + 1
                               print("425")
                            else:
                                ongoing = ongoing + 1
                        print(ongoing)
                        print(complete)
                        # projectLen=len(projectData)
                        adminName=userFound.name
                        return render_template('/NiceAdmin/index.html',completeProject=complete,onGoing=ongoing,AppointmentLength=appointementsLen,adminN=adminName,appointments=appointmentData,data={userFound})
                        
                    else:
                        print("else wala")
                        return render_template("loginAdmin.html", login=">>Not a member please Sign_up")
            except:
                print("pehli exception")
                return render_template("loginAdmin.html", login=">>Invalid UserName")
        except OSError as error:
            print(error)
            print("exception")
            return render_template("login.html", login=">>Not a member please Sign_up")


@myApp.route('/appointment')
def appointmentNonLogin():
    return render_template("withoutLoginAppoForm.html")

@myApp.route('/trainingWorkshop')
def trainingPage():
    return render_template("trainingWorkshop.html")

@myApp.route('/AdminInsertCourse')
def AdminInsertCourses():
   return render_template("/NiceAdmin/form_component.html")

    


@myApp.route('/register', methods=["POST", "GET"])
def register():
    UserReg1 = user()
    UserReg1.userName = request.form['usernamesignup']
    userName1 = UserReg1.userName
    userName1 = userName1.replace(" ", "")
    UserReg1.userName = userName1
    UserReg1.email = request.form['emailsignup']
    UserReg1.pasword = request.form['passwordsignup']
    folderName = os.path.dirname(os.path.abspath(__file__)) + '//static'
    filename = secure_filename(request.files['file'].filename)
    request.files['file'].save(os.path.join(folderName, filename))
    UserReg1.picture = filename
    print(UserReg1.picture)
    # confirmPass=request.form['confirmReg']
    db.session.add(UserReg1)
    db.session.commit()
    return render_template("login.html")


@myApp.route('/userLogin')
def userLoginPoint():
    return render_template("login.html")


@myApp.route('/loginUserOK', methods=["GET", "POST"])
def loginUserOK2():
    # loginUser = user()
    if request.method == "POST":

        try:
            user1 = request.form['userLogin1']
            userLoginName = user1
            userFound = user.query.filter_by(userName=user1).first()
            userPass = request.form['passLogin1']
            userRole = request.form['roleUser']
            try:
                # if (userRole=="Student"):
                if user1 == userFound.userName:
                    print("found")
                    if userRole == userFound.role == "Student":
                        if userFound.userName == user1 and userPass == userFound.pasword:
                            # if userRole=="Student":
                            print("Studnet")
                            return render_template('OnlyForStudent.html', data={userFound})
                        else:
                            return render_template("loginUser.html", login=">>Invalid Password")
                    elif userRole == userFound.role == "Teacher":  # break:
                        print("Teacher")
                        return render_template('OnlyForTeacher.html', data={userFound})
                    else:
                        return render_template("loginUser.html", clr="rgb(70, 127, 202)",
                                               login="Please Select Correct Role",
                                               loginT2="Verify Your UserName,Password")

                        # elif userFound.userName == user1 and userPass == userFound.pasword and userRole=="Teacher":
                        #     return render_template('OnlyForTeacher.html', data={userFound})
                else:
                    return render_template("loginUser.html", login=">>Not a member please Sign_up")

            # 237417
            except:
                return render_template("loginUser.html", login=">>Invalid UserName")

        except OSError as error:
            print(error)
            print("exception")
            return render_template("loginUser.html", login=">>Not a member please Contact Admin")


@myApp.route('/logoutTO')
def logOut():
    return render_template("mainHome.html")


myUserName = ''


@myApp.route('/loginOK', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        loginUser = user()
        # vid=Video()
        try:
            user1 = request.form['username']
            userLoginName = user1
            userFound = loginUser.query.filter_by(userName=user1).first()
            userPass = request.form['password']
            try:
                if user1 == userFound.userName:
                    print("found")
                    if userFound.userName == user1 and userPass == userFound.pasword:

                        myUserName = userFound.userName
                         
                        return render_template('userProfile.html',data={userFound})
                    else:
                        return render_template("login.html", login=">>Not a member please Sign_up")
            except:
                return render_template("login.html", login=">>Invalid UserName")
        except OSError as error:
            print(error)
            print("exception")
            return render_template("login.html", login=">>Not a member please Sign_up")


@myApp.route('/showUser')
def showUser():
    return render_template("secondPage.html")


@myApp.route('/adminAllOption')
def adminPanal():
    return render_template("mainHome.html")


@myApp.route('/form')
def add1User():
    return render_template("form.html")


name = 'asdasd'


@myApp.route('/student')
def showStudent():
    userFound = user.query.filter_by(role="Student")
    return render_template("student.html", data=userFound)


@myApp.route('/studentOnly')
def showStudent1():
    r = db.engine.execute("select userName,email,phone,role,email,picture from user where role Like \'Student\'")
    userFound = user.query.filter_by(role="Student")
    return render_template("studentOnly.html", data=userFound)


@myApp.route('/teacher')
def showTeacher():
    userFound = user.query.filter_by(role="Teacher")
    return render_template("teacher.html", data=userFound)


@myApp.route('/addUser', methods=["GET", "POST"])
def addUser():
    try:
        if request.method == "POST":
            user1 = user()
            user1.userName = request.form['name']
            name = user1.userName
            name = name.replace(" ", "")
            user1.userName = name
            user1.email = request.form['email']
            user1.phone = request.form['phone']
            user1.role = request.form['role']
            user1.pasword = random.randint(1001, 1000000)
            # files save kerne kac ode

            folderName = os.path.dirname(os.path.abspath(__file__)) + '//static'
            filename = secure_filename(request.files['userPicture'].filename)
            request.files['file'].save(os.path.join(folderName, filename))
            user1.picture = filename
            print(user1.picture)
            userName1 = user1.userName
            # userName1 = userName1.replace(" ", "")
            user1.userName = userName1
            msg = Message(subject="Welcome To Ah-Schools",
                          sender="ah.schoolsmail@gmail.com",
                          recipients=[user1.email],  # replace with your email for testing
                          body="Your userName :" + user1.userName + "\n Your Password :" + str(
                              user1.pasword) + "\n \n Please Use these Credential to login to your User Account \n\n Thanku!\n\nFollow https://ah-schools.herokuapp.com/userLogin to Login"
                          )
            mail.send(msg)
            db.session.add(user1)
            db.session.commit()
            print(request.form.get('email'))
            print(request.form.get('name'))
            getUser = user.query.all()
            getUserName = admin.query.all()
            return render_template('adminSideNav.html', users=getUser, login='abdul')


    except OSError as error:
        print(error)
        print("exception")


@myApp.route('/users')
def showAllUser():
    getUser = user.query.all()
    return render_template('adminSideNav.html', users=getUser, adminLogin=myUserName)


@myApp.route('/searchStd', methods=["POST"])
def searchUser():
    user1 = request.form['searchStd']
    try:
        userFound = user.query.filter_by(email=user1).first()
        myUser = user.query.filter_by(role="Student")
        if userFound.role == 'Student':
            return render_template('student.html', data={userFound})
    except:
        return render_template('student.html', data=myUser, err="error", found="Not Found")


@myApp.route('/searchTeacher', methods=["POST"])
def searchTeacher():
    user1 = request.form['searchTeacher']
    try:
        userFound = user.query.filter_by(email=user1).first()
        myUser = user.query.filter_by(role="Teacher")
        if userFound.role == 'Teacher':
            return render_template('teacher.html', data={userFound})
    except:
        return render_template('teacher.html', data=myUser, err="error", found="Not Found")


@myApp.route('/confirmMeeting', methods=["POST","GET"])
def ConfirmMeeting():
    person=user()
    person.appointment = request.form['confirmMeetings']
    # userFound = user.query.filter_by(userName=userName1).first()
    # db.session.delete(userFound)
    print("meeting Confirmed for {}".format(person.appointment))
    db.session.add(person)
    db.session.commit()
    # myUser = user.query.all()
    # userFound = admin.query.all()
    appointmentData = Appointment.query.all()
    projectData=Project.query.all()
    appointementsLen = len(appointmentData)
    ongoing = 0
    complete = 0
    print("421")
    for count in projectData:
        print("423")
        if count.ProjectStatus == "Completed":
            print("425")
            complete = complete + 1
            print("425")
        else:
            ongoing = ongoing + 1
    print(ongoing)
    print(complete)
    # projectLen=len(projectData)
    # adminName=userFound.name
    return render_template('/NiceAdmin/index.html',completeProject=complete,onGoing=ongoing,AppointmentLength=appointementsLen, appointments=appointmentData )
    
    # userFound = user.query.filter_by(role="Student")
    # return render_template("/NiceAdmin/form_component.html")

    print("delete")


@myApp.route('/deleteAppointment', methods=["POST","GET"])
def DeleteAppointment():
    userName1 = request.form['deleteApp']
    userFound = Appointment.query.filter_by(clientAppointment1=userName1).first()
    db.session.delete(userFound)
    db.session.commit()
    # myUser = Appointment.query.all()
    appointmentData = Appointment.query.all()
    projectData=Project.query.all()
    appointementsLen = len(appointmentData)
    ongoing = 0
    complete = 0
    print("421")
    for count in projectData:
        print("423")
        if count.ProjectStatus == "Completed":
        
            complete = complete + 1
      
        else:
            ongoing = ongoing + 1
    print(ongoing)
    print(complete)
    # projectLen=len(projectData)
    # adminName=userFound.name
    return render_template('/NiceAdmin/index.html',completeProject=complete,onGoing=ongoing,AppointmentLength=appointementsLen, appointments=appointmentData)
                        
    # userFound = user.query.filter_by(role="Teacher")
    # return render_template("teacher.html", data=userFound)
    # return render_template('shwoUser.html',users=myUser,login=userLoginName)


# @myApp.route('/update', methods=["POST"])
# def updateText():
#     userName1 = request.form['target_userUpdate']
#     userFound = user.query.filter_by(userName=userName1).first()
#     userFound.userName = request.form['updateText']
#     db.session.commit()
#     myUser = user.query.filter_by(userName=userFound.userName).first()
#     if myUser.role == "Student":
#         return render_template('OnlyForStudent.html', data={myUser})
#     elif myUser.role == "Teacher":
#         return render_template('OnlyForTeacher.html', data={myUser})


@myApp.route('/updateEmail', methods=["POST"])
def updateEmail1():
    Email = request.form['target_userUpdateEmail1']
    userFound = user.query.filter_by(userName=Email).first()
    userFound.email = request.form['updateEmail12']
    db.session.commit()
    myUser = user.query.filter_by(email=userFound.email).first()
    if myUser.role == "Student":
        return render_template('OnlyForStudent.html', data={myUser})
    elif myUser.role == "Teacher":
        return render_template('OnlyForTeacher.html', data={myUser})


if __name__ == "__main__":
    myApp.run(debug=True)
    # socketio.run(myApp, debug=True)