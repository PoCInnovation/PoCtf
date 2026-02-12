from CTFd import create_app
from CTFd.models import db, Configs

app = create_app()

with app.app_context():  # ← ceci est indispensable
    db.create_all()
    db.session.add_all([
        Configs(key="ctf_name", value="PoCtf"),
        Configs(key="ctf_description", value="Bienvenue !"),
        Configs(key="ctf_theme", value="core")
    ])
    db.session.commit()
