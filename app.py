from flask import Flask, render_template, request, redirect, url_for
from models import db, Mahasiswa

app = Flask(__name__)

# Konfigurasi database SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mahasiswa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Buat tabel database
with app.app_context():
    db.create_all()


# Halaman utama - daftar mahasiswa
@app.route('/')
def index():
    data = Mahasiswa.query.all()
    return render_template('index.html', data=data)


# Tambah data
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nama = request.form['nama']
        nim = request.form['nim']
        jurusan = request.form['jurusan']

        mhs = Mahasiswa(nama=nama, nim=nim, jurusan=jurusan)
        db.session.add(mhs)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')


# Edit data
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    mhs = Mahasiswa.query.get_or_404(id)
    if request.method == 'POST':
        mhs.nama = request.form['nama']
        mhs.nim = request.form['nim']
        mhs.jurusan = request.form['jurusan']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', mhs=mhs)


# Hapus data
@app.route('/delete/<int:id>')
def delete(id):
    mhs = Mahasiswa.query.get_or_404(id)
    db.session.delete(mhs)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)