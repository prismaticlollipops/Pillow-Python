#NOTE: the code may take some time to run. images may also take some time to show up too!
from PIL import Image, ImageFilter
import os

#define a welcome message, image opens to what the user inputs
def welcome():
    certain_image = input("Enter a number from 1-10 to choose an image of your choice. \n1 - for cherry blossoms, 2 - for earth, 3 - for icecream, 4 - for jellyfish, 5 - for kitten \n6 - for leaves, 7 - for miffy, 8 - nyan cat, 9 -  seal, or 10 - for stars: ")
    certain_image = int(certain_image)

    if certain_image == 1: 
        image_path = 'cherry_blossom.jpg'

    elif certain_image == 2: 
        image_path = 'earth.jpg'

    elif certain_image == 3: 
        image_path = 'icecream.jpg'

    elif certain_image == 4: 
        image_path = 'jellyfish.jpg'

    elif certain_image == 5: 
        image_path = 'kitten.jpg'

    elif certain_image == 6: 
        image_path = 'leaves.jpg'

    elif certain_image == 7: 
        image_path = 'miffy.jpg'

    elif certain_image == 8: 
        image_path = 'nyan_cat.jpg'

    elif certain_image == 9: 
        image_path = 'seal.jpg'

    elif certain_image == 10: 
        image_path = 'stars.jpg'

    else:
        print("Invalid input. Please choose a number from 1-10.")
        return welcome()

    image = Image.open(image_path)
    image.show()
    return image

def png_image(image, folder_name):
    if not os.path.exists('pngs'):
        os.makedirs('pngs')
    fn, fext = os.path.splitext(os.path.basename(image.filename))
    i = image.copy()
    i.save('{}/{}_.png'.format(folder_name, fn))
    print("Image saved as PNG.")

#define a rotate function which asks user how much they want to rotate the image. prints invalid message if a negative number is inputted
def rotate_image(image):
    if not os.path.exists('rotate'):
        os.makedirs('rotate')
    degrees = int(input("Enter the degrees you want to rotate the image by: "))
    rotated_image = image.rotate(degrees)
    rotated_image.show()
    fn, fext = os.path.splitext(os.path.basename(image.filename))
    rotated_image.save('rotate/{}_{}{}'.format(fn, degrees, fext))
    return rotated_image

#define blur function, 
def blur_image(image):
    if not os.path.exists('blur'):
        os.makedirs('blur')
    blur = int(input("Enter a number from 1-15 corresponding to the amount of blur you want: "))
    if blur <= 0 or blur > 15:
        print("Invalid choice. Please choose a number between 1-15:")
        blur_image(image)
    blurred_image = image.filter(ImageFilter.GaussianBlur(blur))
    blurred_image.show()
    fn, fext = os.path.splitext(os.path.basename(image.filename))
    blurred_image.save('blur/{}_{}{}'.format(fn, blur, fext))
    return blurred_image

def blacknwhite_image(image):
    if not os.path.exists('BnW'):
        os.makedirs('BnW')
    bnw_image = image.convert(mode='L')
    bnw_image.show()
    fn, fext = os.path.splitext(os.path.basename(image.filename))
    bnw_image.save('BnW/{}_{}{}'.format(fn, "L", fext))
    return bnw_image

def edges_image(image):
    if not os.path.exists('edges_embossment'):
        os.makedirs('edges_embossment')
    edges_image = image.convert(mode='L')
    edges = edges_image.filter(ImageFilter.FIND_EDGES)
    edges.show()
    fn, fext = os.path.splitext(os.path.basename(image.filename))
    edges_image.save('edges_embossment/{}_{}{}'.format(fn, "L", fext))
    return edges_image


def welcome_2(image):
    folder_name = 'pngs'
    choice = input("Great! Now let's manipulate the image. Pick the following by entering the abbreviated form:\nRotate (R), Black and White (W), Blur (B), or Edge Embossment (E): ").lower()
    if choice == "R".lower():
        rotate_image(image)
    elif choice == "B".lower():
        blur_image(image)
    elif choice == "W".lower():
        blacknwhite_image(image)
    elif choice== "E".lower() :
        edges_image(image)
    else:
        print("Invalid choice.Please try again.")
        welcome_2(image)
    choice = (input("Enter your choice: Convert image to png (P), or quit(Q): ")).lower()
    if choice == "P".lower():
        png_image(image, folder_name)
        exit()
    elif choice == "Q".lower():
        exit()  
    else:
        print("Invalid choice. Please try again: ")

def save_image(image, size):
    folder_name = str(size)
    fn, fext = os.path.splitext(os.path.basename(image.filename))
    new_size = size

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    if size == 200:
        new_size = (200, 200)
        i = image.copy()
        i.thumbnail(new_size)
        i.save('{}/{}_{}{}'.format(folder_name, fn, size, fext))
        print("Image saved in {} folder as {}_{}{}".format(folder_name, fn, size, fext))
    elif size == 400:
        new_size = (400, 400)
        i = image.copy()
        i.thumbnail(new_size)
        i.save('{}/{}_{}{}'.format(folder_name, fn, size, fext))
        print("Image saved in {} folder as {}_{}{}".format(folder_name, fn, size, fext))
    else:
        if size not in [200, 400, 600]:
            size = int(input("Invalid choice. Please choose 200, 400, or 600: "))
        save_image(image, size)

    image.thumbnail(new_size)
    image.save(os.path.join(folder_name, f"{fn}_{size}{fext}"))

#asks user what size image they want
#if user inputs a different size other than the listed, an invalid message is printed
image = welcome()
size = input("What image size do you want? To choose a size, enter 200, 400, or 600: ")
size = int(size)
save_image(image, size)
welcome_2(image)