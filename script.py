import requests


def cotar():
    url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/365"
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()
    return [float(d["bid"]) for d in dados]


if __name__ == "__main__":
    print(cotar())
