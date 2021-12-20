import discord
import json
import os
from discord import message
from discord import user
from discord.ext import commands
from time import sleep
from colorama import Fore


intents = discord.Intents().all()
bot = commands.Bot(command_prefix='?',intents=intents)
bot.remove_command('help')

def log_id(id):
    with open("ids.json", "r") as file:
        data = json.load(file)

    if id not in data:
        data.append(id)

        with open("ids.json", "w") as file:
            json.dump(data, file)

def masslog_id(id):
    with open("allids.json", "r") as file:
        data = json.load(file)

    if id not in data:
        data.append(id)

        with open("allids.json", "w") as file:
            json.dump(data, file)
        

TOKEN = "<yourtoken>"
memberid = "<yourid>"


@bot.event
async def on_ready():
    member = bot.get_user(memberid)
    print(f"""
        {Fore.WHITE} Logged on to:{Fore.BLUE} {bot.user} {Fore.RESET}
            {Fore.CYAN} MENU : SCRAPING 
                        By peak#0001 {Fore.RESET}


        {Fore.GREEN} [1] {Fore.RESET}{Fore.BLUE}Scrape a guild member's ids {Fore.RESET}        {Fore.GREEN} [4] {Fore.RESET}{Fore.BLUE}DM all users{Fore.RESET}

        {Fore.GREEN} [2] {Fore.RESET}{Fore.BLUE}Mass invite to guilds {Fore.RESET}              {Fore.GREEN} [5] {Fore.RESET}{Fore.BLUE}Mass DM server owners{Fore.RESET}

        {Fore.GREEN} [3] {Fore.RESET}{Fore.BLUE}Fetch all servers (w/membercount) {Fore.RESET}  {Fore.GREEN} [6] {Fore.RESET}{Fore.BLUE}Message spammer{Fore.RESET} 

      
    """)
    choice = input(f"{Fore.WHITE} => Select an option: ")

    if choice == "1":
        os.system("cls")
        sleep(0.5)
        print(f"""
            {Fore.CYAN} SERVER MEMBERS SCRAPER 
                            By peak#0001 {Fore.RESET}
            
         """)
        guild = input(f"{Fore.WHITE} => Enter the server/guild id you want to scrape: {Fore.RESET}")
        if not (int(guild) in bot.guilds):
            guild = bot.get_guild(int(guild))
            open("ids.json","w+").write("[]")
            for member in guild.members:
                try: 
                    log_id(member.id) 
                    print(f"{Fore.GREEN}[+] {Fore.GREEN}{Fore.BLUE} Scraped {member} ({member.id}) from {guild.name} {Fore.RESET}")
                    sleep(0.0005)
                except:
                     print(f"{Fore.GREEN}[!] {Fore.RESET}{Fore.RED} Failed to scrape {member} ({member.id}) {Fore.RESET} ")
            print(f"\n{Fore.GREEN}[=] {Fore.WHITE} Fetched all members for {Fore.BLUE}{guild.name}{Fore.WHITE}, and sent to {Fore.BLUE}ids.json{Fore.WHITE} file {Fore.RESET}")
                   
        else:
            print(F"{Fore.GREEN}[!] {Fore.RESET}{Fore.RED} Im not in the guild or its not a guild. {Fore.RESET}")            
            
    elif choice == "2":
        os.system("cls")
        sleep(0.5)
        print(f"""
            {Fore.CYAN} MASS SERVER INVITER 
                            By peak#0001 {Fore.RESET}
            
         """)
        count = 0
        if memberid == None:
            print(f"{Fore.GREEN}[-] {Fore.RED} Please add an member id to memberid varaible as stated in README.md. {Fore.RESET}")
        else:    
            for guild in bot.guilds:
                count = count + 1
                sleep(0.01)
                try:
                    channel = guild.channels[0]
                    link = await channel.create_invite(max_age = 240)
                    messageto = await bot.fetch_user(memberid)
                    await messageto.send(f"Invite to: {link} - {guild.owner}")
                    print(f"{Fore.GREEN}[=] {Fore.BLUE} Made invite for {guild}{Fore.CYAN}({guild.id} | {len(guild.members)} Members){Fore.WHITE} (TOTAL:{count}/{len(bot.guilds)}){Fore.RESET}")
                    sleep(1)
                except:
                    try: 
                        messageto = await bot.fetch_user(memberid)
                        await guild.owner.send(f"{messageto.name} wants to join **`{guild.name}`**, Please send {messageto} an invite as i couldnt. \n > `requested by {messageto}` *PS: If u get multiple of these message(s) just ignore if already invited.*")
                        print(f"{Fore.GREEN}    [-] {Fore.WHITE} Message guild owner of {guild.name} ({guild.owner}) {Fore.RESET}")
                    except:
                        print(f"{Fore.GREEN}    [!] {Fore.RED} Couldnt find/dm the owner of {guild.name} {Fore.RESET}")
            print(f"\n{Fore.GREEN}[=] {Fore.WHITE} Invited to all servers that {bot.user} is in {Fore.RESET}")

    elif choice == "3":
        os.system("cls")
        sleep(0.5)
        print(f"""
            {Fore.CYAN} SERVER LIST 
                        By peak#0001 {Fore.RESET}            
         """)
        count = 0
        print(f"{Fore.GREEN} [-] Fetching guilds... {Fore.RESET}")
        sleep(1)
        for guild in bot.guilds: 
            count = count + 1
            print(f"{Fore.GREEN}  [=] {Fore.BLUE}{guild}{Fore.CYAN} ({guild.id} - {len(guild.members)} Members){Fore.WHITE} (TOTAL:{count}/{len(bot.guilds)}){Fore.RESET}")
            sleep(0.01)
        print(f"\n{Fore.GREEN}  [=] {Fore.WHITE} Fetched all servers that {bot.user} is in {Fore.RESET}")

    elif choice == "4":
        os.system("cls")
        sleep(0.5)
        print(f"""
            {Fore.CYAN} MASS DM ALL USERS
                        By peak#0001 {Fore.RESET}            
         """)
        count = 0
        print(f"{Fore.GREEN}[-]  Fetching users... {Fore.RESET}")
        print(f"{Fore.GREEN} [=] {Fore.WHITE} Starting in 1.5 seconds \n > This has no threads so may take awhile.{Fore.RESET}")
        sleep(1.5)
        open("allids.json","w+").write("[]")
        for guild in bot.guilds:
                for member in guild.members:
                    try:
                        count = count + 1
                        masslog_id(member.id) 
                        print(f"{Fore.GREEN}  [+] {Fore.GREEN}{Fore.BLUE} Fetched {member} ({member.id}) from {guild.name} {Fore.RESET}")
                        sleep(0.000005)
                    except:
                        print(f"{Fore.GREEN}  [!] {Fore.RESET}{Fore.RED} Failed to scrape {member} ({member.id}) {Fore.RESET} ")
        print(f"\n{Fore.GREEN}[=] {Fore.WHITE} Fetched all members that {bot.user} has access to, and sent to {Fore.BLUE}allids.json{Fore.WHITE} file {Fore.RESET}")   
        os.system("cls")
        sleep(0.5)
        print(f"""
            {Fore.CYAN} MASS DM ALL USERS
                        By peak#0001 {Fore.RESET}            
         """)     
        print(f"{Fore.WHITE} Fetched {count} users of {bot.user} {Fore.RESET}\n")
        sendmsg = input(f"{Fore.WHITE} => Message to send: {Fore.RESET}")
        with open("allids.json", "r") as file:
            data = json.load(file)
        index = 0
        print("\n")
        for i in data:
            index += 1
            member = await bot.fetch_user(i)
            try:
                await member.send(sendmsg)
                print(f"{Fore.GREEN} [=] {Fore.BLUE} Sent message to {member.name} ({index}/{len(data)}) {Fore.RESET}")
                sleep(5)
            except Exception as e:
                print(f"{Fore.RED} [!] DIDNT SEND TO {member} - {Fore.RESET} {e}")

        print("{Fore.GREEN} [+] {Fore.BLUE} Finished mass dming {index} users {Fore.reset}")


    elif choice == "5":
        os.system("cls")
        sleep(0.5)
        print(f"""
            {Fore.CYAN} DM ALL SERVER OWNERS 
                        By peak#0001 {Fore.RESET}            
         """)
        count = 0
        print(f"{Fore.GREEN}[-]  Fetching guilds... {Fore.RESET}")
        sleep(0.5)
        ownermsg = input(f"{Fore.WHITE} => Message to send to Server Owners: {Fore.RESET}")
        messageto = await bot.fetch_user(memberid)
        important = "> **IMPORTANT MESSAGE FROM BOT OWNER**"
        await messageto.send("**__PREVIEW OF WHATS SENT TO OWNERS:__** ^^")
        await messageto.send(important)
        await messageto.send(ownermsg)
        for guild in bot.guilds: 
            count = count + 1
            try:
                print(f"{Fore.GREEN}  [=] {Fore.BLUE} Messaged owner of {guild}{Fore.CYAN} ({guild.id} - {len(guild.members)} Members){Fore.WHITE} (TOTAL:{count}/{len(bot.guilds)}){Fore.RESET}")
                await guild.owner.send(important)
                await guild.owner.send(ownermsg)
            except:
                print(f"{Fore.GREEN} [!] {Fore.RED} Couldnt find/dm the owner of {guild.name} {Fore.RESET}")    
        print(f"\n{Fore.GREEN}[=] {Fore.WHITE} Messaged all servers owner that {bot.user} is in {Fore.RESET}")

    elif choice == "6":
        os.system("cls")
        sleep(0.5)
        print(f"""
            {Fore.CYAN} MESSAGE SPAMMER 
                        By peak#0001 {Fore.RESET}            
        """)
        count = 0
        print(f"{Fore.GREEN} [-] Fetching users...\n {Fore.RESET}")
        sleep(0.5)
        username = input(f"{Fore.WHITE} => Send message to (ID): {Fore.RESET}")
        usermsg = input(f"{Fore.WHITE} => Message to send: {Fore.RESET}")
        amount = input(f"{Fore.WHITE} => How many messages to send: {Fore.RESET}")
        username = await bot.fetch_user(username)
        for i in range(int(amount)): 
            count = count + 1
            try:
                await username.send(usermsg)
                print(f"{Fore.GREEN}  [=] {Fore.BLUE} Messaged {username} (TOTAL:{count}/{amount}){Fore.RESET}")
                sleep(0.1)
            except Exception as e:
                        print(f"{Fore.RED}  [!] I CAN'T MESSAGE THIS USER: {Fore.RESET} {e}")

        print(f"\n{Fore.GREEN}[=] {Fore.WHITE} Finished the message(s) for {username} {Fore.RESET}")
    else:
        print("Please select an vaild option, Restarting", end="\r")



bot.run(TOKEN, bot = True)
