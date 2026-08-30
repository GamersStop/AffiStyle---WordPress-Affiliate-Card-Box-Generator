---
name: brand-guidelines
description: Applies AffiStyle's official brand identity, color palette, typography, glassmorphism textures, composition principles, and visual formatting rules to any web app, UI component, marketing banner, presentation, or documentation.
license: Complete terms in LICENSE.txt
---

# AffiStyle Brand Identity & Visual Design System

## Overview

This skill defines the official visual design guidelines, color palettes, typography, surface textures, and composition standards for **AffiStyle** (by Dreainno / Mayuresh Pandit) — a lightweight, high-conversion WordPress affiliate card and showcase plugin.

Whenever creating UI components, landing pages, marketing banners, SVG assets, documentation, or social graphics for AffiStyle, follow these specifications.

**Keywords**: AffiStyle, Dreainno, WordPress affiliate plugin, brand guidelines, design system, color palette, glassmorphism, typography, Plus Jakarta Sans, composition, banner design, visual identity.

---

## 1. Brand Foundation

* **Brand Name:** AffiStyle
* **Parent Brand / Studio:** Dreainno
* **Author / Founder:** Mayuresh Pandit
* **Official Website:** [https://affistyle.shop/](https://affistyle.shop/)
* **Studio Website:** [https://dreainno.online/](https://dreainno.online/)
* **Core Value Proposition:** Turn plain affiliate links into clean, high-converting product boxes, comparison showdown cards, and cloaked URLs with zero bloat and native Gutenberg integration.
* **Brand Personality:** Modern, high-tech, trustworthy, conversion-focused, lightweight, and frictionless.

---

## 2. Color System & Design Tokens

AffiStyle operates with a dual-system palette: a **Dark Obsidian Cyber Mode** (used in marketing banners, landing page hero sections, and promotional visuals) and a **Clean Surface Light Mode** (used for in-content WordPress product boxes, editorial reading, and FTC disclaimers).

### A. Primary Brand Colors (Vibrant Blues)
| Token Name | Hex Code | Purpose & Usage |
| :--- | :--- | :--- |
| **Primary Blue** | `#2563EB` | Core brand color, primary CTA buttons, active state indicators |
| **Primary Hover** | `#1D4ED8` | Hover/focus states for interactive primary elements |
| **Electric Accent** | `#3B82F6` | Neon borders, glowing highlights, text link emphasis |
| **Vivid Cyan** | `#38BDF8` | Gradient transitions, subtitle accents, tech glow reflections |

### B. Dark Mode & Marketing Surfaces (Obsidian Glass)
| Token Name | Hex / RGBA | Purpose & Usage |
| :--- | :--- | :--- |
| **Obsidian Deep** | `#060912` | Main page background, canvas backdrop |
| **Surface Dark** | `#0C1222` | Header background, secondary panel background |
| **Glass Card Fill**| `rgba(14, 21, 38, 0.70)` | Frosted glassmorphic card body with backdrop blur |
| **Glass Border** | `rgba(255, 255, 255, 0.08)` | Subtle 1px translucent card border stroke |
| **Border Glow** | `rgba(59, 130, 246, 0.35)` | Illuminated rim light on active/featured cards |
| **Text Main (Dark)**| `#F8FAFC` | Primary headings, titles, high-contrast values |
| **Text Muted (Dark)**| `#94A3B8` | Body descriptions, subtitles, secondary metadata |

### C. Light Mode & In-Content Cards (Editorial WordPress Theme)
| Token Name | Hex Code | Purpose & Usage |
| :--- | :--- | :--- |
| **Surface Light** | `#F8FAFC` | Box backgrounds, comparison table alternating stripes |
| **Card White** | `#FFFFFF` | In-post card background, review box surface |
| **Border Neutral** | `#E2E8F0` | Card borders, comparison dividers, input boundaries |
| **Secondary Dark** | `#0F172A` | Card headers, main body copy, strong typography |
| **Muted Slate** | `#718096` / `#64748B` | Helper text, star review counts, FTC affiliate disclosures |

### D. Functional & Conversion Accents
| Token Name | Hex Code | Purpose & Usage |
| :--- | :--- | :--- |
| **Conversion Emerald** | `#10B981` | Pros checkmarks, "Limited Time" tags, "Claim Deal" high-urgency CTAs |
| **Star Gold** | `#F59E0B` / `#FBBF24`| Star rating indicators, review summaries |
| **Urgent Red** | `#EF4444` | Cons markers, discount callouts, warning notices |
| **Editor's Purple** | `#8B5CF6` | "Editor's Choice" pill badges, featured product tag |

---

## 3. Typography Standards

### Font Families
* **Primary Typeface:** `'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
* **Google Fonts Import:**
  ```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  ```
* **Accent / Human Touch Script:** Optional cursive/handwritten script (e.g. *Caveat*, *Playwrite*, or *Architects Daughter*) for subtle humanized annotations (e.g., *"together!"*, *"take a look..."*, *"no coding required"*).

### Type Hierarchy
| Level | Size / Line Height | Weight | Letter Spacing | Styling / Color |
| :--- | :--- | :--- | :--- | :--- |
| **Display / Hero H1** | `44px - 56px` / `1.1` | 800 (ExtraBold) | `-0.03em` | Dual tone: White + Electric Blue accent |
| **Section Title H2** | `32px - 40px` / `1.2` | 700 (Bold) | `-0.02em` | `#F8FAFC` (Dark) / `#0F172A` (Light) |
| **Card Title H3** | `20px - 24px` / `1.3` | 700 (Bold) | `-0.01em` | Bold product title with clear visual weight |
| **Body Text** | `15px - 16px` / `1.6` | 400 - 500 (Regular/Medium) | `normal` | `#94A3B8` (Dark) / `#475569` (Light) |
| **Pill / Badge Label**| `11px - 12px` / `1.2` | 700 (Bold) | `+0.05em` | Uppercase, rounded pill with star/icon |
| **FTC Disclaimer** | `12px - 13px` / `1.4` | 400 (Regular) | `normal` | `#718096`, italic or subdued opacity |

---

## 4. Texture, Lighting & Surface Materials

### 1. Glassmorphism & Translucency
* **Backdrop Blur:** Use `backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);`
* **Translucent Layering:** Dark frosted panels (`rgba(14, 21, 38, 0.70)`) overlaying deep backgrounds.
* **Rim Lighting:** Subtle 1px borders with top-left specular highlights:
  ```css
  border: 1px solid rgba(255, 255, 255, 0.12);
  box-shadow: 0 16px 36px -10px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.15);
  ```

### 2. High-Tech Dot Matrix & Optical Gradients
* **Dot Grid Background:** Subtle techno-pattern in the background creating depth:
  ```css
  background-image: radial-gradient(rgba(59, 130, 246, 0.15) 1px, transparent 1px);
  background-size: 24px 24px;
  ```
* **Radial Lighting Pockets:** Position cyan and blue radial glow spots behind key visual elements:
  ```css
  background: radial-gradient(circle at 80% 20%, rgba(56, 189, 248, 0.12), transparent 40%),
              radial-gradient(circle at 20% 80%, rgba(37, 99, 235, 0.15), transparent 50%);
  ```

### 3. Layered 3D Depth & Ghost Typography
* **Ghost Display Watermarks:** Large, faint uppercase outline or low-opacity typography (`rgba(255, 255, 255, 0.04)`) placed in the background layer behind foreground mockups for editorial depth.
* **Floating Elevation:** High elevation multi-stop shadows for floating cards:
  ```css
  box-shadow: 0 20px 40px -12px rgba(0, 0, 0, 0.4), 0 0 25px rgba(59, 130, 246, 0.15);
  ```

---

## 5. Composition & Layout Principles

### Asymmetric Hero Composition (Banner / Landing Page Pattern)
1. **Left Anchor (Brand & Direct Value):**
   - Official 3D Folded Ribbon Icon + AffiStyle wordmark + version pill.
   - High-impact two-phrase headline: *"Boost Clicks. Increase Commissions."*
   - Clear value explanation: *"no coding required"*.
   - Feature metric grid (4 icons in frosted tiles).
   - Trust strip: WordPress compatibility badge + Gutenberg integration check.
2. **Right Anchor (Dynamic Showcase Stacks):**
   - Cascading, overlapping 3D glass product cards tilted at gentle angles.
   - Interactive anatomy inside each card:
     - Top badge pill (`★ BEST SELLER`, `★ EDITOR'S CHOICE`, `★ LIMITED TIME`).
     - Product thumbnail inside a rounded container with contrasting backdrop.
     - Product title, category subtitle, star rating with review count.
     - Price comparison (`$49.00` strikethrough `$99.00`).
     - High-contrast pill CTA button (`Claim Deal [Lock Icon]`).
   - Floating social proof / CTR metric badge (`📈 35%+ Increase in CTR`).
   - Glowing 3D WordPress pedestal seal anchoring the lower right corner.

---

## 6. Official Brand Assets & Iconography

* **Brand Icon Anatomy:**
  - A stylized, 3D continuous folded architectural ribbon forming the letter **"A"**.
  - Saturated cyan-to-royal-blue gradient with smooth highlight sweeps along curvature.
  - Tactile affiliate price tag ($ symbol) anchored to the right leg of the ribbon with a luminous ring.
  - Background: Dark squircle with subtle embossed browser wireframe dots and header.
* **Card Element Icons:**
  - Modern, 2px stroke geometric line icons (Grid, Sliders, Lightning Bolt, Device Screen, Shield, Star).
  - Enclosed in rounded glass square tiles (`border-radius: 10px; background: rgba(59, 130, 246, 0.1)`).

---

## 7. FTC Compliance & Privacy Rules

* Every generated affiliate box must provide support for an unobtrusive but legally compliant FTC disclosure statement.
* Text: *"Disclosure: When you purchase through links on our site, we may earn an affiliate commission at no extra cost to you."*
* Styling: Muted gray (`#718096` / `#94A3B8`), smaller scale (`12px`), bottom-anchored or discreet footer position.
* Zero third-party tracker scripts or cookie injections; lightweight scoped CSS only.
