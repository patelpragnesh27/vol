from flask import Flask, render_template, jsonify
import yfinance as yf
import pandas as pd

app = Flask(__name__)

# Fetch and process the data
def get_top_volumes():
    nse_stocks = ["EPL.NS",
"CHENNPETRO.NS",
"PAYTM.NS",
"POLICYBZR.NS",
"EQUITASBNK.NS"
]  # Replace with your NSE tickers
    period = '6mo'
    top_volumes_dict = {i: [] for i in range(1, 6)}

    for stock in nse_stocks:
        try:
            data = yf.download(stock, period=period)
            data_sorted = data.sort_values(by='Volume', ascending=False)

            for i in range(1, 6):
                if len(data_sorted) >= i:
                    row = data_sorted.iloc[i-1]
                    top_volumes_dict[i].append({
                        'Date': row.name.strftime('%Y-%m-%d'),
                        'Stock': stock.replace('.NS', ''),
                        'Volume': row['Volume']
                    })
        except Exception as e:
            print(f"Failed to download data for {stock}: {e}")

    return top_volumes_dict

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data/<int:level>')
def data(level):
    top_volumes_dict = get_top_volumes()
    return jsonify(top_volumes_dict.get(level, []))

if __name__ == '__main__':
    app.run(debug=True)
