import plistlib
import os

# gets plist files, this is where your system settings are stored
fileName=os.path.expanduser("~/Library/Preferences/com.apple.Accessibility.plist")
fileName2=os.path.expanduser("~/Library/Preferences/com.apple.universalaccess.plist")


# opens plist files
with open(fileName, 'rb') as fp:
    accPl = plistlib.load(fp)

with open(fileName2, 'rb') as fp:
    uniPl = plistlib.load(fp)



# makes backup, im not evil
with open("~/Downloads/zip/backup1.plist", 'wb') as fp:
    plistlib.dump(accPl, fp)

with open("~/Downloads/zip/backup2.plist", 'wb') as fp:
    plistlib.dump(accPl, fp)


# changes the values
accPl["InvertColorsEnabled"] = 1
accPl["EnhancedBackgroundContrastEnabled"] = 1
accPl["ApplicationAccessibilityEnabled"] = 1
accPl["DarkenSystemColors"] = 1
accPl["AccessibilityEnabled"] = True

uniPl["increaseContrast"] = True
uniPl["closeViewTrackpadGestureZoomEnabled"] = True
uniPl["slowKey"] = True
uniPl["closeViewScrollWheelToggle"] = True
uniPl["closeViewHotkeysEnabled"] = False



# writes changes to the files
with open(fileName, 'wb') as fp:
    plistlib.dump(accPl, fp)

with open(fileName2, 'wb') as fp:
    plistlib.dump(uniPl, fp)