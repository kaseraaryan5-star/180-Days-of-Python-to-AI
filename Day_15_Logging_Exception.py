import os
import sys
import logging
from datetime import datetime

# ==========================================
# 1. LOGGING SETUP (Krish Naik Sir's Logic)
# ==========================================
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.join(os.getcwd(), "logs"), exist_ok=True)
LOG_FILE_PATH = logs_path

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# ==========================================
# 2. CUSTOM EXCEPTION HANDLING SETUP
# ==========================================
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script name [{file_name}] line number [{line_number}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

# ==========================================
# 3. CODE EXECUTION & TESTING
# ==========================================
if __name__ == "__main__":
    try:
        logging.info("Logging successfully shuru ho chuka hai!")
        print("Code running... Chaliye ek error create karte hain.")
        
        # Jaan-bujhkar error (1 / 0) create kar rahe hain test karne ke liye
        result = 1 / 0
        
    except Exception as e:
        logging.error("Ek exception (galti) encounter hui hai.")
        # Custom error raise karna jo exact line batayega
        raise CustomException(e, sys)