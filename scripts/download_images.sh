#!/bin/bash
# download_images.sh — Replace placeholder PNGs with real plugin screenshots
# Run from the repo root: bash scripts/download_images.sh
#
# This script downloads product screenshots from official sources.
# Some URLs may require a browser — those are listed in IMAGE_SOURCES.md for manual download.

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
download "surge-xt" "https://surge-synthesizer.github.io/screenshots/surge-xt.png"

# Wolf Shaper
download "wolf-shaper" "https://raw.githubusercontent.com/wolf-plugins/wolf-shaper/master/docs/images/screenshot.png"

# Dexed — from the user website
download "dexed" "https://asb2m10.github.io/dexed/img/dexed.png"

# OB-Xd
download "ob-xd" "https://raw.githubusercontent.com/reales/OB-Xd/master/Docs/OBXd.png"

# Odin2
download "odin2" "https://thewavewarden.com/assets/img/odin2.png"

# Vital — press kit screenshot
download "vital" "https://vital.audio/img/screenshot.png"

# Helm
download "helm" "https://tytel.org/static/images/helm_screenshot.png"

# CloudSeed
download "cloudseed" "https://raw.githubusercontent.com/ValdemarOrn/CloudSeed/master/Documentation/Screenshot.png"

echo ""
echo "=== Tokyo Dawn Records ==="
download "tdr-nova" "https://www.tokyodawn.net/wp-content/uploads/2014/10/TDR-Nova_display.png"
download "tdr-slickeq" "https://www.tokyodawn.net/wp-content/uploads/2014/10/TDR-VOS-SlickEQ_display.png"
download "tdr-kotelnikov" "https://www.tokyodawn.net/wp-content/uploads/2014/10/TDR-Kotelnikov_display.png"

echo ""
echo "=== Voxengo ==="
download "span" "https://www.voxengo.com/files/product_shots/span.png"
download "marvel-geq" "https://www.voxengo.com/files/product_shots/marvelgeq.png"

echo ""
echo "=== Klanghelm ==="
download "dc1a" "https://klanghelm.com/contents/products/DC1A/DC1A_screenshot.png"
download "mjuc-jr" "https://klanghelm.com/contents/products/MJUCjr/MJUCjr_screenshot.png"
download "klanghelm-ivgi" "https://klanghelm.com/contents/products/IVGI/IVGI_screenshot.png"

echo ""
echo "=== TAL Software ==="
download "tal-noisemaker" "https://tal-software.com/images/products/TAL-NoiseMaker.png"
download "tal-chorus-lx" "https://tal-software.com/images/products/TAL-Chorus-LX.png"
download "tal-reverb-4" "https://tal-software.com/images/products/TAL-Reverb-4.png"
download "tal-dub-iii" "https://tal-software.com/images/products/TAL-Dub-3.png"
download "tal-filter-2" "https://tal-software.com/images/products/TAL-Filter-2.png"

echo ""
echo "=== Xfer Records ==="
download "ott" "https://xferrecords.com/images/freeware/OTT.png"

echo ""
echo "=== Other ==="
download "roughrider3" "https://www.audiodamage.com/cdn/images/products/roughrider3.png"
download "camelcrusher" "https://www.audiopluginsforfree.com/wp-content/uploads/2018/01/CamelCrusher.png"
download "youlean-loudness-meter" "https://youlean.co/wp-content/uploads/2024/youlean-loudness-meter.png"
download "softube-saturation-knob" "https://www.softube.com/images/products/saturationknob.png"

echo ""
echo "=== Summary ==="
total=$(ls -1 "$ASSETS"/*.png 2>/dev/null | wc -l | tr -d ' ')
echo "Total PNGs in assets: $total"
echo ""
echo "For plugins not covered by this script, see IMAGE_SOURCES.md"
echo "for manual download instructions."
