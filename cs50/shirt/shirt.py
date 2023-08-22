import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command_line_arg()
    try:
        imageFile=Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("input does not exist")
    shirtfile= Image.open("shirt.png")
    size= shirtfile.size
    muppet = ImageOps.fit(imageFile,size)
    muppet.paste(shirt,shirt)
    muppet.save(sys.argv[2])

def check_command_line_arg():
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv)> 3:
        sys.exit("Too many command-line arguments")
    file = splitext(sys.argv[1])
    file =splitext(sys.argv[2])
    if check_extension(file1[1]) == False:
        sys.exit("invalid input")  
    if check_extension(file2[1])== False:
        sys.exit("invalid output")
    if file1[1].lower()== file2[1].lower():
        sys.exit("input ad output have different extensions")
def check_extension(file):
    if file in [".jpg","jpeg",".png"]:
                return True
                return False
if __name__=="__main__":
    main()