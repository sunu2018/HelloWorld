# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
cl = LINE("EtHO8rZgTw1q6juRoVvf.4YSrMg2oNLZ3c2qS97Qi+W.k2TeLOz1HTtz2jJ+CuaaDHN+R9wcNMOY2hfRLRA6GvA=")
cl.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()
cl.log("Channel Token : " + str(channelToken))
ghost = LINE("EtQQZ5O8Q9ZNn47rzMCd.ZumT2/Y29n7tOJ4IwPo4tq.1TFAsQAvYzlyAp1XEM5RsdIZwZtoEnir3y6dea1fo1E=")
ghost.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()
ghost.log("Channel Token : " + str(channelToken))
kicker01 = LINE("Et0Oj6SRTe8eGtw9jK3d.SPS+quoffhJbcv30K1vAdq.gD9LSFBUBorGs552hX0ltdIVxai6oaF/Ox4aGWcOFJA=")
kicker01.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()
kicker01.log("Channel Token : " + str(channelToken))
kicker02 = LINE("EtuabQyPa4w1jYNY3sm0.ZaBHUQRqncLKKv+uKgw/qa.uBKyRSqmAN14wzFVY5K/nO+ja0fHE1IoLuFUqDALCsA=")
kicker02.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()
kicker02.log("Channel Token : " + str(channelToken))
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
clProfile = cl.getProfile()
clMID = cl.profile.mid
ghostMID = ghost.profile.mid
kicker01MID = kicker01.profile.mid
kicker02MID = kicker02.profile.mid
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
KAC = [kicker01,kicker02]
admin = ['u28d781fa3ba9783fd5144390352b0c24',clMID,kicker01MID,kicker02MID,ghostMID]
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
}
setTime = {}
setTime = wait2['setTime']
msg_dict = {}
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """
╔═══════════
♥ ✿ CoCo指令表 ✿ ♥
棉花糖の特製機
════✪〘 查看指令表 〙✪════
↪ 「Help」查看全部指令
↪ 「HelpTag」查看標註指令
↪ 「HelpKick」查看踢人指令
↪ 「HelpBot」查看機器指令
════✪〘 狀態 〙✪═══════
↪ 「Rebot」重新啟動機器
↪ 「Runtime」查看機器運行時間
↪ 「Speed」查看機器速度
↪ 「Set」查看設定
↪ 「About」查看自己的狀態
↪ 「Look Protect」查看這個群組的保護狀態
════✪〘 設定 〙✪═══════
↪ 「Add On/Off」自動加入好友 打開/關閉
↪ 「Join On/Off」自動進入群組 打開/關閉
↪ 「Leave On/Off」自動離開副本 打開/關閉
↪ 「Read On/Off」自動已讀 打開/關閉
↪ 「Tag On/Off」標註提醒 打開/關閉
↪ 「Qr On/Off」網址保護 打開/關閉
↪ 「Inviteprotect On/Off」邀請保護 打開/關閉
↪ 「Protect On/Off」群組保護 打開/關閉
↪ 「Allprotect On/Off」全部保護 打開/關閉
↪ 「Contact On/Off」好友資料詳細訊息 打開/關閉
↪ 「Reread On/Off」查看收回 打開/關閉
↪ 「Inviteprotect List」查看邀請保護中的群組
↪ 「Qr List」查看網址保護中的群組
↪ 「Protect List」查看踢人保護中的群組
════✪〘 自己 〙✪═══════
↪ 「Me」丟出自己好友資料
↪ 「Mid」查看自己系統識別碼
↪ 「Contact @」標註查看好友資料
↪ 「Mid @」標註查看系統識別碼
════✪〘 群組 〙✪═══════
↪ 「Gurl」丟出群組網址
↪ 「O/Curl」打開/關閉群組網址
↪ 「Ginfo」查看群組狀態
↪ 「Ri @」標註來回機票
↪ 「Tk @」標注踢出成員
↪ 「Nk Name」使用名子踢出成員
↪ 「Uk mid」使用系統識別碼踢出成員
↪ 「Cancel」取消所有成員邀請
↪ 「Gcancel」取消所有群組邀請
↪ 「Gn Name」更改群組名稱
↪ 「Gc @」標註查看個人資料
↪ 「Inv mid」使用系統識別碼邀請進入群組
↪ 「Ban @」標註加入黑單
↪ 「Unban @」標註解除黑單
↪ 「Clear Ban」清空黑單
↪ 「Kill Ban」剔除黑單
↪ 「Nkk Name」使用名子踢出成員
↪ 「Tkk @」標注踢出成員
════✪〘 特別 〙✪═══════
↪ 「Tagall」標註群組所有成員
↪ 「S N/F/R」已讀點 開啟/關閉/重設
↪ 「R」查看已讀
↪ 「F/Gbc」好友/群組廣播
↪「/invitemeto:」使用群組識別碼邀請至群組
↪ 「Time」查看現在的時間
╚═〘 Credits By: ©CoCo™  〙
"""
    return helpMessage
def helpmessagetag():
    helpMessageTag ="""
╔══[ 標注指令 ]════════
↪ 「Ri @」標註來回機票
↪ 「Tk @」標注踢出成員
↪ 「Vk @」標註踢出並清除訊息
↪ 「Gc @」標註查看個人資料
↪ 「Mid @」標註查看系統識別碼
↪ 「Name @」標註查看名稱
↪ 「Bio @」標註查看狀態消息
↪ 「Picture @」標註查看頭貼
↪ 「VideoProfile @」標註查看動態頭貼
↪ 「Cover @」標注查看封面
↪ 「Copy @」標註複製配置文件
↪ 「Ban @」標註加入黑單
↪ 「Unban @」標註解除黑單
↪ 「Tkk @」標注踢出成員
╚═〘 Credits By: ©CoCo™  〙
"""
    return helpMessageTag
def helpmessagekick():
    helpMessageKick ="""
╔══[ 踢人指令 ]════════
↪ 「Ri @」標註來回機票
↪ 「Tk @」標注踢出成員
↪ 「Nk Name」使用名子踢出成員
↪ 「Uk mid」使用系統識別碼踢出成員
↪ 「Kill ban」踢出黑單成員
↪ 「Nkk Name」使用名子踢出成員
↪ 「Tkk @」標注踢出成員
╚═〘 Credits By: ©CoCo™  〙
"""
    return helpMessageKick
def helpmessagebot():
    helpMessageBot ="""
╔══〘 設定 〙✪═══════
↪ 「Add On/Off」自動加入好友 打開/關閉
↪ 「Join On/Off」自動進入群組 打開/關閉
↪ 「Leave On/Off」自動離開副本 打開/關閉
↪ 「Read On/Off」自動已讀 打開/關閉
↪ 「Tag On/Off」標註提醒 打開/關閉
↪ 「Qr On/Off」網址保護 打開/關閉
↪ 「Inviteprotect On/Off」邀請保護 打開/關閉
↪ 「Protect On/Off」群組保護 打開/關閉
↪ 「Allprotect On」全部保護 打開
↪ 「Contact On/Off」好友資料詳細訊息 打開/關閉
↪ 「Reread On/Off」查看收回 打開/關閉
"""
    return helpMessageBot
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(param2)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker01.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
                kicker02.sendMessage(op.param1, "你好 {} 謝謝你加本機為好友 :D\n       本機為CoCo製作\n       line.me/ti/p/1MRX_Gjbmv".format(str(cl.getContact(op.param1).displayName)))
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
            print ("[11]有人打開群組網址 群組名稱: " + str(group.name) + "\n" + op.param1 + "\n名字: " + contact.displayName)
            if op.param1 in settings["qrprotect"]:
                if op.param2 in admin:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(op.param1)
                    ghost.acceptGroupInvitationByTicket(op.param1,Ti)
                    time.sleep(0.2)
                    ghost.kickoutFromGroup(op.param1,[op.param2])
                    time.sleep(0.2)
                    gs.preventJoinByTicket = True
                    ghost.leaveRoom(op.param1)
                    cl.updateGroup(gs)
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[ 13 ] 通知邀請群組: " + str(group.name) + "\n邀請者: " + contact1.displayName + "\n被邀請者" + contact2.displayName)
            if op.param1 in settings["inviteprotect"]:
                if op.param2 in admin:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param3)
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    if op.param2 in admin:
                        print ("進入群組: " + str(group.name))
                        cl.acceptGroupInvitation(op.param1)
                        if settings["kickerjoin"] == True:
                            G = cl.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(op.param1)
                            kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                            kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) + "\n" + op.param1 +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n被踢者" + contact2.displayName + "\nMid:" + contact2.mid )
            if op.param1 in settings["protect"]:
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    settings["blacklist"][op.param2] = True
            else:
                pass
            if clMID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker01.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker01.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker01.updateGroup(G)
                    invsend = 0
                    Ti = kicker01.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker01MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        kicker02.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = kicker02.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    kicker02.updateGroup(G)
                    invsend = 0
                    Ti = kicker02.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
            if kicker02MID in op.param3:
                if op.param2 in admin:
                    pass
                else:
                    try:
                        print ("[19]有人踢機器 群組名稱: " + str(group.name) +"\n踢人者: " + contact.displayName + "\nMid: " + contact.mid + "\n\n")
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("機器踢人規制或是不在群組、\n["+op.param1+"]\nの\n["+op.param2+"]\n我踢不了他。\n把他加進黑名單。")
                        if op.param2 in settings["blacklist"]:
                            pass
                        else:
                            settings["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker01.acceptGroupInvitationByTicket(op.param1, Ti)
                    kicker02.acceptGroupInvitationByTicket(op.param1, Ti)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
        if op.type == 24:
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
                kicker01.leaveRoom(op.param1)
                kicker02.leaveRoom(op.param1)
        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 13:
                if settings["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                            cl.sendMessage(msg.to,"[顯示名稱]:\n" + msg.contentMetadata["顯示名稱"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[顯示名稱]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[狀態消息]:\n" + contact.statusMessage + "\n[圖片網址]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[封面網址]:\n" + str(cu))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    msg.contentType = 0
                    msg.text = "文章網址\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendMessage(msg.to,msg.text)
            if msg.contentType == 0:
                if text is None:
                    return
            if sender in admin:
                if text.lower() == 'help':
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                    cl.sendContact(to, "u28d781fa3ba9783fd5144390352b0c24")
                elif text.lower() == 'helptag':
                    helpMessageTag = helpmessagetag()
                    cl.sendMessage(to, str(helpMessageTag))
                elif text.lower() == 'helpkick':
                    helpMessageKick = helpmessagekick()
                    cl.sendMessage(to, str(helpMessageKick))
                elif text.lower() == 'helpbot':
                    helpMessageBot = helpMessageBot()
                    cl.sendMessage(to, str(helpMessageBot))
                elif "Fbc:" in msg.text:
                    bctxt = text.replace("Fbc:","")
                    t = cl.getAllContactIds()
                    for manusia in t:
                        cl.sendMessage(manusia,(bctxt))
                elif "Gbc:" in msg.text:
                    bctxt = text.replace("Gbc:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                elif 'alljoin' in text.lower():
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker01.acceptGroupInvitationByTicket(to, Ti)
                            kicker02.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            invsend = 0
                            Ti = cl.reissueGroupTicket(to)
                            kicker01.acceptGroupInvitationByTicket(to, Ti)
                            kicker02.acceptGroupInvitationByTicket(to, Ti)
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                elif text.lower() == 'bot bye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            kicker01.leaveGroup(to)
                            kicker02.leaveGroup(to)
                        except:
                            pass
                elif text.lower() == 'test':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=5000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                    kicker01.sendMessage(to, 'ok')
                    kicker02.sendMessage(to, 'ok')
                elif text.lower() == 'gj':
                    if msg.toType == 2:
                        G = cl.getGroup(msg.to)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(msg.to)
                        ghost.acceptGroupInvitationByTicket(msg.to,Ti)
                        G.preventedJoinByTicket = True
                        cl.updateGroup(G)
                elif text.lower() == 'gbye':
                    if msg.toType == 2:
                        ginfo = cl.getGroup(to)
                        try:
                            ghost.leaveGroup(to)
                        except:
                            pass
                elif "Ri " in msg.text:
                    Ri0 = text.replace("Ri ","")
                    Ri1 = Ri0.rstrip()
                    Ri2 = Ri1.replace("@","")
                    Ri3 = Ri2.rstrip()
                    _name = Ri3
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for s in gs.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                    cl.findAndAddContactsByMid(target)
                                    cl.inviteIntoGroup(to,[target])
                                except:
                                    pass
                elif "Uk " in msg.text:
                    midd = text.replace("Uk ","")
                    cl.kickoutFromGroup(to,[midd])
                elif "Tk " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                                time.sleep(0.1)
                            except:
                                pass
                elif "Tkk " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in admin:
                            pass
                        else:
                            try:
                                klist = [kicker01,kicker02]
                                kickers = random.choice(klist)
                                kickers.kickoutFromGroup(to,[target])
                                time.sleep(0.1)
                            except:
                                pass
                elif "Nk " in msg.text:
                    _name = text.replace("Nk ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    cl.kickoutFromGroup(to,[target])
                                    time.sleep(0.1)
                                except:
                                    pass
                elif "Nkk " in msg.text:
                    _name = text.replace("Nkk ","")
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target in admin:
                                pass
                            else:
                                try:
                                    klist = [kicker01,kicker02]
                                    kickers = random.choice(klist)
                                    kickers.kickoutFromGroup(to,[target])
                                    time.sleep(0.1)
                                except:
                                    pass
                elif "Ulti " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    gs = cl.getGroup(msg.to)
                    gs.preventJoinByTicket = False
                    cl.updateGroup(gs)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(msg.to)
                    klist = [ghost]
                    kickers = random.choice(klist)
                    ghost.acceptGroupInvitationByTicket(to, Ti)
                    time.sleep(0.2)
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    else:
                        for target in targets:
                            try:
                                kickers.kickoutFromGroup(msg.to,[target])
                                ghost.leaveGroup(msg.to)
                                gs.preventJoinByTicket = True
                                cl.updateGroup(gs)
                            except:
                                pass
                elif "NT " in msg.text:
                    _name = text.replace("NT ","")
                    gs = cl.getGroup(to)
                    targets = []
                    net_ = ""
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to, "這個群組沒有這個人")
                    else:
                        for target in targets:
                            try:
                                sendMessageWithMention(to,target)
                            except:
                                pass
                elif text.lower() == 'zt':
                    gs = cl.getGroup(to)
                    targets = []
                    for g in gs.members:
                        if g.displayName in "":
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(to, "這個群組沒有名字0字的人")
                    else:
                        mc = ""
                        for target in targets:
                            mc += sendMessageWithMention(to,target) + "\n"
                        cl.sendMessage(to, mc)
                elif "Mc " in msg.text:
                    mmid = msg.text.replace("Mc ","")
                    cl.sendContact(to, mmid)
                elif "Sc " in msg.text:
                    ggid = msg.text.replace("Sc ","")
                    group = cl.getGroup(ggid)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "未找到"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "沒有"
                    else:
                        gQr = "開啟"
                        gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ 群組資料 ]"
                    ret_ += "\n╠ 顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n╠ 群組ＩＤ : {}".format(group.id)
                    ret_ += "\n╠ 群組作者 : {}".format(str(gCreator))
                    ret_ += "\n╠ 成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n╠ 邀請數量 : {}".format(gPending)
                    ret_ += "\n╠ 群組網址 : {}".format(gQr)
                    ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                    ret_ += "\n╚══[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif msg.text in ["c","C","cancel","Cancel"]:
                  if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = (contact.mid for contact in X.invitee)
                        ginfo = cl.getGroup(msg.to)
                        sinvitee = str(len(ginfo.invitee))
                        start = time.time()
                        for cancelmod in gInviMids:
                            cl.cancelGroupInvitation(msg.to, [cancelmod])
                        elapsed_time = time.time() - start
                        cl.sendMessage(to, "已取消完成\n取消時間: %s秒" % (elapsed_time))
                        cl.sendMessage(to, "取消人數:" + sinvitee)
                    else:
                        cl.sendMessage(to, "沒有任何人在邀請中！！")
                elif text.lower() == 'gcancel':
                    gid = cl.getGroupIdsInvited()
                    start = time.time()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    elapsed_time = time.time() - start
                    cl.sendMessage(to, "全部群組邀請已取消")
                    cl.sendMessage(to, "取消時間: %s秒" % (elapsed_time))
                elif "Gn " in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Gn ","")
                        cl.updateGroup(X)
                    else:
                        cl.sendMessage(msg.to,"無法使用在群組外")
                elif "Gc" in msg.text:
                    if msg.toType == 2:
                        key = eval(msg.contentMetadata["MENTION"])
                        u = key["MENTIONEES"][0]["M"]
                        contact = cl.getContact(u)
                        cu = cl.getProfileCoverURL(mid=u)
                        try:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n頭貼網址 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n封面網址 :\n" + str(cu))
                        except:
                            cl.sendMessage(msg.to,"名字:\n" + contact.displayName + "\n\n系統識別碼:\n" + contact.mid + "\n\n個性簽名:\n" + contact.statusMessage + "\n\n封面網址:\n" + str(cu))
                elif "Inv " in msg.text:
                    midd = msg.text.replace("Inv ","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                elif "Ban" in msg.text:
                    if msg.toType == 2:
                        print ("[Ban] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["blacklist"][target] = True
                                    cl.sendMessage(to, "已加入黑名單")
                                except:
                                    pass
                elif "Unban" in msg.text:
                    if msg.toType == 2:
                        print ("[UnBan] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["blacklist"][target]
                                    cl.sendMessage(to, "已解除黑名單")
                                except:
                                    pass
                elif text.lower() == 'clear ban':
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    cl.sendMessage(to, "已清空黑名單")
                elif text.lower() == 'banlist':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        cl.sendMessage(to, "以下是黑名單")
                        mc = ""
                        for mi_d in settings["blacklist"]:
                            mc += "->" + cl.getContact(mi_d).displayName + "\n"
                        cl.sendMessage(to, mc)
                elif text.lower() == 'banmid':
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "沒有黑名單")
                    else:
                        cl.sendMessage(to, "以下是黑名單")
                        mc = ""
                        for mi_d in settings["blacklist"]:
                            mc += "->" + cl.getContact(mi_d).mid + "\n"
                        cl.sendMessage(to, mc)
                elif text.lower() == 'kill ban':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "沒有黑名單")
                            return
                        klist = [kicker01,kicker02]
                        kickers = random.choice(klist)
                        for jj in matched_list:
                            kickers.kickoutFromGroup(to, [jj])
                        cl.sendMessage(to, "黑名單以踢除")
                elif "/invitemeto:" in msg.text:
                    gid = msg.text.replace("/invitemeto:","")
                    if gid == "":
                        cl.sendMessage(to,"請輸入群組ID")
                    else:
                        try:
                            cl.findAndAddContactsByMid(msg.from_)
                            cl.inviteIntoGroup(gid,[msg.from_])
                        except:
                            cl.sendMessage(to,"我不在那個群組裡")
                elif msg.text in ["SR","Setread"]:
                    cl.sendMessage(msg.to, "設置已讀點")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print ("設置已讀點")
                elif msg.text in ["LR","Lookread"]:
                    if msg.to in wait2['readPoint']:
                        print ("查詢已讀")
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "||已讀順序||%s\n\n||已讀的人||\n\n%s\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "請輸入SR設置已讀點")
                elif text.lower() == 'readset':
                    try:
                        del cctv['point'][msg.to]
                        del cctv['sidermem'][msg.to]
                        del cctv['cyduk'][msg.to]
                    except:
                        pass
                    cctv['point'][msg.to] = msg.id
                    cctv['sidermem'][msg.to] = ""
                    cctv['cyduk'][msg.to]=True
                elif text.lower() == 'offread':
                    if msg.to in cctv['point']:
                        cctv['cyduk'][msg.to]=False
                        cl.sendMessage(to, cctv['sidermem'][msg.to])
                    else:
                        cl.sendMessage(to, "readset")
                elif msg.text in ["Friendlist"]:
                    anl = cl.getAllContactIds()
                    ap = ""
                    for q in anl:
                        ap += "• "+cl.getContact(q).displayName + "\n"
                    cl.sendMessage(msg.to,"「 朋友列表 」\n"+ap+"人數 : "+str(len(anl)))
                elif text.lower() == 'speed' or text.lower() == 'sp':
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'處理速度\n' + str1 + '秒')
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,'指令反應\n' + format(str(elapsed_time)) + '秒')
                elif text.lower() == 'rebot':
                    cl.sendMessage(to, "重新啟動")
                    restartBot()
                elif text.lower() == 'runtime':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "機器運行時間 {}".format(str(runtime)))
                elif text.lower() == 'about':
                    try:
                        arr = []
                        owner = "u28d781fa3ba9783fd5144390352b0c24"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "╔══[ 關於自己 ]"
                        ret_ += "\n╠ 名稱 : {}".format(contact.displayName)
                        ret_ += "\n╠ 群組 : {}".format(str(len(grouplist)))
                        ret_ += "\n╠ 好友 : {}".format(str(len(contactlist)))
                        ret_ += "\n╠ 黑單 : {}".format(str(len(blockedlist)))
                        ret_ += "\n╠══[ 關於機器 ]"
                        ret_ += "\n╠ 版本 : 棉花糖特製機v1.0"
                        ret_ += "\n╠ 作者 : {}".format(creator.displayName)
                        ret_ += "\n╚══[ 未經許可禁止重製 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'set':
                    try:
                        ret_ = "╔══[ 設定 ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠ 自動加入好友 ✅"
                        else: ret_ += "\n╠ 自動加入好友 ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ 自動加入群組 ✅"
                        else: ret_ += "\n╠ 自動加入群組 ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ 自動離開副本 ✅"
                        else: ret_ += "\n╠ 自動離開副本 ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ 自動已讀 ✅"
                        else: ret_ += "\n╠ 自動已讀 ❌"
                        if settings["inviteprotect"] == True: ret_ += "\n╠ 群組邀請保護 ✅"
                        else: ret_ += "\n╠ 群組邀請保護 ❌"
                        if settings["qrprotect"] == True: ret_ += "\n╠ 群組網址保護 ✅"
                        else: ret_ += "\n╠ 群組網址保護 ❌"
                        if settings["protect"] == True: ret_ += "\n╠ 群組保護 ✅"
                        else: ret_ += "\n╠ 群組保護 ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠ 標注提醒 ✅"
                        else: ret_ += "\n╠ 標注提醒 ❌"
                        if settings["contact"] == True: ret_ += "\n╠ 詳細資料 ✅"
                        else: ret_ += "\n╠ 詳細資料 ❌"
                        if settings["reread"] == True: ret_ += "\n╠ 查詢收回開啟 ✅"
                        else: ret_ += "\n╠ 查詢收回關閉 ❌"
                        ret_ += "\n╚══[ 設定 ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'add on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "自動加入好友已開啟")
                elif text.lower() == 'add off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "自動加入好友已關閉")
                elif text.lower() == 'join on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動加入群組已開啟")
                elif text.lower() == 'join off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動加入群組已關閉")
                elif text.lower() == 'leave on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "自動離開副本已開啟")
                elif text.lower() == 'leave off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "自動離開副本已關閉")
                elif text.lower() == 'read on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "自動已讀已開啟")
                elif text.lower() == 'read off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "自動已讀已關閉")
                elif text.lower() == 'tag on':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "標註提醒已開啟")
                elif text.lower() == 'tag off':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "標註提醒已關閉")
                elif text.lower() == 'clonecontact':
                    settings["copy"] = True
                    cl.sendMessage(to, "請丟出好友資料以便複製")
                elif text.lower() == 'contact on':
                    settings["contact"] = True
                    cl.sendMessage(to, "查看好友資料詳情開啟")
                elif text.lower() == 'contact off':
                    settings["contact"] = False
                    cl.sendMessage(to, "查看好友資料詳情關閉")
                elif text.lower() == 'inviteprotect on':
                    gid = cl.getGroup(to)
                    settings["inviteprotect"][gid.id] = True
                    cl.sendMessage(to, "群組邀請保護已開啟")
                elif text.lower() == 'inviteprotect off':
                    del settings["inviteprotect"][gid.id]
                    cl.sendMessage(to, "群組邀請保護已關閉")
                elif  text.lower() == 'inviteprotect list':
                    if settings["inviteprotect"] == {}:
                        cl.sendMessage(to, "沒有網址保護中的群組")
                    else:
                        cl.sendMessage(to, "以下是網址保護中的群組")
                        mc = ""
                        for gi_d in settings["inviteprotect"]:
                            mc += "->" + cl.getGroup(gi_d).name + "\n"
                        cl.sendMessage(to, mc)
                elif text.lower() == 'qr on':
                    gid = cl.getGroup(to)
                    settings["qrprotect"][gid.id] = True
                    cl.sendMessage(to, "群組網址保護已開啟")
                elif text.lower() == 'qr off':
                    del settings["qrprotect"][gid.id]
                    cl.sendMessage(to, "群組網址保護已關閉")
                elif  text.lower() == 'qr list':
                    if settings["qrprotect"] == {}:
                        cl.sendMessage(to, "沒有網址保護中的群組")
                    else:
                        cl.sendMessage(to, "以下是網址保護中的群組")
                        mc = ""
                        for gi_d in settings["qrprotect"]:
                            mc += "->" + cl.getGroup(gi_d).name + "\n"
                        cl.sendMessage(to, mc)
                elif text.lower() == 'allprotect on':
                    gid = cl.getGroup(to)
                    settings["qrprotect"][gid.id] = True
                    settings["protect"][gid.id] = True
                    settings["inviteprotect"][gid.id] = True
                    cl.sendMessage(to, "這群已經開啟全部保護")
                elif text.lower() == 'allprotect off':
                    gid = cl.getGroup(to)
                    del settings["qrprotect"][gid.id]
                    del settings["qrprotect"][gid.id]
                    del settings["inviteprotect"][gid.id]
                    cl.sendMessage(to, "這群已經關閉全部保護")
                elif text.lower() == 'protect on':
                    gid = cl.getGroup(to)
                    settings["protect"][gid.id] = True
                    cl.sendMessage(to, "群組保護已開啟")
                elif text.lower() == 'protect off':
                    gid = cl.getGroup(to)
                    del settings["protect"][gid.id]
                    cl.sendMessage(to, "群組保護已關閉")
                elif text.lower() == 'protectlist':
                    if settings["protect"] == {}:
                        cl.sendMessage(to, "沒有保護中的群組")
                    else:
                        cl.sendMessage(to, "以下是保護中的群組")
                        mc = ""
                        for gi_d in settings["protect"]:
                            mc += "->" + cl.getGroup(gi_d).name + "\n"
                        cl.sendMessage(to, mc)
                elif text.lower() == 'look protect':
                    ret_ = "╔══[ 保護狀態 ]"
                    gid = cl.getGroup(to)
                    if gid.id in settings["protect"]: ret_ += "\n╠ 群組保護 ✅"
          #          else: ret_ += "\n╠ 網址保護 ❌
                    if gid.id in settings["qrprotect"]: ret_ += "\n╠ 網址保護 ✅"
            #        else: ret_ += "\n╠ 網址保護 ❌
                    if gid.id in settings["inviteprotect"]: ret_ += "\n╠ 邀請保護 ✅"
     #               else: ret_ += "\n╠ 邀請保護 ❌
                    ret_ += "\n╚══[ 這個群組 ]"
                    cl.sendMessage(to, str(ret_))
                elif text.lower() == 'reread on':
                    settings["reread"] = True
                    cl.sendMessage(to, "查詢收回開啟")
                elif text.lower() == 'reread off':
                    settings["reread"] = False
                    cl.sendMessage(to, "查詢收回關閉")
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    cl.sendContact(to, sender)
                elif text.lower() == 'mid':
                    cl.sendMessage(msg.to,"[MID]\n" +  sender)
                elif msg.text.lower().startswith("contact "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = ""
                        for ls in lists:
                            ret_ += "" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif text.lower() == 'gurl':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ 群組網址 ]\nhttps://cl.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "群組網址未開啟，請用Ourl先開啟".format(str(settings["keyCommand"])))
                elif text.lower() == 'ourl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "群組網址已開啟")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功開啟群組網址")
                elif text.lower() == 'curl':
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "群組網址已關閉")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "成功關閉群組網址")
                elif text.lower() == 'ginfo':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "未找到"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "關閉"
                        gTicket = "沒有"
                    else:
                        gQr = "開啟"
                        gTicket = "https://cl.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[ 群組資料 ]"
                    ret_ += "\n╠ 顯示名稱 : {}".format(str(group.name))
                    ret_ += "\n╠ 群組ＩＤ : {}".format(group.id)
                    ret_ += "\n╠ 群組作者 : {}".format(str(gCreator))
                    ret_ += "\n╠ 成員數量 : {}".format(str(len(group.members)))
                    ret_ += "\n╠ 邀請數量 : {}".format(gPending)
                    ret_ += "\n╠ 群組網址 : {}".format(gQr)
                    ret_ += "\n╠ 群組網址 : {}".format(gTicket)
                    ret_ += "\n╚══[ 完 ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == 'tagall':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "總共 {} 個成員".format(str(len(nama))))
                elif text.lower() == 'sn':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                cl.sendMessage(msg.to,"已讀點已開始")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to, "設定已讀點:\n" + readTime)
                elif text.lower() == 'sf':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        cl.sendMessage(msg.to,"已讀點已經關閉")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        cl.sendMessage(msg.to, "刪除已讀點:\n" + readTime)
                elif text.lower() == 'sr':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        cl.sendMessage(msg.to, "重置已讀點:\n" + readTime)
                    else:
                        cl.sendMessage(msg.to, "已讀點未設定")
                elif text.lower() == 'r':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            cl.sendMessage(receiver,"[ 已讀者 ]:\n沒有")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ 已讀者 ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ 已讀時間 ]: \n" + readTime
                        try:
                            cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        cl.sendMessage(receiver,"已讀點未設定")
                elif text.lower() == 'time':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    cl.sendMessage(msg.to, readTime)
        if op.type == 26:
            try:
                msg = op.message
                if settings["reread"] == True:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if settings["reread"] == True:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"%s\n[收回了]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["收回訊息"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    cl.sendMessage(to, "標我幹嘛?")
                                    sendMessageWithMention(to, contact.mid)
                                break
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n[•]" + Name
                        wait2['ROM'][op.param1][op.param2] = "[•]" + Name
                        print (time.time() + name)
                else:
                    pass
            except:
                pass
    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
