# XNDRSOUND Design System

**Version:** 1.0.0
**Status:** Defined
**Base Theme:** Urban Collage

---

## 1. Color Palette

### Primary Colors
| Token | Value | Usage |
| :--- | :--- | :--- |
| `var(--bg-color)` | `#0a0a0a` | Global Site Background (Deep Black) |
| `var(--text-color)` | `#ededed` | Primary Text (Off-White) |

### Accent Colors
| Token | Value | Usage |
| :--- | :--- | :--- |
| `var(--neon-accent)` | `#ff3333` | Primary CTA, Hovers, Highlights (Neon Red) |
| `var(--warm-accent)` | `#c2a878` | Secondary Accents, Subtlety (Gold/Beige) |

### Functional
| Value | Usage |
| :--- | :--- |
| `#222222` | Borders, Card Backgrounds |
| `#444444` | Inactive States, Secondary Text |

---

## 2. Typography

### Primary Heading (Display)
*   **Font Family:** 'Anton', sans-serif
*   **Weight:** 400 (Regular)
*   **Usage:** Hero Titles, Section Headers, Navigation Links (Overlay)
*   **Scale:**
    *   `5rem` (Section Titles)
    *   `3rem` (Sub-headers)

### Body Copy (Monospace)
*   **Font Family:** 'Roboto Mono', monospace
*   **Weight:** 400 (Regular), 700 (Bold)
*   **Usage:** Paragraphs, functional text, minimal UI elements.
*   **Scale:** `1rem` (Base), `0.85rem` (Meta/Tags)

---

## 3. UI Components

### Buttons
*   **Standard CTA (`.btn-cta`, `.btn-stream`)**
    *   Border: 1px solid `#444`
    *   Background: Transparent
    *   Text: Uppercase, Bold
    *   **Hover State:** Background `var(--neon-accent)`, Text `#000`

### Navigation
*   **Type:** Overlay / Hamburger
*   **Link Style:** Uppercase, 'Anton' font.
*   **Hover:** Color shift to `var(--neon-accent)`.

---

## 4. Spacing & Layout
*   **Section Padding:** `2rem` (Vertical/Horizontal)
*   **Container Width:** Max `1400px` (Grid), `800px` (Text)
*   **Grid Gap:** `10px` (Collage effect)

---

## 5. Assets Map
*   **Hero Image:** `static/img/hero_new.jpg`
*   **Bio Image:** `static/img/bio_city.jpg`
*   **Logo:** `static/img/official_logo.png`
