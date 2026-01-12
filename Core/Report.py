from Utils.Utility import Color, Center, Font

class Output:
    @staticmethod
    def report(coin, current, avg, signal, diff):
        print("\n" + Center.box("CRYPTO REPORT"))

        print(f"{Font.Bold('Crypto')}        : {coin}")
        print(f"{Font.Bold('Current Price')} : {Color.Green('$')}{Color.Green(f'{current:,.2f}')}")
        print(f"{Font.Bold('Avg (30D)')}     : ${avg:,.2f}")
        print(f"{Font.Bold('Signal')}        : {signal}")

        if diff >= 0:
            diff_text = Color.Green(f"+{diff:.2f}%")
        else:
            diff_text = Color.Red(f"{diff:.2f}%")

        print(f"{Font.Bold('Difference')}    : {diff_text}")
        print(Center.box(""))
