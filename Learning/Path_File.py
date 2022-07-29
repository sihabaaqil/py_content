# Python program to explain os.path.join() method

# importing os module
import os

# Path
path = "/home"

# Join various path components
print("1."+os.path.join(path, "User/Desktop", "file.txt"))


# Path
path = "User/Documents"

# Join various path components
print("2."+os.path.join(path, "/home", "file.txt"))

# In above example '/home'
# represents an absolute path
# so all previous components i.e User / Documents
# are thrown away and joining continues
# from the absolute path component i.e / home.


# Path
path = "/User"

# Join various path components
print("3."+os.path.join(path, "Downloads", "file.txt", "/home"))

# In above example '/User' and '/home'
# both represents an absolute path
# but '/home' is the last value
# so all previous components before '/home'
# will be discarded and joining will
# continue from '/home'

# Path
path = "/home"

# Join various path components
print("4."+os.path.join(path, "User/Public/", "Documents", ""))

# In above example the last
# path component is empty
# so a directory separator ('/')
# will be put at the end
# along with the concatenated value


# Path
path = "\home"

# Join various path components
ROOT_DIR = os.path.abspath(os.curdir)
print("5."+ROOT_DIR +os.path.join(path, "User\Desktop", "file.txt"))
