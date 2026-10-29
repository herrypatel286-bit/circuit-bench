# Signs release builds with the project's own key and sets the version number.
import re, sys
run = sys.argv[1]
p = 'android/app/build.gradle'
s = open(p).read()
s = re.sub(r'versionCode \d+', f'versionCode {run}', s, count=1)
s = re.sub(r'versionName "[^"]*"', f'versionName "1.0.{run}"', s, count=1)
sign = '''    signingConfigs {
        release {
            storeFile file("../../android-signing/circuit-bench.jks")
            storePassword System.getenv("CB_STORE_PASSWORD")
            keyAlias "circuitbench"
            keyPassword System.getenv("CB_STORE_PASSWORD")
        }
    }
    buildTypes {'''
assert '    buildTypes {' in s, 'buildTypes block not found'
s = s.replace('    buildTypes {', sign, 1)
s = re.sub(r'(release \{\s*\n\s*minifyEnabled false)', r'\1\n            signingConfig signingConfigs.release', s, count=1)
assert 'signingConfig signingConfigs.release' in s, 'release block not patched'
open(p, 'w').write(s)
print(s[s.index('android {'):][:900])
