import webbrowser
from webbrowser import *
print("""Choose the website
 1 - Facebook
 2 - Instagram
 3 - Twitter
 4 - LinkedIn
 5 - GitHub
 6 - WhatsApp
 7 - Telegram""")
SocialWebsite = input("Enter the website name:...")
if SocialWebsite == "Facebook":
    webbrowser.open("facebook.com/Ma7moudA7md99")
elif SocialWebsite == "Instagram":
    webbrowser.open("instagram.com/ma7mouda7md99")
elif SocialWebsite == "Twitter":
    webbrowser.open("twitter.com/Ma7moudA7md99")
elif SocialWebsite == "LinkedIn":
    webbrowser.open("linkedin.com/in/ma7mouda7md99")
elif SocialWebsite == "GitHub":
    webbrowser.open(" github.com/Ma7moudA7md99")
elif SocialWebsite == "WhatsApp":
    webbrowser.open("wa.me/qr/7D6UMBWLW6RHB1")
elif SocialWebsite == "Telegram":
    webbrowser.open("t.me/Ma7moudA7md99")
else:
    print("Please check the website name...")
input("type anything to exit:...")
