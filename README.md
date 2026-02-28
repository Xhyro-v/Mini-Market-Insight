# MarketInsight
MarketInsight is a project that helps users decide whether to buy, hold, or sell their crypto assets based on profit or loss calculations derived from the average purchase price compared to current market prices.
This project focuses on simple market analysis and decision-making logic using real-time crypto price data.

--

## Project Structure
MarketInsight/
  │
  ├── Core/
  │   ├── Data_fetcher.py
  │   ├── Input.py
  │   ├── Processor.py
  │   └── Report.py
  │
  ├── Storage/
  │   ├── Data.json
  │   └── Database.py
  │
  ├── Utils/
  │   └── Utility.py
  │
  ├── main.py
  ├── README.md
  └── requirement.txt
  
--

## Tech Stack 
- Python
- NumPy
- REST API (Crypto API)
- JSON Storage

--

## How It Works
1.The system fetches real-time crypto price data and user-input purchase data
2.The system generates a report along with a suggested decision (buy / hold / sell)
3.The system processes and analyzes the data

--

##Instalation
```bash
pip install -r requirement.txt
```
### Run program
```md
```bash
python main.py
```

--

## How to Use
1.Users must register at Coingecko.com to obtain an API key for real-time price data,After that, insert the API keyby replacing the value of 'COINGECKO_API_KEY ='

2.Run the program using the following command inside the MarketInsight folder:

```python main.py'```

3.The user selects the instrument (currently only crypto is supported)

4.The user selects the trading timeframe (1 / 7 / 30 days)

5.The system generates a report and provides a decision based on the analysis

--

## Data & Sources
•Instrument: Cryptocurrency
•Data source: Coingecko API
•Analysis is based on:
   -Real-time market price
   -User’s average purchase price

--