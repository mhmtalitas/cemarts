
with open('gallery.html', 'r', encoding='utf-8') as f:
    gallery_html = f.read()

with open('gallery_content_fixed.html', 'r', encoding='utf-8') as f:
    new_content = f.read()

# We need to replace the content inside <div class="gallery-grid"> ... </div>
# Since the previous state is messed up, we should be careful.
# We know the start is <div class="gallery-grid">
# We know the end is before the closing </div> of container.

# Let's look for the start
start_marker = '<div class="gallery-grid">'
start_pos = gallery_html.find(start_marker)

if start_pos == -1:
    print("Could not find gallery-grid")
    exit(1)

# The end position is tricky because of nested divs.
# But we know the structure:
# <section class="section gallery">
#    <div class="container">
#        <div class="gallery-filters">...</div>
#        <div class="gallery-grid">
#            ... content ...
#        </div>
#    </div>
# </section>

# So we can look for the closing of gallery-grid.
# Since the file is currently messed up, we might rely on the fact that the grid is followed by </div> (container) and </section>.
# Or we can just find the start of footer or lightbox if we are desperate, but that's risky.

# Let's try to find the closing div of gallery-grid by counting braces from start_pos
# Or simpler: The gallery grid ends before the last two closing divs of the section block.
# Let's find </section> and go back.

section_end = gallery_html.find('</section>', start_pos)
if section_end == -1:
    print("Could not find section end")
    exit(1)

# Before </section>, there is </div> (container) and </div> (gallery-grid).
# Let's find the last </div> before section_end.
last_div = gallery_html.rfind('</div>', 0, section_end)
# That should be container closing.
# The one before that should be gallery-grid closing.
grid_end = gallery_html.rfind('</div>', 0, last_div)

if grid_end == -1 or grid_end <= start_pos:
    print("Could not find grid end")
    exit(1)

# Now replace
new_html = gallery_html[:start_pos + len(start_marker)] + '\n' + new_content + '\n' + gallery_html[grid_end:]

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Successfully fixed gallery.html")
