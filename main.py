from PIL import Image
from pytesseract import image_to_string
from googlesearch import search
import webbrowser

def Url_Opener(imagefile):
    Url_list=[]
    image_text = (image_to_string(Image.open(imagefile)))
    for j in search(image_text, num=5, stop=1, pause=2):
        Url_list.append(j)
    print(Url_list)
    for i in Url_list:
        webbrowser.open_new(i)
    return Url_list

