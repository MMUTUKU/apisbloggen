import openai
from dotenv import dotenv_values

# Load API key
config = dotenv_values(".env")
openai.api_key = config.get('API_KEY')

def generate_blog(paragraph_topic):
    response = openai.Completion.create(
        model='gpt-3.5-turbo-instruct',
        prompt=f'Write a paragraph about the following topic: {paragraph_topic}',
        max_tokens=400,
        temperature=0.3
    )

    return response.choices[0].text.strip()

keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? (Y for yes, anything else for no): ').strip().lower()
    if answer == 'y':
        paragraph_topic = input("What should this paragraph talk about? ")
        print(f"\n{generate_blog(paragraph_topic)}\n")
    else:
        keep_writing = False
