import cryptocompare
def analise(cripto):
    coin_name = cripto.upper()
    crypto_data = cryptocompare.get_price(coin=cripto,currency="USD",full=True)['RAW'][coin_name]['USD']
    return crypto_data