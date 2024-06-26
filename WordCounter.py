"""
Word Counter
"""
print(__doc__)

class UserInput:

    def getUserInput(self):

        inputs = []

        while True:
            userInput = input("= ")

            if userInput == "" and len(inputs) == 0:
                break

            else:
                if userInput.lower() == 'done':
                    break

                inputs.append(userInput)

        return inputs


class FileCreate:
    # This class is use for create an input.txt file with or without parameter

    def __init__(self, fileData = None):
        if fileData is None:
            self.fileData = ["Python", "Java", "C", "C++", "PHP", "Python", "Java", "OOP"] # default file data
        else:
            self.fileData = fileData

    def createFile(self):
        file = open("input.txt", "w") # Create or overwrite the file if exist
        file.write('\n'.join(self.fileData))
        file.close()
        return "input.txt"


class WordsCounter:
    # This class is used to output a list of word's count
    # It have default search value if parameter in empty

    def __init__(self,  filePath, search_words = None):

        self.filePath = filePath

        if search_words is None:
            self.search_words = ["python", "C", "OoP", "Hello", "java"] # default search value
        else:
            self.search_words = search_words

    def countWords(self):

        counter = {}
        for word in self.search_words:
            counter[word.lower()] = 0

        file = open(self.filePath, "r")
        for line in file:
            word = line.replace("\n", "").lower()
            if word in counter:
                counter[word] += 1

        countList = []
        for word in self.search_words:
            countList.append(str(word) + ' -> ' + str(counter[word.lower()]))

        return countList


if __name__ == "__main__":

    userInput = UserInput()

    print("Enter file path or write 'create' to create a file:")
    filePath = input()

    if filePath.lower() == 'create':

        print("Enter values for file creation and type 'Done' to finish: \nOr\npress enter to create file with default value:")
        fileInput = userInput.getUserInput()

        if len(fileInput) > 0:
            fileWithParam = FileCreate(fileInput)
            file = fileWithParam.createFile()
        else:
            defaultFile = FileCreate()
            file = defaultFile.createFile()
    else:
        file = filePath

    print("Enter values for search and type 'Done' to finish: \nOr\npress enter to search with default value:")
    searchValueInput = userInput.getUserInput()

    if len(searchValueInput) > 0:
        countWordsWithParam = WordsCounter(file, searchValueInput)
        countList = countWordsWithParam.countWords()
    else:
        defaultCount = WordsCounter(file)
        countList = defaultCount.countWords()

    for i in countList:
        print(i)
