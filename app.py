from flask import Flask, render_template, request, jsonify
from langchain_openai import AzureChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

# import torch
# tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
# model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    return get_chat_response(input)

def get_chat_response(text):
    load_dotenv()
    
    # Setup of environment variables
    os.environ["AZURE_OPENAI_API_KEY"] = "<API_KEY>"
    os.environ["AZURE_OPENAI_ENDPOINT"] = "<OPENAI_ENDPOINT>"
    os.environ["AZURE_OPENAI_API_VERSION"] = "<OPENAI_API_VERSION>"
    os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = "<OPENAI_DEPLOYMENT_NAME>"
    os.environ["AZURE_OPENAI_USER_ID"] = "<OPENAI_USER_ID>"

    llm = AzureChatOpenAI(
        default_headers={
            "User-Id": os.getenv('AZURE_OPENAI_USER_ID')
        },
        temperature=0,
        deployment_name=os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT_NAME'),
        api_version=os.getenv('AZURE_OPENAI_API_VERSION')
    )
    
    for step in range(5):
        # new_user_input_ids = tokenizer.encode(str(text) + tokenizer.eos_token, return_tensors='pt')
        # bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids
        # chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        # return tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        
        return llm.invoke([HumanMessage('Hey, who are you?')]).content

if __name__ == '__main__':
    app.run()