import openai
import serial
import time
import pyttsx3
import threading

# === CONFIGURATION ===
client = openai.OpenAI(api_key="your open ai api key")  #<<need a openai api key
SERIAL_PORT = "/dev/cu.usbmodem11201"
BAUD_RATE = 9600
LONELY_TIMEOUT = 60  # seconds of inactivity before lonely message

# === TTS SETUP ===
engine = pyttsx3.init()
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)

# === SERIAL SETUP ===
try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
    time.sleep(2)
    print("✅ Connected to Arduino.")
except Exception as e:
    print("❌ Could not connect to Arduino.")
    print("Error:", e)
    exit()

# === GPT FUNCTION ===
def get_gpt_reply(user_message):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ GPT error:", e)
        return "I'm feeling shy right now. 🥺"

# === LCD SCROLLING FUNCTION ===
def send_scrolling_text(text, ser, chunk_size=32, delay=0.3):
    text = text.replace('\n', ' ')
    padded = text + ' ' * chunk_size
    for i in range(len(text) + 1):
        chunk = padded[i:i+chunk_size]
        ser.write((chunk + "\n").encode())
        time.sleep(delay)

# === TTS FUNCTION ===
def speak(text):
    engine.say(text)
    engine.runAndWait()

# === Lonely Bot Logic ===
last_interaction = time.time()
lonely_messages = [
    "I'm here if you need me 💭",
    "It's quiet... wanna talk? 🐣",
    "Feeling a bit lonely 😔",
    "I miss your questions 💬",
    "Let's chat again soon! 💖"
]

def check_lonely():
    global last_interaction
    while True:
        time.sleep(5)
        if time.time() - last_interaction > LONELY_TIMEOUT:
            lonely_msg = lonely_messages[int(time.time()) % len(lonely_messages)]
            print("(Lonely message)", lonely_msg)
            ser.write((lonely_msg + "\n").encode())
            speak(lonely_msg)
            last_interaction = time.time()

# === Start lonely checker thread ===
threading.Thread(target=check_lonely, daemon=True).start()

# === MAIN LOOP ===
print("Type your question below:")
while True:
    user_input = input("You: ")
    last_interaction = time.time()
    if user_input.strip() == "":
        continue

    gpt_reply = get_gpt_reply(user_input)
    print("GPT:", gpt_reply)

    # Add emoji flair
    if any(word in gpt_reply.lower() for word in ["love", "friend", "happy", "you"]):
        gpt_reply += " ❤️"

    # Send scrolling text
    send_scrolling_text(gpt_reply, ser)
