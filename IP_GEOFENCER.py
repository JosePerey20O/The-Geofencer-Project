#usr/bin/env python3
#
#AUTHOR: JOSE JR PEREY
#
#DATE: December 14 2022
#
#Works on Line 1 and 4 so far
#
#Validated from Finch to Museum, Wilson to Vaughan and Sheppard-Yonge to Don Mills
#
#Code validation underway

import re

#Explanations that define and form the TCONNECT system
print("Hello, this is the TCONNECT location calculator\n")
print("The Toronto Transit Commission has a deployed public wireless internet system \n at subway stations, cellular in some tunnel areas, \nand WiFi on some bus routes.")
print("The TCONNECT system on the subway lines runs on Cisco devices (access points)\n")
print("This script is limited to Lines 1 and 4 only\n")

#convince the user to input their IP address on the subway 
print("Welcome, place your IP address below... \n")
IP = input()

#All numbers and ranges should be in increasing numeric order

while re.search("10.(10|10[8-9]|11[0-6]|119|120).*", IP) == False:
     print("Enter an IP Address")
     IP = input()
     
else:

#Modular regular expressions in use: <   | | \n> <(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):> <(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):> <(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):> <([0-9]|[1-5][0-9]|6[0-3]).*", IP):>

#Modular print-outs in use: \n\n\n                 △ Line 1 interchange\n                | |\n==[ ] Spadina ==[x] St George ==[ ] Bay =="\n

#For any user that inputted the network router (the first host device)
     if re.search("10.11[1-6].(0|64|128|192).1", IP):
          exit("You are the networking router")
 
#For any use that inputted the network address (The first IP address of the subnet)         
     elif re.search("10.(11[1-6]).(0|64|128|192).0", IP):
          exit("This is the network address")

#For any user that inputted the broadcast address (The last IP address of the subnet)
     elif re.search("10.(11[1-6]).(63127|191|255).255", IP):
          exit("This is the broadcasting address")
          
#For any user with an IP address within 10.116.192.0/18
     elif re.search("10.116.(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):
          exit("You are at Finch Station. \n\n  [x] Finch \n  | | \n  | | \n  [ ] North York Centre\n  | | \n")
          
#For any user with an IP address within 10.116.128.0/18
     elif re.search("10.116.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at North York Centre Station. \n\n  | | \n  [ ] Finch\n  | | \n  | | \n  [x] North York Centre\n  | | \n  | | \n  [ ] Sheppard-Yonge\n  | | \n")
         
#For any user with an IP address within 10.116.64.0/18
     elif re.search("10.116.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):
          exit("You are at Sheppard-Yonge Station. \n\n  | | \n  [ ] North York Centre\n  | | \n  | | \n  [x] Sheppard-Yonge => Line 4 eastbound to Don Mills\n  | | \n  | | \n  [ ] York Mills\n  | | \n\n\n             Line 1 △ interchange\n                   | |\n[=[x]Sheppard-Yonge[x] ====[ ] Bayview ==\n")
          
#For any user with an IP address within 10.116.0.0/18
     elif re.search("10.116.([0-9]|[1-5][0-9]|6[0-3]).*", IP):
          exit("You are at York Mills Station. \n\n  | | \n  [ ] Sheppard-Yonge\n  | | \n  | | \n  [x] York Mills\n  | | \n  | | \n  [ ] Lawrence\n  | | \n")
          
#For any user with an IP address within 10.115.192.0/18
     elif re.search("10.115.(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):
          exit("You are at Lawrence Station. \n\n  | | \n  [ ] York Mills\n  | | \n  | | \n  [x] Lawrence\n  | | \n  | | \n  [ ] Eglinton\n  | | \n")
          
#For any user with an IP address within 10.115.128.0/18
     elif re.search("10.115.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Eglinton Station. \n\n  | | \n  [ ] Lawrence\n  | | \n  | | \n  [x] Eglinton\n  | | \n  | | \n  [ ] Davisville\n  | | \n")
          
#For any user with an IP address within 10.115.64.0/18
     elif re.search("10.115.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):
          exit("You are at Davisville Station. \n\n  | | \n  [ ] Eglinton\n  | | \n  | | \n  [x] Davisville\n  | | \n  | | \n  [ ] St Clair\n  | | \n")
          
#For any user with an IP address within 10.115.0.0/18
     elif re.search("10.115.([0-9]|[1-5][0-9]|6[0-3]).*", IP):
          exit("You are at Saint Clair Station. \n\n  | | \n  [ ] Davisville\n  | | \n  | | \n  [x] St Clair\n  | | \n  | | \n  [ ] Summerhill\n  | | \n")
          
#For any user with an IP address within 10.114.192.0/18
     elif re.search("10.114.(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):
          exit("You are at Summerhill Station. \n\n  | | \n  [ ] St Clair\n  | | \n  | | \n  [x] Summerhill\n  | | \n  | | \n  [ ] Rosedale\n  | | \n")
          
#For any user with an IP address within 10.114.128.0/18
     elif re.search("10.114.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Rosedale Station. \n\n  | | \n  [ ] Summerhill\n  | | \n  | | \n  [x] Rosedale\n  | | \n  | | \n  [ ] Bloor-Yonge\n  | | \n")
          
#For any user with an IP address within 10.114.64.0/18
     elif re.search("10.114.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):
          exit("You are at Bloor-Yonge Station. \n\n  | | \n  [ ] Rosedale\n  | | \n  | | \n  [x] Bloor-Yonge => Line 2 interchange\n  | | \n  | | \n  [ ] Wellesley\n  | | \n\n\n             △ Line 1 interchange\n            | |\n==[ ] Bay ==[x] Yonge ==[ ] Sherbourne ==\n")
          
#For any user with an IP address within 10.114.0.0/18
     elif re.search("10.114.([0-9]|[1-5][0-9]|6[0-3]).*", IP):
          exit("You are at Wellesley Station. \n\n  [ ] Bloor-Yonge\n  | | \n  | | \n  [x] Wellesley\n  | | \n  | | \n  [ ] College\n  | | \n")
          
#For any user with an IP address within 10.113.192.0/18
     elif re.search("10.113.(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):
          exit("You are at College Station. \n\n  [ ] Wellesley\n  | | \n  | | \n  [x] College\n  | | \n  | | \n  [ ] Dundas\n  | | \n")
          
#For any user with an IP address within 10.113.128.0/18
     elif re.search("10.113.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Dundas Station. \n\n  [ ] College\n  | | \n  | | \n  [x] Dundas\n  | | \n  | | \n  [ ] Queen\n  | | \n")
          
#For any user with an IP address within 10.113.64.0/18
     elif re.search("10.113.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):
          exit("You are at Queen Station. \n\n  [ ] Dundas\n  | | \n  | | \n  [x] Queen\n  | | \n  | | \n  [ ] King\n  | | \n")
          
#For any user with an IP address within 10.113.0.0/18
     elif re.search("10.113.([0-9]|[1-5][0-9]|6[0-3]).*", IP):
          exit("You are at King Station. \n\n  [ ] Queen\n  | | \n  | | \n  [x] King\n  | | \n  | | \n  [ ] Union\n  | | \n")         
          
#For any user with an IP address within 10.112.192.0/18
     elif re.search("10.112.(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):
          exit("You are at Union Station. \n\nTo Vaughan <=[ ] St Andrew === [x]Union[x] ===[ ] King => To Finch")
          
#For any user with an IP address within 10.112.128.0/18
     elif re.search("10.112.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Saint Andrew Station. \n\n  [ ] Osgoode\n  | | \n  | | \n  [x] St Andrew\n  | | \n  | | \n  [ ] Union\n  | | \n")
          
#For any user with an IP address within 10.112.64.0/18
     elif re.search("10.112.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):
          exit("You are at Osgoode Station. \n\n  [ ] St Patrick\n  | | \n  | | \n  [x] Osgoode\n  | | \n  | | \n  [ ] St Andrew\n  | | \n")
          
#For any user with an IP address within 10.112.0.0/18
     elif re.search("10.112.([0-9]|[1-5][0-9]|6[0-3]).*", IP):
          exit("You are at Saint Patrick Station. \n\n  [ ] Queen's Park\n  | | \n  | | \n  [x] St Patrick\n  | | \n  | | \n  [ ] Osgoode\n  | | \n")         
          
#For any user with an IP address within 10.111.192.0/18
     elif re.search("10.111.(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):
          exit("You are at Queen's Park Station. \n\n  [ ] Museum\n  | | \n  | | \n  [x] Queen's Park\n  | | \n  | | \n  [ ] St Patrick\n  | | \n")
          
#For any user with an IP address within 10.111.128.0/18
     elif re.search("10.111.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Museum Station. \n\n  [ ] St George\n  | | \n  | | \n  [x] Museum\n  | | \n  | | \n  [ ] Queen's Park\n  | | \n")
          
#For any user with an IP address within 10.111.64.0/18
     elif re.search("10.111.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):
          exit("You are at Saint George Station. \n\n  [ ] Spadina\n  | | \n  | | \n  [x] St George => Line 2 interchange\n  | | \n  | | \n  [ ] Museum\n  | | \n\n\n                 △ Line 1 interchange\n                | |\n==[ ] Spadina ==[x] St George ==[ ] Bay ==\n")

#For any user with an IP address within 10.109.0.0/18
     elif re.search("10.109.([0-9]|[1-5][0-9]|6[0-3]).*", IP):
          exit("You are at Spadina Station. \n\n  [ ] Dupont\n  | | \n  | | \n  [x] Spadina => Line 2 interchange\n  | | \n  | | \n  [ ] St George\n  | | \n\n\n                  △ Line 1 interchange\n                 | |\n==[ ] Bathurst ==[x] Spadina ==[ ] St George ==\n")
          
#For any user with an IP address within 10.109.64.0/18 - Spadina remains on the Line 2 WiFi ecosystem -Nov 13 2022
     elif re.search("10.109.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):
          exit("You are at Dupont Station. \n\n  [ ] St Clair West\n  | | \n  | | \n  [x] Dupont\n  | | \n  | | \n  [ ] Spadina\n  | | \n")
          
#For any user with an IP address within 10.109.128.0/18
     elif re.search("10.109.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Saint Clair West Station. \n\n  [ ] Eglinton West\n  | | \n  | | \n  [x] St Clair West\n  | | \n  | | \n  [ ] Dupont\n  | | \n")
          
#For any user with an IP address within 10.110.128.0/18
     elif re.search("10.110.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Eglinton West Station. \n\n  [ ] Glencairn\n  | | \n  | | \n  [x] Eglinton West\n  | | \n  | | \n  [ ] St Clair West\n  | | \n")
          
#For any user with an IP address within 10.110.0.0/18
     elif re.search("10.110.([0-9]|[1-5][0-9]|6[0-3]).*", IP):
          exit("You are at Glencairn Station. \n\n  [ ] Lawrence West\n  | | \n  | | \n  [x] Glencairn\n  | | \n  | | \n  [ ] Eglinton West\n  | | \n")
          
#For any user with an IP address within 10.110.64.0/18
     elif re.search("10.110.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):
          exit("You are at Lawrence West Station. \n\n  [ ] Yorkdale\n  | | \n  | | \n  [x] Lawrence West\n  | | \n  | | \n  [ ] Glencairn\n  | | \n")
          
#For any user with an IP address within 10.110.128.0/18
     elif re.search("10.11-.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Yorkdale Station !WARNING! TCONNECT current inactive at Yorkdale Station due to heavy construction. \n\n  [ ] Wilson\n  | | \n  | | \n  [x] Yorkdale\n  | | \n  | | \n  [ ] Lawrence West\n  | | \n")       
         
#For any user with an IP address within 10.110.192.0/18
     elif re.search("10.110.(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):
          exit("You are at Wilson Station. \n\n  [ ] Sheppard West\n  | | \n  | | \n  [x] Wilson\n  | | \n  | | \n  [ ] Yorkdale\n  | | \n")
          
#For any user with an IP address within 10.111.0.0/18
     elif re.search("10.111.([0-9]|[1-5][0-9]|6[0-3]).*", IP):
          exit("You are at Sheppard West Station. \n\n  [ ] Downsview Park\n  | | \n  | | \n  [x] Sheppard West\n  | | \n  | | \n  [ ] Wilson\n  | | \n")

#For any user with an IP address within 10.119.128.0/18
     elif re.search("10.119.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Downsview Park Station. \n\n  [ ] Finch West\n  | | \n  | | \n  [x] Downsview Park\n  | | \n  | | \n  [ ] Sheppard West\n  | | \n")
          
#For any user with an IP address within 10.119.192.0/18
     elif re.search("10.119.(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):
          exit("You are at Finch West Station. \n\n  [ ] York University\n  | | \n  | | \n  [x] Finch West\n  | | \n  | | \n  [ ] Downsview Park\n  | | \n")
          
#For any user with an IP address within 10.120.0.0/18
     elif re.search("10.120.([0-9]|[1-5][0-9]|6[0-3]).*", IP):
          exit("You are at York University Station. \n\n  [ ] Pioneer Village\n  | | \n  | | \n  [x] York University\n  | | \n  | | \n  [ ] Finch West\n  | | \n")
          
#For any user with an IP address within 10.120.64.0/18
     elif re.search("10.120.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):
          exit("You are at Pioneer Village Station. \n\n  [ ] Highway 407\n  | | \n  | | \n  [x] Pioneer Village\n  | | \n  | | \n  [ ] York University\n  | | \n")
          
#For any user with an IP address within 10.120.128.0/18
     elif re.search("10.120.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Highway 407 Station. \n\n  [ ] Vaughan Metropolitan Centre\n  | | \n  | | \n  [x] Highway 407\n  | | \n  | | \n  [ ] Pioneer Village\n  | | \n")
          
#For any user with an IP address within 10.120.192.0/18
     elif re.search("10.120.(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):
          exit("You are at Vaughan Metropolitan Centre Station. \n\n  [x] Vaughan Metropolitan Centre\n  | | \n  | | \n  [ ] Highway 407\n  | | \n") 

#For any user with an IP address within 10.108.0.0/18
     elif re.search("10.108.([0-9]|[1-5][0-9]|6[0-3]).*", IP):
          exit("You are at Bayview Station. \n\n [ ] Sheppard-Yonge ===== [x] Bayview =====[ ] Bessarion \n")

#For any user with an IP address within 10.108.64.0/18
     elif re.search("10.108.(6[4-9]|[7-9][0-9]|1[0-1][0-9]|12[0-7]).*", IP):
          exit("You are at Bessarion Station. \n\n [ ] Bayview ===== [x] Bessarion =====[ ] Leslie \n")

#For any user with an IP address within 10.108.128.0/18
     elif re.search("10.108.(12[8-9]|1[3-8][0-9]|19[0-1]).*", IP):
          exit("You are at Bessarion Station. \n\n [ ] Bessarion ===== [x] Leslie =====[ ] Don Mills \n")

#For any user with an IP address within 10.108.192.0/18
     elif re.search("10.108.(19[2-9]|2[0-4][0-9]|25[0-5]).*", IP):
          exit("You are at Don Mills Station. \n\n [ ] Leslie ===== [x] Don Mills\n")
          
#For any user with an IP address within 10.10.100.0/22
     elif re.search("10.10.10[0-2].([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-4])", IP):
          exit("\n\nYou are on the TTC Bus System: Public WiFi")
          
#For any user that inputted the network router (the first host device)
     elif re.search("10.10.100.1", IP):
          exit("You are the networking router\n")
 
#For any use that inputted the network address (The first IP address of the subnet)         
     elif re.search("10.10.100.0", IP):
          exit("This is the network address\n")

#For any user that inputted the broadcast address (The last IP address of the subnet)
     elif re.search("10.10.102.255", IP):
          exit("This is the broadcasting address\n")
    
#In case some cracks exist through the regex calculations
     else:
          exit("IP Address invalid try again.")
          
#In case the IP address does not get entered into the While Loop          
print("This script went nowhere...")
          


