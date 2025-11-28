# -*- coding: utf-8 -*-
import os

file_path = r'c:\Users\mehme\Desktop\eserhane\gallery.html'

replacements = {
    'Ã‡': 'Ç',
    'Ã§': 'ç',
    'Äž': 'Ğ',
    'ÄŸ': 'ğ',
    'Ä°': 'İ',
    'Ä±': 'ı',
    'Ã–': 'Ö',
    'Ã¶': 'ö',
    'Åž': 'Ş',
    'ÅŸ': 'ş',
    'Ãœ': 'Ü',
    'Ã¼': 'ü',
    'Ã¢': 'â',
    'Ã‚': 'Â'
}

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for bad, good in replacements.items():
    content = content.replace(bad, good)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Encoding fixed.")
