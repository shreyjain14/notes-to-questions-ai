from dotenv import load_dotenv
import anthropic
import os

load_dotenv()

IN_FOLDER = 'G:\\My Drive\\Study\\UNIX\\txt'
OUT_FOLDER = 'G:\\My Drive\\Study\\UNIX\\md'

client = anthropic.Anthropic(
    api_key=os.getenv('ANTHROPIC-API-KEY'),
)


def ask_AI(note):
    with open(os.path.join(IN_FOLDER, note), encoding='utf-8') as f:
        data = f.read()

    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        system="THE USER WILL SEND NOTES CREATE QUESTIONS AND REPLY WITH THE QUESTIONS YOU CREATED ALONG WITH THEIR ANSWERS IN THE FOLLOWING FORMAT:\n\n# Title of the questions (Eg: UNIX SYSTEM ADMINSTRATOR)\n\n### 1. Question\nAnswer here and **bold important information** in the answer\n\n### 2. Question\n- use \n- pointers\n- if possible\n\n### 3. Question\n`use code blocks for code`",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": data
                    }
                ]
            }
        ]
    )

    with open(os.path.join(OUT_FOLDER, f'{note[:-4]}.md'), 'w') as f:
        f.write(message.content[0].text)


if __name__ == '__main__':
    files = [f for f in os.listdir(IN_FOLDER)]
    f_len = len(files)
    for index, file in enumerate(files):
        print(f'[{index}/{f_len}] Creating Questions from {file}')
        ask_AI(file)
        print(f'[{index + 1}/{f_len}] Created Questions from {file}')


