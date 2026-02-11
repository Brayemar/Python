# On the try and except block : You run some codes and if it is successful the try block will get executed other than the except block will be executed when there is an anticipated error.


try:
    number = 100
    answer = number / 0
    print("The answer is: ",answer)
except Exception as e:
    print("There is an error: ", e)