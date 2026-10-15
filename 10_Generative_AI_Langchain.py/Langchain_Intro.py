import os
import langchain
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI

# Environment variables load karein
load_dotenv(override=True)

print("LangChain Version:", langchain.__version__)
print("-" * 50)

groq_api_key = os.getenv("GROQ_API_KEY")
google_api_key = os.getenv("GEMINI_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY .env file mein nahi mili")
if not google_api_key:
    raise ValueError("GEMINI_API_KEY .env file mein nahi mili")


def run_model(title, model, prompt):
    """Model ko prompt bhejo aur output print karo."""
    response = model.invoke(prompt)
    print(f"--- {title} ---")
    print(response.text)
    print("-" * 50)


# ==========================================
# SECTION 1: GROQ MODEL INTEGRATION
# ==========================================
groq_model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=groq_api_key,
)
run_model("Groq Poem Output", groq_model, "Write a poem on Gaming")

# ==========================================
# SECTION 2: GOOGLE GEMINI INTEGRATION
# ==========================================
gemini_model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=google_api_key,
)
run_model("Gemini Essay Output", gemini_model, "Write an essay on AI")



# Streaming and Batch
#Streaming 

for chunk in groq_model.stream("Write me a 500 words paragraph on AI"):
    print(chunk.text, end="", flush=True)
print()

#Batch

prompts = [
    "Write a haiku on AI",
    "Explain RAG in one line",
    "Give 3 uses of vector databases",
]
results = groq_model.batch(prompts)
for r in results:
    print(r.text)
    print("-" * 50)