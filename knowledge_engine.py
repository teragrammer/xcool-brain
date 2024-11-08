import json


def load_context(topic):
    with open(f"context_packs/{topic}.json", "r") as file:
        return json.load(file)
