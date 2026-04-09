# Community Submissions

This page tracks every plugin, tool, and resource that has been submitted and **accepted** into the Awesome Audio Plugins & Dev list.

Entries only appear here after they pass review. Submitting something does not guarantee it will be added.

---

## How it works

1. **You submit** a plugin, framework, resource, or sound pack using the format below.
2. **We review it** against the [inclusion standard](README.md#inclusion-standard).
3. **If accepted**, the entry gets added to the main list, receives its own [link page](LINK_PAGES/README.md), and appears in the accepted submissions table below.
4. **If declined**, we may explain why in the issue or PR. Common reasons are listed further down this page.

Submissions that are still under review do not appear anywhere public. Only accepted entries are listed.

---

## Submit a plugin or resource

### Option 1: GitHub Issue

Open an issue with a title like:

- `Submit: Plugin Name`
- `Submit: Framework Name`
- `Submit: DSP Resource Name`

### Option 2: Pull Request

If you already know which category it belongs in, open a PR that adds the entry directly.

### Submission format

Use this template in your issue or PR:

```
Name: Plugin / project name
Link: Official URL
Category: Equalizer / Synth / Reverb / Framework / DSP Resource / etc.
Free status: Fully free / open-source / free tier / legacy free release
Formats: VST3 / AU / CLAP / LV2 / standalone (if applicable)
Why it belongs: 1–3 sentences explaining what makes it worth listing.
```

Example:

```
Name: ExampleReverb
Link: https://example.com/reverb
Category: Reverb
Free status: Fully free
Formats: VST3, AU
Why it belongs: Clean algorithmic reverb with a real production use case,
an active maintainer, and an official download page.
```

---

## What gets accepted

A submission should satisfy at least one of these:

- it is a strong free plugin with a real-world use case
- it is an open-source DSP or plugin project worth studying
- it is a framework, API, or standard relevant to plugin development
- it is a learning resource with lasting technical value
- it is a sound resource that fits naturally into the wider audio-tooling ecosystem

Strong submissions are usually:

- clearly free or open-source
- easy to verify with an official link
- relevant to producers, plugin developers, or DSP learners
- not already listed in the repo
- useful enough to earn attention without bloating the list

## What does not get accepted

- paid-only plugins (no free version at all)
- abandoned or broken projects with dead links
- duplicate entries already covered elsewhere in the repo
- random listicle or mirror pages with no original value
- low-information suggestions with no clear reason to exist here
- tools unrelated to audio plugins, DSP, or adjacent sound workflows

Declined submissions are logged in [DECLINED.md](DECLINED.md) with a short explanation so the same entries are not re-submitted without new context.

---

## Review checklist

Before a submission is accepted, we verify:

- [ ] official source is accessible
- [ ] free status is clear and honest
- [ ] category placement is correct
- [ ] description is concise and non-hype
- [ ] link works
- [ ] entry is not already represented in a stronger position
- [ ] the addition improves the repo instead of just making it longer

---

## Accepted submissions

Everything below has been reviewed and published into the main list.

### Featured Ecosystem — 12 entries

| Entry | Description |
|-------|-------------|
| **FreeEQ8** | Free open-source 8-band parametric EQ with dynamic EQ, linear phase, match EQ, per-band drive, M/S support, oversampling, and spectrum analysis |
| **PaintMask** | Paint-driven audio processing and visual interaction concept |
| **RiftWave Suite** | Modular synth and waveform-focused plugin ecosystem |
| **WURP** | Experimental sound-design engine focused on motion, formant behavior, and destructive coloration |
| **AETHER** | Choir and atmosphere designer for cinematic and ambient sound shaping |
| **WhisperGate** | Procedural whisper and ritual-choir atmosphere plugin concept |
| **Therum** | Free wavetable synth project |
| **FreeSampler** | Lightweight sampler plugin project |
| **MixMaid** | Mixing utility toolkit |
| **BassMaid** | Bass enhancement and low-end processing concept |
| **SpaceMaid** | Spatial processing concept |
| **GlueMaid** | Glue / cohesion mix-bus processor concept |

### Equalizers — 8 entries

| Entry | Description |
|-------|-------------|
| **FreeEQ8** | Free open-source 8-band parametric EQ |
| **TDR Nova** | Dynamic parametric EQ with sidechain |
| **TDR SlickEQ** | Musical 3-band mixing EQ with saturation and output-stage models |
| **MEqualizer** | General-purpose parametric EQ |
| **Luftikus** | Analog-style mastering EQ inspired by the Maag EQ4 |
| **Blue Cat Triple EQ** | Simple 3-band semi-parametric EQ |
| **Marvel GEQ** | Linear-phase 16-band graphic EQ |
| **ReaEQ** | Unlimited-band parametric EQ from Cockos |

### Synthesizers — 8 entries

| Entry | Description |
|-------|-------------|
| **Vital** | Advanced wavetable synthesizer with spectral warping and extensive modulation |
| **Surge XT** | Open-source hybrid synth with deep modulation and a large feature set |
| **Dexed** | Yamaha DX7 FM synthesis emulation |
| **Helm** | Cross-platform polyphonic synth |
| **Odin2** | Hybrid synth with analog-modeled filters |
| **OB-Xd** | Oberheim-inspired virtual analog synth |
| **TAL-NoiseMaker** | Virtual analog synth with strong preset support |
| **Tunefish4** | Additive synthesizer |

### Compression — 5 entries

| Entry | Description |
|-------|-------------|
| **TDR Kotelnikov** | Transparent wideband dynamics processor |
| **RoughRider3** | Character compressor with strong coloration |
| **DC1A** | Minimal one-knob compressor |
| **MJUC jr.** | Variable-mu tube compressor emulation |
| **OTT** | Multiband upward and downward compression |

### Saturation / Distortion — 7 entries

| Entry | Description |
|-------|-------------|
| **Softube Saturation Knob** | One-knob saturation |
| **CamelCrusher** | Distortion/compressor with warm tone |
| **Klanghelm IVGI** | Analog-style saturation |
| **ChowTapeModel** | Open-source analog tape model |
| **Wolf Shaper** | Open-source waveshaper with drawable curve |
| **Cymatics Diablo Lite** | Free distortion and saturation plugin |
| **Dumpster Fire** | Distortion with multiple algorithms |

### Reverb — 8 entries

| Entry | Description |
|-------|-------------|
| **Valhalla Supermassive** | Large-space creative delay and reverb processor |
| **OrilRiver** | Algorithmic stereo reverb |
| **Dragonfly Reverb** | Open-source algorithmic reverb suite |
| **TAL-Reverb-4** | Vintage plate reverb |
| **CloudSeed** | Algorithmic reverb for very large spaces |
| **Cymatics Space Lite** | Free spatial effect plugin |
| **Cymatics Memory** | Atmosphere and reverb-style effect |
| **PocketDimension** | Stereo enhancer and reverb-style utility |

### Delay — 4 entries

| Entry | Description |
|-------|-------------|
| **TAL-Dub-III** | Dub delay with tape-style character |
| **Spaceship Delay** | Delay with filters and modulation |
| **ChowMatrix** | Open-source delay matrix processor |
| **Cymatics Deja Vu** | Lo-fi and tape-style delay |

### Creative Effects — 10 entries

| Entry | Description |
|-------|-------------|
| **Fracture** | Buffer-effect glitch processor |
| **Hysteresis** | Glitch delay with modulation |
| **PaulXStretch** | Extreme time-stretching for ambient textures |
| **Vinyl** | Vinyl simulation |
| **Backmask** | Reverse-audio effect |
| **DreamEater** | Audio mangling effect |
| **MISHBY** | Lo-fi VHS and tape-style processor |
| **MouthOfSorrow** | Granular effects processor |
| **Rift Feedback Lite** | Feedback effect plugin |
| **Rift Filter Lite** | Creative filter plugin |

### Modulation — 3 entries

| Entry | Description |
|-------|-------------|
| **TAL-Chorus-LX** | Juno-style chorus emulation |
| **Blue Cat Chorus** | Classic stereo chorus |
| **ChowPhaser** | Open-source phaser with analog-modeled feedback |

### Filters — 3 entries

| Entry | Description |
|-------|-------------|
| **TAL-Filter-2** | Host-synced filter with tempo-synced modulation |
| **HY-Filter4 Free** | Multi-mode filter with visualization |
| **Morph EQ** | Morphing parametric EQ and filter tool |

### Utility / Metering — 6 entries

| Entry | Description |
|-------|-------------|
| **SPAN** | Real-time FFT spectrum analyzer |
| **Youlean Loudness Meter** | LUFS loudness metering |
| **MLoudnessAnalyzer** | Loudness analyzer |
| **HOFA 4U Meter** | Level, correlation, and goniometer meters |
| **dpMeter5** | Multichannel meter with RMS, LUFS, and true peak |
| **MiniMeters** | Standalone or plugin-style metering tools |

### Open-Source DSP Plugins — 4 entries

| Entry | Description |
|-------|-------------|
| **Airwindows** | Large collection of experimental audio effects |
| **Chowdhury DSP** | Research-driven open-source effects and models |
| **DISTRHO Ports** | Plugins ported to Linux and LV2 ecosystems |
| **ZL-Audio Plugins** | Parametric EQ, compressor, and saturator projects |

### Multi-Effect Bundles — 4 entries

| Entry | Description |
|-------|-------------|
| **Kilohearts Essentials** | Free bundle of snap-in effects and utilities |
| **MeldaProduction MFreeFXBundle** | Large free bundle including EQ, compression, reverb, and analysis tools |
| **Audio Damage Free Collection** | Free plugins including Backmask, DreamEater, Dumpster Fire, MISHBY, MouthOfSorrow, and PocketDimension |
| **Cymatics Free Plugins** | Free plugin collection including Diablo Lite, Space Lite, Memory, and Deja Vu |

### Plugin Frameworks — 5 entries

| Entry | Description |
|-------|-------------|
| **JUCE** | End-to-end C++ framework for audio plugins and apps |
| **iPlug2** | Lightweight C++ plugin framework |
| **DPF** | Cross-platform framework with LV2, VST2/3, and CLAP support |
| **CLAP** | Open plugin standard |
| **NIH-plug** | Rust-based plugin framework |

### DSP Resources — 5 entries

| Entry | Description |
|-------|-------------|
| **Audio EQ Cookbook** | Classic biquad filter formulas and reference material |
| **MusicDSP Archive** | DSP algorithm snippets and references |
| **The Scientist and Engineer's Guide to DSP** | Free DSP textbook |
| **JOS Stanford** | Julius O. Smith's music DSP resources |
| **KVR Developer Forum** | Plugin-development community |

### Free Sample Packs — 6 entries

| Entry | Description |
|-------|-------------|
| **Free 808 Producer Kit** | 94 hand-crafted 808 bass samples tuned across the chromatic range |
| **Free Riser Producer Kit** | 115 riser samples spanning noise, synth, drum, FX, and cinematic categories |
| **Phonk Producer Toolkit** | Drift phonk starter kit with 808s, cowbells, drums, MIDI patterns, and templates |
| **Free Future Bass Producer Kit** | Free future bass sample pack with loops, fills, drums, bass, synths, pads, and FX |
| **Cymatics Free Download Vault** | Rotating collection of free packs and production resources |
| **Stickz** | Free and commercial sample content |
| **Free Dark Piano Sound Kit** | Dark and cinematic piano loops and one-shots for trap, drill, R&B, and film scoring |

---

**Total accepted entries: 99**

---

## Related pages

- [README.md](README.md) — main list
- [CONTRIBUTING.md](CONTRIBUTING.md) — formatting and PR rules
- [DECLINED.md](DECLINED.md) — declined submissions with reasons
- [LINK_PAGES/README.md](LINK_PAGES/README.md) — link page directory
- [Q_AND_A_FAQ.md](Q_AND_A_FAQ.md) — FAQ
