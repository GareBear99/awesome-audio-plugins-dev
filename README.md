# 🎛️ Awesome Audio Plugins & Dev

A curated collection of **free audio plugins**, **open-source DSP tools**, **plugin development frameworks**, and **audio engineering resources** across **VST3, AU, CLAP, and LV2**.

This repository is designed as a **developer-facing discovery hub** for people who want to:
- find genuinely useful free plugins
- study real open-source audio-plugin codebases
- compare frameworks, APIs, and plugin standards
- learn audio DSP from practical references
- discover adjacent sound resources that fit real production workflows

---

## Why this repository exists

A lot of plugin lists are one of two things:
- broad but shallow
- useful for producers, but weak for developers

This repository focuses on the overlap between:
- **free tools worth using**
- **open-source DSP worth studying**
- **frameworks worth building on**
- **learning resources worth keeping bookmarked**

The goal is **not** to become the biggest list. The goal is to stay **useful, readable, and credible**.

## Start here

- **Free EQ plugins and open-source equalizers** → [EQUALIZERS.md](EQUALIZERS.md)
- **Audio plugin development frameworks and APIs** → [PLUGIN_FRAMEWORKS_AND_APIS.md](PLUGIN_FRAMEWORKS_AND_APIS.md)
- **Audio DSP learning resources** → [DSP_LEARNING_RESOURCES.md](DSP_LEARNING_RESOURCES.md)
- **Open-source DSP plugin repositories** → [OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md](OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md)
- **Sample packs and sound resources** → [SAMPLE_PACKS_AND_SOUND_RESOURCES.md](SAMPLE_PACKS_AND_SOUND_RESOURCES.md)
- **FAQ** → [Q_AND_A_FAQ.md](Q_AND_A_FAQ.md)
- **Submission targets** → [OUTREACH_TARGETS.md](OUTREACH_TARGETS.md)

## Scope

This repository covers:
- free audio plugins for mixing, synthesis, effects, and metering
- open-source DSP tools and plugin repositories
- plugin development frameworks for VST3, AU, CLAP, and LV2
- DSP learning resources for beginner through advanced study
- free sample packs and sound resources

It deliberately avoids:
- random low-information plugin dumps
- weak affiliate-list style content
- bloated descriptions
- duplicate entries across categories when one placement is enough

## Quick picks

| Category | Starting Point |
|---|---|
| Equalizers | [FreeEQ8](https://github.com/GareBear99/FreeEQ8) |
| Plugin Frameworks | [JUCE](https://juce.com) |
| DSP Learning | [The Scientist and Engineer's Guide to DSP](http://www.dspguide.com/) |
| Open-Source DSP Repos | [Chowdhury DSP](https://github.com/Chowdhury-DSP) |
| Sample Packs | [SAMPLE_PACKS_AND_SOUND_RESOURCES.md](SAMPLE_PACKS_AND_SOUND_RESOURCES.md) |

## How to use this repository

- Start with the main README for category-level discovery.
- Open the category pages when you want deeper, more focused lists.
- Use the framework and DSP pages when evaluating how to build plugins, not just which plugins to download.
- Use the outreach docs if you want to grow the repository's visibility after publishing.

## Inclusion standard

An entry should usually satisfy at least one of these:
- it is a strong free plugin with a real-world use case
- it is an open-source DSP or plugin project worth studying
- it is a framework, API, or standard relevant to plugin development
- it is a learning resource with lasting technical value
- it is a sound resource that fits naturally into the wider audio-tooling ecosystem

A project does **not** belong here just because it exists.

## Contents

- [Why this repository exists](#why-this-repository-exists)
- [Start here](#start-here)
- [Scope](#scope)
- [Quick picks](#quick-picks)
- [How to use this repository](#how-to-use-this-repository)
- [Inclusion standard](#inclusion-standard)
- [Featured ecosystem](#featured-ecosystem)
- [Equalizers](#equalizers)
- [Synthesizers](#synthesizers)
- [Compression](#compression)
- [Saturation / Distortion](#saturation--distortion)
- [Reverb](#reverb)
- [Delay](#delay)
- [Creative Effects](#creative-effects)
- [Modulation](#modulation)
- [Filters](#filters)
- [Utility / Metering](#utility--metering)
- [Open-Source DSP Plugins](#open-source-dsp-plugins)
- [Multi-Effect Bundles](#multi-effect-bundles)
- [Plugin Frameworks](#plugin-frameworks)
- [DSP Resources](#dsp-resources)
- [Free Sample Packs](#free-sample-packs)
- [Repository structure](#repository-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Featured ecosystem

### [TizWildin Entertainment HUB](https://github.com/GareBear99/TizWildinEntertainmentHUB)

A growing ecosystem of experimental audio plugins, DSP tools, synth projects, and sound resources centered around open-source distribution, plugin development, and creator-facing tooling.

| Project | Summary |
|---|---|
| [**FreeEQ8**](https://github.com/GareBear99/FreeEQ8) | Free open-source 8-band parametric EQ with dynamic EQ, linear phase, match EQ, per-band drive, M/S support, oversampling, and spectrum analysis |
| [**PaintMask**](https://github.com/GareBear99/PaintMask_Free-JUCE-Plugin) | Paint-driven audio processing and visual interaction concept |
| [**RiftWave Suite**](https://github.com/GareBear99/RiftWaveSuite_RiftSynth_WaveForm_Lite) | Modular synth and waveform-focused plugin ecosystem |
| [**WURP**](https://github.com/GareBear99/WURP_Toxic-Motion-Engine_JUCE) | Experimental sound-design engine focused on motion, formant behavior, and destructive coloration |
| [**AETHER**](https://github.com/GareBear99/AETHER_Choir-Atmosphere-Designer) | Choir and atmosphere designer for cinematic and ambient sound shaping |
| [**WhisperGate**](https://github.com/GareBear99/WhisperGate_Free-JUCE-Plugin) | Procedural whisper and ritual-choir atmosphere plugin concept |
| [**Therum**](https://github.com/GareBear99/Therum_JUCE-Plugin) | Free wavetable synth project |
| [**FreeSampler**](https://github.com/GareBear99/FreeSampler_v0.3) | Lightweight sampler plugin project |
| [**MixMaid**](https://github.com/GareBear99/MixMaid) | Mixing utility toolkit |
| [**BassMaid**](https://github.com/GareBear99/BassMaid) | Bass enhancement and low-end processing concept |
| [**SpaceMaid**](https://github.com/GareBear99/SpaceMaid) | Spatial processing concept |
| [**GlueMaid**](https://github.com/GareBear99/GlueMaid) | Glue / cohesion mix-bus processor concept |

## Equalizers

See the full guide: [EQUALIZERS.md](EQUALIZERS.md)

- [**FreeEQ8**](https://github.com/GareBear99/FreeEQ8) — Free open-source 8-band parametric EQ with dynamic EQ, match EQ, linear phase, and spectrum analyzer.
- [**TDR Nova**](https://www.tokyodawn.net/tdr-nova/) — Dynamic parametric EQ with sidechain.
- [**TDR SlickEQ**](https://www.tokyodawn.net/tdr-slickeq/) — Musical 3-band mixing EQ with saturation and output-stage models.
- [**MEqualizer**](https://www.meldaproduction.com/MEqualizer) — General-purpose parametric EQ.
- [**Luftikus**](https://github.com/lkjbdsp/lkjb-plugins) — Analog-style mastering EQ inspired by the Maag EQ4.
- [**Blue Cat Triple EQ**](https://www.bluecataudio.com/Products/Product_TripleEQ/) — Simple 3-band semi-parametric EQ.
- [**Marvel GEQ**](https://www.voxengo.com/product/marvelgeq/) — Linear-phase 16-band graphic EQ.
- [**ReaEQ**](https://www.reaper.fm/reaplugs/) — Unlimited-band parametric EQ from Cockos.

## Synthesizers

- [**Vital**](https://vital.audio) — Advanced wavetable synthesizer with spectral warping and extensive modulation.
- [**Surge XT**](https://surge-synthesizer.github.io) — Open-source hybrid synth with deep modulation and a large feature set.
- [**Dexed**](https://github.com/asb2m10/dexed) — Yamaha DX7 FM synthesis emulation.
- [**Helm**](https://tytel.org/helm/) — Cross-platform polyphonic synth.
- [**Odin2**](https://thewavewarden.com/odin2/) — Hybrid synth with analog-modeled filters.
- [**OB-Xd**](https://github.com/reales/OB-Xd) — Oberheim-inspired virtual analog synth.
- [**TAL-NoiseMaker**](https://tal-software.com/products/tal-noisemaker) — Virtual analog synth with strong preset support.
- [**Tunefish4**](https://github.com/paynebc/tunefish) — Additive synthesizer.

## Compression

- [**TDR Kotelnikov**](https://www.tokyodawn.net/tdr-kotelnikov/) — Transparent wideband dynamics processor.
- [**RoughRider3**](https://www.audiodamage.com/pages/free-and-legacy) — Character compressor with strong coloration.
- [**DC1A**](https://klanghelm.com/contents/products/DC1A.php) — Minimal one-knob compressor.
- [**MJUC jr.**](https://klanghelm.com/contents/products/MJUCjr.php) — Variable-mu tube compressor emulation.
- [**OTT**](https://xferrecords.com/freeware) — Multiband upward and downward compression.

## Saturation / Distortion

- [**Softube Saturation Knob**](https://www.softube.com/saturationknob) — One-knob saturation.
- [**CamelCrusher**](https://www.audiopluginsforfree.com/camelcrusher/) — Distortion/compressor with warm tone.
- [**Klanghelm IVGI**](https://klanghelm.com/contents/products/IVGI.php) — Analog-style saturation.
- [**ChowTapeModel**](https://github.com/jatinchowdhury18/AnalogTapeModel) — Open-source analog tape model.
- [**Wolf Shaper**](https://github.com/wolf-plugins/wolf-shaper) — Open-source waveshaper with drawable curve.
- [**Cymatics Diablo Lite**](https://cymatics.fm/products/diablo-lite) — Free distortion and saturation plugin.
- [**Dumpster Fire**](https://www.audiodamage.com/pages/free-and-legacy) — Distortion with multiple algorithms.

## Reverb

- [**Valhalla Supermassive**](https://valhalladsp.com/shop/reverb/valhalla-supermassive/) — Large-space creative delay and reverb processor.
- [**OrilRiver**](https://www.kvraudio.com/product/orilriver-by-denis-tihanov) — Algorithmic stereo reverb.
- [**Dragonfly Reverb**](https://github.com/michaelwillis/dragonfly-reverb) — Open-source algorithmic reverb suite.
- [**TAL-Reverb-4**](https://tal-software.com/products/tal-reverb-4) — Vintage plate reverb.
- [**CloudSeed**](https://github.com/ValdemarOrn/CloudSeed) — Algorithmic reverb for very large spaces.
- [**Cymatics Space Lite**](https://cymatics.fm/products/space-lite) — Free spatial effect plugin.
- [**Cymatics Memory**](https://cymatics.fm/products/memory) — Atmosphere and reverb-style effect.
- [**PocketDimension**](https://www.audiodamage.com/pages/free-and-legacy) — Stereo enhancer and reverb-style utility.

## Delay

- [**TAL-Dub-III**](https://tal-software.com/products/tal-dub-3) — Dub delay with tape-style character.
- [**Spaceship Delay**](https://www.kvraudio.com/product/spaceship-delay-by-musical-entropy) — Delay with filters and modulation.
- [**ChowMatrix**](https://github.com/jatinchowdhury18/ChowMatrix) — Open-source delay matrix processor.
- [**Cymatics Deja Vu**](https://cymatics.fm/products/deja-vu) — Lo-fi and tape-style delay.

## Creative Effects

- [**Fracture**](https://glitchmachines.com/products/fracture/) — Buffer-effect glitch processor.
- [**Hysteresis**](https://glitchmachines.com/products/hysteresis/) — Glitch delay with modulation.
- [**PaulXStretch**](https://github.com/essej/paulxstretch) — Extreme time-stretching for ambient textures.
- [**Vinyl**](https://www.izotope.com/en/products/vinyl.html) — Vinyl simulation.
- [**Backmask**](https://www.audiodamage.com/pages/free-and-legacy) — Reverse-audio effect.
- [**DreamEater**](https://www.audiodamage.com/pages/free-and-legacy) — Audio mangling effect.
- [**MISHBY**](https://www.audiodamage.com/pages/free-and-legacy) — Lo-fi VHS and tape-style processor.
- [**MouthOfSorrow**](https://www.audiodamage.com/pages/free-and-legacy) — Granular effects processor.
- [**Rift Feedback Lite**](https://www.minimal.audio/) — Feedback effect plugin.
- [**Rift Filter Lite**](https://www.minimal.audio/) — Creative filter plugin.

## Modulation

- [**TAL-Chorus-LX**](https://tal-software.com/products/tal-chorus-lx) — Juno-style chorus emulation.
- [**Blue Cat Chorus**](https://www.bluecataudio.com/Products/Product_Chorus/) — Classic stereo chorus.
- [**ChowPhaser**](https://github.com/jatinchowdhury18/ChowPhaser) — Open-source phaser with analog-modeled feedback.

## Filters

- [**TAL-Filter-2**](https://tal-software.com/products/tal-filter-2) — Host-synced filter with tempo-synced modulation.
- [**HY-Filter4 Free**](https://hy-plugins.com/product/hy-filter4-free/) — Multi-mode filter with visualization.
- [**Morph EQ**](https://kilohearts.com/products/morph_eq) — Morphing parametric EQ and filter tool.

## Utility / Metering

- [**SPAN**](https://www.voxengo.com/product/span/) — Real-time FFT spectrum analyzer.
- [**Youlean Loudness Meter**](https://youlean.co/youlean-loudness-meter/) — LUFS loudness metering.
- [**MLoudnessAnalyzer**](https://www.meldaproduction.com/MLoudnessAnalyzer) — Loudness analyzer.
- [**HOFA 4U Meter**](https://hofa-plugins.de/en/plugins/4u/) — Level, correlation, and goniometer meters.
- [**dpMeter5**](https://www.tb-software.com/TBProAudio/dpmeter5.html) — Multichannel meter with RMS, LUFS, and true peak.
- [**MiniMeters**](https://www.minimeters.app/) — Standalone or plugin-style metering tools.

## Open-Source DSP Plugins

See the full guide: [OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md](OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md)

- [**Airwindows**](https://github.com/airwindows/airwindows) — Large collection of experimental audio effects.
- [**Chowdhury DSP**](https://github.com/Chowdhury-DSP) — Research-driven open-source effects and models.
- [**DISTRHO Ports**](https://github.com/DISTRHO/DISTRHO-Ports) — Plugins ported to Linux and LV2 ecosystems.
- [**ZL-Audio Plugins**](https://github.com/ZL-Audio) — Parametric EQ, compressor, and saturator projects.

## Multi-Effect Bundles

- [**Kilohearts Essentials**](https://kilohearts.com/products/kilohearts_essentials) — Free bundle of snap-in effects and utilities.
- [**MeldaProduction MFreeFXBundle**](https://www.meldaproduction.com/MFreeFXBundle) — Large free bundle including EQ, compression, reverb, and analysis tools.
- [**Audio Damage Free Collection**](https://www.audiodamage.com/pages/free-and-legacy) — Free plugins such as Backmask, DreamEater, Dumpster Fire, MISHBY, MouthOfSorrow, and PocketDimension.
- [**Cymatics Free Plugins**](https://cymatics.fm/pages/free-plugins) — Free plugin collection including Diablo Lite, Space Lite, Memory, and Deja Vu.

## Plugin Frameworks

See the full guide: [PLUGIN_FRAMEWORKS_AND_APIS.md](PLUGIN_FRAMEWORKS_AND_APIS.md)

- [**JUCE**](https://juce.com) — End-to-end C++ framework for audio plugins and apps.
- [**iPlug2**](https://github.com/iPlug2/iPlug2) — Lightweight C++ plugin framework.
- [**DPF**](https://github.com/DISTRHO/DPF) — Cross-platform framework with LV2, VST2/3, and CLAP support.
- [**CLAP**](https://github.com/free-audio/clap) — Open plugin standard.
- [**NIH-plug**](https://github.com/robbert-vdh/nih-plug) — Rust-based plugin framework.

## DSP Resources

See the full guide: [DSP_LEARNING_RESOURCES.md](DSP_LEARNING_RESOURCES.md)

- [**Audio EQ Cookbook**](https://www.w3.org/2011/audio/audio-eq-cookbook.html) — Classic biquad filter formulas and reference material.
- [**MusicDSP Archive**](https://www.musicdsp.org) — DSP algorithm snippets and references.
- [**The Scientist and Engineer's Guide to DSP**](http://www.dspguide.com/) — Free DSP textbook.
- [**JOS Stanford**](https://ccrma.stanford.edu/~jos/) — Julius O. Smith's music DSP resources.
- [**KVR Developer Forum**](https://www.kvraudio.com/forum/viewforum.php?f=33) — Plugin-development community.

## Free Sample Packs

See the full guide: [SAMPLE_PACKS_AND_SOUND_RESOURCES.md](SAMPLE_PACKS_AND_SOUND_RESOURCES.md)

### TizWildin sample packs

| Pack | Summary |
|------|---------|
| [**Free 808 Producer Kit**](https://github.com/GareBear99/Free-808-Producer-Kit) | 94 hand-crafted 808 bass samples tuned across the chromatic range |
| [**Free Riser Producer Kit**](https://github.com/GareBear99/Free-Riser-Producer-Kit) | 115 riser samples spanning noise, synth, drum, FX, and cinematic categories |
| [**Phonk Producer Toolkit**](https://github.com/GareBear99/Phonk_Producer_Toolkit) | Drift phonk starter kit with 808s, cowbells, drums, MIDI patterns, and templates |
| [**Free Future Bass Producer Kit**](https://github.com/GareBear99/Free-Future-Bass-Producer-Kit) | Free future bass sample pack with loops, fills, drums, bass, synths, pads, and FX |

### Additional sources

- [**Cymatics Free Download Vault**](https://cymatics.fm/pages/free-download-vault) — Rotating collection of free packs and production resources.
- [**Stickz**](https://stickz.co) — Free and commercial sample content.

## Repository structure

This project uses a hub-and-spoke layout:
- `README.md` is the main discovery page
- category pages hold denser topic-specific lists
- support docs cover contributions, validation, maintenance, and outreach

That keeps the front page readable while still allowing category depth.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for formatting and inclusion rules.

## License

This repository is distributed under the terms of the [LICENSE](LICENSE) file.
