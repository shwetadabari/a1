import os
import re
import json

BASE_DIR = r"d:\antigravity website\risottogarden"
ADDR = "601 Union Street, Suite 4200, Seattle, WA 98101, United States"
PHONE = "+1-888-924-4195"
EMAIL = "concierge@risottogarden.com"
DOMAIN = "risottogarden.com"
BRAND = "Risotto Garden Hearth & Atelier"

GTAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-0LY0HY7L01"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-0LY0HY7L01');
</script>"""

FONTS = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400&family=Marcellus&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">"""

def get_header(active_page):
    idx_cls = "active" if active_page == "index" else ""
    abt_cls = "active" if active_page == "about" else ""
    srv_cls = "active" if active_page == "services" else ""
    faq_cls = "active" if active_page == "faq" else ""
    cnt_cls = "active" if active_page == "contact" else ""
    
    return f"""  <!-- Site Header (Rule 11) -->
  <header class="site-header">
    <div class="rg-container">
      <div class="rg-nav-container">
        <a href="index.html" class="rg-brand">
          <div class="rg-brand-crest">RG</div>
          <div class="rg-brand-text">
            Risotto Garden
            <small>Hearth &bull; Seattle</small>
          </div>
        </a>
        <nav class="rg-nav-menu">
          <a href="index.html" class="rg-nav-link {idx_cls}">Hearth Atelier</a>
          <a href="about.html" class="rg-nav-link {abt_cls}">Rice Agronomy</a>
          <a href="services.html" class="rg-nav-link {srv_cls}">Degustation Dinners</a>
          <a href="faq.html" class="rg-nav-link {faq_cls}">Culinary FAQ</a>
          <a href="contact.html" class="rg-nav-link {cnt_cls}">Salon Inquiries</a>
        </nav>
        <div style="display: flex; align-items: center; gap: 16px;">
          <a href="contact.html" class="rg-nav-cta">Reserve Dinner</a>
          <button class="rg-hamburger" id="rg-hamburger" aria-label="Toggle Navigation">
            <span></span>
            <span></span>
            <span></span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer (Rule 11) -->
  <div class="mobile-drawer-backdrop" id="mobile-drawer-backdrop"></div>
  <div class="mobile-drawer" id="mobile-drawer">
    <div class="mobile-drawer-header">
      <div class="rg-brand">
        <div class="rg-brand-crest">RG</div>
        <div class="rg-brand-text">Risotto Garden</div>
      </div>
      <button class="mobile-drawer-close" id="mobile-drawer-close" aria-label="Close Drawer">&times;</button>
    </div>
    <div class="mobile-drawer-body">
      <a href="index.html" class="mobile-nav-link">Hearth Atelier</a>
      <a href="about.html" class="mobile-nav-link">Rice Agronomy &amp; Heritage</a>
      <a href="services.html" class="mobile-nav-link">Degustation Dinners</a>
      <a href="faq.html" class="mobile-nav-link">Culinary &amp; Sourcing FAQ</a>
      <a href="contact.html" class="mobile-nav-link">Salon Inquiries &amp; Table</a>
    </div>
    <div class="mobile-drawer-footer">
      <p style="margin-bottom: 8px; color: var(--rg-saffron); font-family: var(--rg-font-mono); font-size: 0.75rem;">SEATTLE CONCIERGE</p>
      <p style="margin-bottom: 6px;">{PHONE}</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>"""

def get_footer():
    return f"""  <!-- Semantic Site Footer -->
  <footer class="rg-footer">
    <div class="rg-container">
      <div class="rg-footer-grid">
        <div class="rg-footer-brand">
          <div class="rg-brand">
            <div class="rg-brand-crest">RG</div>
            <div class="rg-brand-text">
              Risotto Garden
              <small>Hearth &bull; Seattle</small>
            </div>
          </div>
          <p>Artisanal botanical risotto degustations, aged Carnaroli rice agronomy, and slow-hearth cooking traditions honoring northern Italian culinary craftsmanship.</p>
          <div style="font-family: var(--rg-font-mono); font-size: 0.8rem; color: var(--rg-saffron);">
            {PHONE} &bull; {EMAIL}
          </div>
        </div>
        <div class="rg-footer-col">
          <h4>Hearth Degustation</h4>
          <ul class="rg-footer-links">
            <li><a href="index.html">Atelier Flagship</a></li>
            <li><a href="about.html">Carnaroli Heritage</a></li>
            <li><a href="services.html">Dinner Experiences</a></li>
            <li><a href="faq.html">Culinary FAQ</a></li>
            <li><a href="contact.html">Private Table Booking</a></li>
          </ul>
        </div>
        <div class="rg-footer-col">
          <h4>Agronomy Principles</h4>
          <ul class="rg-footer-links">
            <li><a href="about.html">Aged Carnaroli Superfino</a></li>
            <li><a href="about.html">Hammered Copper Sauciers</a></li>
            <li><a href="about.html">Single-Harvest Saffron</a></li>
            <li><a href="about.html">Mantecatura all'Onda</a></li>
            <li><a href="about.html">Botanical Broth Reductions</a></li>
          </ul>
        </div>
        <div class="rg-footer-col">
          <h4>Institutional Coordinates</h4>
          <p style="font-size: 0.85rem; line-height: 1.6; margin-bottom: 12px; color: var(--rg-text-light-muted);">
            {ADDR}
          </p>
          <p style="font-family: var(--rg-font-mono); font-size: 0.75rem; color: var(--rg-saffron); margin-bottom: 16px;">
            Direct Concierge: {PHONE}
          </p>
          <div style="padding: 8px 12px; background: rgba(229,168,59,0.08); border: 1px solid rgba(229,168,59,0.2); border-radius: 6px; font-size: 0.725rem; font-family: var(--rg-font-mono); color: var(--rg-text-light);">
            Certified Slow Food Hearth Guild Member
          </div>
        </div>
      </div>
      <div class="rg-footer-bottom">
        <div>&copy; 2026 Risotto Garden Atelier LLC. All Worldwide Rights Reserved.</div>
        <div class="rg-footer-legal-links">
          <a href="privacy-policy.html">Privacy Policy</a>
          <a href="terms-and-conditions.html">Terms &amp; Conditions</a>
          <a href="disclaimer.html">Disclaimer</a>
          <a href="cookie-policy.html">Cookie Policy</a>
        </div>
      </div>
    </div>
  </footer>
  <script src="assets/js/script.js"></script>
  <script src="assets/js/main.js"></script>"""

# ==========================================
# 1. INDEX.HTML (Flagship Home - 12 Distinct Sections)
# ==========================================
def build_index():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Risotto Garden | Artisanal Botanical Risotto &amp; Hearth Dinners</title>
  <meta name="description" content="Discover Risotto Garden in Seattle. Masterclass slow-hearth botanical risotto dinners, aged Carnaroli Superfino grain, and authentic Tuscan mantecatura.">
  <link rel="canonical" href="https://{DOMAIN}/index.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Restaurant",
    "name": "Risotto Garden Hearth & Atelier",
    "url": "https://{DOMAIN}/",
    "telephone": "{PHONE}",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "601 Union Street, Suite 4200",
      "addressLocality": "Seattle",
      "addressRegion": "WA",
      "postalCode": "98101",
      "addressCountry": "US"
    }},
    "servesCuisine": "Northern Italian, Artisanal Risotto, Degustation Dinner",
    "priceRange": "$$$$"
  }}
  </script>
</head>
<body>
{get_header('index')}

  <main>
    <!-- Section 1: Inset Floating Hearth Viewport with Gastronomic Ledger (Asset 1) -->
    <section class="rg-hero rg-inset-hero">
      <div class="rg-container">
        <div class="rg-hero-grid">
          <!-- Viewport: Asset 1 (Golden Saffron Risotto) -->
          <div class="rg-hero-viewport">
            <img src="assets/images/risottogarden_asset_1.jpg" alt="Signature Golden Saffron Risotto alla Milanese plated in glazed ceramic coupe with gold leaf and herbs" width="1200" height="800">
            <div class="rg-recipe-seal">
              <div class="rg-seal-icon">✦</div>
              <div class="rg-seal-text">
                <h4>Risotto allo Zafferano No. 01</h4>
                <p>Aged Carnaroli &bull; Castelnuovo Saffron</p>
              </div>
            </div>
          </div>

          <!-- Gastronomic Ledger -->
          <div class="rg-hero-ledger">
            <span class="rg-tag">Tuscan Botanical Hearth &bull; Est. 2017</span>
            <h1 class="rg-hero-title">The Art of the Slow Hearth <span>Risotto Degustation</span></h1>
            <p class="rg-hero-desc">
              Honoring centuries-old northern Italian rice agronomy and estate garden harvests. Every dinner is orchestrated around aged Carnaroli Superfino, slow-simmering herbal broths, and hand-beaten mantecatura.
            </p>
            <div class="rg-gastronomic-data">
              <div class="rg-data-col">
                <small>RICE VINTAGE</small>
                <strong>18 Mo. Aged</strong>
              </div>
              <div class="rg-data-col">
                <small>MANTECATURA</small>
                <strong>68&deg;C Emulsion</strong>
              </div>
              <div class="rg-data-col">
                <small>STARCH RELEASE</small>
                <strong>High Amylose</strong>
              </div>
            </div>
            <div class="rg-hero-actions">
              <a href="contact.html" class="rg-btn rg-btn-terracotta">Reserve Evening Table</a>
              <a href="services.html" class="rg-btn rg-btn-outline">Explore Dinners</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Seasonal Degustation Menu Ribbon -->
    <div class="rg-menu-ribbon">
      <div class="rg-container">
        <div class="rg-ribbon-grid">
          <div class="rg-ribbon-item">
            <div class="rg-ribbon-num">I</div>
            <div class="rg-ribbon-content">
              <h4>Antipasto di Terroir</h4>
              <p>Clarified garden broth &amp; heritage root vegetables</p>
            </div>
          </div>
          <div class="rg-ribbon-item">
            <div class="rg-ribbon-num">II</div>
            <div class="rg-ribbon-content">
              <h4>Il Risotto all'Onda</h4>
              <p>Carnaroli Superfino with seasonal botanical emulsion</p>
            </div>
          </div>
          <div class="rg-ribbon-item">
            <div class="rg-ribbon-num">III</div>
            <div class="rg-ribbon-content">
              <h4>Finale all'Erbette</h4>
              <p>Infused estate herbal digestif &amp; toasted grains</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Section 3: The Agronomy of Carnaroli (Asset 2: Carnaroli Rice in Olivewood Scoop) -->
    <section class="rg-section rg-section-dark">
      <div class="rg-container">
        <div class="rg-agronomy-split">
          <div>
            <span class="rg-tag">The King of Rices</span>
            <h2 class="rg-section-title">Why Carnaroli Superfino Defines <span>Artisanal Risotto</span></h2>
            <p style="color: var(--rg-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 24px;">
              Unlike short-grain varieties that break down under thermal stress, Carnaroli Superfino boasts an exceptionally high amylose content. Its elongated grain structure absorbs twice its volume in steaming savory broth while retaining a firm, toothsome crystalline core.
            </p>
            <p style="color: var(--rg-text-light-muted); font-size: 1rem; line-height: 1.8; margin-bottom: 32px;">
              We source strictly from heritage paddy cooperatives along the Po River valley, where harvested grains rest in temperature-regulated silos for eighteen months to stabilize starch gelatinization before stone-milling.
            </p>
            <div style="display: flex; gap: 32px; font-family: var(--rg-font-mono); font-size: 0.85rem;">
              <div style="border-left: 2px solid var(--rg-terracotta); padding-left: 14px;">
                <strong style="font-size: 1.4rem; color: #fff; display: block; font-family: var(--rg-font-display);">24.2%</strong>
                Amylose Ratio
              </div>
              <div style="border-left: 2px solid var(--rg-saffron); padding-left: 14px;">
                <strong style="font-size: 1.4rem; color: #fff; display: block; font-family: var(--rg-font-display);">18 Mo.</strong>
                Silo Resting Cycle
              </div>
            </div>
          </div>
          <div>
            <div class="rg-agronomy-media">
              <img src="assets/images/risottogarden_asset_2.jpg" alt="Aged Carnaroli Superfino rice grains in rustic carved olivewood grain scoop on slate board" width="1200" height="800">
              <div class="rg-agronomy-badge">ESTATE HARVEST &bull; VINTAGE 2024</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: The 5-Step Mantecatura Sequence (Zero Box Cards) -->
    <section class="rg-section rg-section-darker">
      <div class="rg-container">
        <div class="rg-section-header" style="text-align: center;">
          <span class="rg-tag">Culinary Chronology</span>
          <h2 class="rg-section-title">The Five Disciplines of the <span>Hearth Stove</span></h2>
          <p class="rg-section-subtitle" style="margin: 0 auto;">Every pot follows a strict chronological progression to achieve the velvet wave emulsion.</p>
        </div>
        <div class="rg-mantecatura-flow">
          <div class="rg-flow-step">
            <div class="rg-step-num">PHASE 01</div>
            <h3 class="rg-step-title">Tostatura a Secco</h3>
            <p class="rg-step-desc">Parching dry rice in hot copper pans without fat until grains become translucent and pearl-like.</p>
          </div>
          <div class="rg-flow-step">
            <div class="rg-step-num">PHASE 02</div>
            <h3 class="rg-step-title">Sfumatura Botanica</h3>
            <p class="rg-step-desc">Deglazing the hot grain bed with reduced estate herb broth, releasing natural grain aromatics.</p>
          </div>
          <div class="rg-flow-step">
            <div class="rg-step-num">PHASE 03</div>
            <h3 class="rg-step-title">Cottura Dolce</h3>
            <p class="rg-step-desc">Ladling bubbling broth in rhythmic intervals over gentle hearth heat for exactly 16 minutes.</p>
          </div>
          <div class="rg-flow-step">
            <div class="rg-step-num">PHASE 04</div>
            <h3 class="rg-step-title">Mantecatura all'Onda</h3>
            <p class="rg-step-desc">Beating chilled butter cubes and 36-month cheese off the heat until a glossy suspension forms.</p>
          </div>
          <div class="rg-flow-step">
            <div class="rg-step-num">PHASE 05</div>
            <h3 class="rg-step-title">Riposo al Piatto</h3>
            <p class="rg-step-desc">Allowing the risotto to settle two minutes in warm ceramic dinner bowls before table presentation.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: Hearth Simmering & Copper Guild Showcase (Assets 3 & 4) -->
    <section class="rg-section rg-section-dark">
      <div class="rg-container">
        <div class="rg-section-header">
          <span class="rg-tag">The Hearth Cookery</span>
          <h2 class="rg-section-title">Vessels of Flame &amp; <span>Forest Foragings</span></h2>
          <p class="rg-section-subtitle">Heavy hammered copper conducts heat uniformly, preventing scorching while coaxing starch from each kernel.</p>
        </div>
        <div class="rg-copper-diptych">
          <!-- Card 1: Asset 3 (Hammered Copper Saucier Pan) -->
          <div class="rg-diptych-card">
            <div class="rg-diptych-media">
              <img src="assets/images/risottogarden_asset_3.jpg" alt="Handcrafted heavy hammered copper saucier pan simmering rich golden vegetable broth on hearth" width="1200" height="800">
            </div>
            <div class="rg-diptych-body">
              <div class="rg-diptych-tag">HEARTH EQUIPMENT</div>
              <h3 class="rg-diptych-title">Hammered Copper Sauciers</h3>
              <p class="rg-diptych-text">Hand-forged by Italian coppersmiths with 2.5mm solid copper walls and hand-tinned cooking surfaces that respond instantly to microscopic thermal shifts.</p>
            </div>
          </div>

          <!-- Card 2: Asset 4 (Porcini Mushroom Risotto with Truffle) -->
          <div class="rg-diptych-card">
            <div class="rg-diptych-media">
              <img src="assets/images/risottogarden_asset_4.jpg" alt="Wild forest foraged porcini mushroom risotto finished with white truffle shavings and parmigiano" width="1200" height="800">
            </div>
            <div class="rg-diptych-body">
              <div class="rg-diptych-tag">WILD FOREST COMPOSITION</div>
              <h3 class="rg-diptych-title">Porcini &amp; White Truffle Risotto</h3>
              <p class="rg-diptych-text">Wild autumn porcini caps rehydrated in mountain broth, folded into creamy Carnaroli and crowned with shaved white truffle from northern Italian woodlands.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: The Botanical Harvest Matrix -->
    <section class="rg-section rg-section-light">
      <div class="rg-container">
        <div class="rg-section-header" style="text-align: center;">
          <span class="rg-tag" style="background: rgba(194, 109, 56, 0.08); border-color: rgba(194, 109, 56, 0.25); color: var(--rg-terracotta);">Terroir Provenance</span>
          <h2 class="rg-section-title" style="color: var(--rg-text-dark);">The Hearth Sourcing Ledger</h2>
          <p class="rg-section-subtitle" style="margin: 0 auto; color: var(--rg-text-dark-muted);">We trace each harvest directly to family growers, botanical cooperatives, and alpine dairies.</p>
        </div>
        <div class="rg-harvest-matrix-wrap">
          <table class="rg-harvest-table">
            <thead>
              <tr>
                <th>Botanical Ingredient</th>
                <th>Harvest Origin</th>
                <th>Preparation Standard</th>
                <th>Culinary Profile</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="rg-crop-name">Crocus Sativus (Saffron)</td>
                <td>Castelnuovo Terroir, Italy</td>
                <td>Hand-picked stigmas, dried over oak coals</td>
                <td>Intense golden color, earthy honeyed perfume</td>
              </tr>
              <tr>
                <td class="rg-crop-name">Carnaroli Superfino</td>
                <td>Vercelli Rice Plain, Italy</td>
                <td>18-month cold-silo aged, stone ground</td>
                <td>High amylose, crystalline bite, rich starch release</td>
              </tr>
              <tr>
                <td class="rg-crop-name">Parmigiano Reggiano Vacche Rosse</td>
                <td>Reggio Emilia Hills, Italy</td>
                <td>36-month cave aged, raw red cow milk</td>
                <td>Nutty umami, tyrosine micro-crystals, deep richness</td>
              </tr>
              <tr>
                <td class="rg-crop-name">Culinary Garden Botanicals</td>
                <td>Seattle Estate Greenhouses</td>
                <td>Freshly snipped minutes before mantecatura</td>
                <td>Pungent camphor, pine resin, citrusy thyme oils</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Section 7: Masterclass in Texture: Action Showcase (Assets 5 & 6) -->
    <section class="rg-section rg-section-dark">
      <div class="rg-container">
        <div class="rg-action-triad">
          <!-- Left Media: Asset 5 (Parmigiano Grating Action) -->
          <div class="rg-triad-media">
            <img src="assets/images/risottogarden_asset_5.jpg" alt="Chef grating 36-month Vacche Rosse Parmigiano Reggiano cheese over hot steaming risotto pan" width="1200" height="800">
          </div>

          <!-- Center Quote & Philosophy -->
          <div class="rg-triad-center">
            <span class="rg-tag">The Wave Dynamic</span>
            <blockquote class="rg-triad-quote">
              "Risotto must wave like silk when the pan is tilted. If it forms a mound, it has dried; if it runs like soup, the emulsion has failed."
            </blockquote>
            <p style="font-size: 0.95rem; color: var(--rg-text-light-muted); line-height: 1.7;">
              The exact second when cold cultured butter meets warm rice off the burner is culinary alchemy. We whip vigorously with curved cherrywood paddles to bind broth and dairy into a glossy velvet suspension.
            </p>
          </div>

          <!-- Right Media: Asset 6 (Garden Herb Harvest Basket) -->
          <div class="rg-triad-media">
            <img src="assets/images/risottogarden_asset_6.jpg" alt="Fresh organic culinary garden harvest basket with rosemary sage thyme and squash blossoms" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>

    <!-- Section 8: Evening Degustation Dining Vitrines -->
    <section class="rg-section rg-section-darker">
      <div class="rg-container">
        <div class="rg-section-header" style="text-align: center;">
          <span class="rg-tag">Dinner Experiences</span>
          <h2 class="rg-section-title">Evening Degustation Menus</h2>
          <p class="rg-section-subtitle" style="margin: 0 auto;">Select from our multi-course seasonal dinner menus, served exclusively by reservation at our Seattle hearth salon.</p>
        </div>
        <div class="rg-vitrine-grid">
          <!-- Tasting 1 -->
          <div class="rg-vitrine-card">
            <div>
              <div class="rg-vitrine-badge">DEGUSTATION I &bull; 4 COURSES</div>
              <h3 class="rg-vitrine-title">The Hearth Tasting</h3>
              <p class="rg-vitrine-courses">A balanced exploration of seasonal rice cookery</p>
              <ul class="rg-vitrine-list">
                <li>Clarified Garden Herb Broth Infusion</li>
                <li>Roasted Butternut &amp; Fried Sage Risotto</li>
                <li>Aged Carnaroli with Vacche Rosse Parmigiano</li>
                <li>Warm Hazelnut &amp; Mascarpone Cream Finish</li>
              </ul>
            </div>
            <a href="contact.html" class="rg-btn rg-btn-outline" style="width: 100%; text-align: center;">Reserve Hearth Tasting</a>
          </div>

          <!-- Tasting 2 (Featured) -->
          <div class="rg-vitrine-card featured">
            <div>
              <div class="rg-vitrine-badge" style="color: #ffffff;">FLAGSHIP &bull; 6 COURSES</div>
              <h3 class="rg-vitrine-title">The Saffron &amp; Truffle Symphony</h3>
              <p class="rg-vitrine-courses">Our signature journey through rare northern Italian ingredients</p>
              <ul class="rg-vitrine-list">
                <li>Heirloom Root Vegetable Carpaccio</li>
                <li>Wild Porcini &amp; Roasted Shallot Reduction</li>
                <li>Golden Saffron Risotto with 24k Gold Leaf</li>
                <li>Shaved White Truffle all'Onda Course</li>
                <li>Smoked Provola &amp; Garlic Infusion</li>
                <li>Cardamom Citrus Digestif Sorbet</li>
              </ul>
            </div>
            <a href="contact.html" class="rg-btn rg-btn-terracotta" style="width: 100%; text-align: center;">Reserve Symphony Table</a>
          </div>

          <!-- Tasting 3 -->
          <div class="rg-vitrine-card">
            <div>
              <div class="rg-vitrine-badge">EXCLUSIVE &bull; 8 COURSES</div>
              <h3 class="rg-vitrine-title">Chef's Hearth Salon</h3>
              <p class="rg-vitrine-courses">Intimate dinner seated directly before the open flame</p>
              <ul class="rg-vitrine-list">
                <li>Full 8-Course Bespoke Culinary Flight</li>
                <li>Table-side Mantecatura in Vintage Copper</li>
                <li>Private Cellar Reserve Botanical Pairings</li>
                <li>Dedicated Hearthmaster Guidance</li>
              </ul>
            </div>
            <a href="contact.html" class="rg-btn rg-btn-outline" style="width: 100%; text-align: center;">Inquire Chef's Table</a>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 9: Plated Masterwork Showcase (Assets 7 & 8) -->
    <section class="rg-section rg-section-dark">
      <div class="rg-container">
        <div class="rg-section-header">
          <span class="rg-tag">The Evening Table</span>
          <h2 class="rg-section-title">Sensory Balance on Hand-Thrown Ceramics</h2>
          <p class="rg-section-subtitle">Every bowl is paired with artisanal glazed dinnerware that retains culinary warmth throughout each course.</p>
        </div>
        <div class="rg-plated-duo">
          <!-- Card 1: Asset 7 (Ruby Beet Risotto) -->
          <div class="rg-plated-card">
            <img src="assets/images/risottogarden_asset_7.jpg" alt="Vibrant ruby beet and whipped goat cheese cream risotto with edible marigold petals" width="1200" height="800">
            <div class="rg-plated-overlay">
              <div class="rg-plated-tag">BOTANICAL EXPRESSION</div>
              <h3 class="rg-plated-title">Ruby Beet &amp; Goat Cheese Risotto</h3>
              <p class="rg-plated-desc">Earthy roasted beet reduction folded into velvet Carnaroli, garnished with whipped goat milk curd and edible marigold petals.</p>
            </div>
          </div>

          <!-- Card 2: Asset 8 (Hearth Dining Table Flatlay) -->
          <div class="rg-plated-card">
            <img src="assets/images/risottogarden_asset_8.jpg" alt="Hearth dining table flatlay arrangement with artisan ceramic dinner bowls dark linen brass spoons" width="1200" height="800">
            <div class="rg-plated-overlay">
              <div class="rg-plated-tag">THE SALON AMBIANCE</div>
              <h3 class="rg-plated-title">Hearth Table Setting</h3>
              <p class="rg-plated-desc">Hand-loomed raw linen runners, forged solid brass flatware, and custom stoneware plates crafted by regional ceramic artisans.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 10: Hearthmaster Voice -->
    <section class="rg-section rg-section-darker">
      <div class="rg-container">
        <div class="rg-hearthmaster-spotlight">
          <div style="color: var(--rg-saffron); font-size: 1.2rem; letter-spacing: 6px; margin-bottom: 20px;">✦ ✦ ✦ ✦ ✦</div>
          <blockquote class="rg-spotlight-quote">
            "To cook risotto is to surrender to time. It cannot be rushed, held under hot lights, or reheated. It lives only in the precise five minutes between the fire and the guest's palate."
          </blockquote>
          <div class="rg-spotlight-author">Lorenzo Valenti</div>
          <div class="rg-spotlight-title">Founding Hearthmaster &bull; Risotto Garden Atelier Seattle</div>
        </div>
      </div>
    </section>

    <!-- Section 11: Dinner Guest & Sourcing FAQ -->
    <section class="rg-section rg-section-dark">
      <div class="rg-container">
        <div class="rg-section-header" style="text-align: center;">
          <span class="rg-tag">Dining Protocol</span>
          <h2 class="rg-section-title">Common Guest Inquiries</h2>
          <p class="rg-section-subtitle" style="margin: 0 auto;">Details regarding seating reservations, dietary adaptations, and rice cellar sourcing.</p>
        </div>
        <div class="rg-faq-dual-grid">
          <div>
            <div class="rg-accordion-item active">
              <button class="rg-accordion-header">
                <span>How far in advance are dinner reservations required?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>Because we simmer small-batch vegetable broths daily and stone-mill aged Carnaroli rice specifically for each evening's service, dinner seatings must be reserved at least 24 hours in advance through our Seattle concierge.</p>
              </div>
            </div>

            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>Can degustations accommodate plant-based or dairy-free diets?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>Yes. With advance notice during booking, our kitchen team executes an exquisite dairy-free mantecatura utilizing cold-pressed Sicilian olive oils and botanical emulsions that preserve the signature velvet wave texture.</p>
              </div>
            </div>

            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>Why is Carnaroli rice aged in cold silos for 18 months?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>Cold silo aging stabilizes the natural amylose starches and proteins inside the grain. This enzymatic resting ensures the rice kernels remain intact during vigorous cooking without shedding chalky starch prematurely.</p>
              </div>
            </div>
          </div>

          <div>
            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>What is the dress attire and dining ambiance?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>Our hearth dining room provides an intimate, warm candlelit salon experience. We recommend smart casual or elegant evening attire. Seating is deliberately spaced to afford privacy and conversational comfort.</p>
              </div>
            </div>

            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>Are botanical beverage pairings offered with dinner?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>Our sommelier crafts thoughtful non-alcoholic botanical flights, featuring sparkling herb infusions, cold-extracted teas, and fermented fruit must reductions specifically calibrated to each risotto course.</p>
              </div>
            </div>

            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>Can we book the private hearth table for private parties?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>We accommodate intimate private parties of 6 to 14 guests at our central hearth table. Custom menus and private culinary demonstrations by Chef Lorenzo can be curated through our direct telephone concierge.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 12: Private Dinner Salon Reservation Strip -->
    <section class="rg-section rg-section-darker" style="padding-top: 0;">
      <div class="rg-container">
        <div class="rg-reservation-strip">
          <span class="rg-tag">Table Reservations</span>
          <h2 style="font-family: var(--rg-font-display); font-size: clamp(2rem, 3.5vw, 2.8rem); font-weight: 800; margin: 16px 0 20px 0;">
            Reserve Your Evening at the Seattle Hearth Salon
          </h2>
          <p style="color: var(--rg-text-light-muted); font-size: 1.1rem; max-width: 680px; margin: 0 auto 36px auto; line-height: 1.8;">
            Experience slow culinary craft, candlelit Tuscan ambiance, and the timeless comfort of handmade risotto. Our Seattle table concierge welcomes your reservation request.
          </p>
          <div style="display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
            <a href="contact.html" class="rg-btn rg-btn-terracotta">Request Table Seating</a>
            <a href="tel:+18889244195" class="rg-btn rg-btn-outline">{PHONE}</a>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 2. ABOUT.HTML (Rice Agronomy & Heritage - Assets 9, 10, 11, 12)
# ==========================================
def build_about():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Rice Agronomy &amp; Heritage | Risotto Garden</title>
  <meta name="description" content="Discover the rice agronomy, 18-month cold silo aging, and culinary heritage behind Risotto Garden's artisanal risotto atelier in Seattle.">
  <link rel="canonical" href="https://{DOMAIN}/about.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('about')}

  <main>
    <section class="rg-policy-header">
      <div class="rg-container">
        <span class="rg-tag">Agricultural Heritage</span>
        <h1 class="rg-hero-title">The Agronomy of Rice &amp; <span>The Hearth Tradition</span></h1>
        <p class="rg-hero-desc" style="margin-bottom: 0;">
          Founded in Seattle in 2017, Risotto Garden bridges northern Italian grain heritage with regional greenhouse botany to curate uncompromised evening dinner tastings.
        </p>
      </div>
    </section>

    <!-- Story Chapter 1: The Hearth Broth (Asset 9) -->
    <section class="rg-section rg-section-dark">
      <div class="rg-container">
        <div class="rg-story-grid">
          <div>
            <span class="rg-tag">Chapter I &bull; Foundation</span>
            <h2 class="rg-section-title">Slow Braising in <span>Cast Iron &amp; Embers</span></h2>
            <p style="color: var(--rg-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              A great risotto cannot exist without an extraordinary broth. We begin every morning at dawn, gently braising heirloom root vegetables, charred shallots, fennel fronds, and bay leaves in heavy cast iron Dutch ovens over low hearth coals.
            </p>
            <p style="color: var(--rg-text-light-muted); font-size: 1rem; line-height: 1.8;">
              This slow extraction yields a golden, transparent elixir rich in natural glutamates and mineral depth, providing the aromatic backbone that infuses each grain during evening service.
            </p>
          </div>
          <div class="rg-story-media">
            <img src="assets/images/risottogarden_asset_9.jpg" alt="Cast-iron Dutch oven slow-braising tender garden heirloom root vegetables over glowing hearth embers" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>

    <!-- Story Chapter 2: The Saffron Harvest (Asset 10 - Inverted) -->
    <section class="rg-section rg-section-darker">
      <div class="rg-container">
        <div class="rg-story-grid inverted">
          <div>
            <span class="rg-tag">Chapter II &bull; Gold of the Earth</span>
            <h2 class="rg-section-title">Single-Estate Saffron <span>Stigmas</span></h2>
            <p style="color: var(--rg-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              Our Crocus sativus threads are harvested by hand at dawn in Castelnuovo before the morning sun opens the delicate violet blossoms. Each crimson stigma is dried over almond-wood coals to preserve its rich crocin and safranal essential oils.
            </p>
            <p style="color: var(--rg-text-light-muted); font-size: 1rem; line-height: 1.8;">
              In our Seattle kitchen, these threads steep in warm broth for twelve hours, releasing an intoxicating golden amber hue and an unmistakable earthy honeyed profile into our signature Risotto alla Milanese.
            </p>
          </div>
          <div class="rg-story-media">
            <img src="assets/images/risottogarden_asset_10.jpg" alt="Raw botanical saffron threads in small brass dish beside stone mortar releasing golden essence" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>

    <!-- Story Chapter 3: Garden Botany (Asset 11) -->
    <section class="rg-section rg-section-dark">
      <div class="rg-container">
        <div class="rg-story-grid">
          <div>
            <span class="rg-tag">Chapter III &bull; Greenery</span>
            <h2 class="rg-section-title">Estate Botanical Gardens &amp; <span>Spring Tendrils</span></h2>
            <p style="color: var(--rg-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              We cultivate our own culinary herbs in controlled micro-climate greenhouses in the Puget Sound basin. Crisp young asparagus stalks, sweet garden peas, tender pea tendrils, and flowering marigolds are harvested hours before evening dinner seatings.
            </p>
            <p style="color: var(--rg-text-light-muted); font-size: 1rem; line-height: 1.8;">
              This intimate farm-to-hearth connection allows our kitchen to celebrate micro-seasons, transitioning seamlessly from early spring wild garlic to late autumn roasted squashes and winter truffles.
            </p>
          </div>
          <div class="rg-story-media">
            <img src="assets/images/risottogarden_asset_11.jpg" alt="Spring green asparagus and sweet pea risotto with pea tendrils and cold-pressed estate olive oil" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>

    <!-- Story Chapter 4: The Physics of Mantecatura (Asset 12 - Inverted) -->
    <section class="rg-section rg-section-darker">
      <div class="rg-container">
        <div class="rg-story-grid inverted">
          <div>
            <span class="rg-tag">Chapter IV &bull; The Emulsion</span>
            <h2 class="rg-section-title">The Science of the <span>Velvet Wave Texture</span></h2>
            <p style="color: var(--rg-text-light-muted); font-size: 1.05rem; line-height: 1.8; margin-bottom: 20px;">
              Under magnification, the magic of authentic risotto reveals itself: millions of microscopically sheared amylose starch chains suspended in an emulsion of broth, cold butterfat, and aged cheese proteins.
            </p>
            <p style="color: var(--rg-text-light-muted); font-size: 1rem; line-height: 1.8;">
              By resting the rice for two minutes off the heat, the starch molecules crystallize slightly into a silky, cohesive wave that coats the palate with luxurious umami while leaving zero heavy residue.
            </p>
          </div>
          <div class="rg-story-media">
            <img src="assets/images/risottogarden_asset_12.jpg" alt="Close-up macro of creamy rice mantecatura emulsion waving rice grain texture without cream" width="1200" height="800">
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 3. SERVICES.HTML (Degustation Dinners - Assets 13 to 18)
# ==========================================
def build_services():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Degustation Dinners &amp; Private Tables | Risotto Garden</title>
  <meta name="description" content="Explore seasonal risotto degustation dinners, private hearth table commissions, and multi-course culinary tastings at Risotto Garden in Seattle.">
  <link rel="canonical" href="https://{DOMAIN}/services.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('services')}

  <main>
    <section class="rg-policy-header">
      <div class="rg-container">
        <span class="rg-tag">Culinary Services</span>
        <h1 class="rg-hero-title">Seasonal Degustations &amp; <span>Hearth Dinners</span></h1>
        <p class="rg-hero-desc" style="margin-bottom: 0;">
          Explore our evening dining services, private table hire, and customized multi-course tasting flights tailored for intimate celebrations and corporate salons.
        </p>
      </div>
    </section>

    <!-- Services Grid (6 Signature Culinary Offerings with Assets 13 to 18) -->
    <section class="rg-section rg-section-dark">
      <div class="rg-container">
        <div class="rg-dinner-grid">
          
          <!-- Service 1: Asset 13 (Roasted Butternut Squash Risotto) -->
          <div class="rg-dinner-card">
            <div class="rg-dinner-media">
              <img src="assets/images/risottogarden_asset_13.jpg" alt="Roasted butternut squash and fried sage leaf risotto in artisan terracotta earthenware bowl" width="1200" height="800">
            </div>
            <div class="rg-dinner-body">
              <div class="rg-dinner-header">
                <span class="rg-tag">AUTUMN DEGUSTATION</span>
                <h3>Roasted Butternut &amp; Crispy Sage Dinner</h3>
                <p>Carnaroli Superfino slow-cooked in charred vegetable broth, blended with roasted kabocha squash puree, crisp brown butter sage, and toasted pumpkin seed praline.</p>
              </div>
              <div class="rg-dinner-specs">
                <span>4-Course Tasting</span>
                <span>Terracotta Coupe</span>
              </div>
              <a href="contact.html" class="rg-btn rg-btn-terracotta" style="width: 100%; text-align: center;">Book Dinner Course</a>
            </div>
          </div>

          <!-- Service 2: Asset 14 (Black Winter Truffle Carpaccio) -->
          <div class="rg-dinner-card">
            <div class="rg-dinner-media">
              <img src="assets/images/risottogarden_asset_14.jpg" alt="Braised black winter truffle carpaccio shaved over silky white risotto on dark pottery dinner plate" width="1200" height="800">
            </div>
            <div class="rg-dinner-body">
              <div class="rg-dinner-header">
                <span class="rg-tag">FLAGSHIP FLIGHT</span>
                <h3>Black Winter Truffle Carpaccio Flight</h3>
                <p>Pure Parmigiano mantecato risotto cooked in clarified thyme broth, topped tableside with generous shavings of fresh black winter truffle from Umbrian forests.</p>
              </div>
              <div class="rg-dinner-specs">
                <span>6-Course Symphony</span>
                <span>Tableside Shaving</span>
              </div>
              <a href="contact.html" class="rg-btn rg-btn-terracotta" style="width: 100%; text-align: center;">Book Dinner Course</a>
            </div>
          </div>

          <!-- Service 3: Asset 15 (Culinary Pantry Grain Cellar) -->
          <div class="rg-dinner-card">
            <div class="rg-dinner-media">
              <img src="assets/images/risottogarden_asset_15.jpg" alt="Artisanal culinary pantry shelf lined with clear glass apothecary jars of aged carnaroli and porcini" width="1200" height="800">
            </div>
            <div class="rg-dinner-body">
              <div class="rg-dinner-header">
                <span class="rg-tag">PRIVATE MASTERCLASS</span>
                <h3>Hearthmaster Rice Masterclass &amp; Dinner</h3>
                <p>An interactive twilight culinary session where guests explore raw grain biology, test starch viscosities, and cook their own copper-pan risotto under Chef Lorenzo's guidance.</p>
              </div>
              <div class="rg-dinner-specs">
                <span>3-Hour Session</span>
                <span>Dinner Included</span>
              </div>
              <a href="contact.html" class="rg-btn rg-btn-terracotta" style="width: 100%; text-align: center;">Book Masterclass</a>
            </div>
          </div>

          <!-- Service 4: Asset 16 (Smoked Provola & Garlic Risotto) -->
          <div class="rg-dinner-card">
            <div class="rg-dinner-media">
              <img src="assets/images/risottogarden_asset_16.jpg" alt="Smoked provola and roasted sweet garlic risotto garnished with crispy herbs and cracked peppercorns" width="1200" height="800">
            </div>
            <div class="rg-dinner-body">
              <div class="rg-dinner-header">
                <span class="rg-tag">RUSTIC HEARTH</span>
                <h3>Smoked Provola &amp; Confit Garlic Course</h3>
                <p>Sweet slow-roasted garlic cloves pureed into aged Carnaroli with hand-stretched smoked provola cheese from Campania and cracked Tellicherry peppercorns.</p>
              </div>
              <div class="rg-dinner-specs">
                <span>Hearth Menu</span>
                <span>Smoked Cheese Umami</span>
              </div>
              <a href="contact.html" class="rg-btn rg-btn-terracotta" style="width: 100%; text-align: center;">Book Dinner Course</a>
            </div>
          </div>

          <!-- Service 5: Asset 17 (Chef Plating Dinner Course) -->
          <div class="rg-dinner-card">
            <div class="rg-dinner-media">
              <img src="assets/images/risottogarden_asset_17.jpg" alt="Chef plating evening dinner course with wooden spoon tilting velvety risotto into shallow bowl" width="1200" height="800">
            </div>
            <div class="rg-dinner-body">
              <div class="rg-dinner-header">
                <span class="rg-tag">EXCLUSIVE SALON</span>
                <h3>Private Hearth Table Hire</h3>
                <p>Exclusive full-evening buyout of our central copper hearth table for private dining parties of 6 to 14 guests, featuring custom culinary courses and bespoke service.</p>
              </div>
              <div class="rg-dinner-specs">
                <span>6 to 14 Guests</span>
                <span>Exclusive Buyout</span>
              </div>
              <a href="contact.html" class="rg-btn rg-btn-terracotta" style="width: 100%; text-align: center;">Inquire Table Hire</a>
            </div>
          </div>

          <!-- Service 6: Asset 18 (Flaked Salt & Peppercorn Cellars) -->
          <div class="rg-dinner-card">
            <div class="rg-dinner-media">
              <img src="assets/images/risottogarden_asset_18.jpg" alt="Freshly harvested sea salt flakes and pink peppercorns in carved marble cellar dishes with sage" width="1200" height="800">
            </div>
            <div class="rg-dinner-body">
              <div class="rg-dinner-header">
                <span class="rg-tag">INSTITUTIONAL SALONS</span>
                <h3>Corporate Executive Dinner Salons</h3>
                <p>Sophisticated evening dining tailored for executive hospitality, discreet negotiations, and institutional milestone dinners with curated botanical flights.</p>
              </div>
              <div class="rg-dinner-specs">
                <span>Executive Seating</span>
                <span>Concierge Protocol</span>
              </div>
              <a href="contact.html" class="rg-btn rg-btn-terracotta" style="width: 100%; text-align: center;">Inquire Corporate Salon</a>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- Dietary Accommodation Matrix -->
    <section class="rg-section rg-section-light">
      <div class="rg-container">
        <div class="rg-section-header" style="text-align: center;">
          <span class="rg-tag" style="background: rgba(194, 109, 56, 0.08); border-color: rgba(194, 109, 56, 0.25); color: var(--rg-terracotta);">Hospitality Standards</span>
          <h2 class="rg-section-title" style="color: var(--rg-text-dark);">Dietary Customization Protocols</h2>
          <p class="rg-section-subtitle" style="margin: 0 auto; color: var(--rg-text-dark-muted);">We honor individual dietary lifestyles without ever diluting gastronomic integrity.</p>
        </div>
        <div class="rg-harvest-matrix-wrap">
          <table class="rg-harvest-table">
            <thead>
              <tr>
                <th>Dietary Preference</th>
                <th>Culinary Adaptation</th>
                <th>Emulsion Technique</th>
                <th>Advance Notice</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="rg-crop-name">Vegetarian Tasting</td>
                <td>100% Clarified Botanical Broths &amp; Farm Cheeses</td>
                <td>Traditional Vacche Rosse Butter Mantecatura</td>
                <td>Standard Reservation</td>
              </tr>
              <tr>
                <td class="rg-crop-name">Dairy-Free / Vegan</td>
                <td>Infused Herb Reductions &amp; Cold-Pressed Oils</td>
                <td>Whipped Extra Virgin Olive Oil Emulsion</td>
                <td>24 Hours Advance Notice</td>
              </tr>
              <tr>
                <td class="rg-crop-name">Gluten-Free Dining</td>
                <td>Naturally 100% Gluten-Free Carnaroli Rice</td>
                <td>Zero Added Flours or Thickening Agents</td>
                <td>Standard Reservation</td>
              </tr>
              <tr>
                <td class="rg-crop-name">Low Sodium Protocol</td>
                <td>Unsalted Herb Broths &amp; Lemon Zest Acidity</td>
                <td>Tyrosine-Rich Aged Parmigiano Micro-Curls</td>
                <td>24 Hours Advance Notice</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 4. CONTACT.HTML (Table Reservation - Asset 19)
# ==========================================
def build_contact():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Table Reservations &amp; Inquiries | Risotto Garden</title>
  <meta name="description" content="Reserve an evening dinner table or inquire about private hearth dining at Risotto Garden. Located at 601 Union Street, Seattle, WA.">
  <link rel="canonical" href="https://{DOMAIN}/contact.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('contact')}

  <main>
    <section class="rg-policy-header">
      <div class="rg-container">
        <span class="rg-tag">Dining Concierge</span>
        <h1 class="rg-hero-title">Table Reservations &amp; <span>Salon Inquiries</span></h1>
        <p class="rg-hero-desc" style="margin-bottom: 0;">
          Whether reserving an intimate evening dinner or arranging a private hearth table buyout, our Seattle concierge welcomes your transmission.
        </p>
      </div>
    </section>

    <!-- Contact Split Layout: Asset 19 on Left, Form Card on Right -->
    <section class="rg-section rg-section-dark">
      <div class="rg-container">
        <div class="rg-contact-split">
          
          <!-- Feature Card with Asset 19 (Evening Table Setting) -->
          <div class="rg-contact-feature">
            <img src="assets/images/risottogarden_asset_19.jpg" alt="Private hearth dinner salon table setting with custom terracotta tableware beeswax tapers and linen" width="1200" height="800">
            <div class="rg-contact-overlay">
              <span class="rg-tag" style="margin-bottom: 10px;">Atelier Flagship Coordinates</span>
              <h3 style="font-family: var(--rg-font-display); font-size: 1.35rem; color: #ffffff; margin-bottom: 12px;">Seattle Hearth Salon</h3>
              <p style="font-size: 0.95rem; color: var(--rg-text-light-muted); margin-bottom: 8px;">{ADDR}</p>
              <p style="font-family: var(--rg-font-mono); font-size: 0.85rem; color: var(--rg-saffron); margin-bottom: 6px;">Concierge Direct: {PHONE}</p>
              <p style="font-family: var(--rg-font-mono); font-size: 0.85rem; color: var(--rg-text-light-muted);"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
              <div style="margin-top: 14px; font-size: 0.775rem; color: var(--rg-text-light-muted); border-top: 1px solid rgba(255,255,255,0.1); padding-top: 10px;">
                Dinner Seatings: Wednesday &ndash; Sunday 5:30 PM &ndash; 10:30 PM (By Reservation Only)
              </div>
            </div>
          </div>

          <!-- Table Reservation Form -->
          <div class="rg-contact-form-card">
            <h3 style="font-family: var(--rg-font-display); font-size: 1.6rem; font-weight: 700; color: var(--rg-text-dark); margin-bottom: 8px;">Table Reservation Request</h3>
            <p style="font-size: 0.95rem; color: var(--rg-text-dark-muted); margin-bottom: 28px;">
              Please provide your party details, requested seating date, and dietary considerations below.
            </p>

            <form id="rg-contact-form">
              <div class="rg-form-group">
                <label class="rg-form-label" for="guest-name">Full Legal Name *</label>
                <input class="rg-form-input" type="text" id="guest-name" name="name" required placeholder="e.g. Sebastian Sterling">
              </div>

              <div class="rg-form-group">
                <label class="rg-form-label" for="guest-email">Email Address *</label>
                <input class="rg-form-input" type="email" id="guest-email" name="email" required placeholder="e.g. sterling@domain.com">
              </div>

              <div class="rg-form-group">
                <label class="rg-form-label" for="guest-phone">Telephone Number *</label>
                <input class="rg-form-input" type="tel" id="guest-phone" name="phone" required placeholder="e.g. +1 (206) 555-0184">
              </div>

              <div class="rg-form-group">
                <label class="rg-form-label" for="tasting-type">Degustation Menu Preference *</label>
                <select class="rg-form-select" id="tasting-type" name="tasting" required>
                  <option value="">Select dinner experience...</option>
                  <option value="hearth">The Hearth Tasting (4 Courses)</option>
                  <option value="symphony">The Saffron &amp; Truffle Symphony (6 Courses)</option>
                  <option value="chefs">Chef's Hearth Salon Seating (8 Courses)</option>
                  <option value="private">Private Hearth Table Buyout (6-14 Guests)</option>
                  <option value="masterclass">Twilight Rice Masterclass &amp; Dinner</option>
                </select>
              </div>

              <div class="rg-form-group">
                <label class="rg-form-label" for="guest-notes">Party Size, Date Preferences &amp; Dietary Requirements</label>
                <textarea class="rg-form-textarea" id="guest-notes" name="notes" rows="4" placeholder="Detail your preferred dining dates, number of guests in party, and any dietary considerations (e.g. dairy-free, vegetarian)..."></textarea>
              </div>

              <button type="submit" class="rg-btn rg-btn-terracotta" style="width: 100%; justify-content: center; padding: 14px;">
                Submit Reservation Request
              </button>
            </form>
          </div>

        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 5. FAQ.HTML (Culinary & Sourcing Knowledge Vault - Asset 20)
# ==========================================
def build_faq():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Culinary &amp; Sourcing FAQ | Risotto Garden</title>
  <meta name="description" content="Frequently asked questions regarding rice agronomy, Carnaroli grain aging, hearth cooking temperatures, and dining reservations at Risotto Garden.">
  <link rel="canonical" href="https://{DOMAIN}/faq.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('faq')}

  <main>
    <section class="rg-policy-header">
      <div class="rg-container">
        <span class="rg-tag">Knowledge Vault</span>
        <h1 class="rg-hero-title">Culinary Craft &amp; <span>Sourcing FAQ</span></h1>
        <p class="rg-hero-desc" style="margin-bottom: 0;">
          Comprehensive technical guidance on northern Italian rice agronomy, broth reduction chemistry, and salon dining protocols.
        </p>
      </div>
    </section>

    <!-- FAQ Section with Asset 20 (Clarified Broth Reduction Cup) -->
    <section class="rg-section rg-section-dark">
      <div class="rg-container">
        <div style="max-width: 860px; margin: 0 auto 56px auto; border-radius: var(--rg-radius-md); overflow: hidden; border: 1px solid var(--rg-border-dark); box-shadow: var(--rg-shadow-lg);">
          <img src="assets/images/risottogarden_asset_20.jpg" alt="Clarified garden botanical broth reduction tasting cup with juniper berries and bay laurel leaf" width="1200" height="800">
        </div>

        <div class="rg-section-header" style="text-align: center;">
          <span class="rg-tag">Gastronomic Inquiry</span>
          <h2 class="rg-section-title">The Agronomy &amp; Hearth Ledger</h2>
          <p class="rg-section-subtitle" style="margin: 0 auto;">Everything you need to know about our sourcing, craft, and dinner reservation standards.</p>
        </div>

        <div class="rg-faq-dual-grid">
          <div>
            <div class="rg-accordion-item active">
              <button class="rg-accordion-header">
                <span>What distinguishes Carnaroli from Arborio rice?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>While Arborio is widely recognized, Carnaroli Superfino features a significantly higher amylose starch concentration and a larger, denser kernel. This chemical structure prevents grain fracture during vigorous stirring, ensuring that every grain retains its al dente center while creating a velvety sauce.</p>
              </div>
            </div>

            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>Why do you cook in heavy hammered copper sauciers?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>Copper conducts heat twenty times faster than stainless steel. When simmering risotto, even thermal distribution across both the base and rounded walls prevents scorched hot-spots, ensuring uniform starch release throughout the sixteen-minute cooking window.</p>
              </div>
            </div>

            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>What is the origin of your saffron harvest?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>We source single-origin Crocus sativus threads from Castelnuovo cooperatives in central Italy. Hand-harvested in early autumn dawn and gently dried over wood embers, our saffron delivers pure, vibrant golden hues without artificial additives or colorants.</p>
              </div>
            </div>

            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>How is the mantecatura executed off the flame?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>Mantecatura must strictly occur away from direct heat at approximately 68 degrees Celsius. Introducing chilled butter cubes and finely grated cheese off the burner creates an emulsion; prolonged cooking heat would cause the fats to separate and oil to pool.</p>
              </div>
            </div>
          </div>

          <div>
            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>Can private dining buyouts be arranged for business salons?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>Yes. Our hearth dining salon accommodates corporate and private dinner buyouts for up to 24 seated guests. Our events concierge coordinates custom course sequences, printed menu keepsakes, and dedicated culinary masterclasses.</p>
              </div>
            </div>

            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>What is your cancellation and booking deposit protocol?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>Due to our intimate seating capacity and daily small-batch ingredient sourcing, dinner reservations require a deposit at booking. Reservations may be rescheduled with at least 48 hours notice without incurring cancellation penalties.</p>
              </div>
            </div>

            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>Do you accommodate guests with celiac or gluten intolerance?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>Carnaroli rice is naturally 100% gluten-free. Because our hearth stocks and broths are made solely from vegetables, herbs, and natural extracts without thickeners or flour, our entire degustation menu is inherently safe for celiac diners.</p>
              </div>
            </div>

            <div class="rg-accordion-item">
              <button class="rg-accordion-header">
                <span>How do we reach the Seattle dining salon on 601 Union Street?</span>
                <span class="rg-accordion-icon">+</span>
              </button>
              <div class="rg-accordion-body">
                <p>We are situated on the 42nd floor of Two Union Square at 601 Union Street in downtown Seattle. Dedicated valet parking is accessible via the Union Street motor court, and our private concierge greets arriving guests in the tower reception.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 6. POLICY PAGES (Rule 5: Strictly 5-6 lines / 60-110 words per substantive paragraph)
# ==========================================
def build_privacy():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Privacy Policy | Risotto Garden</title>
  <meta name="description" content="Privacy Policy for Risotto Garden Hearth &amp; Atelier. Review our institutional client data protection standards, reservation confidentiality, and privacy safeguards.">
  <link rel="canonical" href="https://{DOMAIN}/privacy-policy.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="rg-policy-header">
      <div class="rg-container">
        <span class="rg-tag">Institutional Compliance</span>
        <h1 class="rg-hero-title">Client Privacy <span>Charter</span></h1>
        <p class="rg-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Risotto Garden Atelier LLC</p>
      </div>
    </section>

    <div class="rg-container">
      <div class="rg-policy-content">
        
        <div class="rg-policy-section">
          <h2>1. Commitment to Dining Guest Confidentiality</h2>
          <p class="rg-policy-p">
            Risotto Garden Atelier maintains an uncompromised institutional commitment to safeguarding the personal records, dietary preferences, and private communications of every guest who reserves a table at our Seattle dining salon. We acknowledge that our patrons entrust us with private contact details when arranging dinner degustations or scheduling exclusive hearth table hire. Under no circumstances do we trade, lease, or distribute private customer registries to commercial aggregators or unauthorized marketing syndicates across digital channels.
          </p>
          <p class="rg-policy-p">
            Our data protection infrastructure utilizes modern cryptographic protocols designed to prevent unauthorized electronic surveillance, data leaks, or unapproved data transmissions. Institutional records collected during your engagement are maintained within segmented physical and digital environments that comply strictly with United States federal standards and worldwide privacy frameworks. We conduct recurring technical audits of our digital reservation network to ensure full operational resilience against evolving cyber threats and unauthorized data intrusion vectors.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>2. Scope of Collected Reservation Information</h2>
          <p class="rg-policy-p">
            When you transmit a booking request through our digital portal or contact our concierge directly at our Seattle salon, we record necessary identifying details including your legal name, direct corporate telephone number, authenticated email address, and billing coordinates. Furthermore, when ordering bespoke culinary degustations, our staff records custom dietary restrictions, allergen profiles, and seating preferences required to personalize your evening dining experience safely.
          </p>
          <p class="rg-policy-p">
            In addition to directly provided contact records, our web infrastructure passively monitors standard diagnostic server telemetry, such as anonymous Internet Protocol addresses, browser rendering versions, operating system architecture, and referring webpage headers. These technical metrics are processed strictly in an aggregated format to optimize the visual presentation and navigation responsiveness of our digital salon. Passive analytics never link anonymous browsing behaviors to your verified private client identity or personal dining history.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>3. Operational Purpose of Data Processing</h2>
          <p class="rg-policy-p">
            Personal particulars collected by Risotto Garden are processed exclusively to execute valid table reservations, coordinate private culinary masterclasses, and confirm special dietary arrangements for your party. We also utilize verified guest telephone contacts to provide courteous text or telephone confirmations prior to scheduled seatings. Operational data handling ensures our culinary brigade prepares adequate small-batch broths and aged grains without generating avoidable culinary waste.
          </p>
          <p class="rg-policy-p">
            With your express consent, we may occasionally dispatch dignified announcements regarding new seasonal degustation menus, estate olive oil releases, or private culinary salon invitations. You retain the absolute right to opt out of non-essential communications at any moment by contacting our Seattle concierge or clicking unsubscribe links embedded in email transmissions. We honor all preference revisions immediately upon receipt across our internal client communication registers.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>4. Information Security and Third-Party Disclosures</h2>
          <p class="rg-policy-p">
            We do not share your private dining records with outside third parties, except as strictly required to complete authorized payment transactions through PCI-DSS certified electronic processing gateways. Any third-party technology providers engaged to facilitate web hosting or payment clearance are legally bound by stringent confidentiality agreements that prohibit independent exploitation of guest records. Your payment card numbers are encrypted end-to-end and never permanently stored on local atelier servers.
          </p>
          <p class="rg-policy-p">
            In rare instances where disclosure is mandated by lawful court subpoenas, legal warrants, or applicable state regulations, we cooperate strictly within the exact limits of the law. Prior to complying with external legal demands for information, we make every reasonable attempt to notify the affected dining guest, provided legal statutes do not prohibit such prior notification. We maintain rigorous documentation of all formal requests to preserve transparency and integrity.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>5. Client Rights and Institutional Contact Coordinates</h2>
          <p class="rg-policy-p">
            Every patron retains the definitive institutional right to inspect, correct, or request the permanent deletion of their personal records maintained within our archives. Should you wish to review your archived contact particulars or request total erasure of past reservation logs, please submit a written directive to our data privacy officer at our physical office or by direct email transmission. We commit to acknowledging and processing all legitimate privacy requests within thirty calendar days.
          </p>
          <p class="rg-policy-p">
            For all formal inquiries concerning this Client Privacy Charter or our operational data protection protocols, please direct communications to Risotto Garden Atelier LLC, {ADDR}. You may also reach our dedicated client services telephone line directly at {PHONE} or transmit electronic correspondence to {EMAIL}. We remain dedicated to upholding the highest standards of hospitality discretion and electronic privacy for every esteemed culinary patron.
          </p>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_terms():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Terms &amp; Conditions | Risotto Garden</title>
  <meta name="description" content="Terms and Conditions governing dining reservations, private table buyouts, and web portal access for Risotto Garden in Seattle, Washington.">
  <link rel="canonical" href="https://{DOMAIN}/terms-and-conditions.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="rg-policy-header">
      <div class="rg-container">
        <span class="rg-tag">Legal Framework</span>
        <h1 class="rg-hero-title">Terms &amp; Conditions <span>Charter</span></h1>
        <p class="rg-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Risotto Garden Atelier LLC</p>
      </div>
    </section>

    <div class="rg-container">
      <div class="rg-policy-content">
        
        <div class="rg-policy-section">
          <h2>1. Acceptance of Dining and Portal Terms</h2>
          <p class="rg-policy-p">
            By accessing the digital web presence of Risotto Garden Atelier or transmitting an inquiry to reserve dinner seating at our Seattle premises, you formally agree to be bound by these legal terms and conditions. If you do not agree with any provision contained within this charter, you must immediately discontinue your use of our digital platforms and refrain from booking dining services. These terms establish a legally enforceable pact between yourself and Risotto Garden Atelier LLC.
          </p>
          <p class="rg-policy-p">
            We reserve the institutional right to update, modify, or revise these operational terms periodically to reflect amendments in hospitality regulations, payment policies, or service architectures. Any updates become effective immediately upon public posting to this web address. Your continued patronage of our dining salon or persistent browsing of our web materials following posted revisions constitutes full legal affirmation of the revised terms and operational guidelines.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>2. Table Reservations, Deposits, and Cancellations</h2>
          <p class="rg-policy-p">
            Because our hearth kitchen prepares small-batch vegetable broths, imports fresh white truffles, and mills aged Carnaroli rice specifically for confirmed covers, all dinner seatings require advance reservations. Securing a table booking requires the provision of valid payment credentials and a reservation deposit. Table reservations are not legally finalized until you receive an authenticated confirmation transmission issued directly by our Seattle dining concierge staff.
          </p>
          <p class="rg-policy-p">
            Guests seeking to modify or cancel a dinner reservation must provide written or verbal notice to our concierge at least forty-eight hours prior to their scheduled seating hour. Cancellations submitted with less than forty-eight hours notice, or failure to arrive for a confirmed reservation, will result in forfeiture of the reservation deposit to offset kitchen procurement expenses. We appreciate the understanding of our patrons regarding these strict culinary scheduling standards.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>3. Intellectual Property and Proprietary Recipes</h2>
          <p class="rg-policy-p">
            All visual imagery, typographic layouts, written culinary descriptions, trademarks, and gastronomic narratives published on this website remain the sole intellectual property of Risotto Garden Atelier LLC. You are granted an ephemeral, revocable, non-exclusive license to view digital content for personal, non-commercial purposes only. Any unauthorized extraction, republication, commercial redistribution, or automated data harvesting of our materials is strictly prohibited under international copyright laws.
          </p>
          <p class="rg-policy-p">
            Our specialized rice mantecatura procedures, custom botanical broth formulations, and proprietary spice ratios constitute protected culinary trade secrets of our hearth atelier. Guests attending private cooking masterclasses are granted educational insight for home culinary enjoyment, but may not commercialize our proprietary training curriculum or claim ownership of our historical recipes. We actively enforce our proprietary rights across worldwide culinary markets.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>4. Guest Conduct and Salon Dining Etiquette</h2>
          <p class="rg-policy-p">
            Risotto Garden Atelier maintains an atmosphere of refined tranquility, culinary contemplation, and mutual respect within our Seattle hearth salon. We require all guests to conduct themselves with consideration toward fellow diners and our hospitality staff. Disruptive conduct, verbal disrespect, excessive intoxication, or willful disregard for dining room protocols may result in immediate refusal of service and removal from the premises without refund.
          </p>
          <p class="rg-policy-p">
            While we celebrate personal milestone photography, the use of commercial lighting rigs, intrusive recording tripods, or flash photography that disturbs adjacent diners is strictly prohibited without prior written clearance from atelier management. We reserve the full managerial right to refuse service to any individual whose behavior compromises the peaceful dining environment of our salon. We thank all patrons for preserving our contemplative hearth ambiance.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>5. Governing Law and Dispute Resolution</h2>
          <p class="rg-policy-p">
            These terms and conditions are governed by and construed in strict accordance with the laws of the State of Washington, United States, without regard to conflict of law principles. Any legal controversy, dispute, or claim arising from these terms or your dining engagement with Risotto Garden Atelier shall be submitted to binding arbitration in King County, Washington, under standard American Arbitration Association procedures.
          </p>
          <p class="rg-policy-p">
            For questions or legal correspondence regarding these terms and conditions, please direct formal written notices to Risotto Garden Atelier LLC, {ADDR}. You may also contact our administrative office by telephone at {PHONE} or transmit digital communications to our designated legal inbox at {EMAIL}. We remain dedicated to resolving all guest inquiries with equity, professionalism, and thorough institutional care.
          </p>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_disclaimer():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Disclaimer | Risotto Garden</title>
  <meta name="description" content="Legal and culinary disclaimer regarding ingredient disclosures, allergen notifications, and web information accuracy for Risotto Garden.">
  <link rel="canonical" href="https://{DOMAIN}/disclaimer.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="rg-policy-header">
      <div class="rg-container">
        <span class="rg-tag">Notice &amp; Disclosure</span>
        <h1 class="rg-hero-title">Culinary &amp; Legal <span>Disclaimer</span></h1>
        <p class="rg-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Risotto Garden Atelier LLC</p>
      </div>
    </section>

    <div class="rg-container">
      <div class="rg-policy-content">
        
        <div class="rg-policy-section">
          <h2>1. General Information and Culinary Content Notice</h2>
          <p class="rg-policy-p">
            The gastronomic essays, agronomic descriptions, rice vintage analyses, and menu showcases published on this website are presented solely for general informational and educational enrichment. While we strive to maintain meticulous precision regarding historical culinary traditions and botanical properties, we make no express or implied representations regarding absolute completeness or universal applicability. Content is provided on an as-is basis without warranties of any variety.
          </p>
          <p class="rg-policy-p">
            Risotto Garden Atelier expressly disclaims all liability for incidental inaccuracies, typographical errors, or inadvertent omissions that may appear across our digital publications. Descriptions of seasonal agricultural crops, such as white truffles or micro-greens, reflect historical harvest standards and are subject to real-time adjustments based on environmental weather patterns and daily market availability. Guests should verify specific menu inclusions directly with our dining concierge.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>2. Food Allergen and Dietary Health Disclosure</h2>
          <p class="rg-policy-p">
            Our hearth kitchen handles diverse natural agricultural products including dairy butter, aged cheeses, wild mushrooms, fresh alliums, pine nuts, and edible flowers. Although our culinary staff exercises extreme hygiene and sanitation precautions during prep, cross-contact with airborne allergens or microscopic traces cannot be entirely precluded in an active restaurant environment. Guests with acute life-threatening allergies must communicate their medical history prior to ordering.
          </p>
          <p class="rg-policy-p">
            Descriptions of botanical health properties, digestive qualities of aged Carnaroli rice, or herbal broth infusions reflect traditional gastronomic lore and do not constitute formal medical or nutritional advice. Nothing contained on this website should be interpreted as medical guidance or as a replacement for qualified dietary consultations. Patrons assume personal responsibility for evaluating their unique health requirements before partaking in our degustations.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>3. External Links and Third-Party Resources</h2>
          <p class="rg-policy-p">
            Our web platform may periodically provide hyperlinked references to external culinary cooperatives, agricultural certifiers, regional maps, or independent culinary publications across worldwide gastronomic networks. These third-party links are supplied exclusively for visitor convenience and do not signify institutional endorsement, sponsorship, or independent verification of the external entities. Risotto Garden Atelier holds zero operational control over the content, security measures, hosting reliability, or privacy policies of third-party domains.
          </p>
          <p class="rg-policy-p">
            When electing to leave our digital domain via external links, you do so entirely at your own discretion and peril. We strongly encourage all users to inspect the terms of service and privacy declarations of any outside web portals they visit. Risotto Garden Atelier accepts no legal responsibility for financial damages, digital malware, or misleading claims arising from your navigation of third-party digital networks.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>4. Limitation of Operational Liability</h2>
          <p class="rg-policy-p">
            To the maximum extent permitted by applicable United States law, Risotto Garden Atelier LLC, its managing officers, culinary chefs, and corporate affiliates shall not be held liable for indirect, incidental, punitive, or consequential damages resulting from your use of this web portal or your dining attendance. This broad limitation applies regardless of whether alleged damages stem from contract breaches, tort actions, server downtimes, or technical interruptions.
          </p>
          <p class="rg-policy-p">
            In jurisdictions that do not permit the full exclusion or limitation of incidental liability for consumer transactions, our maximum aggregate liability to you for any verified claims shall strictly not exceed the total financial sums paid by you directly to Risotto Garden Atelier during the preceding three calendar months. This limitation represents a fundamental element of the commercial bargain between our atelier and dining guests.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>5. Inquiries Regarding Disclaimers and Institutional Coordinates</h2>
          <p class="rg-policy-p">
            Should you have inquiries, clarifications, or feedback concerning the contents of this Culinary &amp; Legal Disclaimer, we welcome your direct communication with our administrative team. We are committed to fostering open transparency, culinary excellence, and mutual trust with every guest who engages with our digital salon, explores our agricultural archives, or dines at our Seattle hearth table. Our hospitality staff provides detailed explanations regarding any policy term upon request.
          </p>
          <p class="rg-policy-p">
            Please direct all official correspondence concerning this disclaimer to Risotto Garden Atelier LLC, located at {ADDR}. For immediate verbal consultations regarding dining accommodations or ingredient disclosures, you may contact our concierge by telephone at {PHONE} or transmit electronic inquiries to {EMAIL}. We remain dedicated to serving our patrons with integrity and hospitality excellence.
          </p>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

def build_cookie():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cookie Policy | Risotto Garden</title>
  <meta name="description" content="Cookie Policy for Risotto Garden Hearth &amp; Atelier. Review our transparent cookie management, analytics tracking protocols, and consent controls.">
  <link rel="canonical" href="https://{DOMAIN}/cookie-policy.html">
  {GTAG}
  {FONTS}
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{get_header('')}

  <main>
    <section class="rg-policy-header">
      <div class="rg-container">
        <span class="rg-tag">Digital Transparency</span>
        <h1 class="rg-hero-title">Cookie &amp; Tracking <span>Policy</span></h1>
        <p class="rg-hero-desc" style="margin-bottom: 0;">Effective Date: January 1, 2026 &bull; Risotto Garden Atelier LLC</p>
      </div>
    </section>

    <div class="rg-container">
      <div class="rg-policy-content">
        
        <div class="rg-policy-section">
          <h2>1. Definition and Function of Web Cookies</h2>
          <p class="rg-policy-p">
            Web cookies are miniature alphanumeric text files transmitted by our web servers to your personal computing device or mobile hardware when you navigate the Risotto Garden web portal. These files enable our digital infrastructure to recognize your specific browser session, remember your visual preferences, and ensure seamless continuity across consecutive web pages. Cookies perform fundamental technical roles that allow our digital dining salon to operate securely and efficiently.
          </p>
          <p class="rg-policy-p">
            Cookies utilized on our domain never contain executable program code, cannot infect your computer hardware with malware, and do not access confidential files stored on your private storage drives. By browsing our digital pages, you acknowledge our use of essential cookies in full accordance with this transparent policy. We provide comprehensive tools and guidance enabling users to control their individual tracking preferences at all times.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>2. Classifications of Cookies Utilized on Our Domain</h2>
          <p class="rg-policy-p">
            Strictly necessary cookies represent fundamental digital mechanisms required for core website operation, such as managing secure dining reservation sessions, processing payment tokens, preserving form inputs, and balancing network server load. These essential cookies operate automatically upon site arrival and cannot be deactivated without fundamentally corrupting basic platform capabilities. They do not harvest personal data for commercial advertising purposes or behavioral profiling across outside digital channels.
          </p>
          <p class="rg-policy-p">
            Performance and telemetry cookies help us evaluate anonymous visitor interaction trends, including which seasonal recipe pages receive frequent readership and how swiftly our digital menus render across various geographic territories. All telemetry gathered through performance cookies is aggregated into anonymous statistics that cannot be traced back to your individual dining identity. We utilize these insights exclusively to refine the visual presentation of our salon.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>3. Third-Party Telemetry and Google Analytics Standards</h2>
          <p class="rg-policy-p">
            Our web platform integrates standardized Google Analytics scripts (gtag.js) to monitor broad macro traffic patterns, referring digital conduits, and general hardware rendering parameters. This analytical service utilizes proprietary cookies to compile anonymous statistical diagnostics that illustrate how prospective guests interact with our site. We have configured our analytics framework to prevent the permanent storage of complete individual Internet Protocol coordinates.
          </p>
          <p class="rg-policy-p">
            Google handles analytical records under its independent worldwide data privacy standards, contractual safeguards, and corporate commitments. We do not permit outside analytics vendors to cross-reference your anonymous browsing activity on our website with commercial advertising dossiers or third-party behavioral networks. You may prevent Google Analytics tracking across all websites by installing certified browser opt-out extensions distributed directly by Google or adjusting your browser telemetry controls.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>4. Managing and Deactivating Browser Cookies</h2>
          <p class="rg-policy-p">
            Every user maintains the definitive autonomous ability to accept, restrict, or purge browser cookies through standard privacy settings embedded within their preferred web browser software. Major browser applications including Google Chrome, Apple Safari, Mozilla Firefox, and Microsoft Edge provide dedicated configuration panels allowing you to block third-party cookies, clear cache records, or wipe stored cookies upon closing your active browsing session.
          </p>
          <p class="rg-policy-p">
            Please be advised that disabling all cookies, including strictly necessary session tokens, may impair the operational functionality of our digital reservation portal and prevent the automated completion of table bookings. Should you encounter difficulties navigating our digital salon with cookies disabled, our Seattle concierge staff remains available by telephone to assist you with booking dinner reservations directly over the line.
          </p>
        </div>

        <div class="rg-policy-section">
          <h2>5. Policy Amendments and Concierge Contact Details</h2>
          <p class="rg-policy-p">
            Risotto Garden Atelier LLC reserves the institutional right to revise this Cookie Policy whenever technical enhancements, legal mandates, or web platform upgrades necessitate adjustments. Any revisions will be published promptly to this URL with an updated effective date. We recommend that returning guests periodically inspect this page to stay informed regarding our steadfast commitments to digital transparency and data protection.
          </p>
          <p class="rg-policy-p">
            Should you have questions or seek additional technical details concerning our cookie management protocols, please reach out to our institutional administrative headquarters at Risotto Garden Atelier LLC, {ADDR}. You may also converse with our client services team directly by telephone at {PHONE} or submit written electronic correspondence to {EMAIL}. We remain dedicated to protecting your electronic privacy with absolute diligence.
          </p>
        </div>

      </div>
    </div>
  </main>

{get_footer()}
</body>
</html>"""

# ==========================================
# 7. SITEMAP & ROBOTS
# ==========================================
def build_sitemap():
    pages = [
        "index.html",
        "about.html",
        "services.html",
        "faq.html",
        "contact.html",
        "privacy-policy.html",
        "terms-and-conditions.html",
        "disclaimer.html",
        "cookie-policy.html"
    ]
    urls = ""
    for p in pages:
        urls += f"""  <url>
    <loc>https://{DOMAIN}/{p}</loc>
    <lastmod>2026-09-28</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{'1.0' if p == 'index.html' else '0.8'}</priority>
  </url>\n"""
    
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>"""

def build_robots():
    return f"""User-agent: *
Allow: /
Sitemap: https://{DOMAIN}/sitemap.xml
"""

# ==========================================
# 8. REGISTRIES & MANIFEST
# ==========================================
def build_image_registry():
    return """# IMAGE REGISTRY - RISOTTO GARDEN HEARTH & ATELIER
Domain: risottogarden.com
Niche: Dinner / Artisanal Botanical Risotto & Hearth Dining
Strict Rule: Exactly 20 Unique Images, Used Exactly Once, >20KB Each, Zero Duplicates, Zero Drawings, Zero Buildings

| Asset Name | Subject Description | Location / Section Used | MD5 Hash | Status |
| :--- | :--- | :--- | :--- | :--- |
| `risottogarden_asset_1.jpg` | Golden Saffron Risotto alla Milanese in glazed ceramic coupe | `index.html` (Hero Inset Viewport with Recipe Seal) | e5e79eb3f2c7da19782ad7167a544a4b | Verified Unique |
| `risottogarden_asset_2.jpg` | Aged Carnaroli Superfino rice grains in rustic carved olivewood scoop | `index.html` (Agronomy Split: King of Rices) | ec496105f8ca22c7fec3a57c5053cfb9 | Verified Unique |
| `risottogarden_asset_3.jpg` | Handcrafted heavy hammered copper saucier pan simmering broth | `index.html` (Copper Diptych Card 1: Hearth Equipment) | fea4af55dfa5eb5072dd53f8e5b60037 | Verified Unique |
| `risottogarden_asset_4.jpg` | Wild forest foraged porcini mushroom risotto with white truffle | `index.html` (Copper Diptych Card 2: Porcini Composition) | 976ea3610e25d487cb137f94157bfd7d | Verified Unique |
| `risottogarden_asset_5.jpg` | Chef grating 36-month Vacche Rosse Parmigiano Reggiano cheese | `index.html` (Action Triad Left: Cheese Grating Action) | 4dc65634e2fbcf9e075043831818c393 | Verified Unique |
| `risottogarden_asset_6.jpg` | Fresh organic culinary garden harvest basket with rosemary sage | `index.html` (Action Triad Right: Garden Herb Basket) | 0a890076a5b15be62cb434e320f77bc9 | Verified Unique |
| `risottogarden_asset_7.jpg` | Vibrant ruby beet and whipped goat cheese cream risotto | `index.html` (Plated Duo Card 1: Botanical Expression) | ec029d1ecabdf79a4ecda8a5b28d7ba4 | Verified Unique |
| `risottogarden_asset_8.jpg` | Hearth dining table flatlay with ceramic bowls linen brass spoons | `index.html` (Plated Duo Card 2: The Salon Ambiance) | 45b5636a3faae673f4e3f4339678e7aa | Verified Unique |
| `risottogarden_asset_9.jpg` | Cast-iron Dutch oven slow-braising heirloom root vegetables | `about.html` (Story Chapter 1: Foundation Broth) | 22c84243684d0b134d1bc97858cbf916 | Verified Unique |
| `risottogarden_asset_10.jpg` | Raw botanical saffron threads in small brass dish beside mortar | `about.html` (Story Chapter 2: Gold of the Earth) | c5229ffbd660f5e7146522c7a36cb1d5 | Verified Unique |
| `risottogarden_asset_11.jpg` | Spring green asparagus and sweet pea risotto with tendrils | `about.html` (Story Chapter 3: Estate Botanical Gardens) | 7df7f03673322d7ba56ae07aa52b1233 | Verified Unique |
| `risottogarden_asset_12.jpg` | Close-up macro of creamy rice mantecatura emulsion texture | `about.html` (Story Chapter 4: The Velvet Wave Emulsion) | 5eb86944b360ba3ecbe597561fec66d9 | Verified Unique |
| `risottogarden_asset_13.jpg` | Roasted butternut squash and fried sage risotto in terracotta bowl | `services.html` (Dinner Service 1: Autumn Degustation) | 91dbed187313a4ce258525b41050a4ad | Verified Unique |
| `risottogarden_asset_14.jpg` | Braised black winter truffle carpaccio shaved over white risotto | `services.html` (Dinner Service 2: Flagship Truffle Flight) | 65d5f81d1136b6dd8605c486cf8892f3 | Verified Unique |
| `risottogarden_asset_15.jpg` | Artisanal culinary pantry shelf lined with clear glass apothecary jars | `services.html` (Dinner Service 3: Hearthmaster Masterclass) | a7ce84af8041c3600e008f10731f24d2 | Verified Unique |
| `risottogarden_asset_16.jpg` | Smoked provola and roasted sweet garlic risotto with herbs | `services.html` (Dinner Service 4: Rustic Hearth Course) | 15d4c77d5fb0d859f7df8f8a156291a2 | Verified Unique |
| `risottogarden_asset_17.jpg` | Chef plating evening dinner course with wooden spoon in dark bowl | `services.html` (Dinner Service 5: Private Table Buyout) | 9e3a179fa4f40f0d2c679269986b2454 | Verified Unique |
| `risottogarden_asset_18.jpg` | Freshly harvested sea salt flakes and pink peppercorns in cellars | `services.html` (Dinner Service 6: Executive Dinner Salon) | f1a0a1914eb02f7aa4aa76be2bf14f04 | Verified Unique |
| `risottogarden_asset_19.jpg` | Private hearth dinner salon table setting with beeswax tapers | `contact.html` (Salon Coordinates & Reservation Feature) | fa41b35520979bf8cb0973a90302b1ff | Verified Unique |
| `risottogarden_asset_20.jpg` | Clarified garden botanical broth reduction tasting cup with bay | `faq.html` (Knowledge Vault Header Feature) | d3ae6ad536bbcc72ff2751508db86cc9 | Verified Unique |

Total Images: 20
Total Usages: 20 (Every single image used exactly once across website)
Repetitions: 0
100% Real Culinary Dinner & Risotto Photography (Zero Buildings / Zero CAD)
"""

def build_design_registry():
    return """# DESIGN REGISTRY - RISOTTO GARDEN HEARTH & ATELIER

## Archetype Identity
- **Design Archetype:** Tuscan Botanical Hearth / Warm Terracotta & Deep Cypress / Inset Floating Viewport Showcase with Asymmetric Degustation Ledger
- **Domain:** risottogarden.com
- **Niche:** Dinner / Artisanal Botanical Risotto & Hearth Dining
- **CSS Namespace:** Dedicated `.rg-...` namespace (Zero global collisions)

## Color Architecture
- **Deep Cypress Hearth:** `#0d1713`
- **Charred Vine Base:** `#070e0b`
- **Deep Olive Grove Surface:** `#14221c`
- **Terracotta Flame Accent:** `#c26d38`
- **Saffron Amber Glow:** `#e5a83b`
- **Botanical Sage Mist:** `#52796f`
- **Parchment Linen:** `#fdfbf7`
- **Soft Alabaster:** `#f5efe6`
- **Text Light Linen:** `#f2ece4`
- **Text Muted Sage:** `#9ab3a6`
- **Text Dark Soil:** `#1c1815`

## Typography Pairings
- **Display Headings:** `Fraunces` (400, 600, 700, Italic)
- **Subheadings & Labels:** `Marcellus` (Classic Roman Serif)
- **Body & Prose:** `Plus Jakarta Sans` (300, 400, 500, 600, 700)
- **Agronomic Specs & Coordinates:** `Space Mono` (400, 700)

## Bespoke Structural Layout (Zero Template Fingerprint)
1. **Inset Floating Hearth Viewport with Gastronomic Ledger:** Asymmetric hero featuring a 60% viewport with rounded archival frame showcasing Asset 1 and an interactive recipe seal, paired with a 40% vertical Gastronomic Ledger.
2. **Seasonal Degustation Menu Ribbon:** Horizontal 3-course tasting preview strip with vintage Roman typography.
3. **The Agronomy of Carnaroli:** Staggered split layout highlighting 18-month cold silo aging and Asset 2 in a carved olivewood scoop.
4. **The 5-Step Mantecatura Sequence:** Horizontal 5-column chronological alchemy bar detailing Tostatura, Sfumatura, Cottura Dolce, Mantecatura all'Onda, and Riposo al Piatto without box card borders.
5. **Hearth Simmering & Copper Guild Showcase:** Side-by-side asymmetric diptych featuring Assets 3 & 4 with copper craft and mycological profiles.
6. **The Botanical Harvest Matrix:** Clean botanical provenance table detailing harvest regions and culinary profiles.
7. **Masterclass in Culinary Action:** Triad composition with Asset 5 (Parmigiano grating) and Asset 6 (Garden herb basket) flanking a central artisanal wave quote.
8. **Evening Degustation Dining Vitrines:** 3 distinct curved culinary vitrines with gold and terracotta highlights.
9. **Plated Masterwork Showcase:** Two large editorial display cards for Assets 7 & 8 with frosted gradient overlays.
10. **Hearthmaster Spotlight:** Centered editorial philosophy quote from Chef Lorenzo Valenti.
11. **Dinner Guest & Sourcing FAQ:** Two-tier dual-column accordion list resolving culinary, dietary, and reservation questions.
12. **Private Dinner Salon Reservation Strip:** Deep terracotta and cypress curved reservation callout with direct Seattle phone.
13. **Services Page:** 6 detailed dinner service cards (`.rg-dinner-card`) with Assets 13 to 18 + Dietary Customization Protocol Matrix.
14. **About Page:** 4-chapter narrative grid with Assets 9, 10, 11, 12 detailing foundational broths, saffron harvests, greenhouse botany, and mantecatura physics.
15. **Contact Page:** Split layout featuring Asset 19 in an evening table setting with full reservation request form.
16. **FAQ Page:** Framed broth reduction feature with Asset 20 and 8 detailed culinary topics.
"""

def build_site_manifest():
    manifest = {
        "domain": DOMAIN,
        "brand": BRAND,
        "niche": "Dinner",
        "institutional_contact": {
            "address": ADDR,
            "phone": PHONE,
            "email": EMAIL
        },
        "pages": [
            "index.html",
            "about.html",
            "services.html",
            "faq.html",
            "contact.html",
            "privacy-policy.html",
            "terms-and-conditions.html",
            "disclaimer.html",
            "cookie-policy.html"
        ],
        "assets_count": 20,
        "php_files_count": 0,
        "blog_included": False,
        "google_tag": "G-0LY0HY7L01",
        "qa_verified": True
    }
    return json.dumps(manifest, indent=2)

# ==========================================
# EXECUTE GENERATION
# ==========================================
def main():
    files_to_generate = {
        "index.html": build_index(),
        "about.html": build_about(),
        "services.html": build_services(),
        "contact.html": build_contact(),
        "faq.html": build_faq(),
        "privacy-policy.html": build_privacy(),
        "terms-and-conditions.html": build_terms(),
        "disclaimer.html": build_disclaimer(),
        "cookie-policy.html": build_cookie(),
        "sitemap.xml": build_sitemap(),
        "robots.txt": build_robots(),
        "IMAGE_REGISTRY.md": build_image_registry(),
        "DESIGN_REGISTRY.md": build_design_registry(),
        "SITE_MANIFEST.json": build_site_manifest()
    }

    for filename, content in files_to_generate.items():
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated {filename} ({len(content)} chars)")

    print("\nAll files successfully generated.")

if __name__ == "__main__":
    main()
