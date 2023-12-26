from PIL import Image
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper
import sys

stream_deck = DeviceManager.enumerate()[0]

imgFolder = 