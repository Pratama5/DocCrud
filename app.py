from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfigurasi database (menggunakan SQLite di sini)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rootpassword@db:3306/doccrud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model untuk menyimpan data
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(300), nullable=False)

# Halaman Utama - Menampilkan data
@app.route('/')
def index():
    documents = Document.query.all()
    return render_template('index.html', documents=documents)

# Halaman Create - Menambah data
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_doc = Document(title=title, content=content)
        db.session.add(new_doc)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

# Halaman Update - Mengupdate data
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    document = Document.query.get_or_404(id)
    if request.method == 'POST':
        document.title = request.form['title']
        document.content = request.form['content']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', document=document)

# Halaman Delete - Menghapus data
@app.route('/delete/<int:id>')
def delete(id):
    document = Document.query.get_or_404(id)
    db.session.delete(document)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context(): #membuat Context aplikasi
        db.create_all()  # Membuat tabel di database
    app.run(host='0.0.0.0', port=5000, debug=True)
