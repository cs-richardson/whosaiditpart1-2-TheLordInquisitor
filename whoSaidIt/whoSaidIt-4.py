import math

# This function takes a word and a dictionary of word counts, and generates a score that
# approximates the relevance of the word in the document from which the word counts
# were generated. The higher the score, the more relevant the word..
def get_score(word, counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)

# This function takes a word and returns the same word with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# This function takes a filename and generates a dictionary whose keys are the unique words in the file and whose
# values are the counts for those words.
def get_counts(filename):
    file = open(filename)
    result_dict = {}
    count = 0
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


def predict(text, shakespeare, austen):
    shakespeare_score = 0
    austen_score = 0
    text = text.split()
    for word in text:
        word = normalize(word)
        if word == "":
            continue
        shakespeare_score = get_score(word, shakespeare) + shakespeare_score
        austen_score = get_score(word, austen) + austen_score
    if shakespeare_score > austen_score:
        print("I think that was William Shakespeare")
    elif austen_score > shakespeare_score:
        print("I think that was Jane Austen")
    else:
        print("I have absolutely no clue")


# Get the counts for the two shortened versions of the texts
shakespeareCounts = get_counts("hamlet-long.txt")
austenCounts = get_counts("pride-and-prejudice-long.txt")

userInput = input("Enter some text: ")
predict(userInput, shakespeareCounts, austenCounts)
