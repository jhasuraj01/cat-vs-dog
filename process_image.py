# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow
from PIL import Image
import os

for path in os.listdir("./dataset/training_set/cats"):
    image = Image.open("./dataset/training_set/cats/" + path)
    image.convert('L').resize((200, 200)).save("./processed_dataset/training_set/cats/" + path)

for path in os.listdir("./dataset/training_set/dogs"):
    image = Image.open("./dataset/training_set/dogs/" + path)
    image.convert('L').resize((200, 200)).save("./processed_dataset/training_set/dogs/" + path)

for path in os.listdir("./dataset/test_set/cats"):
    image = Image.open("./dataset/test_set/cats/" + path)
    image.convert('L').resize((200, 200)).save("./processed_dataset/test_set/cats/" + path)

for path in os.listdir("./dataset/test_set/dogs"):
    image = Image.open("./dataset/test_set/dogs/" + path)
    image.convert('L').resize((200, 200)).save("./processed_dataset/test_set/dogs/" + path)
