# Nesse arquivo é definido o nosso app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy #Banco 1º: importar o SQLALchemy do flask para criar o banco de dados 
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db" #Banco 3º: Passar entre ['O local onde fica o nosso banco de dados, isso é definido pelo flask']
app.config["SECRET_KEY"] = "1f59aa649fe4c8fa8c72c5b06323f672"
app.config["UPLOAD_FOLDER"] = "static/fotos_posts"

database = SQLAlchemy(app) #Banco 2º: da mesma forma que cria-se o app a gente cria o banco de dados dessa forma
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "homepage"


# Qualquer importação futura deve ser feita depois do app, devido a REFERENCIA CIRCULAR, onde os outros arquivos dependem do app para funcionar

from fakepinterest import routes