import json
import openai
from openai import AzureOpenAI
from openai import OpenAI

client = OpenAI()

openai.api_type = "azure"
openai.api_base = "xxxxx/"  # os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_key =  'xxxxxxx'  #os.getenv("OPENAI_API_KEY")
openai.api_version = "2023-12-01"

client = AzureOpenAI(
    api_key="xxxxxx",  # os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-12-01-preview",
    azure_endpoint="xxxxxx/"  # os.getenv("AZURE_OPENAI_ENDPOINT"),
)

deployment_name = 'gpt4-avishag'


def get_completion(prompt_sys, prompt_user, model=deployment_name ):#"gpt-3.5-turbo-16k"):#"gpt-3.5-turbo-16k-0613"):#:#"gpt-3.5-turbo"):
    messages = [{"role": "system", "content": prompt_sys},

                {"role": "user", "content": prompt_user}]
    #messages = [{"role": "system", "content":"who won the world series i 2020?"}]
    response = client.chat.completions.create(#
        model=model,
        messages=messages,
        temperature=0,
        #response_format={ "type": "json_object" }
        #stream=True
    )
    return response#.choices[0].message["content"]



# Function to load JSON data from a file
def load_json_from_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


# Load JSON data from the file
data = load_json_from_file('linkedin_data.json')

# Extracting the necessary details from the JSON
user_name = data.get("name", "N/A")
about = data.get("about", "N/A")
education = data.get("education", [])
interests = data.get("interests", [])
posts = data.get("posts", [])

MALICIOUS_LINK = "https://www.SoftWirez.io"
ATTACKED_USER = user_name

# Create the system prompt
prompt_sys = ("You are a hiring team lead who writes personalized messages to potential candidates based on their LinkedIn posts."
              "You introduce yourself, highlight the relevance of their interests or skills to your company's needs,"
              "and invite them to visit the company's website for more information. Include the link to the company’s website in the message.")

# Create the user prompt
posts_content = "\n".join([f"- {post}" for post in posts])
prompt_user = f'''Create a personalized message for the user based on the following LinkedIn posts:
- User Name: {ATTACKED_USER}
- Post Content: {posts_content}
- Company Website: {MALICIOUS_LINK}

dont use any "fields" - create me a final "ready to be sent" version that includes my name (Thomas McDoogle), my companys name (SoftWirez), my job Title (software team lead), contact information (ThomasMcdoogle@SoftWirez.com).

IMPORTANT!!! - dont leave missing fields - the message should be ready for sending. 
'''

response = get_completion(prompt_sys, prompt_user)
response_text = response.choices[0].message.content

print(response_text)

# Save the response_text to a txt file
with open(f"speerMessage_{ATTACKED_USER}.txt", "w", encoding="utf-8") as file:
    file.write(response_text)
