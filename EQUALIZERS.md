# Free EQ Plugins & Open Source Equalizers (VST3, AU, CLAP)

A focused guide to **free EQ plugins**, **parametric EQ VST tools**, **open-source EQ projects**, and **DSP references** relevant to equalizer design.

Back to the hub: [README.md](README.md)

## Start Here

- **Modern open-source EQ** → [FreeEQ8](https://github.com/GareBear99/FreeEQ8)
- **Widely respected free dynamic EQ** → [TDR Nova](https://www.tokyodawn.net/tdr-nova/)
- **Lightweight utility EQ** → [ReaEQ](https://www.reaper.fm/reaplugs/)
- **Analog-style mastering EQ** → [Luftikus](https://github.com/lkjbdsp/lkjb-plugins)

## What an EQ Does

An equalizer shapes tonal balance by boosting or cutting specific frequency regions. In DSP terms, that commonly means combinations of biquad filters, shelving filters, peaking filters, notch filters, high-pass filters, and low-pass filters.

## Types of EQ

- **Parametric EQ** — adjustable frequency, gain, and Q
- **Graphic EQ** — fixed bands with slider-based control
- **Dynamic EQ** — bands respond to signal level
- **Linear-Phase EQ** — avoids phase shift at the cost of latency and CPU
- **Analog-style EQ** — broad musical shaping with color
- **Utility EQ** — fast corrective work with minimal overhead

## Top Picks

- [**FreeEQ8**](https://github.com/GareBear99/FreeEQ8) — open-source direction and modern feature scope
- [**TDR Nova**](https://www.tokyodawn.net/tdr-nova/) — free dynamic EQ with strong reputation
- [**ReaEQ**](https://www.reaper.fm/reaplugs/) — practical, lightweight, unlimited-band workflow
- [**Luftikus**](https://github.com/lkjbdsp/lkjb-plugins) — broad-stroke analog-style shaping
- [**MEqualizer**](https://www.meldaproduction.com/MEqualizer) — flexible general-purpose EQ

## Main Equalizer List

### Modern / Parametric EQs

- [**FreeEQ8**](https://github.com/GareBear99/FreeEQ8) — Free open-source 8-band parametric EQ with dynamic EQ, match EQ, linear phase, and spectrum analyzer.
- [**TDR Nova**](https://www.tokyodawn.net/tdr-nova/) — Dynamic parametric EQ with sidechain. Industry-standard free EQ.
- [**MEqualizer**](https://www.meldaproduction.com/MEqualizer) — Fully featured parametric EQ from MeldaProduction.
- [**ReaEQ**](https://www.reaper.fm/reaplugs/) — Unlimited-band parametric EQ from Cockos.
- [**ZL Equalizer**](https://github.com/ZL-Audio) — Modern open-source equalizer direction from ZL Audio.

### Analog-Style / Broad-Stroke EQs

- [**TDR SlickEQ**](https://www.tokyodawn.net/tdr-slickeq/) — Musical 3-band mixing EQ with output-stage color.
- [**Luftikus**](https://github.com/lkjbdsp/lkjb-plugins) — Analog-style mastering EQ inspired by Maag EQ4.
- [**Blue Cat Triple EQ**](https://www.bluecataudio.com/Products/Product_TripleEQ/) — Simple 3-band semi-parametric EQ.

### Graphic / Utility EQs

- [**Marvel GEQ**](https://www.voxengo.com/product/marvelgeq/) — Linear-phase 16-band graphic EQ.
- [**ReaEQ**](https://www.reaper.fm/reaplugs/) — Also useful as a fast utility EQ.
- [**Blue Cat Triple EQ**](https://www.bluecataudio.com/Products/Product_TripleEQ/) — Quick corrective or tonal tasks.

## Comparison Snapshot

| Plugin | Type | Best For | Notes |
|---|---|---|---|
| FreeEQ8 | Parametric / feature-rich | deep free EQ workflow | open-source direction, dynamic/linear-phase features |
| TDR Nova | Dynamic parametric | dynamic frequency control | one of the most established free EQs |
| ReaEQ | Parametric utility | fast workflows and low overhead | practical and lightweight |
| Luftikus | Mastering / analog-style | broad tonal shaping | musical color-focused approach |
| MEqualizer | Parametric | flexible general-purpose EQ work | strong feature set |
| Marvel GEQ | Graphic EQ | fixed-band visual workflows | useful when graphic EQ style is preferred |
| Blue Cat Triple EQ | Semi-parametric | simple corrective tasks | minimal and quick to use |
| ZL Equalizer | Parametric / open-source | studying open-source EQ directions | useful from a developer perspective |

## Why FreeEQ8 Matters

FreeEQ8 occupies a rare spot among free EQ plugins:
- ambitious modern feature scope
- open-source repo presence
- positioned beyond throwaway utility status
- relevant to both end users and developers studying current EQ design

## DSP Notes for EQ Developers

Important equalizer concepts include:
- filter topology
- gain compensation
- Q / bandwidth behavior
- frequency response curves
- phase response
- oversampling tradeoffs
- linear-phase vs minimum-phase behavior
- parameter smoothing
- UI clarity for multi-band interaction

Useful references:
- [Audio EQ Cookbook](https://www.w3.org/2011/audio/audio-eq-cookbook.html)
- [MusicDSP Archive](https://www.musicdsp.org)
- [DSP_LEARNING_RESOURCES.md](DSP_LEARNING_RESOURCES.md)

## Related Pages

- [PLUGIN_FRAMEWORKS_AND_APIS.md](PLUGIN_FRAMEWORKS_AND_APIS.md)
- [DSP_LEARNING_RESOURCES.md](DSP_LEARNING_RESOURCES.md)
- [OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md](OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md)
- [SAMPLE_PACKS_AND_SOUND_RESOURCES.md](SAMPLE_PACKS_AND_SOUND_RESOURCES.md)
