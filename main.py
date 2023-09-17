from io import StringIO
import json
from dotenv import load_dotenv
from pdfminer.high_level import extract_text
from langchain.chat_models import ChatOpenAI
from langchain.chains import create_extraction_chain


output_string = StringIO()

load_dotenv()

PAGES = 70

for page in range(23, PAGES + 1):
    print("Extracting page", page)
    text = extract_text("gre_vocab.pdf", page_numbers=[page])

    schema = {
        "properties": {
            "number": {"type": "integer"},
            "word": {"type": "string"},
            "word_type": {"type": "string"},
            "meaning": {"type": "string"},
        },
    }

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    chain = create_extraction_chain(schema, llm)
    res = chain.run(text)
    output_path = f"output/data-{page}.json"
    with open(output_path, "w") as output_file:
        output_file.write(json.dumps(res))

    print("Wrote to", output_path)
    print("--------------------")
