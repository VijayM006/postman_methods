from flask import Flask,jsonify,request,render_template
import json
vj=Flask(__name__)
postman=[]
# @vj.route("/",methods=["GET","POST"])
# def home():
#     if request.method=="GET":

#         return jsonify({"request":"this is get request","Name":"Vijay"})
    
# @vj.route("/",methods=["GET","POST"])
# def forms():
#     if request.method=="POST":
#         Name=request.form.get("Name")
#         Age=request.form.get("Age")
#         RollNo=request.form.get("RollNo")
#         mark1=request.form.get("mark1")
#         mark2=request.form.get("mark2")
#         mark3=request.form.get("mark3")
#         mark4=request.form.get("mark4")
#         mark5=request.form.get("mark5")
#         Mark_list=[]
#         Mark_list.append(mark1)
#         Mark_list.append(mark2)
#         Mark_list.append(mark3)
#         Mark_list.append(mark4)
#         Mark_list.append(mark5)
#         student_dict={}
#         student_dict.update({"Name":Name})
#         student_dict.update({"Age":Age})
#         student_dict.update({"RollNo":RollNo})
#         student_dict.update({"Marks":Mark_list})
#         postman.append(student_dict)
#     return render_template("table.html",value=postman)
@vj.route("/",methods=["GET","POST"])
def homie():

    if request.method=="POST":
       Name=request.form.get("Name")
       Age=request.form.get("Age")
       Dprtment=request.form.get("Department")
       RollNo=request.form.get("RollNo")
       Tamil=request.form.get("Tamil")
       English=request.form.get("English")
       Maths=request.form.get("Maths")
       Science=request.form.get("Science")
       Science2=request.form.get("S.Science")
       Marks_list=[]
       Marks_list.append(Tamil)
       Marks_list.append(English)
       Marks_list.append(Maths)
       Marks_list.append(Science)
       Marks_list.append(Science2)
       dicti={}
       dicti.update({"Name":Name})
       dicti.update({"Age":Age})
       dicti.update({"Department":Dprtment})
       dicti.update({"RollNo":RollNo})
       dicti.update({"Marks":Marks_list})
       postman.append(dicti)
    return render_template("index.html",value=postman)

@vj.route("/a",methods=["GET","POST"])
def posti():
    postman.append(request.get_json())
    return postman

@vj.route("/b",methods=["GET","POST"])
def thanga():
    thangam=json.load(postman)
    return render_template("table.html",value=thangam)
if __name__=="__main__":
    vj.run(debug=True)