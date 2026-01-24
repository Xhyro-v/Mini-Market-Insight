class Color:
    def Black(teks):
      return f"\033[30m{teks}\033[0m"
    def Red(teks): 
      return f"\033[31m{teks}\033[0m"
    def Green(teks):
      return f"\033[32m{teks}\033[0m"
    def Yellow(teks):
      return f"\033[33m{teks}\033[0m"
    def Blue(teks): 
      return f"\033[34m{teks}\033[0m"
    def Magenta(teks):
      return f"\033[35m{teks}\033[0m"
    def Cyan(teks):
      return f"\033[36m{teks}\033[0m"
    def White(teks): 
      return f"\033[37m{teks}\033[0m"
    def BrightBlack(teks): 
      return f"\033[90m{teks}\033[0m"
    def BrightRed(teks): 
      return f"\033[91m{teks}\033[0m"
    def BrightGreen(teks): 
      return f"\033[92m{teks}\033[0m"
    def BrightYellow(teks): 
      return f"\033[93m{teks}\033[0m"
    def BrightBlue(teks):
      return f"\033[94m{teks}\033[0m"
    def BrightMagenta(teks): 
      return f"\033[95m{teks}\033[0m"
    def BrightCyan(teks):
      return f"\033[96m{teks}\033[0m"
    def BrightWhite(teks):
      return f"\033[97m{teks}\033[0m"

class Backcol:
    def Black(teks):
      return f"\033[40m{teks}\033[0m"
    def Red(teks):
      return f"\033[41m{teks}\033[0m"
    def Green(teks): 
      return f"\033[42m{teks}\033[0m"
    def Yellow(teks): 
      return f"\033[43m{teks}\033[0m"
    def Blue(teks):
      return f"\033[44m{teks}\033[0m"
    def Magenta(teks):
      return f"\033[45m{teks}\033[0m"
    def Cyan(teks): 
      return f"\033[46m{teks}\033[0m"
    def White(teks): 
      return f"\033[47m{teks}\033[0m"
    def BrightBlack(teks): 
      return f"\033[100m{teks}\033[0m"
    def BrightRed(teks):
      return f"\033[101m{teks}\033[0m"
    def BrightGreen(teks):
      return f"\033[102m{teks}\033[0m"
    def BrightYellow(teks): 
      return f"\033[103m{teks}\033[0m"
    def BrightBlue(teks): 
      return f"\033[104m{teks}\033[0m"
    def BrightMagenta(teks):
      return f"\033[105m{teks}\033[0m"
    def BrightCyan(teks):
      return f"\033[106m{teks}\033[0m"
    def BrightWhite(teks):
      return f"\033[107m{teks}\033[0m"

class Font:
    def Bold(teks):
      return f"\033[1m{teks}\033[0m"
    def Dim(teks): 
      return f"\033[2m{teks}\033[0m"
    def Italic(teks): 
      return f"\033[3m{teks}\033[0m"
    def Underline(teks): 
      return f"\033[4m{teks}\033[0m"
    def Blink(teks): 
      return f"\033[5m{teks}\033[0m"
    def Inverse(teks): 
      return f"\033[7m{teks}\033[0m"
    def Hidden(teks): 
      return f"\033[8m{teks}\033[0m"
    def Strike(teks): 
      return f"\033[9m{teks}\033[0m"

class Center:
    def box(text: str, padding=2):
      import shutil
      width = shutil.get_terminal_size().columns
  
      content = " " * padding + text + " " * padding
      line = content.center(width, "=")
  
      return line
    def text(text: str) -> str:
        import shutil
        width = shutil.get_terminal_size().columns
        return text.center(width)

class Input:
    def letter(prompt: str) -> str:
      while True:
          text = input(prompt).strip()
  
          if not text:
              print(Font.Bold(Center.text(Color.Red("Tidak boleh kosong\n"))))
              continue
  
          if len(text) > 30:
              print(Color.Red(Font.Bold(Center.text("Maksimal 30 huruf\n"))))
              continue
  
          valid = True
          for karakter in text:
              if not (karakter.isalpha() or karakter.isspace()):
                  valid = False
                  break
          
          if valid:
              return text
          else:
              print(Color.Red(Font.Bold(Center.text("Hanya huruf\n"))))
    def number(prompt: str) -> str:
      while True:
          text = input(prompt).strip()
  
          if not text:
              print(Color.Red(Font.Bold(Center.text("Tidak boleh kosong\n"))))
              continue
  
          if len(text) > 20:
              print(Color.Red(Font.Bold(Center.text("Maksimal 20 angka\n"))))
              continue
  
          valid = True
          for karakter in text:
              if not (karakter.isdigit() or karakter.isspace()):
                  valid = False
                  break
          
          if valid:
              return text
          else:
              print(Color.Red(Font.Bold(Center.text("Hanya angka!\n"))))

class JKit:
    def load_json(file):
          import json
          with open(file, "r") as f:
              return json.load(f)
    def save_json(file, data):
          import json
          with open(file, "w") as f:
              json.dump(data, f, indent=2)

class crypto:
    def ApiKey(API_KEY) -> str:
        COINGECKO_API_KEY = API_KEY
        return (str(COINGECKO_API_KEY))

    def CL():
        LIST = [
        "bitcoin",
        "ethereum",
        "tether",
        "binancecoin",
        "XRP",
        "solana",
        "dogecoin",
        "cardano",
        "shibainu",
        "litecoin",
        "bitcoincash",
        "stellar",
        "chainlink",
        "polkadot",
        "uniswap",
        "tron",
        "avalanche",
        "monero",
        "cosmos",
        "eos"
          ]
        return LIST
        
    def url():
        BASE_URL = "https://api.coingecko.com/api/v3/"
        return BASE_URL

    def global_url():
        GB_URL = "https://api.coingecko.com/api/v3/global"
        return GB_URL