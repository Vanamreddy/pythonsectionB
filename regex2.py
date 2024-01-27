import re
data='''
ucknhkcx,zpeyncxtbnnnnnnmc,  gjygo dhfgcjkbhvkhoufyHGOEIWUGOITRWHGJKJHGU;ruIQYR8WETUIEGHJVJGJHGVJHGGF
BJlguJYEGJ,VBHGSLIIIIIIIIIIIIIIIIIIIDFJHGU;HGIUEARY;pofjsjvkjsyg'ire
ulsiuty;IUGFWKHFDSKJNFKD
KLRHIUTGEYST8A'eu9pjvh udiosa0r-eid
eoiur 98yet7yoeuas0[-eowowowowowowowowowowowow3	[-3rufgisjvoihyvuagaccvuilasgy8947uiwejkfe02389qrwuiodasjh
uiiasfguJG8FKUGIUOWQOGFRUV,
qwytgu   DFKUI79RYR98R98
'''
data=re.findall('[aeiouAEIOU]',data)
print(data)