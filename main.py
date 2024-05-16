import os
import sys
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format

def clear_terminal():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

# Initialize colorama
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

def display_welcome_message():
    clear_terminal()
    cprint(figlet_format('Cipher', font='starwars'),
           'green', 'on_black', end='')

# Define the menu structure using a nested dictionary
menu = {
    "1": {
        "SearchEngines": {
            "1": "Ahmia",
            "2": "Haystak",
            "3": "Torch",
            "4": "DuckDuckGo",
            "5": "TheHiddenWiki",

            # Add more search options here
        }
    },
    "2": {
        "Email + Messaging": {
            "1": "Mail2Tor",
            "2": "Elude.in",
            "3": "ProtonMail",
            "4": "DNMX",
            "5": "Onion Mail",
            # Add more watch options here
        }
    },
    "3": {
        "Commercial Services": {
            "1": "FakeId Store",
            "2": "WhiteRabbit",
            "3": "Rent-A-Hacker",
            "4": "CryptoHackers",
            "5": "Onion Identity Services",

            # Add more search options here
        },
    },
    "4": {
        "Financial Services": {
            "1": "The Green Machine",
            "2": "Hidden Wallet",
            "3": "Cash Machine",
            "4": "Walt Cards",
            "5": "Imperial Market",

            # Add more search options here
        }
    },
    "5": {
        "ChatRooms": {
            "1": "Black Hat Chat",
            "2": "Ableonion",
            "3": "Mega Tor",
            "4": "Semen Alert",
            "5": "Random",

            # Add more search options here
        }
    },
    # Add more categories here

}

# Define URLs for selected options
option_urls = {
    "Ahmia": "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/",
    "Haystak": "http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/",
    "Torch": "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/",
    "DuckDuckGo": "duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion",
    "TheHiddenWiki": "zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion",
    "Black Hat Chat": "http://blkhatjxlrvc5aevqzz5t6kxldayog6jlx5h7glnu44euzongl4fh5ad.onion/",
    "Ableonion": "http://notbumpz34bgbz4yfdigxvd6vzwtxc3zpt5imukgl6bvip2nikdmdaad.onion/",
    "Mega Tor": "http://ylmjp76zk4ndvgpncbtgzrfsrzpblvlzgtuoduqgygwdlexou64iwfqd.onion/",
    "Semen Alert": "http://ejaculatelqqkdhpjvjzhjpuldfuup2q37cfgmf6eknikq5xkliep4yd.onion/",
    "Random": "http://notbumpz34bgbz4yfdigxvd6vzwtxc3zpt5imukgl6bvip2nikdmdaad.onion/",
    "Mail2Tor": "mail2torjgmxgexntbrmhvgluavhj7ouul5yar6ylbvjkxwqf6ixkwyd.onion",
    "Elude.in": "eludemailxhnqzfmxehy3bk5guyhlxbunfyhkcksv4gvx6d3wcf6smad.onion",
    "ProtonMail": "protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion",
    "DNMX": "dnmxjaitaiafwmss2lx7tbs5bv66l7vjdmb5mtb3yqpxqhk3it5zivad.onion",
    "Onion Mail": "pflujznptk5lmuf6xwadfqy6nffykdvahfbljh7liljailjbxrgvhfid.onion",
    "White Rabbit": "wrabbitzqridxnvqevem4hayi5wkbeauqbt66v4dabm5y3gmddgbcqyd.onion",
    "FakeId Store": "fakeid6mmmaqes6odqilvawtfkfwydu47a2cp77uvtrxck5m4p6wo6yd.onion",
    "Rent-A-Hacker": "jn6weomv6klvnwdwcgu55miabpwklsmmyaf5qrkt4miif4shrqmvdhqd.onion",
    "CryptoHackers": "cryptobcgaxxj35k3yvcyaaxm5c6si5sufq4sck3pgxlbu6qt23goqqd.onion",
    "Onion Identity Services": "endtovmbc5vokdpnxrhajcwgkfbkfz4wbyhbj6ueisai4prtvencheyd.onion",
    "The Green Machine": "vw5vzi62xqhihghvonatid7imut2rkgiudl3xomj4jftlmanuwh4r2qd.onion",
    "Hidden Wallet": "d46a7ehxj6d6f2cf4hi3b424uzywno24c7qtnvdvwsah5qpogewoeqid.onion",
    "Cash Machine": "n3irlpzwkcmfochhuswpcrg35z7bzqtaoffqecomrx57n3rd5jc72byd.onion",
    "Imperial Market": "imperialk4trdzxnpogppugbugvtce3yif62zsuyd2ag5y3fztlurwyd.onion",
    "Walt Cards": "waltc5t7hd6kp2rhwf2onyamo2o3qag6cfuv27yquwo3uaasxupnazqd.onion",
    


    # Add more URLs here
}

def main():
    display_welcome_message()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Welcome to Cipher, your gateway to the hidden web.")
    print("We have an extensive collection of websites, from search engines to commercial services and more.")
    print("Whether you're searching for information or looking for unique experiences, Cipher has you covered.")
    print("NOTE: This is for Educational Purposes Only ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

    # Ask the user if they want to proceed
    while True:
        proceed = input("Would you like to proceed? (yes/no): ")
        if proceed.lower() in ['yes', 'no']:
            if proceed.lower() == 'no':
                print("Thank you for considering Cipher. Goodbye!")
                return
            break
        print("Invalid input. Please type 'yes' or 'no'.")
    
    while True:
        # Display the welcome message
        display_welcome_message()
        
        # Display the menu
        print("Menu:")
        for category_key, category_value in menu.items():
            print(f"{category_key}. {list(category_value.keys())[0]}:")
            for option_key, option_value in category_value.items():
                for index, option in enumerate(option_value, start=1):
                    print(f"    {index}. {option_value[option]}")
        
        # Get user input for category
        category = input("\nChoose a category (1, 2, 3, 4, 5.): ")
        if category in menu:
            category_options = menu[category]
            category_name = list(category_options.keys())[0]
            options = category_options[category_name]
            
            # Get user input for option
            option_index = input(f"Choose an option (1-{len(options)}): ")
            if option_index.isdigit() and 1 <= int(option_index) <= len(options):
                selected_option = list(options.values())[int(option_index) - 1]
                print("You chose:", selected_option)
                # Check if URL is available for the selected option
                if selected_option in option_urls:
                    url = option_urls[selected_option]
                    print(f"Here is the URL to {selected_option}: {url}")
                else:
                    print("No URL available for the selected option.")
            else:
                print("Invalid option index.")
        else:
            print("Invalid category.")
        
        # Ask the user if they want to choose again
        while True:
            choice = input("\nDo you want to choose again? (yes/no): ")
            if choice.lower() in ['yes', 'no']:
                break
            print("Invalid input. Please type 'yes' or 'no'.")
            
        if choice.lower() != 'yes':
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Thank you for exploring the hidden web with Cipher.")
            print("Note: This is for Educational Purposes Only")
            print("Stay safe and curious!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Made By Kotlin ♥")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


            break

if __name__ == "__main__":
    main()
