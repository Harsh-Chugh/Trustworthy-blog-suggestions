from metaphor_python import Metaphor
import re
import bardapi
import os
from urllib.parse import urlparse


client = Metaphor(api_key="METAPHOR_API_KEY")

token = 'BARD_API_KEY'
# bard = bardapi.core.Bard(token)

TOPIC_MESSAGE = "You are an intelligent assistant. I will provide you a text and you need to find out the content category of that text in no more than 4 words and output only that no other words: "

def search():
    
    user_query = input("What do you want to read about: ")
    topic = bardapi.core.Bard(token).get_answer(TOPIC_MESSAGE + user_query)['content']

    ###############################################################################
    # assign topic with a call to bard

    # topic = "cryptocurrency"
    print("topic: ", topic)
    relevant_response = client.search("Here are 10 most reliable websites about " + topic, 
        num_results= 10
    )

    url_array=[]

    for result in relevant_response.results:
        url_array.append(result.url)

    print(url_array, end="\n\n\n")

    domain_array=[]
    # domain = urlparse('http://www.example.test/foo/bar?var=3').netloc
    # print(domain) # --> www.example.test
    for url in url_array:
        domain_array.append(urlparse(url).netloc)

    print(domain_array, end="\n\n\n")


    response = client.search(user_query,
        num_results=1,
        include_domains=domain_array
    )

    # print fetched blog title and url
    # for result in response.results:
    #     print(result.title, result.url)

    id=response.results[0].id
    print(id, end="\n\n\n")

    response = client.get_contents(id)

    blog_content = response.contents[0].extract
    print(blog_content, end="\n\n\n")

    print("######\n\n\n")

    data = re.sub(r'<.*?>', '', blog_content)
    print(data, end="\n\n\n")
    print(response.contents[0].url)

    return response.contents[0].url

def get_similar_link(URL):
    print(1)
def get_random_result():
    print(2)


user_input = "random"
URL = ""

while user_input != 'quit':
    input()
    if(user_input == "similar"):
        URL = get_similar_link(URL)
    elif(user_input == "random"):
        URL = get_random_result()
    else:
        URL = search()

    user_input = input("random, similar or quit: ")
        



# # set your __Secure-1PSID value to key
# token = 'BARD_API_KEY'
# # set your input text
# input_text = "You are a helpful assisstant. Give tips on how to write resume"

# # Send an API request and get a response.
# response = bardapi.core.Bard(token).get_answer(input_text)
# print(response['content'])

