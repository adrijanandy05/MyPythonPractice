#Create a dictionary and take input from the user and return the meaning of the word from the dictionary
#(Assuming the user inputs the words which are already present in the dictionary)
dictionary={"Programs":"sequence of instructions in a programming language that a computer can execute or interpret.",
            "Mutable":"prone to change",
            "Software":"collection of instructions that tell a computer how to work",
            "Compiler":"computer program that translates computer code written in one programming language (the source language) into another language (the target language)"}
print("Enter the word you want the meaning for:",end=" ")
word=input()
print(dictionary[word])
