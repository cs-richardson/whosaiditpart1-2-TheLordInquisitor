# This function takes a word and returns the same word with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()


# This function takes a filename and generates a dictionary whose keys are the unique words in the file and whose
# values are the counts for those words.
def get_counts(filename):
    result_dict = {}
    count = 0
    file = open(filename)
    for line in file:
        line = line.strip()
        line = line.split()
        for word in line:
            word = normalize(word)
            if word == "":
                continue
            if word in result_dict:
                result_dict[word] = result_dict.get(word) + 1
            else:
                result_dict[word] = 1
            count += 1
    result_dict["_total"] = count
    file.close()
    return result_dict

# Get the counts for the two shortened versions of the texts
shakespeare_counts = get_counts("hamlet-long.txt")
austen_counts = get_counts("pride-and-prejudice-long.txt")

# Check the contents of the dictionaries
for key in shakespeare_counts:
   print(key + ": " + str(shakespeare_counts[key]))

print("-----")

for key in austen_counts:
    print(key + ": " + str(austen_counts[key]))
