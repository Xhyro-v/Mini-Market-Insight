from Utils.Utility import crypto ,crypto_LIST, Color ,Center
from Storage.Database import Database


class WatchlistManager:
    MAX_COINS = 20

    def __init__(self):
        self.db = Database("Watchlist")
        self.available_coins = crypto_LIST

    # =============================
    # CREATE
    # =============================
    def create_watchlist(self, name):
        if self.db.get(name):
            print(Color.Yellow(Center.text("Watchlist sudah ada")))
            return

        self.db.insert(name, {"coins": []})
        print(Color.Green(Center.text(f"Watchlist '{name}' telah dibuat")))

    # =============================
    # SHOW
    # =============================
    def show_watchlists(self):
        if not self.db.data:
            print(Color.Yellow(Center.text("Watchlist tidak ada/kosong")))
            return

        for name, data in self.db.data.items():
            print(f"\n📁 {name} ({len(data['coins'])}/{self.MAX_COINS})")
            for coin in data["coins"]:
                print(f"   - {coin}")

    def show_watchlist(self, name):
        watchlist = self.db.get(name)

        if not watchlist:
            print(Color.Red(Center.text("Watchlist tidak ada/kosong!")))
            return

        print(f"\n📁 {name} ({len(watchlist['coins'])}/{self.MAX_COINS})")
        for coin in watchlist["coins"]:
            print(f"   - {coin}")

    # =============================
    # ADD MULTIPLE COINS
    # =============================
    def add_coins(self, name, inputs: list):
        watchlist = self.db.get(name)
    
        if not watchlist:
            print(Color.Red(Center.text("Watchlist tidak ada/kosong!")))
            return
    
        selected_coins = []
    
        for item in inputs:
            item = item.strip()
    
            # Kalau angka
            if item.isdigit():
                index = int(item) - 1
                if 0 <= index < len(crypto_LIST):
                    selected_coins.append(crypto_LIST[index].lower())
                else:
                    print(Color.Yellow(Center.text(f"Invalid number: {item}")))
                    return
            else:
                # Kalau nama crypto
                coin = item.lower()
                if coin in [c.lower() for c in crypto_LIST]:
                    selected_coins.append(coin)
                else:
                    print(Color.Yellow(Center.text(f"Invalid coin name: {item}")))
                    return
    
        # Hindari duplikat
        selected_coins = list(set(selected_coins))
    
        new_coins = [c for c in selected_coins if c not in watchlist["coins"]]
    
        if len(watchlist["coins"]) + len(new_coins) > self.MAX_COINS:
            print(Color.Red(Center.text("Cannot exceed 20 coins in one watchlist.")))
            return
    
        watchlist["coins"].extend(new_coins)
        self.db._save()
        print(Color.Green(Center.text("Koin berhasil ditambahkann")))

    # =============================
    # DELETE COIN
    # =============================
    def delete_coins(self, name: str, coins: list[str]) -> dict:
        watchlist = self.db.get(name)
    
        if not watchlist:
            print(Color.Red(Center.text("Watchlist tidak ada/kosong!")))
    
        coins = [c.lower() for c in coins]
        existing = watchlist.get("coins", [])
    
        removed = [c for c in coins if c in existing]
        not_found = [c for c in coins if c not in existing]
    
        if removed:
            watchlist["coins"] = [c for c in existing if c not in removed]
            self.db._save()
    
        return {
            "status": "success",
            "removed": removed,
            "not_found": not_found
        }
    # =============================
    # DELETE WATCHLIST
    # =============================
    def delete_watchlist(self, name):
        if not self.db.get(name):
            print(Color.Red(Center.text("Watchlist tidak ada/kosong!")))
            return

        del self.db.data[name]
        self.db._save()

        print(Color.Green(Center.text(f"Watchlist '{name}' telah dihapus.")))

    # =============================
    # EDIT WATCHLIST NAME
    # =============================
    def rename_watchlist(self, old_name, new_name):
        watchlist = self.db.get(old_name)

        if not watchlist:
            print(Color.Red(Center.text("Watchlist tidak ada/kosong!")))
            return

        if self.db.get(new_name):
            print(Color.Red(Center.text("Watchlist sudah ada!")))
            return

        self.db.data[new_name] = self.db.data.pop(old_name)
        self.db._save()

        print(Color.Green(Center.text(f"Watchlist telah diganti menjadi :'{new_name}'.")))

    # =============================
    # REPLACE ALL COINS (EDIT CONTENT)
    # =============================
    def replace_coin(self, name, index, new_coin):
        watchlist = self.db.get(name)
    
        if not watchlist:
            print(Color.Red(Center.text("Watchlist tidak ada/kosong!")))
            return
      
    
        coins = watchlist["coins"]
    
        if new_coin in coins:
            print(Color.Yellow(Center.text("Koin sudah ada di dalam watchlist!")))
            return
    
        if index < 0 or index >= len(coins):
            print(Color.Yellow(Center.text("Invalid selection")))
            return
    
        new_coin = new_coin.lower()
    
        if new_coin not in self.available_coins:
            print(Color.Yellow(Center.text("Invalid coin.")))
            return
    
        coins[index] = new_coin
        self.db._save()
    
        print(Color.Green(Center.text("Koin berhasil diganti!")))


if __name__ == '__main__':
    manager = WatchlistManager()

    manager.create_watchlist("Long Term")
    
    manager.add_coins("Long Term", [
        "bitcoin",
        "ethereum",
        "solana"
    ])
    
    manager.show_watchlist("Long Term")
    
    manager.delete_coin("Long Term", "solana")
    
    manager.rename_watchlist("Long Term", "Holdings")
    
    manager.replace_coins("Holdings", [
        "bitcoin",
        "cardano"
    ])
    
    manager.show_watchlists()