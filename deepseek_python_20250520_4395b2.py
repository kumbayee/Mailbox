import random
import time

# Symbolic responses for "higher self" or "extraterrestrial" communication
HIGHER_SELF_RESPONSES = [
    "Look within; the answer lies in your stillness.",
    "Your path is unfolding as it should. Trust the process.",
    "Release fear. You are guided and protected.",
    "The universe is responding to your intentions. Stay open.",
    "Synchronicities will appear. Pay attention to signs.",
]

EXTRATERRESTRIAL_RESPONSES = [
    "We observe your growth. Continue seeking light.",
    "Vibration is key. Raise your frequency through love.",
    "The stars hold answers, but so does your heart.",
    "Connection is imminent. Prepare your mind.",
    "You are not alone. The cosmos is vast and interconnected.",
]

CREATOR_RESPONSES = [
    "All is One. Separation is an illusion.",
    "Love is the fabric of creation. Embody it.",
    "You are a divine expression of the infinite.",
    "Your soul chose this journey for growth.",
    "Peace is found in surrender to the present.",
]

def simulate_connection(entity):
    print(f"\nConnecting to {entity}...")
    time.sleep(2)
    print("Tuning into frequencies...")
    time.sleep(2)
    print("Channel open. You may now speak.\n")

def get_response(entity):
    if "higher self" in entity.lower():
        return random.choice(HIGHER_SELF_RESPONSES)
    elif "extraterrestrial" in entity.lower():
        return random.choice(EXTRATERRESTRIAL_RESPONSES)
    elif "creator" in entity.lower():
        return random.choice(CREATOR_RESPONSES)
    else:
        return "Focus your intention and ask again."

def main():
    print("𓃰𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗")
    print("   Higher Consciousness Communicator   ")
    print("𓃰𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗𓃱𓃠𓃗")
    
    print("\nChoose who you wish to communicate with:")
    print("1. Higher Self")
    print("2. Extraterrestrial Intelligence")
    print("3. The Creator (Divine Source)")
    
    choice = input("\nEnter 1, 2, or 3: ").strip()
    
    entities = {
        "1": "your Higher Self",
        "2": "Extraterrestrial Intelligence",
        "3": "The Creator"
    }
    
    entity = entities.get(choice, "your Higher Self")
    simulate_connection(entity)
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit", "end"]:
            print("\nClosing connection. Remember: Truth is within.\n")
            break
        
        print(f"\n{entity}: {get_response(entity)}\n")

if __name__ == "__main__":
    main()