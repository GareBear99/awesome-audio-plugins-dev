# Open-Source DSP Plugin Repositories

A focused reference page for **open-source audio plugin repos**, **DSP codebases**, and **projects worth studying**.

Back to the hub: [README.md](README.md)

## Why Repositories Matter

A plugin list is useful for discovery. A repository list is useful for understanding how the work is actually done.

Source repos expose:
- project structure
- build systems
- DSP/UI separation
- maintenance style
- code quality tradeoffs
- scope decisions

## Main Repositories

- [**Airwindows**](https://github.com/airwindows/airwindows) — large collection of experimental audio effects by Chris Johnson.
- [**Chowdhury DSP**](https://github.com/Chowdhury-DSP) — high-quality open-source effects and research-driven work.
- [**DISTRHO Ports**](https://github.com/DISTRHO/DISTRHO-Ports) — collection of plugins ported to Linux/LV2.
- [**ZL-Audio Plugins**](https://github.com/ZL-Audio) — parametric EQ, compressor, and saturator.
- [**lkjb plugins**](https://github.com/lkjbdsp/lkjb-plugins) — lightweight free plugin collection.

## What These Repositories Show

### Airwindows
- unconventional processing approaches
- huge breadth of effect ideas
- minimalist plugin philosophy

### Chowdhury DSP
- modern research flavor
- modeling-heavy work
- stronger emphasis on advanced DSP topics

### DISTRHO Ports
- plugin portability
- Linux relevance
- adaptation across formats and ecosystems

### ZL-Audio Plugins
- modern open-source plugin direction
- practical feature-oriented tools
- useful for comparison against other EQ/compressor repos

### lkjb plugins
- lean plugin design
- light utility focus
- clean examples for smaller-scope tools

## Study Method

A practical study path:

1. pick one simple repo
2. identify where parameters enter the system
3. trace DSP processing code
4. separate UI code from audio-thread code
5. compare that repo to a larger or more ambitious one

## What to Look For in Code

- processing callbacks
- parameter smoothing
- state serialization
- build configuration
- plugin-format wrappers
- DSP module boundaries
- testing or validation patterns

## Related Pages

- [DSP_LEARNING_RESOURCES.md](DSP_LEARNING_RESOURCES.md)
- [PLUGIN_FRAMEWORKS_AND_APIS.md](PLUGIN_FRAMEWORKS_AND_APIS.md)
- [EQUALIZERS.md](EQUALIZERS.md)
- [Q_AND_A_FAQ.md](Q_AND_A_FAQ.md)
