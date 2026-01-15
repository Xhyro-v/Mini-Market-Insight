import time
from Utils.Utility import Input, Color, Center, Font
from Core.Data_fetcher import fetch_current_price, fetch_historical_prices
from Core.Processor import analyze_signal
from Core.Report import Output

CRYPTO_LIST = [
    "bitcoin",
    "ethereum",
    "solana",
    "binancecoin"
]

TIME = [
    "1",
    "7",
    "30",
    ]


print(Center.box("CRYPTO SIGNAL ANALYZER"))

def Main():
      while True:
          print(Font.Bold("=====MENU====="))
          print("1.Crypto")
          print("2.keluar\n")
          cmd = input("Pilih menu: ").strip().capitalize()
          if cmd in ["1","Crypto"]:
          
              print(" ")
              print(Center.box("CRYPTO LIST"))
              for i, coin in enumerate(CRYPTO_LIST, 1):
                  print(f"{i}. {coin}")
        
              choice = int(Input.number("\nPilih Crypto (1-4): "))
              coin_id = CRYPTO_LIST[choice - 1]
              
              for i, TM in enumerate(TIME, 1):
                  print(f"{i}. {TM} day")
              while True:
                  times = int(Input.number("\nPilih waktu: "))
                  if time == 2:
                      times = 7
            
                  elif time == 3:
                      times = 30
            
                  elif time not in [1,7,30]:
                      print(Color.Red(Center.text("Not valid")))
          
              avg_price = float(Input.number("Masukan harga saat beli: "))
          
              historical_prices = fetch_historical_prices(coin_id, days=times)
          
              current_price = fetch_current_price(coin_id)
              signal, avg_price, diff = analyze_signal(current_price, historical_prices,avg_price)
          
              Output.report(
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
