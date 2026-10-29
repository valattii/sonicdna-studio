# SonicDNA Studio
Built in 24 hours for the Pocket FM Sound Architect application.

## Why this project exists (read this first)
Pocket FM needs people who can keep a character's voice consistent across
hundreds of episodes, ship fast with AI, and mix for mobile listeners.
This repo is a small working version of that system, with one episode
("The Last Frequency", Scene 1) pushed through it end-to-end.

## Project structure

- `script/scene_ep01.yml` — dialogue and speaker instructions.
- `dna_cards/*.json` — voice IDs and generation settings.
- `pipeline/generate_dialogue.py` — calls ElevenLabs and saves each dialogue line.
- `pipeline/consistency_gate.py` — compares speaker embeddings and writes a JSON report.
- `pipeline/master.py` — optional FFmpeg loudness normalization for a WAV mix exported from a DAW.
- `episodes/` — generated output; excluded from Git.

## The pipeline (what happens to one line of dialogue)
script (scene YAML) -> ElevenLabs TTS (voice locked per character)
-> consistency check (same voice every line) -> FL Studio mix
(Suno music + SFX) -> master at -16 LUFS for mobile -> done.

## Folder guide
- script/          the recipe (scene graph). Edit text here, re-render.
- dna_cards/       each character's voice settings = their "sonic DNA"
- pipeline/        scripts that do the boring work so you can be creative
- episodes/ep01/   stems (raw pieces) and masters (finished audio)
- dashboard/       numbers about your pipeline (loudness, consistency)


