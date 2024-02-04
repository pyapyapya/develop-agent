import os
import json

import openai
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from dotenv import load_dotenv

from tools import tools
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
user_input = input("검색어를 입력해주세요 ")


def get_title(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")
    for title in soup.find_all('title'):
        return title.get_text()

def get_url_from_query(query) -> str:
    url_list = []
    urls = search(query, num_results=5, lang="ko")
    for url in urls:
        if url.endswith(".pdf"):
            continue

        url_list.append(f"{get_title(url)}: {url}")
    return "\n".join(url_list)

def get_product_price(query, name):
    # urls = get_url_from_query(query)
    urls = search(query, num_results=5, lang="ko")
    search_info = ""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    for url in urls:
        if url.endswith(".pdf"):
            continue
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')

        index = text.find(name)
        if index == -1:
            print("Not found")
        else:
            search_info += text[index:index+100]
    context = {"role": "user", "content": f"You are a web-agent. You provide a information to user's query {query} from {search_info}. If you can't answer the question, try to find a similar answer. user wait for your response 1 minute. You say Korean and kindly."}
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[context],
    )
    response = response.choices[0].message.content
    return response

def get_information_from_query(query):
    # urls = get_url_from_query(query)
    urls = search(query, num_results=3, lang="ko")
    search_info = ""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    for url in urls:
        if url.endswith(".pdf"):
            continue
        html = requests.get(url, headers=headers).content
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text().replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
        search_info += text[:2000]
    context = {"role": "user", "content": f"You are a web-agent. You need to answer what the user wants to know. If user want to know {user_input}, you should explain a search result from {search_info}. You must answer only what is relevant to the user's question. When you've gathered enough information to answer, you can stop reading and start explaining. You must answer Korean and kindly."}
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[context],
    )
    response = response.choices[0].message.content
    return response



response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": f"You are a web-agent. You provide information from user's query {user_input}."}],
    functions=tools,
    function_call="auto",
)
response = response.choices[0].message
if response.get("function_call"):
    available_functions = {
        "get_url_from_query": get_url_from_query,
        "get_product_price": get_product_price,
        "get_information_from_query": get_information_from_query,
    }
    function_name = response.get("function_call")["name"]
    function_args = json.loads(response.get("function_call")["arguments"])
    function_call = available_functions[function_name]
    result = function_call(*list(function_args.values()))
    print(f"-------------------\n{result}\n-------------------")