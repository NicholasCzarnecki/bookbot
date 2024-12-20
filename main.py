def main(): 
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  print(f"There are {count_words(text)} words in this document.")
  print(count_characters(text))

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  return len(text.split())  

def count_characters(text):
  lower_text = text.lower()
  char_dict = {}
  for char in lower_text: 
    if char not in char_dict:
      char_dict[char] = 1
    else:
      char_dict[char] += 1
  return char_dict

main()