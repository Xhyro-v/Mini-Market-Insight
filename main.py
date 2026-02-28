from Utils.Utility import Input, Color, Center, Font, crypto_LIST, time_LIST, crypto
from Core.Data_fetcher import fetch_current_price, fetch_historical_prices, Global_market
from Core.Processor import analyze_signal
from Core.Report import Output
from Storage.Database import Database
from Services.Watchlist_service import Watchlist_Service
from Services.Login_service import Auth_service



print(Center.box(Center.text("CRYPTO SIGNAL ANALYZER")))
def main_menu(username):
      while True:
          """
          Enter your API key down here ↓
          """
          CAK = "CG-7qQZF5SzkFCZhcbXg9wAUvAv"
          """
          ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
          """
          TIME_LIST = time_LIST
          CRYPTO_LIST = crypto_LIST
          print(Font.Bold("=====MENU====="))
          print("1.Crypto")
          print("2.keluar\n")
          cmd = input("Pilih menu: ").strip().capitalize()
          if cmd in ["1","Crypto"]:
        
              print("\n=====CRYPTO=MENU=====")
              print("1.Lihat harga")
              print("2.Buat watchlist")
              print("3.Market global")
              print("4.Buat saran keputusan\n")
              print("0.Kembali")
            
              submenu = input("Pilih Submenu: ").strip()
              if submenu in ["1"]:
                  Output.list_crypto(CRYPTO_LIST)
                  while True:
                      choice = int(Input.number("\nPilih Crypto (1-4): "))
                      if choice == 0:
                          break
                      try:
                        coin_id = CRYPTO_LIST[choice - 1]
                
                        current_price = fetch_current_price(coin_id, CAK)
                        Output.report_info(coin_id,current_price)
  
                      except:
                          print(Color.Red(Center.text("Gagal menampilkan harga!")))

              elif submenu in ["2"]:
                  WS = Watchlist_Service()
                  WS.watchlist_menu()
  
              elif submenu in ["3"]:
                  try:
                      data = Global_market()
                      cap = data["market_cap"]
                      vol = data["volume"]
                      Output.global_val(cap, vol)
                  except:
                    print(Color.Red(Center.text("Gagal menampilkan hasil!")))
                  
              elif submenu in ["4"]:
              
                  Output.list_crypto(CRYPTO_LIST)
                  choice = int(Input.number("\nPilih Crypto (1-4): "))
                  coin_id = CRYPTO_LIST[choice - 1]
                  
                  for i, TM in enumerate(TIME_LIST, 1):
                      print(f"{i}. {TM}")

                  chtimes = int(Input.number("\nPilih waktu: "))
                  times = TIME_LIST[chtimes - 1]
  
  
                  avg_price = float(input("Masukan saat beli: "))
              
                  try:
                      historical_prices = fetch_historical_prices(coin_id, CAK, days=times)
                  
                      current_price = fetch_current_price(coin_id, CAK)
                      signal, avg_price, diff = analyze_signal(current_price, historical_prices,avg_price)
                  
                      Output.report_decc(
                          coin=coin_id,
                          current=current_price,
                          avg=avg_price,
                          signal=signal,
                          diff=diff,
                          times=times
                      )
                      print("")
                  except:
                      print(Color.Red(Center.text("Gagal menampilkan hasil!")))
                  
      
          elif cmd in ["2","Keluar"]:
              print(Color.Blue(Center.text("Program selesai")))
              break
          
          else:
              print(Color.Red(Center.text(f"Tidak ada menu bernama {cmd}\n")))

def Main():
    username = Auth_service.auth_menu()
    main_menu(username)

if __name__ == '__main__':
    Main()