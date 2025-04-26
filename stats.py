def get_book_text(file_path):
  with open(file_path) as f:
    file_contents = f.read()
    return file_contents
  
def word_count_in_doc(content):
  return len(content.split())


def character_count(content):
  characterMap = {}
  for c in content:
    lower_c = c.lower()
    if lower_c in characterMap:
      count = characterMap[lower_c] + 1
    else:
      count = 1
    characterMap[lower_c] = count
  return characterMap

def character_count_sorted(content_object):
  sorted_list = []
  for char in content_object:
    if char.isalpha():
      sorted_list.append({"char":char,"num":content_object[char]})
    else:
      continue

  return sorted(sorted_list,key=lambda x: x['num'],reverse=True)