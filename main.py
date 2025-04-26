from stats import word_count_in_doc,get_book_text,character_count,character_count_sorted
import sys
  
def main():
  arguments = sys.argv
  path = ""
  if len(arguments) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    path = arguments[1]
  file_contents = get_book_text(path)
  num_words = word_count_in_doc(file_contents)
  cm = character_count(file_contents)
  sorted_list = character_count_sorted(cm)
  print("============ BOOKBOT ============")
  print("Analyzing book found at books/frankenstein.txt...")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for i in sorted_list:
    print(f"{i["char"]}: {i["num"]}")
  print("============= END ===============")

main()
