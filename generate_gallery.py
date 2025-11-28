
oil_html = ''
for i in range(1, 20):
    oil_html += f'''
                <div class="gallery-item yagliboya" data-category="yagliboya">
                    <div class="gallery-img-wrapper">
                        <img src="assets/{i}.jpeg" alt="Yağlı Boya Eser {i}">
                        <div class="gallery-overlay">
                            <i class="fas fa-search-plus"></i>
                        </div>
                    </div>
                    <div class="gallery-info">
                        <h3>Yağlı Boya Eser {i}</h3>
                        <p class="category">Yağlı Boya Tablo</p>
                        <p class="price">₺5.000</p>
                        <a href="https://wa.me/905551234567?text=Merhaba, 'Yağlı Boya Eser {i}' adlı eser hakkında bilgi almak istiyorum."
                            target="_blank" class="btn btn-whatsapp">
                            <i class="fab fa-whatsapp"></i> Bilgi Al / Satın Al
                        </a>
                    </div>
                </div>'''

charcoal_html = ''
for i in range(1, 16):
    charcoal_html += f'''
                <div class="gallery-item karakalem" data-category="karakalem">
                    <div class="gallery-img-wrapper">
                        <img src="assets/karakalem{i}.jpeg" alt="Karakalem Eser {i}">
                        <div class="gallery-overlay">
                            <i class="fas fa-search-plus"></i>
                        </div>
                    </div>
                    <div class="gallery-info">
                        <h3>Karakalem Eser {i}</h3>
                        <p class="category">Karakalem Çalışması</p>
                        <p class="price">₺1.500</p>
                        <a href="https://wa.me/905551234567?text=Merhaba, 'Karakalem Eser {i}' adlı eser hakkında bilgi almak istiyorum."
                            target="_blank" class="btn btn-whatsapp">
                            <i class="fab fa-whatsapp"></i> Bilgi Al / Satın Al
                        </a>
                    </div>
                </div>'''

sculpture_html = '''
                <!-- Heykel Item -->
                <div class="gallery-item heykel" data-category="heykel">
                    <div class="gallery-img-wrapper">
                        <img src="assets/sculpture.png" alt="Mermer Heykel">
                        <div class="gallery-overlay">
                            <i class="fas fa-search-plus"></i>
                        </div>
                    </div>
                    <div class="gallery-info">
                        <h3>Sessiz Çığlık</h3>
                        <p class="category">Mermer Heykel</p>
                        <p class="price">₺12.000</p>
                        <a href="https://wa.me/905551234567?text=Merhaba, 'Sessiz Çığlık' adlı eser hakkında bilgi almak istiyorum."
                            target="_blank" class="btn btn-whatsapp">
                            <i class="fab fa-whatsapp"></i> Bilgi Al / Satın Al
                        </a>
                    </div>
                </div>
                <!-- Duplicate for demo -->
                <div class="gallery-item heykel" data-category="heykel">
                    <div class="gallery-img-wrapper">
                        <img src="assets/sculpture.png" alt="Modern Form">
                        <div class="gallery-overlay">
                            <i class="fas fa-search-plus"></i>
                        </div>
                    </div>
                    <div class="gallery-info">
                        <h3>Formun Gücü</h3>
                        <p class="category">Bronz Döküm</p>
                        <p class="price">₺8.500</p>
                        <a href="https://wa.me/905551234567?text=Merhaba, 'Formun Gücü' adlı eser hakkında bilgi almak istiyorum."
                            target="_blank" class="btn btn-whatsapp">
                            <i class="fab fa-whatsapp"></i> Bilgi Al / Satın Al
                        </a>
                    </div>
                </div>'''

with open('gallery_content.html', 'w', encoding='utf-8') as f:
    f.write(oil_html + charcoal_html + sculpture_html)
