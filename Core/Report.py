from Utils.Utility import Color, Center, Font

class Output:
    @staticmethod
    def report_decc(coin, current, avg, signal, diff,times) -> None:
        print("\n" + Center.box("CRYPTO REPORT"))

        print(f"{Font.Bold('Crypto')}         : {coin}")
        print(f"{Font.Bold('Current Price')}  : {Color.Green('$')}{Color.Green(f'{current:,.2f}')}")
        print(f"{Font.Bold(f'Avg {times}')}        : ${avg:,.2f}")
        print(f"{Font.Bold('Insight')}        : {signal}")

        if diff >= 0:
            diff_text = Color.Green(f"+{diff:.2f}%")
        else:
            diff_text = Color.Red(f"{diff:.2f}%")

        print(f"{Font.Bold('Difference')}     : {diff_text}")
        print(Center.box(""))
    
    def report_info(coin,current):
        print("\n" + Center.box("CRYPTO INFO"))
        print(f"{Font.Bold('Crypto')}         : {coin}")
        print(f"{Font.Bold('Current Price')}  : {Color.Green('$')}{Color.Green(f'{current:,.2f}')}")
        print(Center.box(""))
        print("")
    
    def list_crypto(CRYPTO_LIST):
        print(" ")
        print(Center.box("CRYPTO LIST"))
        for i, coin in enumerate(CRYPTO_LIST, 1):
            print(f"{i}. {coin}")
        print(Center.box(""))
        print("")
    
    def global_val(cap, vol):
        print("")
        print(Center.box("Global Market"))
        print(f"Total Market Cap: ${Color.Green(f'{cap:,.0f}')}")
        print(f"Total Volume: ${Color.Green(f'{vol:,.0f}')}")
        print(Center.box(""))
        print("")
