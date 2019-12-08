import os

# current_path = os.getcwd()
new_folder = "app"
# print("Your current working path is %s" % current_path)

try:
    os.mkdir(new_folder)
except OSError:
    print("Creation of directory failed: %s" % new_folder)
else:
    print("Creation of directory success: %s" % new_folder)
