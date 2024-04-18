import qrcode

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
text = input("Enter text or link do you want to convert to qrcode: ")
name = input("Enter your picture name: ")
location = input("Enter location do you want to save: ")
myqrcode = qrcode.make(text)
myqrcode.save(location + name + ".png",scale=8)
plt.imshow(mpimg.imread(location + name + ".png"))
plt.show()