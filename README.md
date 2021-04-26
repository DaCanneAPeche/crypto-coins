# crypto-coins

A simple python lib for get info about crypto-moneys, using the `https://coincap.io/` API.

# functions :

`get_top_list()` :
return the more expensive crypto-moneys, in order

````python
from crypto-coins import get_top_list

print(get_top_list())

````

result :

````python
>> ['bitcoin', 'ethereum', 'binance-coin', 'xrp', 'tether', 'cardano', 'dogecoin', 'polkadot', 'uniswap', 'litecoin', 'bitcoin-cash', 'chainlink', 'solana', 'usd-coin', 'theta', 'stellar', 'filecoin', 'wrapped-bitcoin', 'binance-usd', 'monero', 'terra-luna', 'neo', 'iota', 'eos', 'cosmos', 'aave', 'bitcoin-sv', 'crypto-com-coin', 'bittorrent', 'maker', 'tezos', 'multi-collateral-dai', 'algorand', 'huobi-token', 'compound', 'kusama', 'thorchain', 'elrond-egld', 'dash', 'nem', 'decred', 'zcash', 'matic-network', 'chiliz', 'hedera-hashgraph', 'enjin-coin', 'decentraland', 'zilliqa', 'synthetix-network-token', 'digibyte', 'basic-attention-token', 'siacoin', 'theta-fuel', 'yearn-finance', 'uma', 'sushiswap', 'waves', 'blockstack', 'horizen', 'qtum', 'ontology', 'icon', 'celo', 'harmony', '0x', 'bancor', 'swissborg', 'reserve-rights', 'xinfin-network', 'ankr', 'omg', 'kucoin-shares', 'fantom', 'dent', 'iostoken', 'ren', 'verge', 'bitmax-token', 'vethor-token', 'livepeer', 'loopring', 'lisk', 'kyber-network', 'nervos-network', 'origin-protocol', 'storj', 'ocean-protocol', 'nxm', 'maidsafecoin', 'augur', 'golem-network-tokens', 'electroneum', 'iotex', 'wink-tronbet', 'nkn', 'ardor', 'trustswap', 'fetch', 'singularitynet', 'aragon']
````

the `index 0` is the more expensive crypto-money, and the `index 1` the second, etc.

`get_money_by_rank(rank=1)` :
return the money who has the rank number (ex : bitcoin = 1)

````python
from crypto-coins import get_money_by_rank

print(get_money_by_rank(3))
````

result :

````python
>> binance-coin
````

`get_rank_by_money(money='bitcoin)`:
return the rank of a money

```python
from crypto-coins import get_rank_by_money

print(get_rank_by_money('stellar'))

```

result :

````python
>> 16
````
