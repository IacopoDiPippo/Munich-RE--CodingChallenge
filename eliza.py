import re
from transformers import pipeline
from blockchain import BlockchainHandler
from dotenv import load_dotenv
import os

load_dotenv()

class Eliza:
    def __init__(self):
        self.blockchain = BlockchainHandler()
        
        # Initialize LLM with proper settings
        self.llm = pipeline(
            "text-generation",
            model="distilgpt2",
            device=-1,  # Use CPU
            pad_token_id=50256  # Explicitly set pad token
        )
    
    def respond(self, text):
        # Check for ETH transfer pattern (strict format)
        tx_match = re.match(
            r"(?i)^send\s+(\d+\.?\d*)\s+ETH\s+to\s+(0x[a-fA-F0-9]{40})$", 
            text.strip()
        )
        
        if tx_match:
            try:
                amount = float(tx_match.group(1))
                recipient = tx_match.group(2)
                
                tx_hash = self.blockchain.send_transaction(
                    recipient=recipient,
                    amount_eth=amount
                )
                return f"✅ Sent {amount} ETH! Track: https://sepolia.etherscan.io/tx/{tx_hash}"
            except Exception as e:
                return f"❌ Transaction failed: {str(e)}"
        
        # LLM response for all other inputs
        try:
            response = self.llm(
                f"""The following is a conversation with Eliza, a Rogerian therapist.
                User: {text}
                Eliza:""",
                max_length=100,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                num_return_sequences=1
            )
            # Clean up the response
            full_text = response[0]['generated_text']
            eliza_response = full_text.split("Eliza:")[-1].strip()
            return eliza_response.split('\n')[0]
        except Exception as e:
            return f"I'm having trouble responding. ({str(e)})"

if __name__ == "__main__":
    eliza = Eliza()
    print("Eliza: Hello! I can help with ETH transfers or chat.")
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                break
            print("Eliza:", eliza.respond(user_input))
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break