"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто
встречающееся и самое длинное.
"""


MIN_WORD_LENGTH = 4


def get_text_stats(text: str) -> dict:
    # Remove punctuation marks and split by word
    text = text.replace(".", " ").replace(",", " ").split()

    # Calculate word stats in the text
    result = {}
    for word in text:
        # Remove spaces around the word
        word = word.strip()

        # Skip "small" words
        if len(word) < MIN_WORD_LENGTH:
            continue

        # Check if we already found current word
        if word in result:
            result[word]["count"] += 1
        else:
            # We add initial value and use a word as a key
            result[word] = {
                "length": len(word),
                "count": 1
            }
    return result


def get_most_frequent_word(text_stats: dict) -> str:
    # Assume that first word (text stats key) is the most frequent
    most_frequent = list(text_stats.keys())[0]

    # Try to find a word that is more frequent
    for word, stats in text_stats.items():
        if text_stats[most_frequent]["count"] < stats["count"]:
            most_frequent = word
    return most_frequent


def get_longest_word(text_stats: dict) -> str:
    # Assume that first word (text stats key) is the longest
    longest = list(text_stats.keys())[0]

    # Try to find a word that is more frequent
    for word, stats in text_stats.items():
        if text_stats[longest]["length"] < stats["length"]:
            longest = word
    return longest


example_text = """
    Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind 
    texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A 
    small river named Duden flows by their place and supplies it with the necessary regelialia. It is a 
    paradisematic country, in which roasted parts of sentences fly into your mouth. Even the all-powerful Pointing 
    has no control about the blind texts it is an almost unorthographic life.
"""

example_stats = get_text_stats(example_text)
print("Longest word: ", get_longest_word(example_stats))
print("Most frequent word: ", get_most_frequent_word(example_stats))
