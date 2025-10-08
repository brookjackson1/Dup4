# Static Images Documentation

## Overview
All static images for the F1 Racing App are stored in `app/static/images/pages/` and properly referenced using Jinja2's `url_for()` function.

## Images Added

### 1. **f1-hero.jpg** (114 KB)
- **Used in:** `index.html`
- **Purpose:** Hero banner image on homepage
- **Dimensions:** 1400x600px
- **Features:** Dark overlay with white text overlay for better readability

### 2. **f1-history.jpg** (40 KB)
- **Used in:** `history.html`
- **Purpose:** Header image for F1 History page
- **Dimensions:** 1200x400px
- **Content:** Vintage Formula 1 racing imagery

### 3. **f1-championship.jpg** (182 KB)
- **Used in:** `championships.html`
- **Purpose:** Header image for Championships page
- **Dimensions:** 1200x400px
- **Content:** F1 racing action shot

### 4. **f1-circuits.jpg** (128 KB)
- **Used in:** `circuits.html`
- **Purpose:** Header image for Famous Circuits page
- **Dimensions:** 1200x400px
- **Content:** Racing circuit track imagery

### 5. **f1-about.jpg** (127 KB)
- **Used in:** `about.html`
- **Purpose:** Header image for About page
- **Dimensions:** 1200x400px
- **Content:** Formula 1 car close-up

### 6. **f1-racing-action.jpg** (182 KB)
- **Used in:** Available for future use
- **Purpose:** Backup/alternative racing image
- **Dimensions:** 1200x400px

## Implementation Details

### Jinja2 Template Usage
All images use the proper Flask static file pattern:
```html
<img src="{{ url_for('static', filename='images/pages/f1-hero.jpg') }}"
     class="card-img-top"
     alt="Formula 1 Racing"
     onerror="this.src='https://via.placeholder.com/1200x400/E10600/FFFFFF?text=Fallback+Text'"
     style="max-height: 400px; object-fit: cover;">
```

### Features
- ✅ **Fallback URLs:** Each image has a placeholder fallback using `onerror`
- ✅ **Responsive:** Images use `object-fit: cover` for proper scaling
- ✅ **Performance:** All images optimized to reasonable file sizes
- ✅ **Accessibility:** All images include descriptive `alt` attributes

## Pages with Static Images

1. **Home (index.html)** - Hero image with overlay
2. **About (about.html)** - Header image with detailed content sections
3. **History (history.html)** - Header image with F1 history timeline
4. **Championships (championships.html)** - Header image with champion tables
5. **Circuits (circuits.html)** - Header image with famous circuit information

## Directory Structure
```
app/
├── static/
│   └── images/
│       ├── pages/
│       │   ├── f1-hero.jpg
│       │   ├── f1-history.jpg
│       │   ├── f1-championship.jpg
│       │   ├── f1-circuits.jpg
│       │   ├── f1-about.jpg
│       │   └── f1-racing-action.jpg
│       └── drivers/
│           └── (driver photos)
└── templates/
    ├── index.html
    ├── about.html
    ├── history.html
    ├── championships.html
    └── circuits.html
```

## Total Storage
- **Total Size:** 784 KB
- **Number of Images:** 6
- **Average Size:** 131 KB per image

## Notes
- All images are from Unsplash and are free to use
- Images are high-quality JPEG format
- All images are properly committed to Git repository
- Changes pushed to GitHub repository (brookjackson1/Dup4)
