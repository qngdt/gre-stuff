import genanki
import json

model = genanki.Model(
    1607392319,
    "GRE Vocab Model",
    fields=[
        {"name": "Number"},
        {"name": "Word"},
        {"name": "Type"},
        {"name": "Meaning"},
    ],
    templates=[
        {
            "name": "GRE Word",
            "qfmt": "{{Number}}: {{Word}}",
            "afmt": "{{FrontSide}}<hr id='answer'>({{Type}})<br>{{Meaning}}",
        }
    ],
)

deck = genanki.Deck(
    2059400110,
    "GRE Vocab",
)

PAGES = 70

for i in range(1, 70):
    with open(f"output/data-{i}.json") as f:
        print("i", i)
        data = json.load(f)
        for word in data:
            print("word", word)
            note = genanki.Note(
                model=model,
                fields=[
                    str(word["number"]),
                    word["word"],
                    word["word_type"],
                    word["meaning"],
                ],
            )
            deck.add_note(note)

genanki.Package(deck).write_to_file("gre-vocab.apkg")
