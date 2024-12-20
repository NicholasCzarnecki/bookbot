def main(): 
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  counted_char_dict = count_characters(text)
  sorted_char_list= chars_dict_to_sorted_list(counted_char_dict)
  
  print(f"There are {count_words(text)} words in this document: {book_path}")
  print("\n--- Start report ---")
  
  for item in sorted_char_list:
    print(f"The letter {item['char']} appears {item['count']} times.")
  
  print("--- End report ---")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  return len(text.split())  

def count_characters(text):
  lower_text = text.lower()
  char_dict = {}
  for char in lower_text:
    if char.isalpha():
      if char not in char_dict:
        char_dict[char] = 1
      else:
        char_dict[char] += 1

  return char_dict

def chars_dict_to_sorted_list(dict):
  dict_to_list = [{"char": key, "count": value} for key, value in dict.items()]
  return sorted(dict_to_list, key=lambda item: item["count"], reverse=True)

main()