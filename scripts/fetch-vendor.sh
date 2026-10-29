#!/usr/bin/env bash
# Downloads the PDF and zip libraries so the apps and website work offline.
set -euo pipefail
mkdir -p www/vendor
curl -fsSL https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js -o www/vendor/jszip.min.js
curl -fsSL https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js -o www/vendor/jspdf.umd.min.js
sha256sum www/vendor/*.js
