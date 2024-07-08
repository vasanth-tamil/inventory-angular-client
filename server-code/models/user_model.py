import hashlib
from models.model import Model

class User(Model):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = hashlib.md5(password.encode()).hexdigest()
        super().__init__()

    def create(self):
        self.cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", (self.name, self.email, self.password))
        self.commit()

    @staticmethod
    def get_user_by_email_and_password(email, password):
        password = hashlib.md5(password.encode()).hexdigest()
        model = Model()
        model.cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = model.cursor.fetchone()
        return user
    
    @staticmethod
    def email_exists(email):
        model = Model()
        model.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = model.cursor.fetchone()

        # email already exists return true
        if user:
            return True
        return False