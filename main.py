#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun one-liner entry.

One funny line, under 200 characters, pitching a terrible pizza
topping: durian, the fruit already banned from hotels and airports
for its smell, now defeating the pizza itself — the cheese, which
survives everything, surrenders first.
"""
import os

ENTRY = "Durian: banned in 11 hotels, but on pizza it's somehow worse — the cheese surrenders first."


def main() -> None:
    assert len(ENTRY) < 200, "entry must stay under 200 characters"
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
