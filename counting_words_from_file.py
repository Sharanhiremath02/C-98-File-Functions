def count_words_from_file():
    fileName=input("Enter the File Name:")
    file=open(fileName,"r")

    num_words=0
    for line in file:
        words=line.split()
        num_words=num_words+len(words)

    print("number of words:",num_words)

count_words_from_file()