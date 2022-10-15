import bdkpython as bdk


descriptor = "wpkh(tprv8ZgxMBicQKsPcx5nBGsR63Pe8KnRUqmbJNENAfGftF3yuXoMMoVJJcYeUw5eVkm9WBPjWYt6HMWYJNesB5HaNVBaFc1M6dRjWSYnmewUMYy/84h/0h/0h/0/*)"
db_config = bdk.DatabaseConfig.MEMORY()
blockchain_config = bdk.BlockchainConfig.CBF(
    bdk.CbfConfig(
        bdk.Network.TESTNET,
        None
    )
)
blockchain = bdk.Blockchain(blockchain_config)

wallet = bdk.Wallet(
    descriptor=descriptor,
    change_descriptor=None,
    network=bdk.Network.TESTNET,
    database_config=db_config,
)

class LogProgress(bdk.Progress): 
    def update(self, progress, message):
        print(f"Chain sync is in progress: {progress}, {message}")

# print new receive address
address_info = wallet.get_address(bdk.AddressIndex.LAST_UNUSED)
address = address_info.address
index = address_info.index
print(f"New BIP84 testnet address: {address} at index {index}")

# print wallet balance
progress = LogProgress()
wallet.sync(blockchain, progress)
balance = wallet.get_balance()
print(f"Wallet balance is: {balance.total}")
