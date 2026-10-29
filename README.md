# Circuit Bench

Design breadboard circuits, schematics and PCBs, and simulate Arduino sketches — in the browser, or as an app on Android, iPhone and iPad.

## Get it

- **Website:** https://herrypatel286-bit.github.io/circuit-bench/ — on iPad or iPhone, open it in Safari, tap **Share → Add to Home Screen**. On Android, open it in Chrome and tap **Install app**. It works offline after the first visit.
- **Android app:** download `CircuitBench.apk` from the [latest release](../../releases/latest) and open it.
- **iPhone / iPad app:** download `CircuitBench-unsigned.ipa` from the [latest release](../../releases/latest) and sign it with a sideloading app that uses your own Apple ID (SideStore, AltStore or Sideloadly).

Every push to `main` rebuilds the apps and the website automatically (see the **Actions** tab).

## Privacy

Projects and imported modules are stored only on the device you use. Nothing is uploaded.

## Notes

- The Android signing key in `android-signing/` is deliberately public so the build is reproducible without setup. That is fine for sideloading among friends; use your own private key (as a repository secret) before publishing to any app store.
- Built with [Capacitor](https://capacitorjs.com).

## Credits

The parts library uses parts from the [Fritzing](https://fritzing.org) 1.0.6 parts by the Fritzing team and contributors, used under [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/).
