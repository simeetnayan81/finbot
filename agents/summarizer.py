# agents/summarizer.py

from autogen import AssistantAgent, UserProxyAgent
from config import GEMINI_API_KEY
from dotenv import load_dotenv

load_dotenv()

# Set up OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Please set OPENAI_API_KEY in your environment or .env file")


config_list =  {
        "model": "gemini-2.0-flash",
        "api_key": GEMINI_API_KEY,
        "api_type": "google",
    }


summarizer = AssistantAgent(
    name="GeminiSummarizer",
    llm_config=config_list,
    code_execution_config={"use_docker": False}
)

user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=3,
    is_termination_msg=lambda x: "FINAL SUMMARY" in x.get("content", "")
)

def summarize_articles(articles):
    summaries = []
    for article in articles:
        if not article: continue
        title = article['title']
        text = article['text']
        prompt = f"""You are a financial summarizer. Summarize the following article in 5 bullet points max:

Title: {title}

{text}

Respond with "FINAL SUMMARY" followed by the bullet points."""
        user_proxy.initiate_chat(summarizer, message=prompt)
        responses = user_proxy.chat_messages[summarizer]
        for msg in responses[::-1]:
            if "FINAL SUMMARY" in msg.get("content", ""):
                summaries.append(msg["content"])
                break
    return summaries
