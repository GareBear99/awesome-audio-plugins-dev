# VF-PlexLab

![VF-PlexLab demo card](assets/vf-plexlab.png)

> **TizWildin Entertainment HUB — Experimental**
> **Role:** VocalForge PersonaPlex Lab
> **Status:** 🚧 Dev
> **Formats:** VST3 · AU
> **License:** FREE (open source)

## Tagline
A GitHub-ready starter repo for building a JUCE plugin + local backend + HTML tester around NVIDIA PersonaPlex, focused on voice-conditioned vocal asset generation.

## Overview
VF-PlexLab (VocalForge PersonaPlex Lab) is a structured starter project for building a JUCE plugin, a Python backend, and an HTML tester around NVIDIA PersonaPlex. The stated focus is voice-conditioned vocal asset generation — spoken hooks, whispers, chants, robotic/system phrases, and sample-pack export.

The project is split intentionally into three layers (plugin, backend, tester) so that each can be iterated, debugged, and deployed independently. PersonaPlex itself is tracked as a separate dependency so the project can track upstream or a local fork.

## Core features
- JUCE plugin frame for DAW-side control, auditioning, and export
- Python backend bridge for queued jobs, health checks, and filesystem outputs
- HTML tester for fast iteration outside the DAW
- PersonaPlex dependency layer tracked separately
- Sample-pack export pipeline for generated voice assets

## Typical workflows
- Generating spoken hooks and chants for sample packs
- Prototyping voice-conditioned pipelines before DAW integration
- Research / educational exploration of PersonaPlex-style systems

## Compatibility
macOS (Intel + Apple Silicon), Windows 10+ (plugin layer); Python 3 backend

## Source & downloads
- **Repo / source:** [https://github.com/GareBear99/VF-PlexLab](https://github.com/GareBear99/VF-PlexLab)
- **Latest release:** [https://github.com/GareBear99/VF-PlexLab/releases/latest](https://github.com/GareBear99/VF-PlexLab/releases/latest)
- **HUB dashboard:** [https://garebear99.github.io/TizWildinEntertainmentHUB/](https://garebear99.github.io/TizWildinEntertainmentHUB/)
- **HUB repo:** [https://github.com/GareBear99/TizWildinEntertainmentHUB](https://github.com/GareBear99/TizWildinEntertainmentHUB)

## Related projects
- [TizWildin HUB](https://github.com/GareBear99/TizWildinEntertainmentHUB)
- [PAP Forge](https://github.com/GareBear99/PAP-Forge-Audio)
- [NVIDIA PersonaPlex](https://github.com/NVIDIA/personaplex)

---

_This page is part of the Awesome Audio Plugins & Dev link-page set. It is the human-readable landing spot for **VF-PlexLab** inside the TizWildin Entertainment HUB ecosystem._
