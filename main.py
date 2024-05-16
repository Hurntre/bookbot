def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)

  print(f"--- Begin report of {book_path} ---")
  word_count = get_words_count(text)
  print(f"{word_count} words found in the document \n\n")

  char_count = get_letters_count(text)
  char_count_list = convert_dictionary_to_list(char_count)

  char_count_list.sort(reverse=True, key=sort_on)
  
  for entry in char_count_list:
    print(f"The '{entry["char"]}' character was found {entry["num"]} times")

  print("-- End report --")



def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_words_count(text):
  words = text.split()
  return len(words)

def get_letters_count(text):
  chars = {}
  for char in text:
    if char.isalpha():
      lowered_char = char.lower()
      if lowered_char in chars:
        chars[lowered_char] += 1
      else:
        chars[lowered_char] = 1
  return chars

def convert_dictionary_to_list(dictionary):
  dictionary_list = []
  for key in dictionary:
    dictionary_list.append({ "char": key, "num": dictionary[key]})
  return dictionary_list

def sort_on(dict):
  return dict["num"]




main()