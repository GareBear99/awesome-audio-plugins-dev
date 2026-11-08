# FreeVox8

> **TizWildin Entertainment HUB — Flagship**
> **Role:** Spectral vocoder, ghost-freeze resynthesis, morph, and dynamic spectral masking
> **Status:** 🚧 In development — source-complete for local JUCE compilation (v0.5.0), not yet built as a plugin anywhere: no pluginval run, no DAW test yet
> **Formats:** — (no plugin build yet; VST3 / AU planned)
> **License:** FREE (open source, GPL-3.0)

- Repository: <https://github.com/GareBear99/FreeVox8>
- Ecosystem router: <https://garebear99.github.io/TizWildinEntertainmentHUB/>
- Parent discovery hub: <https://github.com/GareBear99/awesome-audio-lists>
- Research bridge: <https://github.com/GareBear99/awesome-python-audio-science/blob/main/docs/FREEVOX8_RESEARCH_BRIDGE.md>

## Tagline

A free spectral vocoder built for ghost resynthesis — freeze a vocal, morph it, mask it, and play it back as an alien choir.

## Overview

FreeVox8 is the spectral-vocoder lane of the TizWildin ecosystem: a JUCE-based
spectral vocoder, ghost-freeze resynthesis, morph, and dynamic spectral masking
plugin for vocals, synths, drums, and experimental sound design. It is a
standalone plugin source package derived from the FreeEQ8 codebase hygiene
patterns, not an EQ rename.

The audio path is built around a dual engine: a conservative **128-band
realtime-safe spectral vocoder core** plus a **Spectral Ghost 1024**
high-resolution FFT cross-synthesis engine for ghost/freeze and morph
resynthesis. The Ghost resynthesis works — STOI ~0.78–0.79, above TAL-Vocoder
3.0.3 at 0.7434 (see PAPER.md §3.8 in the repo).

**Honest status (2026-11-08, v0.5.0):** the source is complete for local JUCE
compilation, but FreeVox8 has **never been built as a plugin anywhere** — no
JUCE vendored in the repo, no pluginval run, no DAW test. The next step is a
Mac build + pluginval strictness 10 + one DAW smoke test. Until that lands,
treat FreeVox8 as a research direction with working DSP, not a shippable
plugin. Citation is gated on the same honest certification (see the research
bridge linked above).

## Why it belongs here

FreeVox8 is included as a flagship audio-plugin anchor because it connects audio-plugin development, spectral DSP, vocoder design, creator tools, and public release routing into the same ecosystem as FreeEQ8 and the TizWildin HUB.

## Core features

- 128-band log-spaced spectral envelope vocoder core
- Spectral Ghost 1024 high-resolution FFT cross-synthesis engine
- MIDI-controlled internal carrier with saw / sine / pulse / sub blend
- External-carrier blend from the main input
- Optional sidechain modulator bus
- Vocoder, Mask, Ghost, and Morph modes
- Freeze envelope memory for ghost / frozen textures
- Formant shift via RT-safe envelope remapping
- Air / noise excitation for intelligibility and breath
- Transient Protect macro for consonants and punch
- Stereo Width macro
- Quality macro for higher-density tone shaping
- Atomic spectral display taps for low-cost UI visualization

## Typical workflows

- Robot / vocoded vocals with a MIDI-played carrier
- Frozen vocal textures and alien choirs from the Ghost engine
- Morphing between two sources for transitions and sound design
- Dynamic spectral masking for drums and experimental layers
- Playable frozen textures as pads and atmospheres

## Compatibility

No plugin build exists yet, so there is no DAW compatibility to report.
Planned: VST3 / AU on macOS and Windows (JUCE build, CMake).

## Source & downloads

- **Repo / source:** [https://github.com/GareBear99/FreeVox8](https://github.com/GareBear99/FreeVox8)
- **Paper:** [PAPER.md](https://github.com/GareBear99/FreeVox8/blob/main/PAPER.md) in the repo
- **Research bridge:** [FREEVOX8_RESEARCH_BRIDGE.md](https://github.com/GareBear99/awesome-python-audio-science/blob/main/docs/FREEVOX8_RESEARCH_BRIDGE.md)
- **HUB dashboard:** [https://garebear99.github.io/TizWildinEntertainmentHUB/](https://garebear99.github.io/TizWildinEntertainmentHUB/)
- **HUB repo:** [https://github.com/GareBear99/TizWildinEntertainmentHUB](https://github.com/GareBear99/TizWildinEntertainmentHUB)

## Related projects

- [TizWildin HUB](https://github.com/GareBear99/TizWildinEntertainmentHUB)
- [FreeEQ8](https://github.com/GareBear99/FreeEQ8)
- [Therum](https://github.com/GareBear99/Therum_JUCE-Plugin)

---

_This page is part of the Awesome Audio Plugins & Dev link-page set. It is the human-readable landing spot for **FreeVox8** inside the TizWildin Entertainment HUB ecosystem._

## Keywords

free vocoder plugin, spectral vocoder, ghost resynthesis, dynamic spectral masking, JUCE vocoder, open-source audio plugin, vocal resynthesis, TizWildin, GareBear99.
