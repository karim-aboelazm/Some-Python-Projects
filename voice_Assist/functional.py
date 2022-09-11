import time
import datetime
import wikipedia
import pywhatkit
import requests
import webbrowser
import wolframalpha
from pywikihow import search_wikihow
import speedtest
import bs4
from os import startfile,system
from pyautogui import click
from keyboard import press,write
from googletrans import Translator
from voice_input import Listen
from voice_output import say
from newscatcherapi import NewsCatcherApiClient

# getting time
def get_time():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    say(f'Time is {time}')

# getting date
def get_date():
    date = datetime.date.today()
    say(f'Today is {date}')

# getting day
def get_day():  
    day = datetime.datetime.now().strftime("%A")
    say(f'Today is {day}')

# open Ms word
def open_word():
    click(x=22, y=751)
    time.sleep(2)
    write('word')
    time.sleep(1)
    press('enter')

# close Ms word
def close_word():
    time.sleep(1)
    system('taskkill /f /im WINWORD.EXE')

# open Ms excel
def open_excel():
    click(x=22, y=751)
    time.sleep(2)
    write('excel')
    time.sleep(1)
    press('enter')

# close Ms excel
def close_excel():
    time.sleep(1)
    system('taskkill /f /im EXCEL.EXE')

# open Ms ppt
def open_powerpoint():
    click(x=22, y=751)
    time.sleep(2)
    write('powerpoint')
    time.sleep(1)
    press('enter')

# close Ms excel
def close_powerpoint():
    time.sleep(1)
    system('taskkill /f /im POWERPNT.EXE')

# open Ms access
def open_access():
    click(x=22, y=751)
    time.sleep(2)
    write('access')
    time.sleep(1)
    press('enter')

# close Ms ppt
def close_access():
    time.sleep(1)
    system('taskkill /f /im MSACCESS.EXE')

# open chrome
def open_chrome():
    click(x=22, y=751)
    time.sleep(2)
    write('google chrome')
    time.sleep(1)
    press('enter')

# close chrome
def close_chrome():
    time.sleep(1)
    system('taskkill /f /im chrome.exe')

# open vscode
def open_vscode():
    click(x=22, y=751)
    time.sleep(2)
    write('vscode')
    time.sleep(1)
    press('enter')

# close chrome
def close_vscode():
    time.sleep(1)
    system('taskkill /f /im Code.exe')

# open cmd
def open_command():
    click(x=22, y=751)
    time.sleep(2)
    write('cmd')
    time.sleep(1)
    press('enter')

# close cmd
def close_command():
    time.sleep(1)
    system('taskkill /f /im cmd.exe')

# open ps
def open_photoshop():
    click(x=22, y=751)
    time.sleep(2)
    write('photoshop')
    time.sleep(1)
    press('enter')

# close ps
def close_photoshop():
    time.sleep(1)
    system('taskkill /f /im Photoshop.exe')

# open jupyter
def open_jupyter():
    click(x=22, y=751)
    time.sleep(2)
    write('jupyter')
    time.sleep(1)
    press('enter')

# close jupyter
def close_jupyter():
    time.sleep(1)
    system('taskkill /f /im chrome.exe')

# open spyder 
def open_spyder():
    click(x=22, y=751)
    time.sleep(2)
    write('spyder')
    time.sleep(1)
    press('enter')

# close spyder
def close_spyder():
    time.sleep(1)
    system('taskkill /f /im pythonw.exe')
    
# open zoom
def open_zoom():
    click(x=22, y=751)
    time.sleep(2)
    write('zoom')
    time.sleep(1)
    press('enter')

# close zoom
def close_zoom():
    time.sleep(1)
    system('taskkill /f /im zoom.exe')

# open my python scripts 
def open_py_projects ():
    click(x=126, y=756)
    time.sleep(1)
    click(x=69, y=586)
    time.sleep(1)
    click(x=1089, y=149)
    click(x=1089, y=149)

# open my django scripts
def open_dj_projects():
    click(x=126, y=756)
    time.sleep(1)
    click(x=69, y=586)
    time.sleep(1)
    click(x=680, y=152)
    click(x=680, y=152)

# open instagram 
def open_instagram():
    click(x=22, y=751)
    time.sleep(2)
    write('instagram')
    time.sleep(1)
    press('enter')

# close instagram
def close_instagram():
    time.sleep(1)
    system('taskkill /f /im msedge.exe')

# opening notepad
def open_notepad():
    click(x=22, y=751)
    time.sleep(2)
    write('notepad')
    time.sleep(1)
    press('enter')

# close notepad
def close_notepad():
    time.sleep(1)
    system('taskkill /f /im notepad.exe')

# opening paint
def open_paint():
    click(x=22, y=751)
    time.sleep(2)
    write('paint')
    time.sleep(1)
    press('enter')

# close paint 
def close_paint():
    time.sleep(1)
    system('taskkill /f /im mspaint.exe')

# opening draw 
def open_paint3d():
    click(x=22, y=751)
    time.sleep(2)
    write('paint3d')
    time.sleep(1)
    press('enter')

# close draw 
def close_paint3d():
    time.sleep(1)
    system('taskkill /f /im PaintStudio.View.exe')

# check the speed of the internet connection
def speedOfInternet():
    say('Checking Sir ....')
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correct_download = int(downloading/800000)
    uploading = speed.upload()
    correct_upload = int(uploading/800000)
    say(f'The Downloading speed is {correct_download} m/s  and \nThe Uploading speed is {correct_upload} m/s')

# voice break
def break_assistant():   
    say("Ok Sir , You Can Call Me At Anytime ..")
    say("Just Say Wake Up Omar!")
    exit()

# getting Egyptian today news 
def egy_news():
    say("Getting News from The internet..")
    url = "https://english.ahram.org.eg/Portal/1/Egypt.aspx"
    results = requests.get(url)
    soup = bs4.BeautifulSoup(results.text,'lxml')
    titles = []
    descriptions = []
    div = soup.find_all('div',class_="portal-section")
    for h in div:
        title = h.find('h3')
        des = h.find('p')
        titles.append(title.string)
        descriptions.append(des.string)

    say(f"Category [1] : {titles[0]}")
    say(f"Description : {descriptions[0][1:-2]}")
    print("="*50)
    stm = ''
    i = 0
    while i < (len(titles)-1):
        stm = Listen()
        if stm == 'next':
            print()
            say(f"Category [{i+2}] : {titles[i+1]}")
            say(f"Description : {descriptions[i+1][1:-2]}")
            print("="*50)
            i+=1
        else:
            break

# getting news from nasa
def nasa_news():
    say('Getting Data from Nasa ....')
    Api_key = "TDhA4g5vdtJFf41rQdx1pRfrNJiT2CneJVgwEVLs"
    url = "https://api.nasa.gov/planetary/apod?api_key="+str(Api_key)
    today = datetime.date.today()
    date = today
    parameters = {'date':str(date)}
    request = requests.get(url,params=parameters)
    Data = request.json()
    Info = Data['explanation']
    title = Data['title']
    image_url = Data['url']
    webbrowser.open(image_url)
    say(f"title : {title}")
    say(f"According to Nasa : {Info}")


# get non input error
def singleCommand(query):
    query = str(query)
    if 'time' in query:
        get_time()
    elif 'date' in query:
        get_date()
    elif 'day' in query:
        get_day()
    elif "break" in query:
        break_assistant()
    elif "open word" in query:
        open_word()
    elif "close word" in query:
        close_word()
    elif "open powerpoint" in query:
        open_powerpoint()
    elif "close powerpoint" in query:
        close_powerpoint()
    elif "open excel" in query:
        open_excel()
    elif "close excel" in query:
        close_excel()
    elif "open access" in query:
        open_access()
    elif "close access" in query:
        close_access()
    elif "open chrome" in query:
        open_chrome()
    elif "close chrome" in query:
        close_chrome()
    elif "open vscode" in query:
        open_vscode()
    elif "close vscode" in query:
        close_vscode()
    elif "open command" in query:
        open_command()
    elif "close command" in query:
        close_command()
    elif "open photoshop" in query:
        open_photoshop()
    elif "close Photprototype" in query:
        close_photoshop()
    elif "open jupyter" in query:
        open_jupyter()
    elif "close jupyter" in query:
        close_jupyter()
    elif "open spyder" in query:
        open_spyder()
    elif "close spyder" in query:
        close_spyder()
    elif "open zoom" in query:
        open_zoom()
    elif "close zoom" in query:
        close_zoom()
    elif "open instagram" in query:
        open_instagram()
    elif "close instagram" in query:
        close_instagram()
    elif "open python projects" in query:
        open_py_projects()
    elif "open django projects" in query:
        open_dj_projects()
    elif "open notepad" in query:
        open_notepad()
    elif "close notepad" in query:
        close_notepad()
    elif "open paint" in query:
        open_paint()
    elif "close paint" in query:
        close_paint()
    elif "open paint3d" in query:
        open_paint3d()
    elif "close paint3d" in query:
        close_paint3d() 
    elif "egy news" in query:
        egy_news()

    elif "nasa news" in query:
        nasa_news()
    elif 'internet speed' in query:
        speedOfInternet()
    


# wolframalpha 
def wolframalpha_settings(query):
    api_key = 'WY8246-P267T477J4'
    request = wolframalpha.Client(api_key)
    response = request.query(query)
    try:
        return next(response.results).text
    except:
        say('This query Is Not Defined')

# sending whatsapp_message
def whatsapp_message(name,message): 
    click(x=22, y=751)
    time.sleep(2)
    write('whatsapp')
    time.sleep(1)
    press('enter')
    time.sleep(20)
    click(x=83, y=112)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=264, y=236)
    time.sleep(1.5)
    click(x=971, y=704)
    time.sleep(1.5)
    write(message)
    press('enter')

# making whatsapp_call
def whatsapp_call(name):
    click(x=22, y=751)
    time.sleep(2)
    write('whatsapp')
    time.sleep(1)
    press('enter')
    time.sleep(20)
    click(x=83, y=112)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=264, y=236)
    time.sleep(1.5)
    click(x=1208, y=60)

# making whatsapp_video
def whatsapp_video(name):
    click(x=22, y=751)
    time.sleep(2)
    write('whatsapp')
    time.sleep(1)
    press('enter')
    time.sleep(20)
    click(x=83, y=112)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=264, y=236)
    time.sleep(1.5)
    click(x=1170, y=60)

# opening whatsapp_chat
def whatsapp_chat(name):
    click(x=22, y=751)
    time.sleep(2)
    write('whatsapp')
    time.sleep(1)
    press('enter')
    time.sleep(20)
    click(x=83, y=112)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=264, y=236)
    time.sleep(1.5)
  
# sending messenger message
def facebook_message(name,message): 
    click(x=22, y=751)
    time.sleep(2)
    write('messenger')
    time.sleep(1)
    press('enter')
    time.sleep(20)
    click(x=300, y=107)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=358, y=162)
    time.sleep(1.5)
    click(x=766, y=706)
    time.sleep(1.5)
    write(message)
    press('enter')

# making massenger call
def facebook_call(name): 
    click(x=22, y=751)
    time.sleep(2)
    write('messenger')
    time.sleep(1)
    press('enter')
    time.sleep(20)
    click(x=1120, y=21)
    time.sleep(1)
    click(x=300, y=107)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=358, y=162)
    time.sleep(1.5)
    click(x=1233, y=55)

# making massenger video
def facebook_video(name): 
    click(x=22, y=751)
    time.sleep(2)
    write('messenger')
    time.sleep(1)
    press('enter')
    time.sleep(20)
    click(x=1120, y=21)
    time.sleep(1)
    click(x=300, y=107)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=358, y=162)
    time.sleep(1.5)
    click(x=1255, y=55)

# opening massenger chat
def facebook_chat(name): 
    click(x=22, y=751)
    time.sleep(2)
    write('messenger')
    time.sleep(1)
    press('enter')
    time.sleep(20)
    click(x=1120, y=21)
    time.sleep(1)
    click(x=300, y=107)
    time.sleep(1)
    write(name)
    time.sleep(1.5)
    click(x=358, y=162)

def recognizing(name): 
    name = str(name).replace("he is ","")
    name = name.replace("she is ","")
    name = name.replace("i am ","")
    name = name.replace("i'am ","")
    say(f"Hello {name} It Nice To Meet You..")

def covidVirus(country):
    countries = str(country).replace(" ","")
    countries = str(country).replace("Corona in ","")
    countries = str(country).replace("covid in ","")
    countries = str(country).replace("covid-19 in ","")
    countries = str(country).replace("virus in ","")
    url = f"https://www.worldometers.info/coronavirus/country/{countries.lower()}/"
    result = requests.get(url)
    # pip install bs4
    # pip install lxml
    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_="maincounter-number")
    Data = []
    for case in corona:
        span = case.find('span')
        Data.append(span.string)
    cases ,Death, recovored = Data
    say(f"The corona virus in {countries} Statistics are..")
    say(f"The Number of all Cases is      {cases}")
    say(f"The Number of all Death is      {Death}")
    say(f"The Number of all Recovored is  {recovored}")
    webbrowser.open(f"https://www.google.com/search?q={countries.lower()}+coronavirus")

def how_to_do(query):
    say("Getting Data from the internet !")
    query = str(query).replace("Omar","")
    max_result = 1
    how_to_func = search_wikihow(query, max_result)
    assert len(how_to_func) == 1
    say(how_to_func[0].summary)   



# get information from wikipedia    
def multiCommand(tag,query):
    
    if "wikipedia" in tag:
        name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
        result = wikipedia.summary(name)
        say(result)

    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        query = query.replace("search for","")
        query = query.replace("searching for","")
        pywhatkit.search(query)
        res = wikipedia.summary(query,5)
        say(res)
    
    elif "YouTube" in tag:
        query = str(query).replace("YouTube","").replace("open","").replace("in YouTube","")
        query = query.replace(" ","")
        youtube = "https://www.youtube.com/results?search_query="+query
        webbrowser.open(youtube)

    elif "website" in tag:
        query = str(query).replace("open","")
        query = query.replace(" ","")
        web = "https://www."+str(query.lower())+".com/"
        webbrowser.open(web)

    elif "playmusic" in tag:
        query = str(query).replace("play music","").replace("play","")
        query = query.replace("youtube music","")
        query = query.replace(" ","")
        pywhatkit.playonyt(query)
    
    elif "weather" in tag:
        query = str(query).replace("weather in","")
        query = query.replace("what is weather in","")
        query = query.replace("weather for","")
        api_key = "382898aca8ccf36781e1452584f5d79a"
        root_url = "http://api.openweathermap.org/data/2.5/weather?"
        url = f"{root_url}appid={api_key}&q={query}"
        r = requests.get(url)
        data = r.json()
        if data['cod'] == 200:
            temp = data['main']['temp']
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            descr = data['weather'][0]['description']
            wind = data['wind']['speed']
            say(f"Weather Information In : {query}")
            say(f"The Weather Condition is {descr}")
            say(f"The temperature is {temp}kelvin")
            say(f"The pressure is {pressure}hPa")
            say(f"The humidity is {humidity}%")
            say(f"The speed of wind is {wind}m/s")
        else:
            say("Something Went Wrong")

    elif "temperature" in tag:
        query = str(query).replace("what is the temperature","temperature in")
        query = query.replace("temperature for","temperature in")
        say(wolframalpha_settings(query))

    elif "calculate" in tag:
        query = str(query).replace("Omar","")
        query = query.replace("multiply","*")
        query = query.replace("in","*")
        query = query.replace("into","*")
        query = query.replace("power","**")
        query = query.replace("to the power","**")
        query = query.replace("plus","+")
        query = query.replace("minus","-")
        query = query.replace("divide","/")
        query = query.replace("over","/")
        query = query.replace("div","/")
        query = query.replace("2-","2 ")
        try:
            say(f'The result is : {wolframalpha_settings(query)}')
        except:
            say("I Can Not Calculate This Query")

    elif "whatsapp message" in tag:
        say('For Whom Sir ..')
        name = Listen()
        say('Ok Sir , Tell me The Message..')
        query = Listen()
        whatsapp_message(str(name),str(query))
    
    elif "whatsapp call" in tag:
        say('For Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , Making a voice call Right Now For {query} ..')
        whatsapp_call(str(query))
    
    elif "whatsapp video" in tag:
        say('For Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , Making a video call Right Now For {query}..')
        whatsapp_video(str(query))

    elif "whatsapp chat" in tag:
        say('chat with Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , opening whatsapp chat with {query}..')
        whatsapp_chat(str(query))
    
    elif "facebook message" in tag:
        say('For Whom Sir ..')
        name = Listen()
        say('Ok Sir , Tell me The Message..')
        query = Listen()
        facebook_message(str(name),str(query))
    
    elif "facebook call" in tag:
        say('For Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , Making a voice call Right Now For {query} ..')
        facebook_call(str(query))
    
    elif "facebook video" in tag:
        say('For Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , Making a video call Right Now For {query}..')
        facebook_video(str(query))

    elif "facebook chat" in tag:
        say('chat with Whom Sir ..')
        query = Listen()
        say(f'Ok Sir , opening facebook chat with {query}..')
        facebook_chat(str(query))
    
    elif "remember that" in tag:
        rmsg = str(query).replace("remember that","")
        rmsg = rmsg.replace("remind me that","")
        say(f"You Told me to remind you that {rmsg}")
        remember = open('remind.txt','w')
        remember.write(rmsg)
        remember.close()

    elif "what do you remember" in tag:
        remember_message = open('remind.txt','r')
        say(f"You Told me to remember you that {str(remember_message.read())}")

    elif "how to" in tag:
        how_to_do(query)

    elif "recognize" in tag:
        recognizing(query)

    elif "corona" in tag:
        covidVirus(query)
    
   

