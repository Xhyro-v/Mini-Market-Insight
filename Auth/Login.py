import hashlib
from Storage.Database import Database
from Utils.Utility import Color, Center

class Auth:
    def __init__(self):
        self.DB = Database("Users")

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username, password ):
        if self.DB.get(username):
            return False, Color.Yellow(Center.text("Username sudah ada!"))

        self.DB.insert(username, {
            "password": self.hash_password(password)
        })

        return True, Color.Green(Center.text("Registrasi berhasil!"))

    def login(self, username, password):
        user = self.DB.get(username)

        if not user:
            return False, Color.Yellow(Center.text("User tidak ditemukan!"))

        if user["password"] == self.hash_password(password):
            return True, Color.Green(Center.text("Login berhasil!"))

        return False ,Color.Yellow(Center.text("Password salah!"))