from time import sleep

print(
    """
██╗███╗   ██╗████████╗███████╗██████╗ ███╗   ██╗███████╗████████╗    ███████╗██████╗ ███████╗███████╗██████╗ 
██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗████╗  ██║██╔════╝╚══██╔══╝    ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗
██║██╔██╗ ██║   ██║   █████╗  ██████╔╝██╔██╗ ██║█████╗     ██║       ███████╗██████╔╝█████╗  █████╗  ██║  ██║
██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗██║╚██╗██║██╔══╝     ██║       ╚════██║██╔═══╝ ██╔══╝  ██╔══╝  ██║  ██║
██║██║ ╚████║   ██║   ███████╗██║  ██║██║ ╚████║███████╗   ██║       ███████║██║     ███████╗███████╗██████╔╝
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝       ╚══════╝╚═╝     ╚══════╝╚══════╝╚═════╝ 
                                                                                                             
         ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗      █████╗ ██╗███╗   ██╗███████╗██████╗                     
        ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║     ██╔══██╗██║████╗  ██║██╔════╝██╔══██╗                    
        ██║     ██║   ██║██╔████╔██║██████╔╝██║     ███████║██║██╔██╗ ██║█████╗  ██████╔╝                    
        ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══██║██║██║╚██╗██║██╔══╝  ██╔══██╗                    
        ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ███████╗██║  ██║██║██║ ╚████║███████╗██║  ██║                    
         ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝                    
"""
)

sleep(1); print("This is the setup of this little software, that is as your guessed analyse your internet bandwidth daily to verify the promise given to you by your ISP. These inforamation are importent to complete your personal automated complainer, for more impormation, please visit: https://github.com/RedeemedSpoon/Internet-Speed-Complainer")
sleep(2); print("let's start :\n"); sleep(1)

def verify(question, type="str"):
    while True:
        anwser = input(question)
        if type == "str":
            try:
                return str(anwser)
            except:
                print("Error, not a string")
        if type == "int":
            try:
                return int(anwser)
            except:
                print("Error, not an int")

ISP = verify("What is your internet service provider (ex: verizon, comcast)?\nIt must be the twitter/x name of the company including the '@' : ")
PROMISED_DL = verify(f"What is the promised Internet download speed by {ISP}? \nIt must be the an interger : ", "int")
PROMISED_UP = verify(f"What is the promised Internet upload speed by {ISP}? \nIt must be the an interger : ", "int")
AVG_SPEED = verify("How long do you want the test to last in second? The recommended duration is around 45 second\nIt must be an interger: ", "int")
BROWSER = verify("What browser do you use? 'Firefox', 'Chrome', 'Edge',  'Safari' ?\nIt must between these for, and no other browser in supported : ").capitalize()
TWITTER_USERNAME = verify("What is your twitter/x Username \nIt must include the '@' : ")
TWITTER_PASSWORD = verify(f"What is {TWITTER_USERNAME}'s password ?\nPlease type it correctly : ")

with open("data.py", "w") as data_file:
    data_file.write(f"ISP = '{ISP}'\n")
    data_file.write(f"PROMISED_DL = {PROMISED_DL}\n")
    data_file.write(f"PROMISED_UP = {PROMISED_UP}\n")
    data_file.write(f"TWITTER_USERNAME = '{TWITTER_USERNAME}'\n")
    data_file.write(f"TWITTER_PASSWORD = '{TWITTER_PASSWORD}'\n")
    data_file.write(f"BROWSER = '{BROWSER}'\n")
    data_file.write(f"AVG_SPEED = {AVG_SPEED}\n")
    data_file.write(f"START_TWEET = 'Hey, {ISP}! Why is my internet speed'\n")
    data_file.write(f"END_TWEET = 'When I pay for {PROMISED_DL}dl/{PROMISED_UP}up?'\n")

sleep(1.5)
print("\nAlright! We finised the setup of your program. To automate it, please read our documentation at https://github.com/RedeemedSpoon/Internet-Speed-Complainer/")
