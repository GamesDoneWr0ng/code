from AppKit import NSPasteboard, NSHTMLPboardType

pasteboard = NSPasteboard.generalPasteboard()
html_data = pasteboard.dataForType_(NSHTMLPboardType)
html_string = str(html_data, 'utf-8')
#print(html_string)