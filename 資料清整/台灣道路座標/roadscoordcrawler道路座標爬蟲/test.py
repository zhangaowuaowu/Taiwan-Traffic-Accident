from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
import pyautogui
import keyboard
from PIL import Image
from io import BytesIO
import numpy as np
import cv2


img = cv2.imread('test.png')

# result = np.where(img == [219,249,255])
# result
print(img)