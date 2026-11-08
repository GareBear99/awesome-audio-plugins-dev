#!/bin/bash
# download_images.sh — Replace placeholder PNGs with real plugin screenshots
# Run from the repo root: bash scripts/download_images.sh
#
# This script downloads product screenshots from official sources.
# Some URLs may require a browser — those are listed in IMAGE_SOURCES.md for manual download.
# Image sources re-verified 2026-11-08: dead sources either have a live replacement
# above or are commented out with a dated note (local asset retained, nothing deleted).

set -o pipefail
ASSETS="LINK_PAGES/assets"
mkdir -p "$ASSETS"

download() {
  local name="$1" url="$2"
  local dest="$ASSETS/${name}.png"
  echo "Downloading: $name"
  if curl -sL --max-time 30 -o "$dest" "$url" 2>/dev/null; then
    local size
    size=$(wc -c < "$dest" 2>/dev/null | tr -d ' ')
    if [ "$size" -gt 5000 ]; then
      echo "  ✓ $name ($size bytes)"
    else
      echo "  ✗ $name — too small ($size bytes), likely failed"
      rm -f "$dest"
    fi
  else
    echo "  ✗ $name — download failed"
  fi
}

echo "=== GitHub Repo Screenshots ==="

# Dragonfly Reverb — collage of all 4 reverb UIs
download "dragonfly-reverb" "https://raw.githubusercontent.com/michaelwillis/dragonfly-reverb/master/collage.png"

# PaulXStretch
download "paulxstretch" "https://sonosaurus.com/paulxstretch/assets/images/paulxstretch_screenshot.png"

# Surge XT — from the official website assets
download "surge-xt" "https://surge-synthesizer.github.io/images/digital.png"

# Wolf Shaper
download "wolf-shaper" "https://raw.githubusercontent.com/wolf-plugins/wolf-shaper/master/docs/images/screenshot.png"

# Dexed — from the user website
# dexed — screenshot source DEAD as of 2026-11-08: old https://asb2m10.github.io/dexed/img/dexed.png 404s;
# no full screenshot exists in the repo. Local asset is the repo logo (assets/ui/dexed-logo.png).
# download "dexed" "https://raw.githubusercontent.com/asb2m10/dexed/master/assets/ui/dexed-logo.png"

# Chowdhury DSP — screenshots from the plugin repos (verified live 2026-11-08)
download "chowmatrix" "https://raw.githubusercontent.com/Chowdhury-DSP/ChowMatrix/main/manual/screenshots/full_gui.png"
download "chowtapemodel" "https://raw.githubusercontent.com/jatinchowdhury18/AnalogTapeModel/master/Plugin/Screenshots/full_gui.png"
download "chowphaser" "https://raw.githubusercontent.com/jatinchowdhury18/ChowPhaser/master/res/screenshot_stereo.PNG"

# OB-Xd
# ob-xd — DEAD as of 2026-11-08: repo is README-only now, Docs/ folder gone.
# No live screenshot source found. Local LINK_PAGES/assets/ob-xd.png retained.
# download "ob-xd" "https://raw.githubusercontent.com/reales/OB-Xd/master/Docs/OBXd.png"

# Odin2
download "odin2" "https://cdn.shopify.com/s/files/1/0641/1304/9835/files/odin.2.4_fading.png?v=1748421452"

# Vital — press kit screenshot
download "vital" "https://vital.audio/images/vital_screenshot_1080.png"

# Helm
download "helm" "https://tytel.org/static/images/helm_screenshot.png"

# CloudSeed
download "cloudseed" "https://raw.githubusercontent.com/ValdemarOrn/CloudSeed/master/interface.png"

echo ""
echo "=== Tokyo Dawn Records ==="
download "tdr-nova" "https://www.tokyodawn.net/wp-content/uploads/2018/11/Seite-1-Kopie-1-1.png"
download "tdr-slickeq" "https://www.tokyodawn.net/cache/4a5942f6d2121ae0af31e8de88fd7173_w480_h230_grav_north_sc.png"
download "tdr-kotelnikov" "https://www.tokyodawn.net/cache/5c3faff56a5d38db011922dc62f83fe7_w480_h230_grav_center_sc.png"

echo ""
echo "=== Voxengo ==="
download "span" "https://www.voxengo.com/cdn/img/09/0944y0hob-1.jpg"
download "marvel-geq" "https://www.voxengo.com/cdn/img/56/56ofracri-1.jpg"

echo ""
echo "=== Klanghelm ==="
download "dc1a" "https://klanghelm.com/assets/img/Preview/DC1A.png"
download "mjuc-jr" "https://klanghelm.com/assets/img/Preview/MJUCjr.png"
download "klanghelm-ivgi" "https://klanghelm.com/assets/img/Preview/IVGI.png"

echo ""
echo "=== TAL Software ==="
download "tal-noisemaker" "https://tal-software.com/images/products/tal-noisemaker-new.jpg"
download "tal-chorus-lx" "https://tal-software.com/images/products/tal-chorus-lx_.png"
download "tal-reverb-4" "https://tal-software.com/images/products/tal-reverb-402.jpg"
download "tal-dub-x" "https://tal-software.com/images/products/tal-dub-x-4.jpg"
# tal-filter-2 — DEAD as of 2026-11-08: TAL no longer lists it (listing now points at KVR);
# no TAL product image exists anymore. Local LINK_PAGES/assets/tal-filter-2.png retained.
# download "tal-filter-2" "https://tal-software.com/images/products/TAL-Filter-2.png"

echo ""
echo "=== Xfer Records ==="
# ott — DEAD as of 2026-11-08: old Xfer image path 404s and the freeware page shows
# no product image. Local LINK_PAGES/assets/ott.png retained.
# download "ott" "https://xferrecords.com/images/freeware/OTT.png"

echo ""
echo "=== Other ==="
# roughrider3 — DEAD as of 2026-11-08: old Audio Damage CDN path 404s; no product
# image URL found on the live free-and-legacy page. Local asset retained.
# download "roughrider3" "https://www.audiodamage.com/cdn/images/products/roughrider3.png"
# camelcrusher — DEAD as of 2026-11-08: audiopluginsforfree.com 502s (whole-site outage).
# Local LINK_PAGES/assets/camelcrusher.png retained.
# download "camelcrusher" "https://www.audiopluginsforfree.com/wp-content/uploads/2018/01/CamelCrusher.png"
download "youlean-loudness-meter" "https://cdn.youlean.co/wp-content/uploads/2018/11/YLM-Dynamics-e1575992355220.png"
download "softube-saturation-knob" "https://cdn.softube.com/storage/8603B448D6052880DE75214C902ADD74CC93CFE4B0B7000927AC6BF1293BE9F6/93f520222dc0452e8ee981b0d5163923/jpg/media/81bf7cea81f74ff79d394788a1aa7ee1/saturation-knob-hero.jpg"

echo ""
echo "=== Summary ==="
total=$(ls -1 "$ASSETS"/*.png 2>/dev/null | wc -l | tr -d ' ')
echo "Total PNGs in assets: $total"
echo ""
echo "For plugins not covered by this script, see IMAGE_SOURCES.md"
echo "for manual download instructions."
