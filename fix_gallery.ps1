$lines = Get-Content 'c:\Users\mehme\Desktop\eserhane\gallery.html'
$newLines = $lines[0..520] + $lines[716..($lines.Count-1)]
$newLines | Set-Content 'c:\Users\mehme\Desktop\eserhane\gallery.html' -Encoding UTF8
