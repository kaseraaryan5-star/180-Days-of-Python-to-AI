import langchain
print(langchain.__version__)

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

# Groq API Key सेट करें
os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')

# वर्तमान में एक्टिव सही मॉडल का उपयोग करें
model = init_chat_model("openai/gpt-oss-120b", model_provider="groq")
print(model)

# प्रॉम्प्ट रन करें
response = model.invoke('Write a poem on Gaming')
print(response.content)



# LLM MODEL INTEGRATION WITH GOOGLE GEMINI
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# .env फाइल का सटीक पाथ लोड करें
load_dotenv(override=True)

# या फिर आप सीधे अपनी की यहाँ सेट कर सकते हैं ताकि None न आए:
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(override=True)

# 'model_name' की जगह 'model' लिखें और सही मॉडल नाम दें
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
response = model.invoke('Write an essay on about AI')
print(response.content)