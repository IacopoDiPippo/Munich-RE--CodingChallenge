# Munich RE –Coding Challenge

# Eliza Blockchain Chatbot

A conversational agent that combines:
- Ethereum blockchain transactions (Sepolia testnet)
- Hugging Face LLM for natural language processing

## Features
- Send ETH transactions via natural language commands
- Therapeutic conversation mode
- Secure testnet environment

## Environment Setup

### Prerequisites
- **Python**: 3.9
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
   conda create -n eliza python=3.9
   conda activate eliza
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create `.env` file:
   ```ini
   ALCHEMY_API_KEY=your_alchemy_key
   PRIVATE_KEY=your_metamask_private_key
   HUGGINGFACE_API_KEY=your_huggingface_api_key
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

2. **Chat Mode**:
   ```
   Is a paper white? 
   YEs
   You: Is a tree a plant?
   AI: Yes, it is.
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
   - Chat mode: Can respond to simple questions

###NOTE:
##The model used for chatting is a little model from hugging face due to local computational power, therefor the response it may give might be strange.
The best way to use this model is by asking little questions.
Also due to time constraints I capped the response to a fixed length, so there might be more text generate that should be not considered.
