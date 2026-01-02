import os
from flask import Flask, send_from_directory
from flask_cors import CORS

from backend.database_config import criar_tabelas_remoto
from backend.socketio_instance import init_socketio
from backend.routes.auth import auth_bp
from backend.routes.usuarios import usuarios_bp
from backend.routes.salas import salas_bp
from backend.routes.apostas import apostas_bp
from backend.routes.online import online_bp

app = Flask(
    __name__,
    static_folder=os.path.join(os.path.dirname(__file__), "static"),
    static_url_path=""
)

app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

socketio = init_socketio(app)

CORS(app)

# Registrar blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
app.register_blueprint(salas_bp, url_prefix="/salas")
app.register_blueprint(apostas_bp, url_prefix="/apostas")
app.register_blueprint(online_bp, url_prefix="/online")

# Criar tabelas ao iniciar
criar_tabelas_remoto()

if __name__ == "__main__":
    socketio.run(app, debug=True)
