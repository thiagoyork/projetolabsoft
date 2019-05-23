from flask import Flask,render_template,request
import os 
from flask_sqlalchemy import SQLAlchemy
#from db_setup import init_db, db_session

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir,'bookdatabase.db'))
#database_file2 = "sqlite:///{}".format(os.path.join(project_dir,'voos.db'))



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Socio(db.Model):
	matricula = db.Column(db.String(80),unique = True, nullable = False,primary_key=True)
	nome = db.Column(db.String(80), nullable = True,unique = False)
	sobrenome =db.Column(db.String(80), nullable = True)
	telefone = db.Column(db.String(80), nullable = True)
	endereco = db.Column(db.String(80), nullable = True)
	idade = db.Column(db.String(80), nullable = True)
	email = db.Column(db.String(80), nullable = True)
	cpf = db.Column(db.String(80), nullable = True)
	sexo = db.Column(db.String(80), nullable = True)
	numero_horas = db.Column(db.String(80), nullable = True)
	senha = db.Column(db.String(80), nullable = True)
	instituicao = db.Column(db.String(80), nullable = True)
	tipo = db.Column(db.String(80), nullable = True)
	data_diploma = db.Column(db.String(80), nullable = True)
	numero_brevet= db.Column(db.String(80), nullable = True)

	def __repr__(self):
		return "<Nome: {} e matricula {}>".format(self.nome)#,self.matricula)

class Voo():

	numero_voo = db.Column(db.String(80),unique = True, nullable = False,primary_key=True)
	aluno = db.Column(db.String(80), nullable = True)
	instrutor = db.Column(db.String(80), nullable = True)
	horas = db.Column(db.String(80), nullable = True)
	rate = db.Column(db.String(80), nullable = True)
	data_hora = db.Column(db.String(80), nullable = True)

	
@app.route('/cadastro-aluno',methods =["GET","POST"])
def home():
	if request.form:
		print(request.form)
		aluno = Socio(nome = request.form.get('nome'),
						matricula = request.form.get('matricula'),
						senha = request.form.get('senha'),
						sobrenome = request.form.get('sobrenome'),
						idade = request.form.get('idade'),
						telefone = request.form.get('telefone'),
						endereco = request.form.get('endereco'),
						email = request.form.get('email'),
						cpf = request.form.get('cpf'),
						sexo = request.form.get('sexo'),
						numero_brevet = None,
						instituicao = None,
						tipo = 'aluno',
						data_diploma = None,
						numero_horas = 0,

						)
		db.session.add(aluno)
		db.session.commit()
		#alunos = Aluno.query.all()
	return render_template('TelaCadastroAluno.html')

@app.route('/cadastro-piloto',methods =["GET","POST"])
def home1():
	if request.form:
		print(request.form)
		piloto = Socio(nome = request.form.get('nome'),
						matricula = request.form.get('matricula'),
						senha = request.form.get('senha'),
						sobrenome = request.form.get('sobrenome'),
						idade = request.form.get('idade'),
						telefone = request.form.get('telefone'),
						endereco = request.form.get('endereco'),
						email = request.form.get('email'),
						cpf = request.form.get('cpf'),
						sexo = request.form.get('sexo'),
						numero_brevet = request.form.get('breve'),
						instituicao = None,
						tipo = 'piloto',
						data_diploma = None,
						numero_horas = None,
						)
		db.session.add(piloto)
		db.session.commit()
		#pilotos = Piloto.query.all()
	return render_template('TelaCadastroPiloto.html')#,pilotos =pilotos) #,alunos = alunos)
@app.route('/visualizar-cadastro',methods=['GET'])
def visualizar():
	alunos = Socio.query.filter_by(tipo = 'aluno')
	pilotos = Socio.query.filter_by(tipo = 'piloto')
	instrutores = Socio.query.filter_by(tipo = 'instrutor')
	db.session.commit()
	return render_template('Visualizar.html',alunos = alunos
						,pilotos = pilotos,instrutores = instrutores)

@app.route('/cadastro-instrutor',methods =["GET","POST"])
def home2():
	if request.form:
		print(request.form)
		instrutor = Socio(nome = request.form.get('nome'),
						matricula = request.form.get('matricula'),
						senha = request.form.get('senha'),
						sobrenome = request.form.get('sobrenome'),
						idade = request.form.get('idade'),
						telefone = request.form.get('telefone'),
						endereco = request.form.get('endereco'),
						email = request.form.get('email'),
						cpf = request.form.get('cpf'),
						sexo = request.form.get('sexo'),
						numero_brevet = request.form.get('breve'),
						instituicao = request.form.get('formacao'),
						tipo = 'instrutor',
						data_diploma = request.form.get('diploma'),
						numero_horas = None)

		db.session.add(instrutor)
		db.session.commit()
		#instrutores = Instrutor.query.all()
	return render_template('TelaCadastroInstrutor.html')#, instrutores = instrutores)

@app.route('/consultar',methods =["GET","POST"])
def home3():
	return render_template('Consulta.html')

@app.route('/',methods =["GET","POST"])
def home4():
	return render_template('TelaInicial.html')

@app.route('/resultado-consulta',methods =["GET","POST"])
def home6():

	if request.method =='POST':
		matricula = request.form.get('matricula')
		socios = Socio.query.filter_by(matricula = matricula)
	return render_template('ResultadoConsulta.html',socios = socios)

@app.route('/cadastro-voo',methods =["GET","POST"])
def home7():
	if request.form:
		print(request.form)
		voo = Voo(numero_voo = request.form.get('numero_voo'),
					aluno = request.form.get('matricula_aluno'),
					instrutor = request.form.get('matricula_instrutor'),
					horas = request.form.get('horas_de_voo'),
					rate = request.form.get('rate'),
					data_hora = request.form.get('data_hora_voo'),
			)
	return render_template('TelaCadastroVoo.html')

@app.route('/login',methods =["GET","POST"])
def home8():
	return render_template('TelaLogin.html')


if __name__ == '__main__':
	app.run(debug=True)