
$path = 'c:\Users\mehme\Desktop\eserhane\gallery.html'
$content = Get-Content $path -Raw -Encoding UTF8

# Define replacements for common mojibake patterns
$replacements = @{
    'Ã‡' = 'Ç'
    'Ã§' = 'ç'
    'Äž' = 'Ğ'
    'ÄŸ' = 'ğ'
    'Ä°' = 'İ'
    'Ä±' = 'ı'
    'Ã–' = 'Ö'
    'Ã¶' = 'ö'
    'Åž' = 'Ş'
    'ÅŸ' = 'ş'
    'Ãœ' = 'Ü'
    'Ã¼' = 'ü'
    'Ã¢' = 'â'
    'Ã‚' = 'Â'
}

foreach ($key in $replacements.Keys) {
    $content = $content.Replace($key, $replacements[$key])
}

$content | Set-Content $path -Encoding UTF8
