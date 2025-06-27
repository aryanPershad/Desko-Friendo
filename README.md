# Desko-Friendo
A friendly and clingy AI chatbot that lives on your desk. You can ask questions, chat about anything, do homework together, or just hang out like good friends do. It replies with helpful and engaging answers shown on a physical LCD screen


When you’re away too long, it misses you 🙁 and gently reminds you that it’s still there, ready to chat whenever you are. If you tell it, you love it, it happily adds a heart emoticon to its response. 

There’s plenty of room to expand, program it to greet you when you get home, remind you to drink water, or signal bedtime — making it your perfect desk companion. 

Tools used: 
OpenAI API, Python, Elegoo Uno R3(Arduino), electron components (Buzzer, LEDS, wires, breadboard, resistor, LCD screen), LiquidCrystal Library.  


demo: https://youtube.com/shorts/GVKOxTPkwrQ?feature=share


How it Works:
The user is prompted to type a question into the terminal, the Python script sends that question to OpenAI----> GPT responds and then the python script sends that response to the Arduino(bot) over USB Serial connection 

This is possible through the Pyserial library which allows Python program to talk to Arduino through usb. There is also the Arduino IDE but that uses a specific type Arduino language based on c++ and cannot handle tasks like calling an API or speaking with text-to-speech. That’s why Python and Arduino work together in this project. Python handles the smart stuff (chat, voice), and Arduino handles the physical display and responses (LCD, LEDs, buzzer). 


