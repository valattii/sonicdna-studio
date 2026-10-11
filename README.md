# SonicDNA Studio
Built in 24 hours for the Pocket FM Sound Architect application.

## Why this project exists (read this first)
Pocket FM needs people who can keep a character's voice consistent across
hundreds of episodes, ship fast with AI, and mix for mobile listeners.
This repo is a small working version of that system, with one episode
("The Last Frequency", Scene 1) pushed through it end-to-end.

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

## Today's checklist
- [ ] 1. Read script/scene_ep01.yml - understand the format
- [ ] 2. Create the 2 character voices in ElevenLabs Voice Designer
- [ ] 3. Save voice IDs into dna_cards/*.json and into the YAML
- [ ] 4. Generate every line, listen, re-generate the weak ones
- [ ] 5. Consistency check: does Signal sound like the SAME person in all 6 lines?
- [ ] 6. Generate a tense music bed (Suno, instrumental) + SFX list
- [ ] 7. Assemble in FL Studio: dialogue loud, music quiet underneath
- [ ] 8. Master: ~-16 LUFS, then LISTEN ON YOUR PHONE SPEAKER
- [ ] 9. Render the US and Europe vibe versions (score/mix changes only)
- [ ] 10. Record a 2-min Loom walkthrough -> apply
