from flask import Flask, render_template, request, session, current_app, jsonify, redirect, url_for

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Project
import os

engine = create_engine('sqlite:///projecten.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__, static_url_path='/static')
app.config["DEBUG"] = True

@app.route('/')
def home():
    return render_template('landingspagina.html')

@app.route('/About')
def portfolio():
    return render_template('about.html')

@app.route('/CV')
def CVpagina():
    return render_template('cv.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/productoverzicht')
def productoverzicht():
    projecten = session.query(Project).all()
    return render_template('productoverzicht.html', projecten = projecten)

@app.route('/nieuwproject')
def nieuwProject():
    return render_template('nieuwProject.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Onjuiste inloggegevens, probeer opnieuw'
        else:
            return redirect(url_for('projecten'))
    return render_template('login.html', error=error)

@app.route('/projecten')
def projecten():
    projecten = session.query(Project).all()
    print(projecten)
    return render_template('projecten.html', projecten = projecten)

@app.route('/createProject/', methods = ['POST'])
def createProject():
  if request.method == 'POST':
      nieuwProject = Project(titel = request.form['titel'], datum = request.form['datum'], afbeeldingUrl = request.form['afbeeldingUrl'])
      session.add(nieuwProject)
      session.commit()
      return redirect(url_for('projecten'))

@app.route('/editProject/', methods = ['GET','POST'])
def editProject():
    editedProject = session.query(Project).filter_by(id=project_id).one()
    if request.method == 'POST':
        if request.form['titel']:
           editedProject.title = request.form['titel']
           return redirect(url_for('projecten'))
        else:
           return render_template('editProject.html', project = editedProject)





#@app.route('/project/<int:project_id>/edit/', methods = ['GET','POST'])
#def editProject(project_id):
#   editedProject = session.query(Project).filter_by(id=project_id).one()
#   if request.method == 'POST':
#       if request.form['titel']:
#           editedProject.title = request.form['titel']
#           return redirect(url_for('productoverzicht'))
#   else:
#       return render_template('editProject.html', project = editedProject)

@app.route('/projecten/<int:project_id>/delete/', methods = ['GET','POST'])
def deleteProject(project_id):
   projectToDelete = session.query(Project).filter_by(id=project_id).one()
   if request.method == 'POST':
       session.delete(projectToDelete)
       session.commit()
       return redirect(url_for('productoverzicht', project_id=project_id))
   else:
       return render_template('deleteProject.html',project = projectToDelete)

if __name__ == '__main__':
    app.run(debug=True)