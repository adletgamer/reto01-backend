from flask import Flask, request, render_template
from my_profile import Profile
from fireb import FirebaseAdmin

app = Flask(__name__)

fb = FirebaseAdmin()

@app.route('/')
def index():
    perfil = Profile()
    context = {
        'nombre': perfil.name,
        'imagen': perfil.image,
        'rol': perfil.role,
        'ubicacion': perfil.location,
        'url_github': perfil.url_github
    }
    return render_template('index.html', **context)

@app.route('/projects')
def projects():
    lista_proyectos = fb.get_proyectos()
    context = {
        'proyectos': lista_proyectos
    }
    return render_template('projects.html', **context)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/resume')
def resume():
    lista_education = fb.get_education()
    lista_experiencia = fb.get_experiencia_laboral()
    context = {
        'education': lista_education,
        'experiencia': lista_experiencia
    }
    return render_template('resume.html', **context)

app.run(debug=True)
