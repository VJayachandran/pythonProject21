# importing datetime module
import datetime

# datetime.datetime.now() to get
# current date as filename.
filename = datetime.datetime.now()


# create empty file
def create_file():
    # Function creates an empty file
    # %d - date, %B - month, %Y - Year
    with open(filename.strftime("%d %B %Y") + ".txt", "w") as file:
        file.write("")
print("Hello")
# Driver Code
create_file()

a=str(input("Enter the name of the file with .txt extension:"))
file2=open(a,'r')
line=file2.readline()
while(line!=""):
    print(line)
    line=file2.readline()
file2.close()