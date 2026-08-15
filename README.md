# AffiStyle Pro - Custom Affiliate Card Generator for WordPress

**AffiStyle Pro** is a high-performance, conversion-focused WordPress plugin designed for affiliate marketers, niche bloggers, and product review sites. Create stunning, responsive affiliate product boxes, multi-product comparison tables, vs-cards, and high-converting deal cards with automatic international geo-routing, built-in click analytics, and native Gutenberg block support.

---

## 🚀 Key Features

- **16+ High-Converting Layout Templates**: Choose from 2 Free minimalist horizontal/vertical styles and 14 Pro templates (Dark Mode Sleek, Rounded Modern Shadow, Tiered 3-Column Comparison Grids, A vs B Versus Cards, Horizontal Spec Sheets, and Minimalist Dark Grids).
- **🌍 Geo-Targeted Multi-Destination Links**: Automatically detect your visitors' geographic location (US, UK, India, etc.) and route them to regional store URLs (Amazon US, Amazon UK, Amazon IN) to maximize affiliate commissions.
- **⚡ Native Gutenberg Block & Shortcode Integration**: Insert affiliate boxes seamlessly into any page, post, or custom post type using the native Gutenberg block or simple shortcodes: `[aff_box id="123"]`.
- **📊 Built-In Click Tracking Analytics**: Monitor affiliate link engagement with an asynchronous AJAX tracker and view total click counts per card directly within your WordPress admin post list table.
- **🔒 Tamper-Proof Cryptographic Licensing**: Powered by Lemon Squeezy API with HMAC SHA-256 cryptographic signatures tied to your site domain, guarding against unauthorized database option tampering.
- **🛡️ Privacy-First & GDPR Compliant**: Privacy-by-design architecture that prioritizes CDN/edge server headers (Cloudflare, Cloudfront, GeoIP), validates IP formats, respects loopbacks, and provides developer filter hooks (`affistyle_enable_remote_geo_lookup`) to prevent unauthorized third-party PII transmission.
- **⚡ Sub-Millisecond Performance**: Single-query metadata compilation, in-memory static status caching, and conditional asset loading ensure zero impact on page load speed or Google Core Web Vitals.

---

## 📥 Installation Instructions

1. **Download the Plugin**: Download the plugin `.zip` archive from your repository or store account.
2. **Upload to WordPress**:
   - Log in to your WordPress Dashboard.
   - Navigate to **Plugins > Add New > Upload Plugin**.
   - Select the `AffiStyle-Affiliate-Card-Generator.zip` file and click **Install Now**.
3. **Activate the Plugin**: Click **Activate Plugin** to complete the installation.
4. **Access AffiStyle Menu**: A new **AffiStyle** item will appear in your admin sidebar.

---

## 🔑 Pro License Activation

To unlock Pro templates (Styles 3 through 16), geo-targeted store links, and click tracking analytics:

1. **Get a License Key**: Visit our official store at [dreainno.lemonsqueezy.com](https://dreainno.lemonsqueezy.com/) to purchase an AffiStyle Pro license key.
2. **Open License Page**: In your WordPress dashboard, navigate to **AffiStyle > Pro License**.
3. **Activate License**:
   - Enter your Lemon Squeezy license key into the **License Key** field.
   - Click **Activate License**.
   - Once verified, your status will update to **Active (Pro Unlocked)**, enabling all 16 layout templates and advanced features instantly.

To deactivate or transfer a license to another domain, return to **AffiStyle > Pro License** and click **Deactivate License**.

---

## 📖 Usage Guide

### 1. Creating an Affiliate Card Box
1. Navigate to **AffiStyle > Add New Box**.
2. Enter a title for your affiliate card (e.g., *Sony WH-1000XM5 Wireless Headphones*).
3. In the **Affiliate Card Builder Details** metabox:
   - **Template Style**: Select from Free or Pro templates (Styles 1–16).
   - **Product Description / Snippet**: Add a short review or summary text.
   - **Default Destination URL**: Set your primary affiliate destination link.
   - **Button Text**: Customize the CTA button (e.g., *Claim Deal*, *Buy Now*, *Check Price*).
   - **Geo-Targeted Links (Pro)**: Enter specific regional store URLs for US, UK, and India.
   - **Badge Text**: Add an optional tag (e.g., *Editor's Choice*, *Best Budget*, *Top Pick*).
   - **Product Image**: Upload or select a product image via the WordPress Media Library.
   - **Custom Styling**: Adjust card background and button background colors with native color pickers.
4. Click **Publish**.

### 2. Embedding via Shortcode
Copy the auto-generated ID from the post list or editor and place the shortcode anywhere in your content:
```text
[aff_box id="123"]
```

### 3. Embedding via Gutenberg Block Editor
1. Edit any page or post in the Block Editor.
2. Click the **+** (Add Block) icon and search for **Affiliate Box** (`affistyle/aff-box`).
3. Select your saved affiliate card from the block settings dropdown menu in the sidebar.
4. The card will automatically render server-side in your layout.

---

## 🛠️ Developer & Technical Notes

### Architecture & Standards Compliance
- **WordPress Coding Standards (WPCS)**: 100% compliant with official WPCS rules, incorporating strict Yoda conditions, `wp_unslash()` superglobal handling, and type-specific sanitization (`sanitize_text_field`, `esc_url_raw`, `sanitize_hex_color`).
- **Internationalization (i18n)**: Fully translation-ready with text domain `'affistyle'`, `load_plugin_textdomain()` on `plugins_loaded`, and placeholders (`printf`) for global multi-language compatibility.
- **Single-Query Metadata Fetching**: `AffiStyle_Database::get_box_data()` compiles all custom post meta in a single cached database call (`get_post_meta($post_id)`), eliminating redundant `wp_postmeta` SQL queries.
- **Bigint Analytics Schema**: Uses a lightweight custom table (`{$wpdb->prefix}affistyle_clicks`) with composite `UNIQUE KEY (post_id, region)` and `bigint(20)` counters for ultra-fast SQL upserts (`INSERT ... ON DUPLICATE KEY UPDATE`).
- **Conditional Asset Loading**: Frontend stylesheets and tracking scripts are conditionally enqueued only when an affiliate card is rendered on the page, maintaining 100/100 Lighthouse performance scores.
- **GDPR Privacy Hooks**:
  ```php
  // Disable remote third-party IP lookups programmatically if required by privacy policy
  add_filter( 'affistyle_enable_remote_geo_lookup', '__return_false' );
  ```

---

## 📄 License & Credits

- **License**: GPL v2 or later
- **Author**: Mayuresh Pandit ([GitHub](https://github.com/GamersStop))
- **Repository**: [AffiStyle on GitHub](https://github.com/GamersStop/AffiStyle---WordPress-Affiliate-Card-Box-Generator)
