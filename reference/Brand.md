# AffiStyle Brand Identity & Feature Guide

AffiStyle is a lightweight, conversion-focused WordPress affiliate card and showcase plugin designed for bloggers, niche publishers, and content creators. It pairs modern design aesthetics with native block-editor workflows, zero layout bloat, and transparent compliance standards.

---

## Brand Foundation

* **Brand Name:** AffiStyle
* **Parent Brand / Studio:** Dreainno
* **Official Website:** [https://affistyle.shop/](https://affistyle.shop/)
* **Parent Brand Website:** [https://dreainno.online/](https://dreainno.online/)
* **Author:** Mayuresh Pandit
* **Value Proposition:** Fast, modular, high-converting affiliate product boxes built specifically for the modern WordPress editing experience.

---

## Visual Design System

| Token | Hex Value | Usage |
| :--- | :--- | :--- |
| **Primary Blue** | `#2563EB` | Primary call-to-action buttons, active indicators, accents |
| **Primary Hover** | `#1D4ED8` | Hover state for primary interactive elements |
| **Secondary Accent** | `#0F172A` | Card headers, main body copy, strong typography |
| **Success Green** | `#10B981` | Ratings, pros checkmarks, active status badges |
| **Alert Red** | `#EF4444` | Cons markers, critical notices, deletion warnings |
| **Border Neutral** | `#E2E8F0` | Card borders, table dividers, input boundaries |
| **Surface Light** | `#F8FAFC` | Box backgrounds, comparison stripes, preview surfaces |
| **Muted Gray** | `#718096` | Subtitles, helper descriptions, FTC disclaimers |

---

## Core Feature Architecture

### 1. Dynamic Gutenberg Integration
* Native block with real-time server-side previews inside the block editor.
* Pure dynamic data rendering: never locks stale HTML into post content.
* Automatic status detection that gracefully handles trashed or deleted cards without breaking post layouts.

### 2. High-Conversion Card Layouts
* Responsive layouts optimized across mobile, tablet, and desktop screens.
* Built-in display modules: pros & cons lists, star ratings, pricing badges, and custom call-to-action buttons.
* Side-by-side comparison cards and multi-product tables for product reviews and roundups.

### 3. Compliance & Privacy
* Automatic FTC affiliate disclosure injection beneath cards.
* Granular disclosure controls: toggle globally or customize messaging per product card.
* Privacy-first architecture: no third-party tracking scripts or cookie dependencies.

### 4. Click Analytics & Insights
* Built-in click tracking using nonces and client-side debouncing to eliminate duplicate logging.
* Interactive analytics dashboard displaying total clicks, top-performing cards, and visitor demographic insights.
* Date-range filtering to evaluate campaign trends over customizable periods.

---

## Free vs. Pro Feature Tiers

| Feature Capability | Core (Free) | Pro |
| :--- | :--- | :--- |
| **Gutenberg Dynamic Block** | Included | Included |
| **Responsive Card Styles** | Standard responsive styles | 12+ advanced & comparison styles |
| **FTC Compliance Engine** | Global automated disclaimer | Per-box custom overrides & placement |
| **Click Tracking** | Included (with anti-duplicate protection) | Included |
| **Analytics Dashboard** | 7-day performance overview | Advanced date filtering & regional insights |
| **Multi-Product Comparisons** | Single-product focus | Side-by-side matrices & versus cards |
| **License & Automatic Updates** | WordPress.org repository | Dedicated license activation & priority updates |

---

## Technical Specifications

* **Minimum WordPress Version:** 6.3+
* **Minimum PHP Version:** 7.4+
* **Asset Footprint:** Lightweight scoped CSS, zero heavy external JavaScript libraries
* **License:** GPL-2.0-or-later