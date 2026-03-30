# Audio DSP Learning Resources

A structured reference page for **audio DSP fundamentals**, **signal-processing study**, and **plugin-development learning paths**.

Back to the hub: [README.md](README.md)

## Foundations

Audio DSP starts with a few core ideas:

- signals change over time
- systems transform those signals
- digital systems operate on discrete samples
- every design choice trades something off: latency, CPU, phase, accuracy, or flexibility

## Beginner Topics

- signal flow
- gain and level
- waveform vs frequency content
- sample rate
- bit depth
- clipping
- basic filter behavior
- mono vs stereo
- time-domain thinking

## Beginner References

- [**The Scientist and Engineer's Guide to DSP**](http://www.dspguide.com/)
- [**Audio EQ Cookbook**](https://www.w3.org/2011/audio/audio-eq-cookbook.html)
- [**MusicDSP Archive**](https://www.musicdsp.org)

## Intermediate Topics

- FFTs and spectral analysis
- convolution
- dynamics processing
- delay and feedback systems
- modulation
- nonlinear processing and saturation
- transient behavior
- parameter smoothing

## Intermediate Questions Worth Studying

- how does an FFT differ from a filter?
- what makes a compressor feel transparent or aggressive?
- how do feedback systems become unstable?
- why do saturators sound different even when they all “add harmonics”?
- what causes zipper noise in badly smoothed parameters?

## Advanced Topics

- linear-phase processing
- oversampling
- physical modeling
- neural-network-based modeling
- real-time constraints
- CPU and latency tradeoffs
- denormals
- numerical stability
- aliasing control
- phase tradeoffs

## Advanced Concerns

- latency budgets in real products
- automation behavior under host control
- real-time safe design
- balancing feature depth with usability
- separating DSP correctness from UI polish

## Key References

- [**Audio EQ Cookbook**](https://www.w3.org/2011/audio/audio-eq-cookbook.html)
- [**MusicDSP Archive**](https://www.musicdsp.org)
- [**The Scientist and Engineer's Guide to DSP**](http://www.dspguide.com/)
- [**JOS Stanford**](https://ccrma.stanford.edu/~jos/)
- [**DAFX**](https://www.dafx.de/)
- [**KVR Developer Forum**](https://www.kvraudio.com/forum/viewforum.php?f=33)

## Recommended Study Order

1. signal flow, gain, and frequency basics
2. simple filters and EQ
3. delay, reverb, and modulation systems
4. compressors and dynamics
5. spectral processing and FFT workflows
6. open-source plugin repos
7. plugin frameworks and deployment pipelines

## How This Connects to Plugin Development

DSP knowledge becomes much more practical when tied to:
- real plugin frameworks
- open-source codebases
- specific categories like EQ, dynamics, delay, reverb, and modulation
- validation and deployment workflows

## Related Pages

- [EQUALIZERS.md](EQUALIZERS.md)
- [PLUGIN_FRAMEWORKS_AND_APIS.md](PLUGIN_FRAMEWORKS_AND_APIS.md)
- [OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md](OPEN_SOURCE_DSP_PLUGIN_REPOSITORIES.md)
- [Q_AND_A_FAQ.md](Q_AND_A_FAQ.md)
