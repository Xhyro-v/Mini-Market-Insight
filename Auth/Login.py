import hashlib
from Storage.Database import Database
from Utils.Utility import Color, Center

class Auth:
    def __init__(self):
        self.db = Database("Users")

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password):
        if self.db.get(username):
            return False, Color.Yellow(Center.text("Username sudah ada!"))

        self.db.insert(username, {
            "password": self.hash_password(password)
        })

        return True, Color.Green(Center.text("Registrasi berhasil!"))

    def login(self, username, password):
        user = self.db.get(username)

        if not user:
            return False, Color.Yellow(Center.text("User tidak ditemukan!"))

        if user["password"] == self.hash_password(password):
            return True, Color.Green(Center.text("Login berhasil!"))

        return False, Color.Green(Center.text("Password salah!"))