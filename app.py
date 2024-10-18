from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="12345",
    database="library_db"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

# Add new book
@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    publisher = request.form['publisher']
    isbn = request.form['isbn']
    quantity = request.form['quantity']
    
    cursor.execute(
        "INSERT INTO books (title, author, publisher, isbn, quantity) VALUES (%s, %s, %s, %s, %s)",
        (title, author, publisher, isbn, quantity)
    )
    db.commit()
    
    return redirect('/')

# Display books
@app.route('/books')
def display_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
