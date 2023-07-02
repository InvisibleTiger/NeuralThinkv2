import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def summarize(url):
    response = requests.get(url)
    response.close()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text data from website
    text_data = ''
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        text_data += tag.get_text()
    # print(text_data)

    if len(text_data) > 1024:
        text_data = text_data[:1024]

    # Load the summarization pipeline
    summarizer = pipeline("summarization")
    summary=summarizer(text_data, max_length=130, min_length=30, do_sample=False)

    return (summary[0]['summary_text'])