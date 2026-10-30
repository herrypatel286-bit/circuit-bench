# Turns the Claude artifact page into the stand-alone page used by the website and the apps.
import sys, re
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<meta name="theme-color" content="#1d7566">
<meta name="description" content="Circuit Bench: design breadboard circuits, schematics and PCBs, and simulate Arduino sketches.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Circuit Bench">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/icon-180.png">
'''
s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')
s = s.replace('https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js', 'vendor/jszip.min.js')
s = s.replace('https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js', 'vendor/jspdf.umd.min.js')
assert 'vendor/jszip.min.js' in s and 'vendor/jspdf.umd.min.js' in s
s = head + s.replace('<title>Circuit Bench</title>', '<title>Circuit Bench</title>\n</head>\n<body>', 1)
s += '''
<script>
// Offline support for the website (the installed apps already carry every file).
if ('serviceWorker' in navigator && location.protocol === 'https:' && !window.Capacitor) addEventListener('load', () => navigator.serviceWorker.register('sw.js').catch(() => {}));
</script>
</body>
</html>
'''
open(out, 'w', encoding='utf-8').write(s)
print('ok', len(s))
