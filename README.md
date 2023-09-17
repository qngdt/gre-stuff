# What is this?
---
- This repo is used to extract words from [TTP's GRE Vocabulary PDF](https://gre.blog.targettestprep.com/gre-vocabulary/) using OpenAI GPT-3.5 API and Langchain

## Requirements
- An `.env` file containing `OPENAI_API_KEY`

## Contents
- `main.py`: Extracting words from each page of the PDF and saving them to the `output` folder
- `anki.py`: Import the data from `output` folder to Anki
