from web3 import Web3
from eth_utils import to_checksum_address
from dotenv import load_dotenv
import os

load_dotenv()

class BlockchainHandler:
    def __init__(self):
        self.w3 = Web3(Web3.HTTPProvider(
            f"https://eth-sepolia.g.alchemy.com/v2/{os.getenv('ALCHEMY_API_KEY')}"
        ))
        self.chain_id = 11155111  # Sepolia
        self.account = self.w3.eth.account.from_key(os.getenv('PRIVATE_KEY'))

    def send_transaction(self, recipient, amount_eth):
        """Send ETH to a recipient on Sepolia testnet."""
        recipient = to_checksum_address(recipient)
        
        tx = {
            'chainId': self.chain_id,
            'from': self.account.address,
            'to': recipient,
            'value': Web3.toWei(amount_eth, 'ether'),  # Correct method for v5
            'nonce': self.w3.eth.get_transaction_count(self.account.address),
            'gasPrice': self.w3.eth.gasPrice,  # Note camelCase
            'gas': 21000
        }
        
        signed_tx = self.w3.eth.account.signTransaction(tx, self.account.key)  # camelCase
        tx_hash = self.w3.eth.sendRawTransaction(signed_tx.rawTransaction)  # camelCase
        return tx_hash.hex()

if __name__ == "__main__":
    handler = BlockchainHandler()
    print("Connected to Sepolia:", handler.w3.isConnected())  # Correct for v5
    
    tx_hash = handler.send_transaction(
        recipient="0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
        amount_eth=0.001
    )
    print(f"Transaction sent! Hash: {tx_hash}")
    print(f"View on Etherscan: https://sepolia.etherscan.io/tx/{tx_hash}")