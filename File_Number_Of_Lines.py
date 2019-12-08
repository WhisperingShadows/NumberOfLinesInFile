file = input("Enter file to be measured (number of lines): ")

#file = 'C:/Users/admin/Desktop/New Text Document.txt'

from timeit import default_timer as timer
import time

start = timer()
def file_lines(file):
    num1 = sum(1 for line in open(file, mode="r",encoding="utf-8"))
    return num1
print(file_lines(file))
end = timer()
time1 = (end-start)
print("Time 1:",time1,"secs")

time.sleep(2)

start = timer() 
def file_lines_2(file):
    with open(file, mode="r",encoding="utf-8") as file:
        num2 = sum(1 for line in file)
        return num2
print(file_lines_2(file))
end = timer()
time2 = (end-start)
print("Time 2:",time2,"secs")


## There seems to be a major bias towards whichever function is called first
## Will do more testing later

if time1 < time2:
    print("Time1 was faster")
else:
    print("Time2 was faster")




