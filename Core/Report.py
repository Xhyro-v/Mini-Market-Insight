from Utils.Utility import Color, Center, Font

class Output:
    @staticmethod
    def report(coin, current, avg, signal, diff,times) -> None:
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
