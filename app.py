from metaphor_python import Metaphor
import re
import bardapi
import os
from urllib.parse import urlparse


# client = Metaphor(api_key="METAPHOR_API_KEY")
client = Metaphor(api_key="6f209af2-f0c9-46c3-b5e8-f21791576865")

# token = 'BARD_API_KEY'
token = 'bgipRD2u17OfJ4l-in6HtjKP5poyLrai9B7bu8F2mAvGepA445aAz55WiR4IecaOzucvqw.'
# bard = bardapi.core.Bard(token)

TOPIC_MESSAGE = "You are an intelligent assistant. I will provide you a text and you need to find out the content category of that text in no more than 4 words and output only that no other words: "

def search():
    
    user_query = input("What do you want to read about: ")
    topic = bardapi.core.Bard(token).get_answer(TOPIC_MESSAGE + user_query)['content']

    ###############################################################################
    # assign topic with a call to bard

    # topic = "cryptocurrency"
    print("topic: ", topic)
    relevant_response = client.search("This is the best website to learn about: " + topic, 
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

    id=response.results[0].id
    print(id, end="\n\n\n")

    response = client.get_contents(id)

    blog_content = response.contents[0].extract
    print(blog_content, end="\n\n\n")

    print("######\n\n\n")

    data = re.sub(r'<.*?>', '', blog_content)
    print(data, end="\n\n\n")
    print(response.contents[0].url)

    return response.contents[0]





def get_similar_link(previous):
    # print("##\n\n", previous, "##\n\n")
    blog_content = previous.extract
    data = re.sub(r'<.*?>', '', blog_content)

    topic = bardapi.core.Bard(token).get_answer(TOPIC_MESSAGE + data)['content']
    print("topic: ", topic)
    
    
    relevant_response = client.search("This is the best website to learn about: " + topic, 
        num_results= 10
    )
    url_array=[]
    for result in relevant_response.results:
        url_array.append(result.url)
    print(url_array, end="\n\n\n")

    domain_array=[]
    for url in url_array:
        domain_array.append(urlparse(url).netloc)
    print(domain_array, end="\n\n\n")

    response = client.find_similar(previous.url, 
        num_results=1,
        include_domains=domain_array
    )

    id=response.results[0].id
    print(id, end="\n\n\n")

    response = client.get_contents(id)

    blog_content = response.contents[0].extract
    print(blog_content, end="\n\n\n")

    print("######\n\n\n")

    data = re.sub(r'<.*?>', '', blog_content)
    print(data, end="\n\n\n")
    print(response.contents[0].url)

    return response.contents[0]


def get_random_result():
    print(2)


user_input = "random"
previous = ""

while user_input != 'quit':
    input()
    if(user_input == "similar"):
        previous = get_similar_link(previous)
    elif(user_input == "random"):
        previous = get_random_result()
    else:
        previous = search()

    user_input = input("random, similar or quit: ")
        



# # set your __Secure-1PSID value to key
# token = 'BARD_API_KEY'
# # set your input text
# input_text = "You are a helpful assisstant. Give tips on how to write resume"

# # Send an API request and get a response.
# response = bardapi.core.Bard(token).get_answer(input_text)
# print(response['content'])

