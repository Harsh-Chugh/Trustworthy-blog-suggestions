from metaphor_python import Metaphor
import re

client = Metaphor(api_key="METAPHOR_API_KEY")


response = client.search("funny article about tech culture",
    num_results=1
)

# print fetched blog title and url
# for result in response.results:
#     print(result.title, result.url)

id=response.results[0].id
print(id)

response = client.get_contents(id)

blog_content = response.contents[0].extract
print(response.contents[0].extract)

print("######\n")

data = re.sub(r'<.*?>', '', blog_content)
print(data)

# from urllib.parse import urlparse

# domain = urlparse('http://www.example.test/foo/bar?var=3').netloc
# print(domain) # --> www.example.test

# import bardapi
# import os

# # set your __Secure-1PSID value to key
# token = 'BARD_API_KEY'

# # set your input text
# input_text = "You are a helpful assisstant. Give tips on how to write resume"

# # Send an API request and get a response.
# response = bardapi.core.Bard(token).get_answer(input_text)
# print(response['content'])

