import argparse
from hsanagrams.anagrams import Anagrams

def main(word, wordspath):
    anagrams = Anagrams(wordspath)
    print(anagrams.get_anagrams(word))



def mainexternal():
    parser = argparse.ArgumentParser(description="Process a file with optional settings.")
    parser.add_argument("word", help="Word")
    parser.add_argument("filename", help="The target file to process")  # Positional (required)
    args = parser.parse_args()
    main(args.word, args.filename)

if __name__ == "__main__":
    mainexternal()
