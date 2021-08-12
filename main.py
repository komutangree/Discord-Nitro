import random, string
import webbrowser
import time 
import requests 

num=input("Input How Many Codes To Generate And Check")

#f=open("Nitro Codes.txt", "w", encoding='utf-8')

print ("Wait, Generating For You!")

for n in range(int(num)):
  y = ''. join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range (16))
  
  url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + y + "?with_application=false&with_subscription_plan=true"

  r = requests.get(url)

  if r.status_code == 200:
    print(" Valid | {} ")
    print ("https://discord.gift/"+y)
    break
  else:
    print (" Invalid | {}")
    print ("https://discord.gift/"+y)
#  f.write ('https://discord.gift/')
#  f.write (y)
#  f.write("\n")

#f.close 

  #checkers#

#with open("Nitro Codes.txt") as f:
#    for line in f:
#      nitro = line.strip("\n")

#      url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

#      r = requests.get(url)

#      if r.status_code == 200:
#        print(" Valid | {} " .format(line.strip("\n")))
#        break
#      else:
#        print (" Invalid | {}" .format(line.strip("\n")))
input("The end ! Press Enter 5 times to close the program.")
input ("5")
input ("4")
input ("3")
input ("2")
input ("1")