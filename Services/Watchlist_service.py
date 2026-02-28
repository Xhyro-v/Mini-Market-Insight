from Data_manager.WatchList_manager import WatchlistManager
from Core.Report import Output
from Utils.Utility import crypto_LIST

WM = WatchlistManager()


#name , pilihan nomer coin , coin baru
class Watchlist_Service:
      def delete_coins(self):
          name = input("Nama watchlist: ")
          coins_input = input("coin yang ingin dihapus (pisahkan dengan koma): ")
          
          coins = [c.strip() for c in coins_input.split(",")]
          
          WM.delete_coins(name, coins)
      
      def rename_watchlist(self):
          old = input("Masukan nama watchlist yang ingin di rename:: ")
          new = input("Masukan nama baru: ")
          WM.rename_watchlist(old, new)
      
      def replace_coins(self):
          watchlist = input("Masukan nama watchlist: ")
          choice = int(input("Masukan nomer coin yang diganti: ")) -1
          coin = int(input("Pilih coin: "))-1
          coin = crypto_LIST[-1]
          WM.replace_coin(watchlist,choice, coin)
      
      def Edit_menu(self):
          submenu_actions = {
              "1": self.rename_watchlist,
              "2": self.replace_coins,
          }
      
          while True:
              print("\n-- Submenu Lihat --")
              print("1. Rename watchlist")
              print("2. Edit coin ")
              print("0. Kembali")
      
              choice = input("Pilih: ")
      
              if choice == "0":
                  break
      
              action = submenu_actions.get(choice)
              if action:
                  action()
              else:
                  print("Pilihan tidak valid")
      
      def Show_menu(self):
          submenu_actions = {
              "1": WM.show_watchlists,
              "2": lambda: WM.show_watchlist(input("Masukkan nama watchlist: "))
          }
      
          while True:
              print("\n-- Submenu Lihat --")
              print("1. Lihat semua")
              print("2. Lihat detail")
              print("0. Kembali")
      
              choice = input("Pilih: ")
      
              if choice == "0":
                  break
      
              action = submenu_actions.get(choice)
              if action:
                  action()
              else:
                  print("Pilihan tidak valid")
       
      
      def Delete_menu(self):
          submenu_actions = {
              "1": lambda: WM.delete_watchlist(input("Masukan watchlist yang ingin dihapus: ")),
              "2": self.delete_coins,
          }
      
          while True:
              print("\n-- Submenu Lihat --")
              print("1. Hapus watchlist")
              print("2. Hapus coin")
              print("0. Kembali")
      
              choice = input("Pilih: ")
      
              if choice == "0":
                  break
      
              action = submenu_actions.get(choice)
              if action:
                  action()
              else:
                  print("Pilihan tidak valid")
      
      
      def add_coins(self):
          name = input("Nama watchlist: ")
          coins_input = input("Masukkan nomor / nama coin (pisahkan koma): ")
          coins = coins_input.split(",")
          
          WM.add_coins(name, coins)
      
      def create_menu(self):
          submenu_actions =  {
            "1" : lambda : WM.create_watchlist(input("Masukan nama watchlist baru: ")),
            "2" : self.add_coins,
          }
          
          while True:
              print("\n-- Submenu Buat --")
              print("1. Buat watchlist")
              print("2. Tambah coin")
              print("0. Kembali")
      
              choice = input("Pilih: ")
      
              if choice == "0":
                  break
      
              action = submenu_actions.get(choice)
              if action:
                  action()
              else:
                  print("Pilihan tidak valid")
      
      def watchlist_menu(self):
          menu_actions = {
              "1": self.create_menu,
              "2": self.Show_menu,
              "3": self.Edit_menu,
              "4": self.Delete_menu
          }
      
          while True:
              print("\n==== WATCHLIST ====")
              print("1. Buat watchlist")
              print("2. Lihat watchlist")
              print("3. Edit watchlist")
              print("4. Hapus watchlist")
              print("5. Keluar")
      
              choice = input("Pilih menu: ")
      
              if choice in ["5","keluar"]:
                  print("Program selesai.")
                  break
      
              action = menu_actions.get(choice)
              
              if action:
                  action()
              else:
                  print("Pilihan tidak valid")


if __name__ == '__main__':
    WS = Watchlist_Service()
    WS.watchlist_menu()