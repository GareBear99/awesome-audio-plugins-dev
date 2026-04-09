# 🏛️ Awesome Audio Plugins & Dev

<a href="https://github.com/sponsors/GareBear99"><img src="https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?style=flat&logo=githubsponsors&logoColor=white" alt="Sponsor" /></a>
<a href="https://buymeacoffee.com/garebear99"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=flat&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee" /></a>
<a href="https://ko-fi.com/luciferai"><img src="https://img.shields.io/badge/Ko--fi-ff5e5b?style=flat&logo=ko-fi&logoColor=white" alt="Ko-fi" /></a>

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
- **Community submissions** → [COMMUNITY_SUBMISSIONS.md](COMMUNITY_SUBMISSIONS.md)
- **Link pages directory** → [LINK_PAGES/README.md](LINK_PAGES/README.md)
- **Outreach targets** → [OUTREACH_TARGETS.md](OUTREACH_TARGETS.md)

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

## Topics

`free-vst-plugins` `audio-dsp` `open-source-audio` `vst3` `au` `clap` `lv2` `juce` `plugin-development` `music-production` `free-sample-packs` `audio-engineering` `synthesizer` `equalizer` `reverb` `compressor` `awesome-list`

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
- [Community submissions](#community-submissions)
- [Contributing](#contributing)
- [License](#license)

---

## Featured ecosystem

### [TizWildin Entertainment HUB](https://github.com/GareBear99/TizWildinEntertainmentHUB)

A growing ecosystem of experimental audio plugins, DSP tools, synth projects, and sound resources centered around open-source distribution, plugin development, and creator-facing tooling.

| Project | Summary |
|---|---|
| [**FreeEQ8**](LINK_PAGES/freeeq8.md) | Free open-source 8-band parametric EQ with dynamic EQ, linear phase, match EQ, per-band drive, M/S support, oversampling, and spectrum analysis · [Official site / repo](https://github.com/GareBear99/FreeEQ8) |
| [**PaintMask**](LINK_PAGES/paintmask.md) | Paint-driven audio processing and visual interaction concept · [Official site / repo](https://github.com/GareBear99/PaintMask_Free-JUCE-Plugin) |
| [**RiftWave Suite**](LINK_PAGES/riftwave-suite.md) | Modular synth and waveform-focused plugin ecosystem · [Official site / repo](https://github.com/GareBear99/RiftWaveSuite_RiftSynth_WaveForm_Lite) |
| [**WURP**](LINK_PAGES/wurp.md) | Experimental sound-design engine focused on motion, formant behavior, and destructive coloration · [Official site / repo](https://github.com/GareBear99/WURP_Toxic-Motion-Engine_JUCE) |
| [**AETHER**](LINK_PAGES/aether.md) | Choir and atmosphere designer for cinematic and ambient sound shaping · [Official site / repo](https://github.com/GareBear99/AETHER_Choir-Atmosphere-Designer) |
| [**WhisperGate**](LINK_PAGES/whispergate.md) | Procedural whisper and ritual-choir atmosphere plugin concept · [Official site / repo](https://github.com/GareBear99/WhisperGate_Free-JUCE-Plugin) |
| [**Therum**](LINK_PAGES/therum.md) | Free wavetable synth project · [Official site / repo](https://github.com/GareBear99/Therum_JUCE-Plugin) |
| [**FreeSampler**](LINK_PAGES/freesampler.md) | Lightweight sampler plugin project · [Official site / repo](https://github.com/GareBear99/FreeSampler_v0.3) |
| [**MixMaid**](LINK_PAGES/mixmaid.md) | Mixing utility toolkit · [Official site / repo](https://github.com/GareBear99/MixMaid) |
| [**BassMaid**](LINK_PAGES/bassmaid.md) | Bass enhancement and low-end processing concept · [Official site / repo](https://github.com/GareBear99/BassMaid) |
| [**SpaceMaid**](LINK_PAGES/spacemaid.md) | Spatial processing concept · [Official site / repo](https://github.com/GareBear99/SpaceMaid) |
| [**GlueMaid**](LINK_PAGES/gluemaid.md) | Glue / cohesion mix-bus processor concept · [Official site / repo](https://github.com/GareBear99/GlueMaid) |

## Equalizers

See the full guide: [EQUALIZERS.md](EQUALIZERS.md)

- [**FreeEQ8**](LINK_PAGES/freeeq8.md) — Free open-source 8-band parametric EQ with dynamic EQ, match EQ, linear phase, and spectrum analyzer. [Official site / repo](https://github.com/GareBear99/FreeEQ8)
- [**TDR Nova**](LINK_PAGES/tdr-nova.md) — Dynamic parametric EQ with sidechain. [Official site / repo](https://www.tokyodawn.net/tdr-nova/)
- [**TDR SlickEQ**](LINK_PAGES/tdr-slickeq.md) — Musical 3-band mixing EQ with saturation and output-stage models. [Official site / repo](https://www.tokyodawn.net/tdr-slickeq/)
- [**MEqualizer**](LINK_PAGES/mequalizer.md) — General-purpose parametric EQ. [Official site / repo](https://www.meldaproduction.com/MEqualizer)
- [**Luftikus**](LINK_PAGES/luftikus.md) — Analog-style mastering EQ inspired by the Maag EQ4. [Official site / repo](https://github.com/lkjbdsp/lkjb-plugins)
- [**Blue Cat Triple EQ**](LINK_PAGES/blue-cat-triple-eq.md) — Simple 3-band semi-parametric EQ. [Official site / repo](https://www.bluecataudio.com/Products/Product_TripleEQ/)
- [**Marvel GEQ**](LINK_PAGES/marvel-geq.md) — Linear-phase 16-band graphic EQ. [Official site / repo](https://www.voxengo.com/product/marvelgeq/)
- [**ReaEQ**](LINK_PAGES/reaeq.md) — Unlimited-band parametric EQ from Cockos. [Official site / repo](https://www.reaper.fm/reaplugs/)

## Synthesizers

- [**Vital**](LINK_PAGES/vital.md) — Advanced wavetable synthesizer with spectral warping and extensive modulation. [Official site / repo](https://vital.audio)
- [**Surge XT**](LINK_PAGES/surge-xt.md) — Open-source hybrid synth with deep modulation and a large feature set. [Official site / repo](https://surge-synthesizer.github.io)
- [**Dexed**](LINK_PAGES/dexed.md) — Yamaha DX7 FM synthesis emulation. [Official site / repo](https://github.com/asb2m10/dexed)
- [**Helm**](LINK_PAGES/helm.md) — Cross-platform polyphonic synth. [Official site / repo](https://tytel.org/helm/)
- [**Odin2**](LINK_PAGES/odin2.md) — Hybrid synth with analog-modeled filters. [Official site / repo](https://thewavewarden.com/odin2/)
- [**OB-Xd**](LINK_PAGES/ob-xd.md) — Oberheim-inspired virtual analog synth. [Official site / repo](https://github.com/reales/OB-Xd)
- [**TAL-NoiseMaker**](LINK_PAGES/tal-noisemaker.md) — Virtual analog synth with strong preset support. [Official site / repo](https://tal-software.com/products/tal-noisemaker)
- [**Tunefish4**](LINK_PAGES/tunefish4.md) — Additive synthesizer. [Official site / repo](https://github.com/paynebc/tunefish)

## Compression

- [**TDR Kotelnikov**](LINK_PAGES/tdr-kotelnikov.md) — Transparent wideband dynamics processor. [Official site / repo](https://www.tokyodawn.net/tdr-kotelnikov/)
- [**RoughRider3**](LINK_PAGES/roughrider3.md) — Character compressor with strong coloration. [Official site / repo](https://www.audiodamage.com/pages/free-and-legacy)
- [**DC1A**](LINK_PAGES/dc1a.md) — Minimal one-knob compressor. [Official site / repo](https://klanghelm.com/contents/products/DC1A.php)
- [**MJUC jr.**](LINK_PAGES/mjuc-jr.md) — Variable-mu tube compressor emulation. [Official site / repo](https://klanghelm.com/contents/products/MJUCjr.php)
- [**OTT**](LINK_PAGES/ott.md) — Multiband upward and downward compression. [Official site / repo](https://xferrecords.com/freeware)

## Saturation / Distortion

- [**Softube Saturation Knob**](LINK_PAGES/softube-saturation-knob.md) — One-knob saturation. [Official site / repo](https://www.softube.com/saturationknob)
- [**CamelCrusher**](LINK_PAGES/camelcrusher.md) — Distortion/compressor with warm tone. [Official site / repo](https://www.audiopluginsforfree.com/camelcrusher/)
- [**Klanghelm IVGI**](LINK_PAGES/klanghelm-ivgi.md) — Analog-style saturation. [Official site / repo](https://klanghelm.com/contents/products/IVGI.php)
- [**ChowTapeModel**](LINK_PAGES/chowtapemodel.md) — Open-source analog tape model. [Official site / repo](https://github.com/jatinchowdhury18/AnalogTapeModel)
- [**Wolf Shaper**](LINK_PAGES/wolf-shaper.md) — Open-source waveshaper with drawable curve. [Official site / repo](https://github.com/wolf-plugins/wolf-shaper)
- [**Cymatics Diablo Lite**](LINK_PAGES/cymatics-diablo-lite.md) — Free distortion and saturation plugin. [Official site / repo](https://cymatics.fm/products/diablo-lite)
- [**Dumpster Fire**](LINK_PAGES/dumpster-fire.md) — Distortion with multiple algorithms. [Official site / repo](https://www.audiodamage.com/pages/free-and-legacy)

## Reverb

- [**Valhalla Supermassive**](LINK_PAGES/valhalla-supermassive.md) — Large-space creative delay and reverb processor. [Official site / repo](https://valhalladsp.com/shop/reverb/valhalla-supermassive/)
- [**OrilRiver**](LINK_PAGES/orilriver.md) — Algorithmic stereo reverb. [Official site / repo](https://www.kvraudio.com/product/orilriver-by-denis-tihanov)
- [**Dragonfly Reverb**](LINK_PAGES/dragonfly-reverb.md) — Open-source algorithmic reverb suite. [Official site / repo](https://github.com/michaelwillis/dragonfly-reverb)
- [**TAL-Reverb-4**](LINK_PAGES/tal-reverb-4.md) — Vintage plate reverb. [Official site / repo](https://tal-software.com/products/tal-reverb-4)
- [**CloudSeed**](LINK_PAGES/cloudseed.md) — Algorithmic reverb for very large spaces. [Official site / repo](https://github.com/ValdemarOrn/CloudSeed)
- [**Cymatics Space Lite**](LINK_PAGES/cymatics-space-lite.md) — Free spatial effect plugin. [Official site / repo](https://cymatics.fm/products/space-lite)
- [**Cymatics Memory**](LINK_PAGES/cymatics-memory.md) — Atmosphere and reverb-style effect. [Official site / repo](https://cymatics.fm/products/memory)
- [**PocketDimension**](LINK_PAGES/pocketdimension.md) — Stereo enhancer and reverb-style utility. [Official site / repo](https://www.audiodamage.com/pages/free-and-legacy)

## Delay

- [**TAL-Dub-III**](LINK_PAGES/tal-dub-iii.md) — Dub delay with tape-style character. [Official site / repo](https://tal-software.com/products/tal-dub-3)
- [**Spaceship Delay**](LINK_PAGES/spaceship-delay.md) — Delay with filters and modulation. [Official site / repo](https://www.kvraudio.com/product/spaceship-delay-by-musical-entropy)
- [**ChowMatrix**](LINK_PAGES/chowmatrix.md) — Open-source delay matrix processor. [Official site / repo](https://github.com/jatinchowdhury18/ChowMatrix)
- [**Cymatics Deja Vu**](LINK_PAGES/cymatics-deja-vu.md) — Lo-fi and tape-style delay. [Official site / repo](https://cymatics.fm/products/deja-vu)

## Creative Effects

- [**Fracture**](LINK_PAGES/fracture.md) — Buffer-effect glitch processor. [Official site / repo](https://glitchmachines.com/products/fracture/)
- [**Hysteresis**](LINK_PAGES/hysteresis.md) — Glitch delay with modulation. [Official site / repo](https://glitchmachines.com/products/hysteresis/)
- [**PaulXStretch**](LINK_PAGES/paulxstretch.md) — Extreme time-stretching for ambient textures. [Official site / repo](https://github.com/essej/paulxstretch)
- [**Vinyl**](LINK_PAGES/vinyl.md) — Vinyl simulation. [Official site / repo](https://www.izotope.com/en/products/vinyl.html)
- [**Backmask**](LINK_PAGES/backmask.md) — Reverse-audio effect. [Official site / repo](https://www.audiodamage.com/pages/free-and-legacy)
- [**DreamEater**](LINK_PAGES/dreameater.md) — Audio mangling effect. [Official site / repo](https://www.audiodamage.com/pages/free-and-legacy)
- [**MISHBY**](LINK_PAGES/mishby.md) — Lo-fi VHS and tape-style processor. [Official site / repo](https://www.audiodamage.com/pages/free-and-legacy)
- [**MouthOfSorrow**](LINK_PAGES/mouthofsorrow.md) — Granular effects processor. [Official site / repo](https://www.audiodamage.com/pages/free-and-legacy)
- [**Rift Feedback Lite**](LINK_PAGES/rift-feedback-lite.md) — Feedback effect plugin. [Official site / repo](https://www.minimal.audio/)
- [**Rift Filter Lite**](LINK_PAGES/rift-filter-lite.md) — Creative filter plugin. [Official site / repo](https://www.minimal.audio/)

## Modulation

- [**TAL-Chorus-LX**](LINK_PAGES/tal-chorus-lx.md) — Juno-style chorus emulation. [Official site / repo](https://tal-software.com/products/tal-chorus-lx)
- [**Blue Cat Chorus**](LINK_PAGES/blue-cat-chorus.md) — Classic stereo chorus. [Official site / repo](https://www.bluecataudio.com/Products/Product_Chorus/)
- [**ChowPhaser**](LINK_PAGES/chowphaser.md) — Open-source phaser with analog-modeled feedback. [Official site / repo](https://github.com/jatinchowdhury18/ChowPhaser)

## Filters

- [**TAL-Filter-2**](LINK_PAGES/tal-filter-2.md) — Host-synced filter with tempo-synced modulation. [Official site / repo](https://tal-software.com/products/tal-filter-2)
- [**HY-Filter4 Free**](LINK_PAGES/hy-filter4-free.md) — Multi-mode filter with visualization. [Official site / repo](https://hy-plugins.com/product/hy-filter4-free/)
- [**Morph EQ**](LINK_PAGES/morph-eq.md) — Morphing parametric EQ and filter tool. [Official site / repo](https://kilohearts.com/products/morph_eq)

## Utility / Metering

- [**SPAN**](LINK_PAGES/span.md) — Real-time FFT spectrum analyzer. [Official site / repo](https://www.voxengo.com/product/span/)
- [**Youlean Loudness Meter**](LINK_PAGES/youlean-loudness-meter.md) — LUFS loudness metering. [Official site / repo](https://youlean.co/youlean-loudness-meter/)
- [**MLoudnessAnalyzer**](LINK_PAGES/mloudnessanalyzer.md) — Loudness analyzer. [Official site / repo](https://www.meldaproduction.com/MLoudnessAnalyzer)
- [**HOFA 4U Meter**](LINK_PAGES/hofa-4u-meter.md) — Level, correlation, and goniometer meters. [Official site / repo](https://hofa-plugins.de/en/plugins/4u/)
- [**dpMeter5**](LINK_PAGES/dpmeter5.md) — Multichannel meter with RMS, LUFS, and true peak. [Official site / repo](https://www.tb-software.com/TBProAudio/dpmeter5.html)
- [**MiniMeters**](LINK_PAGES/minimeters.md) — Standalone or plugin-style metering tools. [Official site / repo](https://www.minimeters.app/)

## Open-Source DSP Plugins

See the full guide: [OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md](OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md)

- [**Airwindows**](LINK_PAGES/airwindows.md) — Large collection of experimental audio effects. [Official site / repo](https://github.com/airwindows/airwindows)
- [**Chowdhury DSP**](LINK_PAGES/chowdhury-dsp.md) — Research-driven open-source effects and models. [Official site / repo](https://github.com/Chowdhury-DSP)
- [**DISTRHO Ports**](LINK_PAGES/distrho-ports.md) — Plugins ported to Linux and LV2 ecosystems. [Official site / repo](https://github.com/DISTRHO/DISTRHO-Ports)
- [**ZL-Audio Plugins**](LINK_PAGES/zl-audio-plugins.md) — Parametric EQ, compressor, and saturator projects. [Official site / repo](https://github.com/ZL-Audio)

## Multi-Effect Bundles

- [**Kilohearts Essentials**](LINK_PAGES/kilohearts-essentials.md) — Free bundle of snap-in effects and utilities. [Official site / repo](https://kilohearts.com/products/kilohearts_essentials)
- [**MeldaProduction MFreeFXBundle**](LINK_PAGES/meldaproduction-mfreefxbundle.md) — Large free bundle including EQ, compression, reverb, and analysis tools. [Official site / repo](https://www.meldaproduction.com/MFreeFXBundle)
- [**Audio Damage Free Collection**](LINK_PAGES/audio-damage-free-collection.md) — Free plugins such as Backmask, DreamEater, Dumpster Fire, MISHBY, MouthOfSorrow, and PocketDimension. [Official site / repo](https://www.audiodamage.com/pages/free-and-legacy)
- [**Cymatics Free Plugins**](LINK_PAGES/cymatics-free-plugins.md) — Free plugin collection including Diablo Lite, Space Lite, Memory, and Deja Vu. [Official site / repo](https://cymatics.fm/pages/free-plugins)

## Plugin Frameworks

See the full guide: [PLUGIN_FRAMEWORKS_AND_APIS.md](PLUGIN_FRAMEWORKS_AND_APIS.md)

- [**JUCE**](LINK_PAGES/juce.md) — End-to-end C++ framework for audio plugins and apps. [Official site / repo](https://juce.com)
- [**iPlug2**](LINK_PAGES/iplug2.md) — Lightweight C++ plugin framework. [Official site / repo](https://github.com/iPlug2/iPlug2)
- [**DPF**](LINK_PAGES/dpf.md) — Cross-platform framework with LV2, VST2/3, and CLAP support. [Official site / repo](https://github.com/DISTRHO/DPF)
- [**CLAP**](LINK_PAGES/clap.md) — Open plugin standard. [Official site / repo](https://github.com/free-audio/clap)
- [**NIH-plug**](LINK_PAGES/nih-plug.md) — Rust-based plugin framework. [Official site / repo](https://github.com/robbert-vdh/nih-plug)

## DSP Resources

See the full guide: [DSP_LEARNING_RESOURCES.md](DSP_LEARNING_RESOURCES.md)

- [**Audio EQ Cookbook**](LINK_PAGES/audio-eq-cookbook.md) — Classic biquad filter formulas and reference material. [Official site / repo](https://www.w3.org/2011/audio/audio-eq-cookbook.html)
- [**MusicDSP Archive**](LINK_PAGES/musicdsp-archive.md) — DSP algorithm snippets and references. [Official site / repo](https://www.musicdsp.org)
- [**The Scientist and Engineer's Guide to DSP**](LINK_PAGES/the-scientist-and-engineer-s-guide-to-dsp.md) — Free DSP textbook. [Official site / repo](http://www.dspguide.com/)
- [**JOS Stanford**](LINK_PAGES/jos-stanford.md) — Julius O. Smith's music DSP resources. [Official site / repo](https://ccrma.stanford.edu/~jos/)
- [**KVR Developer Forum**](LINK_PAGES/kvr-developer-forum.md) — Plugin-development community. [Official site / repo](https://www.kvraudio.com/forum/viewforum.php?f=33)

## Free Sample Packs

See the full guide: [SAMPLE_PACKS_AND_SOUND_RESOURCES.md](SAMPLE_PACKS_AND_SOUND_RESOURCES.md)


### TizWildin sample packs

| Pack | Description |
|------|-------------|
| [**Free Dark Piano Sound Kit**](https://github.com/GareBear99/Free-Dark-Piano-Sound-Kit) | 88 piano notes + dark/cinematic loops and MIDI |
| [**Free 808 Producer Kit**](https://github.com/GareBear99/Free-808-Producer-Kit) | 94 hand-crafted 808 bass samples tuned to every chromatic key |
| [**Free Riser Producer Kit**](https://github.com/GareBear99/Free-Riser-Producer-Kit) | 115+ risers and 63 downlifters — noise, synth, drum, FX, cinematic |
| [**Phonk Producer Toolkit**](https://github.com/GareBear99/Phonk_Producer_Toolkit) | Drift phonk starter kit — 808s, cowbells, drums, MIDI, templates |
| [**Free Future Bass Producer Kit**](https://github.com/GareBear99/Free-Future-Bass-Producer-Kit) | Loops, fills, drums, bass, synths, pads, and FX |


### Additional sources

- [**Cymatics Free Download Vault**](LINK_PAGES/cymatics-free-download-vault.md) — Rotating collection of free packs and production resources. [Official site / repo](https://cymatics.fm/pages/free-download-vault)
- [**Stickz**](LINK_PAGES/stickz.md) — Free and commercial sample content. [Official site / repo](https://stickz.co)

## Repository structure

This project uses a hub-and-spoke layout:
- `README.md` is the main discovery page
- category pages hold denser topic-specific lists
- support docs cover contributions, validation, maintenance, and outreach

That keeps the front page readable while still allowing category depth.

## Community submissions

Want to suggest a plugin, framework, or resource? See [COMMUNITY_SUBMISSIONS.md](COMMUNITY_SUBMISSIONS.md) for how to submit, what gets accepted, and a full list of every accepted entry.

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for formatting and inclusion rules.

## Support this project

If this repository saves you time or helps you discover something useful:

<a href="https://github.com/sponsors/GareBear99"><img src="https://img.shields.io/badge/sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors&style=for-the-badge" alt="GitHub Sponsors"></a>
<a href="https://buymeacoffee.com/garebear99"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?logo=buy-me-a-coffee&logoColor=black&style=for-the-badge" alt="Buy Me a Coffee"></a>
<a href="https://ko-fi.com/luciferai"><img src="https://img.shields.io/badge/Ko--fi-ff5e5b?logo=ko-fi&logoColor=white&style=for-the-badge" alt="Ko-fi"></a>

## License

This repository is distributed under the terms of the [LICENSE](LICENSE) file.
