import discord
import json
import os
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
        


TOKEN = "<yourtoken>"
memberid = "<yourid>"


@bot.event
async def on_ready():
    member = bot.get_user(memberid)
    print(f"""
        {Fore.WHITE} Logged on to:{Fore.BLUE} {bot.user} {Fore.RESET}
            {Fore.CYAN} MENU : SCRAPING 
                        By peak#0001 {Fore.RESET}


        {Fore.GREEN} [1] {Fore.RESET}{Fore.BLUE}Scrape a guild member's ids {Fore.RESET}

        {Fore.GREEN} [2] {Fore.RESET}{Fore.BLUE}Mass invite to guilds {Fore.RESET}

        {Fore.GREEN} [3] {Fore.RESET}{Fore.BLUE}Fetch all servers (w/membercount) {Fore.RESET}

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
                     print(f"{Fore.GREEN}[-] {Fore.RESET}{Fore.RED} Failed to scrape {member} ({member.id}) {Fore.RESET} ")
            print(f"\n{Fore.GREEN}[=] {Fore.WHITE} Fetched all members for {Fore.BLUE}{guild.name}{Fore.WHITE}, and sent to {Fore.BLUE}ids.json{Fore.WHITE} file {Fore.RESET}")
                   
        else:
            print(F"{Fore.GREEN}[-] {Fore.RESET}{Fore.RED} Im not in the guild or its not a guild. {Fore.RESET}")            
            
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
                            print(f"{Fore.GREEN}    [-] {Fore.RED} Couldnt find/dm the owner of {guild.name} {Fore.RESET}")
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
            print(f"{Fore.GREEN}[=] {Fore.BLUE}{guild}{Fore.CYAN} ({guild.id} - {len(guild.members)} Members){Fore.WHITE} (TOTAL:{count}/{len(bot.guilds)}){Fore.RESET}")
            sleep(0.01)
        print(f"\n{Fore.GREEN}[=] {Fore.WHITE} Fetched all servers that {bot.user} is in {Fore.RESET}")
    else:
        print("Please select an vaild option, Restarting", end="\r")
    

bot.run(TOKEN, bot = True)
