# Step-by-step cheat sheet (for a beginner - every command explained)

## Step 4: generate one line with ElevenLabs (Python)
# 1. pip install elevenlabs
# 2. export ELEVENLABS_API_KEY="your key"   <- the key is like a password, keep it secret
# 3. Run the script below for each line in scene_ep01.yml

from elevenlabs import ElevenLabs
import yaml  # pip install pyyaml

client = ElevenLabs()
scene = yaml.safe_load(open("script/scene_ep01.yml"))

for line in scene["lines"]:
    char = scene["characters"][line["speaker"]]
    audio = client.text_to_speech.convert(
        voice_id=char["voice"],
        text=line["text"],
        model_id="eleven_multilingual_v2",
        voice_settings={"stability": 0.5, "similarity_boost": 0.75},
    )
    with open(f"episodes/ep01/stems/{line['speaker']}_take1.mp3", "wb") as f:
        for chunk in audio:
            f.write(chunk)

## Step 8: master to -16 LUFS with ffmpeg (free tool, no FL Studio needed for this part)
# ffmpeg -i mix.wav -af loudnorm=I=-16:TP=-1.5:LRA=11 masters/ep01_india_master.wav
# I=-16  -> loudness target (podcast/mobile streaming standard)
# TP=-1.5 -> true peak, stops distortion on phone speakers
