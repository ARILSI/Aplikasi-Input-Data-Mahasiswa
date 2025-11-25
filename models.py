from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mahasiswa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    nim = db.Column(db.String(20), unique=True, nullable=False)
    jurusan = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Mahasiswa {self.nama}>'