from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from g4f.client import Client

chats = [
    {"role": "user", "content": "What is the official website of the Zambia Revenue Authority?"},
    {"role": "assistant", "content": "The official website of the Zambia Revenue Authority (ZRA) is www.zra.org.zm. You can visit the website to access information about taxes in Zambia, including tax types, tax brackets, and the importance of paying taxes. The website also provides links to relevant resources, contact information for ZRA offices, and other services offered by the ZRA."},
    
    {"role": "user", "content": "How can I contact the Zambia Revenue Authority?"},
    {"role": "assistant", "content": "You can find contact information for the Zambia Revenue Authority on their Contact Us page at www.zra.org.zm/contact-us. This page includes phone numbers, email addresses, and physical addresses of ZRA offices."},
    
    {"role": "user", "content": "What types of taxes are there in Zambia?"},
    {"role": "assistant", "content": "You can learn about the various types of taxes in Zambia on the ZRA Tax Types page at www.zra.org.zm/types-of-taxes. This page provides detailed information about Income Tax, Corporate Tax, Value Added Tax (VAT), Withholding Tax, Property Transfer Tax, and Mineral Royalty Tax."},
    
    {"role": "user", "content": "Where can I find the Income Tax Guide for Zambia?"},
    {"role": "assistant", "content": "The Income Tax Guide for Zambia is available on the ZRA Income Tax Guide page at www.zra.org.zm/income-tax. This guide provides comprehensive information about income tax rates, tax brackets, and filing procedures."},
    
    {"role": "user", "content": "Where can I find information about Corporate Tax in Zambia?"},
    {"role": "assistant", "content": "Information about Corporate Tax in Zambia is available on the ZRA Corporate Tax Guide page at www.zra.org.zm/corporate-tax. This page provides details on corporate tax rates, filing requirements, and other relevant information."},
    
    {"role": "user", "content": "Where can I find the VAT Guide for Zambia?"},
    {"role": "assistant", "content": "The VAT Guide for Zambia is available on the ZRA VAT Guide page at www.zra.org.zm/value-added-tax. This guide includes information on VAT rates, registration requirements, and filing procedures."},
]

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
    # Create a new instance of the client
    global chats
    chats.append({"role": "user", "content": text})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": chats}],
    )

    print(f"Bot: {response.choices[0].message.content}")
    ans=response.choices[0].message.content 
    chats.append({"role": "assistant", "content": ans})

    return ans


if __name__ == '__main__':
    client = Client()
    app.run()
