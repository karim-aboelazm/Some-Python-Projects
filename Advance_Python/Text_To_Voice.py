import pyttsx3 as v

def text_to_voice():
    text = str(input('Your Text : '))
    engine = v.init()
    if text == 'Hi ,' or text == 'Hi' or text == 'hi ,' or text == 'hi':
        engine.say('Hi')
    elif text == 'Good Morning Bola ?' or text == 'good morning ?':
        engine.say('Good Morning Kimo , How are you today ?')
    elif text == 'I am fine . And What about you Anna ?':
        engine.say("That's fantastic . I am Ok ! , Tell me How can I help You Karim ?")


        
    engine.runAndWait()

while True:
    text_to_voice()
