file_read = open('C:/Users/hp/Desktop/Coding/Python/lesson 12/file.txt', 'r')
print("File in Read Mode")
print(file_read.read())
file_read.close()

file_write = open('C:/Users/hp/Desktop/Coding/Python/lesson 12/file.txt', 'w')
file_write.write("File in write mode....\n")
file_write.write("Hi! I am a Penguin. I am 1 yr. old\n")
file_write.close()

file_append = open('C:/Users/hp/Desktop/Coding/Python/lesson 12/file.txt', 'a')
file_append.write("File in append mode....\n")
file_append.write("Hi! I am a Penguin. I am 1 yr. old\n")
file_append.close()
# hello
