from Utils.Utility import Input, Color, Center, Font, crypto
from Core.Data_fetcher import fetch_current_price, fetch_historical_prices, Global_market
from Core.Processor import analyze_signal
from Core.Report import Output

#Global_val

time_list = [
    "1 day",
    "7 days",
    "30 days",
    ]


print(Center.box(Center.text("CRYPTO SIGNAL ANALYZER")))

def Main():
      while True:
          """
          Enter your API key down here ↓
          """
          CAK = crypto.ApiKey("CG-7qQZF5SzkFCZhcbXg9wAUvAv")
          """
          ----------------------
          """
          CRYPTO_LIST = crypto.CL()
          print(Font.Bold("=====MENU====="))
          print("1.Crypto")
          print("2.keluar\n")
          cmd = input("Pilih menu: ").strip().capitalize()
          if cmd in ["1","Crypto"]:
        
              print("\n=====CRYPTO=MENU=====")
              print("1.Lihat harga")
              print("2.Buat saran keputusan\n")
            
              submenu = input("Pilih Submenu: ").strip()
              if submenu in ["1"]:
                  Output.list_crypto(CRYPTO_LIST)
                  while True:
                      choice = int(Input.number("\nPilih Crypto (1-4): "))
                      if choice == 909:
                          break
                      coin_id = CRYPTO_LIST[choice - 1]
                
                      current_price = fetch_current_price(coin_id, CAK)
                      Output.report_info(coin_id,current_price)

                      data = Global_market()
                      cap = data["market_cap"]
                      vol = data["volume"]
                      Output.global_val(cap, vol)

              elif submenu in ["2"]:
              
                  Output.list_crypto(CRYPTO_LIST)
                  choice = int(Input.number("\nPilih Crypto (1-4): "))
                  coin_id = CRYPTO_LIST[choice - 1]
                  
                  for i, TM in enumerate(time_list, 1):
                      print(f"{i}. {TM}")

                  chtimes = int(Input.number("\nPilih waktu: "))
                  times = time_list[chtimes - 1]
  
  
                  avg_price = float(input("Masukan saat beli: "))
              
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
          elif cmd in ["2","Keluar"]:
              print(Color.Blue(Center.text("Program selesai")))
              break
          
          else:
              print(Color.Red(Center.text(f"There's no menu name {cmd}\n")))

if __name__ == '__main__':
    Main()