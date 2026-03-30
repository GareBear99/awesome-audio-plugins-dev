# Audio Plugin Development Frameworks & APIs

A reference page for **audio plugin frameworks**, **plugin formats**, **SDKs**, and **build tools** relevant to VST3, AU, CLAP, and LV2 development.

Back to the hub: [README.md](README.md)

## Core Frameworks

- [**JUCE**](https://juce.com) — Industry-standard C++ framework for audio plugins and apps.
- [**iPlug2**](https://github.com/iPlug2/iPlug2) — Lightweight C++ framework for VST2/3, AU, AAX, and web audio.
- [**DPF**](https://github.com/DISTRHO/DPF) — Cross-platform framework with LV2, VST2/3, and CLAP support.
- [**CLAP**](https://github.com/free-audio/clap) — Open plugin standard by Bitwig and u-he.
- [**NIH-plug**](https://github.com/robbert-vdh/nih-plug) — Rust-based plugin framework.

## Build Tools & SDKs

- [**VST3 SDK**](https://github.com/steinbergmedia/vst3sdk) — Official VST3 SDK.
- [**Projucer**](https://juce.com/learn/tutorials/) — JUCE project creation and editing workflow.
- [**CMake**](https://cmake.org) — Common build system for modern cross-platform plugin projects.
- [**pluginval**](https://github.com/Tracktion/pluginval) — Plugin validation and compatibility testing.
- [**Pamplejuce**](https://github.com/sudara/pamplejuce) — JUCE starter template with CI and CMake.

## Framework Comparison

| Framework | Language | Strength | Best Fit |
|---|---|---|---|
| JUCE | C++ | mature end-to-end workflow | general-purpose plugin development |
| iPlug2 | C++ | lighter-weight framework | leaner projects |
| DPF | C++ | open-source and Linux-friendly | cross-platform open toolchains |
| NIH-plug | Rust | Rust-native development | Rust DSP stacks |
| CLAP | format / API spec | modern open standard | future-facing format support |

## Plugin Formats

- **VST3** — dominant in many modern DAW workflows
- **AU** — essential for Apple ecosystems
- **CLAP** — open standard with growing developer interest
- **LV2** — relevant in Linux and open-audio communities

## How Frameworks Matter

A framework generally provides:
- host integration
- parameter handling
- UI abstractions
- project organization
- format wrapping
- lifecycle management for processing and state

## Build Pipeline Notes

A typical plugin-development workflow:

1. choose a framework
2. scaffold the project
3. configure builds with CMake or the framework’s workflow
4. validate with `pluginval`
5. test in hosts
6. iterate on DSP/UI separation and packaging

## Related Pages

- [EQUALIZERS.md](EQUALIZERS.md)
- [DSP_LEARNING_RESOURCES.md](DSP_LEARNING_RESOURCES.md)
- [OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md](OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md)
- [SAMPLE_PACKS_AND_SOUND_RESOURCES.md](SAMPLE_PACKS_AND_SOUND_RESOURCES.md)
