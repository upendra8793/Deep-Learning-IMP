import os

def remove_first_letter(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            new_filename = filename[1:]
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))

directory = "K:/pythonINTERNS/aadesh/Signature-Forgery-Detection-main/real1/augmentated"
remove_first_letter(directory)

