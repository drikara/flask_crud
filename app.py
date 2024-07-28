from flask import Flask,render_template,redirect,request
import db



app = Flask(__name__)


 
@app.route('/')
def home():
    return render_template('accueil.html')

@app.route('/ajouter',methods = ["POST","GET"])
def addStudent():
    if request.method == 'POST':
        nom = request.form["Nom"].strip()
        prenoms = request.form["Prenom"].strip()
        age =int(request.form["Age"].strip())
        resultat = db.n_inscription(nom,prenoms,age)
        print(resultat)
        return render_template('add_student.html')
    else:
         return render_template('add_student.html')



   

@app.route('/liste')
def listStudent():
    students=db.get_students()
    return render_template("list_student.html",students=students)

@app.route("/delete/<int:id>")
def deleteStudent(id):
    res = db.delete_student(id)
    print(res)
    return redirect("/liste")

@app.route("/edit/<int:id>",methods=["POST","GET"])
def editStudent(id):
    if request.method == "POST":
        nom = request.form["Nom"].strip()
        prenom = request.form["Prenom"].strip()
        age = int(request.form["Age"].strip())
        r=db.modify_student(id,nom,prenom,age)
        print(r)
        return redirect("/liste")
    else:
        student = db.get_students().filter_by(id=id).first()
        
        return render_template("modify.html",student=student)


    
