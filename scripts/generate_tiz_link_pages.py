#!/usr/bin/env python3
"""Generate professional LINK_PAGES for every TizWildin ecosystem plugin.

This regenerates / overwrites the existing TizWildin LINK_PAGES with richer
content and creates pages for every plugin in the TizWildin Entertainment
HUB catalog (17 plugins). Run from the repository root.
"""
from __future__ import annotations
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
LINK_DIR = ROOT / "LINK_PAGES"
LINK_DIR.mkdir(exist_ok=True)

HUB_URL = "https://github.com/GareBear99/TizWildinEntertainmentHUB"
DASHBOARD_URL = "https://garebear99.github.io/TizWildinEntertainmentHUB/"

# Structured plugin catalog. Each entry becomes a LINK_PAGES/<slug>.md page.
# Key fields:
#   slug         : filename without .md, also used for asset name
#   name         : display name
#   repo         : GitHub slug (GareBear99/<repo>)
#   category     : HUB category (Flagship / Instruments / Maid Suite / Sound Design / Experimental)
#   role         : short one-liner shown next to the name
#   status       : Production / Beta / Dev
#   formats      : list of format strings
#   tagline      : one-sentence pitch
#   overview     : multi-paragraph description (plain paragraphs separated by blank lines)
#   features     : bullet list of capabilities
#   internals    : bullet list describing architecture / DSP decisions (optional)
#   workflows    : bullet list of typical use cases / sound-design contexts
#   compat       : platform / DAW string
#   related      : list of (label, url) linking to sibling projects
PLUGINS = [
    {
        "slug": "freeeq8",
        "name": "FreeEQ8",
        "repo": "FreeEQ8",
        "category": "Flagship",
        "role": "Free open-source 8-band parametric EQ",
        "status": "Production",
        "formats": ["VST3", "AU", "Standalone"],
        "tagline": "A professional-grade, fully open-source 8-band parametric EQ built with JUCE — linear phase, dynamic EQ, match EQ, per-band drive, M/S processing, oversampling, and a 4096-point real-time spectrum analyzer.",
        "overview": (
            "FreeEQ8 is engineered as the reference equalizer inside the TizWildin ecosystem. It is "
            "not a stripped-down demo; it is a mixing- and mastering-grade EQ that ships free under "
            "GPL-3.0 and competes directly with commercial dynamic/linear-phase EQs.\n\n"
            "The plugin is designed around a \"selected-band\" paradigm — eight colored band buttons "
            "rebind a single set of high-precision controls — giving producers an interface that is "
            "fast to operate in a mix session while exposing the full depth of modern EQ features."
        ),
        "features": [
            "Eight independent parametric bands with full frequency / Q / gain control",
            "Six filter types per band: Bell, Low/High Shelf, High/Low Pass, Bandpass",
            "12 / 24 / 48 dB per octave slopes via cascaded biquad stages",
            "Linear-phase mode (overlap-add FFT convolution, 2048-sample latency)",
            "Dynamic EQ per band with threshold, ratio, attack, release, and sidechain bandpass",
            "Per-band saturation (gain-compensated tanh waveshaper, 0-100 %)",
            "Mid/Side processing with per-band channel routing",
            "Oversampling at 1× / 2× / 4× / 8× using JUCE polyphase IIR half-bands",
            "Band linking groups (A/B) with frequency-ratio and delta-gain/Q propagation",
            "Match EQ — capture reference spectrum, compute per-bin correction",
            "Adaptive Q that widens with gain for musical boosts",
            "Real-time 4096-point FFT spectrum analyzer with pre/post toggle",
            "30 factory presets, undo/redo via JUCE UndoManager and APVTS",
        ],
        "internals": [
            "Transposed Direct Form II biquad with 64-bit internal arithmetic",
            "RBJ Audio EQ Cookbook coefficients",
            "Coefficient refresh every 16 samples, 20 ms parameter smoothing",
            "Zero latency in minimum-phase mode; 2048-sample FIR in linear-phase mode",
            "Built with JUCE 7.0.12 against VST3 and AU SDKs",
        ],
        "workflows": [
            "Corrective mixing - pinpoint resonances with narrow Q and automate",
            "Mastering - linear-phase mode plus adaptive Q for transparent shaping",
            "Dynamic taming - frequency-specific compression via per-band dynamics",
            "Sound design - stack bells at the same frequency with different Q for resonant sweeps",
        ],
        "compat": "macOS 10.13+ (Intel + Apple Silicon), Windows 10+ (64-bit), Debian/Ubuntu 20.04+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("Live dashboard", DASHBOARD_URL),
            ("Therum (wavetable synth)", "https://github.com/GareBear99/Therum_JUCE-Plugin"),
        ],
    },
    {
        "slug": "therum",
        "name": "Therum",
        "repo": "Therum_JUCE-Plugin",
        "category": "Flagship",
        "role": "Free wavetable synthesizer",
        "status": "Production",
        "formats": ["VST3", "AU"],
        "tagline": "A flagship free wavetable synthesizer built as a full alternative to paid wavetable workstations — visual wave editing, deep modulation, and a modern interface.",
        "overview": (
            "Therum is the flagship synthesizer of the TizWildin ecosystem. It is designed to "
            "deliver the sonic range of a modern premium wavetable synth (Serum-class workflows) "
            "under an unrestricted free license with an open GitHub release cadence.\n\n"
            "The engine is built around a multi-oscillator wavetable core, a matrix-style "
            "modulation system, and a visual waveform editor so producers can design and share "
            "wavetables directly inside the plugin."
        ),
        "features": [
            "Multi-oscillator wavetable engine with visual waveform editing",
            "Unison, detune, pan-spread, and stacking per oscillator",
            "Flexible modulation matrix: LFOs, envelopes, velocity, aftertouch",
            "Built-in filter bank with low-pass, band-pass, high-pass, and formant modes",
            "Effects chain including distortion, chorus, delay, and reverb",
            "Preset system with save, load, and browse",
        ],
        "workflows": [
            "EDM / trap bass design and wobble patches",
            "Cinematic leads with evolving wavetable sweeps",
            "Retro analog emulation via filtered classic waves",
            "Sound design for sync and media libraries",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+, Linux (VST3)",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("FreeEQ8", "https://github.com/GareBear99/FreeEQ8"),
            ("RiftWave Suite", "https://github.com/GareBear99/RiftWaveSuite_RiftSynth_WaveForm_Lite"),
        ],
    },
    {
        "slug": "instrudio",
        "name": "Instrudio",
        "repo": "Instrudio",
        "category": "Instruments",
        "role": "Ten-instrument cross-platform instrument ecosystem",
        "status": "Beta",
        "formats": ["VST3", "AU", "Standalone"],
        "tagline": "A hybrid HTML/plugin instrument ecosystem that ships ten fully playable instruments under one roof, tuned for cross-platform production workflows.",
        "overview": (
            "Instrudio is a multi-instrument suite that delivers ten independently playable "
            "instruments behind a single host surface. It combines native plugin rendering with "
            "a hybrid HTML layer, allowing Instrudio to share the same instrument definitions "
            "between a DAW plugin, a standalone app, and an in-browser tester.\n\n"
            "Every instrument in Instrudio is built from the same sampling / physical-modeling "
            "layer that powers the Free Violin Synth Sample Kit, giving the set a consistent "
            "tone and a uniform MIDI response."
        ),
        "features": [
            "Ten playable instruments available from one plugin surface",
            "Hybrid HTML/plugin architecture for cross-platform rendering",
            "Shared sampling layer across all instruments",
            "Velocity, round-robin, and keyswitch support where appropriate",
            "Standalone mode for practice, testing, or live performance",
            "Source-level repo distribution so every instrument can be forked",
        ],
        "workflows": [
            "Film / game scoring using the full instrument roster",
            "Sketching orchestral layers before committing to paid libraries",
            "Live performance with the standalone build",
            "Developer reference for hybrid plugin + HTML UX",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+, Linux (VST3)",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("XyloCore", "https://github.com/GareBear99/XyloCore"),
            ("Free Violin Synth Sample Kit", "https://github.com/GareBear99/Free-Violin-Synth-Sample-Kit"),
        ],
    },
    {
        "slug": "xylocore",
        "name": "XyloCore",
        "repo": "XyloCore",
        "category": "Instruments",
        "role": "Playable xylophone / tuned-percussion instrument",
        "status": "Beta",
        "formats": ["VST3", "AU"],
        "tagline": "A playable, velocity-aware xylophone and tuned-percussion instrument designed to slot into the Instrudio family without its overhead.",
        "overview": (
            "XyloCore is the focused, tuned-percussion entry point in the TizWildin instrument "
            "line. Where Instrudio bundles ten instruments under one shell, XyloCore exposes a "
            "single, high-quality tuned-percussion engine optimized for quick MIDI sketching and "
            "layering.\n\n"
            "It is ideal for producers who want a clean, believable xylophone / mallet voice "
            "without loading a full instrument suite."
        ),
        "features": [
            "Velocity-mapped sample playback across a full playable range",
            "Keyboard-based MIDI control with consistent tuning reference",
            "Low-footprint load for quick insertion into any template",
            "Cleanly scoped scope so the instrument can be extended later",
        ],
        "workflows": [
            "Arpeggiated mallet lines in cinematic and game scoring",
            "Bright rhythmic layers in pop and hybrid productions",
            "Teaching / learning context for tuned percussion parts",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("Instrudio", "https://github.com/GareBear99/Instrudio"),
        ],
    },
    {
        "slug": "bassmaid",
        "name": "BassMaid",
        "repo": "BassMaid",
        "category": "Maid Suite",
        "role": "Low-end processing toolkit",
        "status": "Production",
        "formats": ["VST3", "AU"],
        "tagline": "A focused low-end processor that enhances bass weight, controls sub-bass energy, and tightens kick / 808 interaction without the usual multiband headaches.",
        "overview": (
            "BassMaid is the low-end specialist in the Maid Suite. It combines harmonic "
            "enhancement, dynamic low-band control, and mono-management into a compact tool "
            "producers can drop on a bass bus to dial in the final sub without a chain of "
            "six plugins.\n\n"
            "The intent is to keep decisions simple where they should be simple — sub level, "
            "weight, tightness — while still exposing the parameters that matter when mixing."
        ),
        "features": [
            "Sub-bass enhancement with tuned harmonic generation",
            "Low-band dynamic shaping for tight kick / 808 relationships",
            "Mono-summing below an adjustable cutoff",
            "Gain-matched bypass for honest A/B evaluation",
        ],
        "workflows": [
            "Tightening kick plus 808 interaction in trap and drill",
            "Adding speaker-audible weight to a sub-heavy mix",
            "Cleaning up mono compatibility for streaming masters",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("SpaceMaid", "https://github.com/GareBear99/SpaceMaid"),
            ("GlueMaid", "https://github.com/GareBear99/GlueMaid"),
            ("MixMaid", "https://github.com/GareBear99/MixMaid"),
            ("ChainMaid", "https://github.com/GareBear99/ChainMaid"),
        ],
    },
    {
        "slug": "spacemaid",
        "name": "SpaceMaid",
        "repo": "SpaceMaid",
        "category": "Maid Suite",
        "role": "Spatial audio processor",
        "status": "Production",
        "formats": ["VST3", "AU"],
        "tagline": "A spatial processor covering depth, width, and reverb placement with the same minimal-decisions UX as the rest of the Maid Suite.",
        "overview": (
            "SpaceMaid is the space designer of the Maid Suite. It wraps stereo widening, "
            "depth control, and algorithmic reverb sends into a single panel so producers can "
            "place a source in a room without negotiating five separate plugins.\n\n"
            "Mono compatibility and phase integrity are treated as first-class concerns — "
            "widening never trades off bass centering or mono translation."
        ),
        "features": [
            "Haas / mid-side stereo widening with mono-safety metering",
            "Depth control via filtered early reflections",
            "Algorithmic reverb with pre-delay, size, and damping",
            "Wet / dry balance with integrated gain matching",
        ],
        "workflows": [
            "Placing vocals in a defined perceptual room",
            "Widening pads and synths while keeping the bass mono",
            "Adding depth to percussion without smearing transients",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("BassMaid", "https://github.com/GareBear99/BassMaid"),
            ("MixMaid", "https://github.com/GareBear99/MixMaid"),
        ],
    },
    {
        "slug": "gluemaid",
        "name": "GlueMaid",
        "repo": "GlueMaid",
        "category": "Maid Suite",
        "role": "Mix-bus glue and cohesion",
        "status": "Production",
        "formats": ["VST3", "AU"],
        "tagline": "A mix-bus cohesion processor that merges gentle bus compression, saturation, and tonal shaping into a single glue stage.",
        "overview": (
            "GlueMaid sits on the mix bus and focuses on a specific job: give a mix a cohesive, "
            "finished feel without squashing transients or dulling the top end.\n\n"
            "It combines a transparent bus compressor with musical analog-style saturation and a "
            "broad tilt EQ, tuned so default values already sound good on most sources."
        ),
        "features": [
            "Program-dependent bus compression",
            "Analog-style saturation stage with drive and mix controls",
            "Broad tilt EQ for fast overall tonal balance",
            "Internal gain matching so decisions remain tonal, not loud",
        ],
        "workflows": [
            "Mix-bus or stem-bus glue during mixing",
            "Final-cleanup stage before mastering hand-off",
            "Parallel glue on aggressive drum busses",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("MixMaid", "https://github.com/GareBear99/MixMaid"),
            ("ChainMaid", "https://github.com/GareBear99/ChainMaid"),
        ],
    },
    {
        "slug": "mixmaid",
        "name": "MixMaid",
        "repo": "MixMaid",
        "category": "Maid Suite",
        "role": "Spectral balance and mix correction",
        "status": "Production",
        "formats": ["VST3", "AU"],
        "tagline": "Real-time spectral balance and mix-correction assistant — gently guides a mix toward a balanced tonal distribution, proper headroom, and controlled dynamics.",
        "overview": (
            "MixMaid is a correction-oriented assistant that continuously evaluates a mix for "
            "spectral balance, dynamic consistency, and headroom.\n\n"
            "It applies gentle corrective moves rather than aggressive processing, making it "
            "suitable for a late-stage mixing insert or a pre-mastering reference tool."
        ),
        "features": [
            "Real-time spectral analysis against a reference curve",
            "Gentle multiband correction guided by the analysis",
            "Dynamic-range monitoring with loudness and crest metering",
            "Headroom and ceiling warnings",
        ],
        "workflows": [
            "Late-stage mix balancing before mastering",
            "Teaching context: showing students where the mix leans",
            "Reality check after long mixing sessions when ears are tired",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("GlueMaid", "https://github.com/GareBear99/GlueMaid"),
            ("FreeEQ8", "https://github.com/GareBear99/FreeEQ8"),
        ],
    },
    {
        "slug": "chainmaid",
        "name": "ChainMaid",
        "repo": "ChainMaid",
        "category": "Maid Suite",
        "role": "Sidechain ducking and pumping",
        "status": "Production",
        "formats": ["VST3", "AU"],
        "tagline": "A dedicated sidechain plugin for clean ducking and musical pumping effects across EDM, trap, and mix-engineering contexts.",
        "overview": (
            "ChainMaid is the sidechain specialist of the Maid Suite. Rather than relying on an "
            "ambiguous compressor sidechain setup, ChainMaid exposes a shaped envelope that "
            "can be driven by MIDI, a sidechain input, or an internal tempo clock.\n\n"
            "The result is consistent, DAW-portable pumping behaviour that is easier to share "
            "across projects than a hand-drawn volume automation curve."
        ),
        "features": [
            "MIDI-triggered, sidechain-driven, or tempo-synced envelope",
            "Shaped curve with depth, attack, hold, and release controls",
            "Waveform display showing the duck response in real time",
            "Low CPU footprint for heavy use on EDM / trap mixes",
        ],
        "workflows": [
            "Classic EDM kick-vs-bass pumping",
            "Rhythmic ducking of pads and atmospheres",
            "Creative gating / chopping on vocal beds and drones",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("GlueMaid", "https://github.com/GareBear99/GlueMaid"),
            ("BassMaid", "https://github.com/GareBear99/BassMaid"),
        ],
    },
    {
        "slug": "riftwave-suite",
        "name": "RiftWave Suite",
        "repo": "RiftWaveSuite_RiftSynth_WaveForm_Lite",
        "category": "Sound Design",
        "role": "Modular synth + waveform synthesis",
        "status": "Beta",
        "formats": ["VST3", "AU"],
        "tagline": "A modular synthesis + waveform-synthesis plugin suite — RiftSynth and WaveForm in Lite and Pro editions — aimed at deep sound design.",
        "overview": (
            "RiftWave Suite is a two-engine synthesis system: RiftSynth is the modular patch-"
            "oriented synth, and WaveForm is the waveform-sculpting engine. The suite ships in "
            "Lite and Pro editions; the Lite edition is free and GitHub-distributed.\n\n"
            "The architecture is designed to let producers switch between subtractive, "
            "additive, and wavetable thinking without leaving the suite."
        ),
        "features": [
            "RiftSynth modular engine with patchable modulation",
            "WaveForm waveform-sculpting engine for additive / wavetable hybrids",
            "Shared preset format across Lite and Pro",
            "Open source Lite edition available on GitHub",
        ],
        "workflows": [
            "Sound design for sync, games, and sample libraries",
            "Modular-style patching inside a DAW session",
            "Creative wavetable / additive hybrids",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("Therum", "https://github.com/GareBear99/Therum_JUCE-Plugin"),
            ("FreeSampler", "https://github.com/GareBear99/FreeSampler_v0.3"),
        ],
    },
    {
        "slug": "paintmask",
        "name": "PaintMask",
        "repo": "PaintMask_Free-JUCE-Plugin",
        "category": "Experimental",
        "role": "Paint-driven audio / MIDI processor",
        "status": "Beta",
        "formats": ["VST3", "AU"],
        "tagline": "Visual paint-based audio processing — shape sound with brush strokes, splashes, and geometry that become MIDI patterns and modulation sources.",
        "overview": (
            "PaintMask is an experimental sound-design tool that converts a painted canvas into "
            "MIDI and modulation data. Brush strokes, splashes, and geometric shapes map to "
            "pitch, time, and velocity fields that feed downstream instruments.\n\n"
            "It is designed for composers who think visually and for sound designers who want "
            "to break out of the piano-roll grid."
        ),
        "features": [
            "Interactive paint canvas with multiple brushes and splash tools",
            "Deterministic mapping from geometry to MIDI (pitch, time, velocity)",
            "Modulation lanes derived from canvas features",
            "Preset system for painted patterns",
        ],
        "workflows": [
            "Generative motif writing outside the piano roll",
            "Cinematic texture design via painted gesture",
            "Teaching: explaining pitch/time/velocity through a visual metaphor",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("WURP", "https://github.com/GareBear99/WURP_Toxic-Motion-Engine_JUCE"),
            ("AETHER", "https://github.com/GareBear99/AETHER_Choir-Atmosphere-Designer"),
        ],
    },
    {
        "slug": "wurp",
        "name": "WURP",
        "repo": "WURP_Toxic-Motion-Engine_JUCE",
        "category": "Experimental",
        "role": "Toxic Motion Engine - formant, saturation, elastic pitch",
        "status": "Production",
        "formats": ["VST3", "AU"],
        "tagline": "An experimental sound-design engine that mutates audio with formant motion, corrosive saturation, elastic pitch shifting, and a reactive animated UI.",
        "overview": (
            "WURP is the Toxic Motion Engine of the TizWildin ecosystem — an intentionally "
            "aggressive sound-design plugin designed to mangle, morph, and corrode input audio.\n\n"
            "It is built around three interlocking modules: a formant-mover, a nonlinear "
            "saturator, and an elastic pitch stage. The UI responds to the signal in real time "
            "so that creative parameter moves have a visible, tactile feedback loop."
        ),
        "features": [
            "Formant motion with user-defined trajectories",
            "Corrosive non-linear saturation with multiple character modes",
            "Elastic pitch shifting that can be modulated",
            "Reactive animated UI tied to the signal analysis",
            "Preset system with save / load / browse",
        ],
        "workflows": [
            "Vocal FX and chant-style mutation",
            "Creature / monster design for games and film",
            "Aggressive trap / hyperpop / industrial sound design",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("AETHER", "https://github.com/GareBear99/AETHER_Choir-Atmosphere-Designer"),
            ("WhisperGate", "https://github.com/GareBear99/WhisperGate_Free-JUCE-Plugin"),
        ],
    },
    {
        "slug": "aether",
        "name": "AETHER",
        "repo": "AETHER_Choir-Atmosphere-Designer",
        "category": "Experimental",
        "role": "Choir and atmosphere designer",
        "status": "Beta",
        "formats": ["VST3", "AU"],
        "tagline": "A choir and atmosphere designer for cinematic sound design — procedural choirs, pads, and evolving textures.",
        "overview": (
            "AETHER is an atmosphere and choir designer built for cinematic, ambient, and game "
            "sound designers. It procedurally generates choral textures and evolving pads from "
            "a small set of high-level parameters.\n\n"
            "Rather than playing back pre-recorded choirs, AETHER synthesises them, so every "
            "pad is unique to a project."
        ),
        "features": [
            "Procedural choir generation with syllable / formant control",
            "Evolving pad textures driven by slow modulators",
            "High-level macro controls for size, brightness, and tension",
            "Preset system with room for user-saved slots",
        ],
        "workflows": [
            "Film / trailer beds and ambient transitions",
            "Game-engine-friendly procedural atmospheres",
            "Ambient production and drone composition",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("WhisperGate", "https://github.com/GareBear99/WhisperGate_Free-JUCE-Plugin"),
            ("WURP", "https://github.com/GareBear99/WURP_Toxic-Motion-Engine_JUCE"),
        ],
    },
    {
        "slug": "whispergate",
        "name": "WhisperGate",
        "repo": "WhisperGate_Free-JUCE-Plugin",
        "category": "Experimental",
        "role": "Procedural whispers and ritual atmospheres",
        "status": "Production",
        "formats": ["VST3", "AU"],
        "tagline": "Procedural whispers, ghost choirs, and ritual atmospheres controlled through an interactive geometry interface.",
        "overview": (
            "WhisperGate generates whispered voices, ghost-choir beds, and ritual-sounding "
            "atmospheres. The defining feature is its control surface: a geometric diagram "
            "where points, edges, and regions map to voice density, pitch range, phrasing, "
            "and emotion.\n\n"
            "The plugin is aimed at game sound designers, horror-adjacent producers, and "
            "film composers who need believable but unsettling vocal atmospheres without "
            "recording them by hand."
        ),
        "features": [
            "Procedural whisper / choir generation",
            "Interactive geometry UI for shaping voice behaviour",
            "Density, pitch-range, phrasing, and mood macros",
            "Stereo imaging tuned for headphones and cinematic mixes",
        ],
        "workflows": [
            "Horror and psychological thriller sound design",
            "Ritual-style ambient and dark cinematic",
            "Game-engine streamable beds for dynamic scenes",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("AETHER", "https://github.com/GareBear99/AETHER_Choir-Atmosphere-Designer"),
            ("PAP Forge", "https://github.com/GareBear99/PAP-Forge-Audio"),
        ],
    },
    {
        "slug": "freesampler",
        "name": "FreeSampler",
        "repo": "FreeSampler_v0.3",
        "category": "Experimental",
        "role": "Lightweight high-performance sampler",
        "status": "Dev",
        "formats": ["VST3", "AU"],
        "tagline": "A lightweight, high-performance free sampler plugin aimed at producers who want the core 80 % of a commercial sampler with none of the overhead.",
        "overview": (
            "FreeSampler is the sampler project of the TizWildin ecosystem. The v0.3 line is "
            "explicitly a development release — the architecture is stable enough to ship, and "
            "the goal is to iterate toward a fully playable free sampler.\n\n"
            "The plugin loads common audio files, maps them across keys, and exposes the "
            "parameters producers need for day-to-day sampling without burying them in menus."
        ),
        "features": [
            "Drag-and-drop audio file loading",
            "Keyboard mapping with configurable root key",
            "Basic envelope and filter stages",
            "Light CPU footprint suitable for many simultaneous instances",
        ],
        "workflows": [
            "Quick one-shot layering in beat-making",
            "Prototype sampling for sound designers",
            "Free reference sampler for teaching sampler fundamentals",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("Instrudio", "https://github.com/GareBear99/Instrudio"),
            ("RiftWave Suite", "https://github.com/GareBear99/RiftWaveSuite_RiftSynth_WaveForm_Lite"),
        ],
    },
    {
        "slug": "vf-plexlab",
        "name": "VF-PlexLab",
        "repo": "VF-PlexLab",
        "category": "Experimental",
        "role": "VocalForge PersonaPlex Lab",
        "status": "Dev",
        "formats": ["VST3", "AU"],
        "tagline": "A GitHub-ready starter repo for building a JUCE plugin + local backend + HTML tester around NVIDIA PersonaPlex, focused on voice-conditioned vocal asset generation.",
        "overview": (
            "VF-PlexLab (VocalForge PersonaPlex Lab) is a structured starter project for "
            "building a JUCE plugin, a Python backend, and an HTML tester around NVIDIA "
            "PersonaPlex. The stated focus is voice-conditioned vocal asset generation — "
            "spoken hooks, whispers, chants, robotic/system phrases, and sample-pack export.\n\n"
            "The project is split intentionally into three layers (plugin, backend, tester) so "
            "that each can be iterated, debugged, and deployed independently. PersonaPlex "
            "itself is tracked as a separate dependency so the project can track upstream or a "
            "local fork."
        ),
        "features": [
            "JUCE plugin frame for DAW-side control, auditioning, and export",
            "Python backend bridge for queued jobs, health checks, and filesystem outputs",
            "HTML tester for fast iteration outside the DAW",
            "PersonaPlex dependency layer tracked separately",
            "Sample-pack export pipeline for generated voice assets",
        ],
        "workflows": [
            "Generating spoken hooks and chants for sample packs",
            "Prototyping voice-conditioned pipelines before DAW integration",
            "Research / educational exploration of PersonaPlex-style systems",
        ],
        "compat": "macOS (Intel + Apple Silicon), Windows 10+ (plugin layer); Python 3 backend",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("PAP Forge", "https://github.com/GareBear99/PAP-Forge-Audio"),
            ("NVIDIA PersonaPlex", "https://github.com/NVIDIA/personaplex"),
        ],
    },
    {
        "slug": "pap-forge-audio",
        "name": "PAP-Forge-Audio",
        "repo": "PAP-Forge-Audio",
        "category": "Experimental",
        "role": "Procedural Autonomous Plugins runtime",
        "status": "Dev",
        "formats": ["CLI", "VST3 (export)", "AU (export)"],
        "tagline": "A governed runtime for generating, checkpointing, branching, validating, and restoring plugin projects from natural-language sound intent.",
        "overview": (
            "PAP Forge (PAP = Procedural Autonomous Plugins) is a runtime and reproducible "
            "build-state system for generating plugin projects from natural-language intent. "
            "Every state of a plugin project — parameters, routing, DSP scaffolding — is "
            "expressed as a single canonical JSON that can be copied, saved, reapplied, and "
            "rebuilt.\n\n"
            "The runtime manages project initialization, specification inference from "
            "prompts, routing between effect and synth scaffolds, checkpointing, branching, "
            "validation, and preview export."
        ),
        "features": [
            "Initializes PAP plugin projects from natural-language prompts",
            "Infers plugin specifications from prompts and routes them into scaffolds",
            "Canonical JSON build state for reproducible rebuilds",
            "Checkpoint / branch / mutate / preview workflow",
            "Validation stage before release or export",
        ],
        "workflows": [
            "Rapid plugin prototyping driven by written sound intent",
            "Research into governed AI-assisted plugin authorship",
            "Reproducible science: regenerating a plugin state from a JSON file",
        ],
        "compat": "macOS / Linux CLI; plugin export targets VST3 / AU",
        "related": [
            ("TizWildin HUB", HUB_URL),
            ("VF-PlexLab", "https://github.com/GareBear99/VF-PlexLab"),
            ("ARC-Core", "https://github.com/GareBear99/ARC-Core"),
        ],
    },
]

STATUS_BADGE = {
    "Production": "\u2705 Production",
    "Beta":       "\u26a0\ufe0f Beta",
    "Dev":        "\U0001f6a7 Dev",
}


def page_for(plugin: dict) -> str:
    name = plugin["name"]
    slug = plugin["slug"]
    repo = plugin["repo"]
    repo_url = f"https://github.com/GareBear99/{repo}"
    raw_latest = f"{repo_url}/releases/latest"
    category = plugin["category"]
    role = plugin["role"]
    status = STATUS_BADGE[plugin["status"]]
    formats = " \u00b7 ".join(plugin["formats"])
    tagline = plugin["tagline"]
    overview = plugin["overview"]

    features = "\n".join(f"- {f}" for f in plugin["features"])
    internals = plugin.get("internals")
    internals_md = ""
    if internals:
        internals_md = "## Architecture & internals\n" + "\n".join(f"- {f}" for f in internals) + "\n\n"

    workflows = "\n".join(f"- {f}" for f in plugin["workflows"])
    compat = plugin["compat"]
    related = "\n".join(f"- [{label}]({url})" for label, url in plugin["related"])

    return f"""# {name}

![{name} demo card](assets/{slug}.png)

> **TizWildin Entertainment HUB \u2014 {category}**
> **Role:** {role}
> **Status:** {status}
> **Formats:** {formats}
> **License:** FREE (open source)

## Tagline
{tagline}

## Overview
{overview}

## Core features
{features}

{internals_md}## Typical workflows
{workflows}

## Compatibility
{compat}

## Source & downloads
- **Repo / source:** [{repo_url}]({repo_url})
- **Latest release:** [{raw_latest}]({raw_latest})
- **HUB dashboard:** [{DASHBOARD_URL}]({DASHBOARD_URL})
- **HUB repo:** [{HUB_URL}]({HUB_URL})

## Related projects
{related}

---

_This page is part of the Awesome Audio Plugins & Dev link-page set. It is the human-readable landing spot for **{name}** inside the TizWildin Entertainment HUB ecosystem._
"""


def write_all() -> None:
    for p in PLUGINS:
        (LINK_DIR / f"{p['slug']}.md").write_text(page_for(p), encoding="utf-8")
    # Duplicate FreeEQ8 page used from the Equalizers section.
    eq_page = page_for(PLUGINS[0]).replace(
        "TizWildin Entertainment HUB \u2014 Flagship",
        "TizWildin Entertainment HUB \u2014 Flagship \u00b7 Equalizers",
    )
    (LINK_DIR / "freeeq8-2.md").write_text(eq_page, encoding="utf-8")
    print(f"wrote {len(PLUGINS) + 1} pages to {LINK_DIR}")


if __name__ == "__main__":
    write_all()
