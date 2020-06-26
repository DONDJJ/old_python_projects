import datetime, time

def take_time():
    hours=int(input("Часы: "))
    minutes=int(input("Минуты: "))
    seconds=int(input("Секунды: "))
    date_string="%d:%d:%d"%(hours,minutes,seconds)
    time_since_now=hours*60*60+minutes*60+seconds
    return time_since_now

def onemoretimer():
    ans=input("Хотите ли вы завести еще один таймер?(y/n) ")
    while ans not in ("y","n"):
        ans = input("Введите в нужном формате!!!(y/n) ")
    if ans=="y":
        return True
    else:
        return False

while onemoretimer():
    user_timer=take_time()
    time_now=datetime.datetime.timestamp(datetime.datetime.now())

    final_time=time_now+user_timer
    while final_time>datetime.datetime.timestamp(datetime.datetime.now()):
        time.sleep(0.1)
    print("\a")
