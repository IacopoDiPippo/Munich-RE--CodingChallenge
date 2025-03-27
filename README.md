# Munich RE –Coding Challenge

# Eliza Blockchain Chatbot

A conversational agent that combines:
- Classic Eliza therapist chatbot functionality
- Ethereum blockchain transactions (Sepolia testnet)
- Hugging Face LLM for natural language processing

## Features
- Send ETH transactions via natural language commands
- Therapeutic conversation mode
- Secure testnet environment

## Environment Setup

### Prerequisites
- **Python**: 3.8+
- **Node.js**: Not required (pure Python implementation)
- **Ethereum Wallet**: MetaMask with Sepolia testnet configured

### Dependency Versions
| Package | Version |
|---------|---------|
| web3.py | 5.31.3 |
| transformers | 4.28.1 |
| torch | 2.0.1 |
| python-dotenv | 0.21.0 |
| eth-utils | 2.0.0 |

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/eliza-blockchain.git
   cd eliza-blockchain
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create `.env` file:
   ```ini
   ALCHEMY_API_KEY="your_alchemy_key"
   PRIVATE_KEY="your_metamask_private_key"
   ```

## Usage

### Running the Chatbot
```bash
python eliza.py
```

### Example Commands
1. **Blockchain Mode**:
   ```
   send 0.001 ETH to 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
   ```

2. **Therapist Mode**:
   ```
   I feel anxious about my job
   ```

## Project Structure
```
eliza-blockchain/
├── .env.example
├── requirements.txt
├── eliza.py               # Main chatbot logic
├── blockchain.py          # Ethereum transaction handler
└── README.md
```

## Configuration

### Getting API Keys
1. **Alchemy**:
   - Create account at [alchemy.com](https://www.alchemy.com/)
   - Create Sepolia testnet app
   - Copy HTTPS API key

2. **Test ETH**:
   - Get Sepolia ETH from [faucet](https://sepoliafaucet.com)


### Key Components Explained:

1. **Blockchain Integration**:
   - Handles ETH transactions on Sepolia testnet
   - Requires Alchemy API key and testnet ETH

2. **Chatbot Modes**:
   - Transaction mode: Processes ETH transfer requests
   - Therapist mode: Provides psychological responses

3. **Safety Notes**:
   - Never commit `.env` to version control
   - Use only testnet private keys

4. **Version Control**:
   - Explicit version locking for stability
   - Tested with Python 3.8-3.10

To use this README:
1. Save as `README.md` in your project root
2. Update the repository URL
3. Customize the example commands if needed

The document provides clear setup instructions while maintaining security best practices for blockchain development.
