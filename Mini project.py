import sys
import random
# ऊपर: हमारे बनाए हुए दोनों टूल्स को यहाँ बुला लिया
from src.logger import logging
from src.exception import CustomException

if __name__ == "__main__":
    try:
        # ऊपर: गेम शुरू होते ही डायरी में एंट्री होगी
        logging.info("हमारा गेसिंग गेम और पासवर्ड जनरेटर शुरू हो गया है!")
        
        # 🎯 1. आपका पहला गेम: Guess Number
        target = random.randint(1, 100)
        while True:
            userChoice = input("Guess the target or Quit: ")
            if userChoice == "Quit" or userChoice == "quit":
                break
            
            userChoice = int(userChoice)
            if userChoice == target:
                print("Success : Correct Guess !!")
                break
            elif userChoice < target:
                print("your number was too small. Take a bigger guess...")
            else:
                print("your number was too big. Take a small guess...")
                
        print("-----GAME OVER-----")
        
        # 🔑 2. आपका दूसरा गेम: Random Password Generator
        print("\n--- Random Password Generator ---")
        import random
        # (यहाँ नीचे आप अपनी बची हुई पासवर्ड जनरेशन की लॉजिक लिख सकते हैं जो आपकी स्क्रीनशॉट में थी)
        
        # नीचे: दोनों गेम बिना किसी खराबी के खत्म होने पर डायरी में एंट्री
        logging.info("गेम सफलतापूर्वक खत्म हुआ।")

    except Exception as e:
        # नीचे: अगर गेम में कोई भी गड़बड़ हुई
        logging.error("गेम के अंदर कोई गड़बड़ हुई है!")
        raise CustomException(e, sys)