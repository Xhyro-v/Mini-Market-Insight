from Auth.Login import Auth
from Utils.Utility import Input, Center, Color

class Auth_service:
    def auth_menu():
          while True:
              auth = Auth()
              print("1. Login")
              print("2. Daftar")
              print("0. Keluar")
      
              pilihan = input("Pilih: ")
      
              if pilihan == "1":
                  password_token = 5
                  while password_token > 0 :
    
                      username = Input.Auth_in("Username: ")
                      password = Input.Auth_in("Password: ", hidden = True)
          
                      status, msg = auth.login(username, password)
                      if status is False:
                          print(msg)
                          password_token -= 1
          
                      else:
                          print(msg)
                          if status:
                              return username 
                          
          
      
      
              elif pilihan == "2":
                  username = Input.Auth_in(Color.BrightBlue("Username: "))
                  password = Input.Auth_in(Color.BrightBlue("Password: "))

                  status, msg = auth.register(username, password)
                  print(msg)
                  
      
              elif pilihan == "0":
                  exit()
      
              else:
                  print(Color.Red(Center.text("Pilihan tidak valid!")))

