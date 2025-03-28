from transformers import pipeline
from blockchain import BlockchainHandler
from dotenv import load_dotenv
import re
import os

# Disable symlink warnings for HuggingFace cache
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'
load_dotenv()

class Eliza:
    def __init__(self):
        # Initialize blockchain handler with error checking
        try:
            self.blockchain = BlockchainHandler()
        except Exception as e:
            print(f"⚠️ Blockchain initialization failed: {str(e)}")
            self.blockchain = None
        
        # Initialize smaller LLM model with better configuration
        try:
            self.llm = pipeline(
                "text-generation",
                model="EleutherAI/gpt-neo-125M",  # Smaller and faster model
                device=-1,
                torch_dtype='auto',
                pad_token_id=50256
            )
        except Exception as e:
            print(f"⚠️ LLM initialization failed: {str(e)}")
            self.llm = None

    def respond(self, text):
        # Handle greetings first
        if text.lower().strip() in ['hi', 'hello', 'hey']:
            return "Hello! How can I assist you today?"
            
        # Handle transaction requests
        if self._is_transaction_request(text):
            if self.blockchain is None:
                return "⚠️ Blockchain service is currently unavailable"
            return self._handle_transaction(text)
            
        # Handle all other queries with LLM
        if self.llm is None:
            return "⚠️ I'm having trouble processing requests right now"
        return self._generate_response(text)

    def _is_transaction_request(self, text):
        # More flexible transaction detection
        return bool(re.match(
            r"(?i)(?:send|transfer)\s+(\d+\.?\d*)\s*(?:ETH|ether)?\s*(?:to)?\s*(0x[a-fA-F0-9]{40})", 
            text.strip()
        ))

    def _handle_transaction(self, text):
        try:
            match = re.match(
                r"(?i)(?:send|transfer)\s+(\d+\.?\d*)\s*(?:ETH|ether)?\s*(?:to)?\s*(0x[a-fA-F0-9]{40})",
                text.strip()
            )
            if not match:
                return "Please format your request as: 'Send X ETH to 0x...'"
                
            amount = float(match.group(1))
            if amount <= 0:
                return "❌ Amount must be positive"
                
            tx_hash = self.blockchain.send_transaction(
                recipient=match.group(2),
                amount_eth=amount
            )
            return f"✅ Sent {amount} ETH! Track: https://sepolia.etherscan.io/tx/{tx_hash}"
        except ValueError as e:
            return f"❌ Invalid input: {str(e)}"
        except Exception as e:
            return f"❌ Transaction failed: {str(e)}"

    def _generate_response(self, text):
        try:
            # Better prompt structure
            prompt = f"""The following is a question the User asks to an AI assistant.
    The assistant is helpful, concise, and responds in complete sentences. Complete the answer of the assistant.

    User: {text}
    Assistant:"""
            
            response = self.llm(
                prompt,
                max_new_tokens=30,  # Increased length
                temperature=0.7,
                do_sample=True,
                no_repeat_ngram_size=2,  # Prevents repetition
                early_stopping=True,
                eos_token_id=self.llm.tokenizer.eos_token_id
            )
            
            # Cleaner response extraction
            full_response = response[0]['generated_text']
            assistant_part = full_response.split("Assistant:")[-1]
            return assistant_part.split("User:")[0].strip()
        except Exception as e:
            return f"I'm having trouble responding right now. ({str(e)})"

if __name__ == "__main__":
    print("Initializing Eliza...")
    eliza = Eliza()
    print("AI: Hello! How can I help you today? (Type 'quit' to exit)")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["quit", "exit"]:
                break
            print("AI:", eliza.respond(user_input))
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break