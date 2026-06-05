import requests

def get_token_price(chain, token_address):
    url = f"https://coins.llama.fi/prices/current/{chain}:{token_address}"
    try:
        response = requests.get(url).json()
        return response['coins'][f"{chain}:{token_address}"]['price']
    except:
        return None

tokens = {
    "ethereum": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    "polygon": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    "arbitrum": "0xaf88d065e77c8cc2239327c5edb3a432268e5831",
    "optimism": "0x0b2c639c533813f4aa9d7837caf62653d097ff85",
    "bsc": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
    "solana": "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v",
    "sui": "0xdba34672e30cb065b1f93e3ab55318768fd6f066bc5a234f95f088190760451e::usdc::USDC",
    "sei": "factory/sei1cnas20js8p84q0y46m7v2z0z99q9g4h574l2s2/usdc",
    "aptos": "0xf22bede237a07e121b56d91a491eb7bcdfd1f5907926a9e58338f964a01b17fa::asset::USDC",
    "mantle": "0x09bc4e0d864854c6a3fbca91e578388437ede3b8"
}

print("--- Cross-Chain Arbitrage Finder (Extended) ---")

price_list = {}
for chain, address in tokens.items():
    price = get_token_price(chain, address)
    if price:
        price_list[chain] = price
        print(f"{chain.capitalize():<10} : ${price:.4f}")

if price_list:
    min_chain = min(price_list, key=price_list.get)
    max_chain = max(price_list, key=price_list.get)
    
    print("-" * 30)
    print(f"Lowest Price : ${price_list[min_chain]:.4f} ({min_chain.capitalize()})")
    print(f"Highest Price: ${price_list[max_chain]:.4f} ({max_chain.capitalize()})")
    print(f"Potential Spread : ${price_list[max_chain] - price_list[min_chain]:.4f}")
else:
    print("Could not fetch data for any network.")
