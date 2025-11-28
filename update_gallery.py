
with open('gallery.html', 'r', encoding='utf-8') as f:
    gallery_html = f.read()

with open('gallery_content.html', 'r', encoding='utf-8') as f:
    new_content = f.read()

start_marker = '<div class="gallery-grid">'
end_marker = '</div>'

# Find the start of the grid
start_index = gallery_html.find(start_marker)
if start_index != -1:
    start_index += len(start_marker)
    
    # Find the end of the grid. We need to be careful to find the matching closing div.
    # Since the structure is simple:
    # <div class="gallery-grid">
    #    ... items ...
    # </div>
    # We can find the next </div> after the start_index, but wait, items have divs too.
    # So we need to count divs or find the closing tag based on indentation if consistent, or just regex.
    # However, looking at the file, the grid ends before the closing </div> of container.
    # Let's use a simpler approach: split by the marker and reconstruct.
    
    # Actually, I know the lines from previous view_file: 56 to 167.
    # But line numbers might change if I edited before.
    # Let's rely on the string replacement of the inner content.
    # The inner content starts after <div class="gallery-grid"> and ends before the </div> that closes it.
    
    # Let's try to identify the block by content.
    # The block starts with <div class="gallery-grid">
    # It ends with </div> followed by </div> (container end) and </section>.
    
    # A safer way:
    # Read all lines. Find the line with class="gallery-grid".
    # Find the matching closing div.
    
    lines = gallery_html.splitlines()
    start_line = -1
    end_line = -1
    
    depth = 0
    found_start = False
    
    for i, line in enumerate(lines):
        if 'class="gallery-grid"' in line:
            start_line = i
            found_start = True
            depth = 1 # We are inside the grid now (conceptually, after this line)
            continue
            
        if found_start:
            # Count open and close divs to find the matching close
            # This is a bit fragile with simple string counting if multiple divs on one line, but let's assume standard formatting
            open_divs = line.count('<div')
            close_divs = line.count('</div>')
            depth += open_divs - close_divs
            
            if depth == 0:
                end_line = i
                break
    
    if start_line != -1 and end_line != -1:
        # We want to keep the start_line (the opening tag) and the end_line (the closing tag)
        # and replace everything in between.
        
        new_lines = lines[:start_line+1] + [new_content] + lines[end_line:]
        final_html = '\n'.join(new_lines)
        
        with open('gallery.html', 'w', encoding='utf-8') as f:
            f.write(final_html)
        print("Successfully updated gallery.html")
    else:
        print("Could not find gallery-grid block")

