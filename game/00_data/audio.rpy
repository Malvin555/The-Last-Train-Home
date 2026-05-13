# game/00_data/audio.rpy
# ============================================================
# AUDIO DEFINITIONS
# ============================================================
# This file centralizes all audio paths.
# By defining audio variables here, you don't need to type the full path
# every time. If you ever move a file, you only need to change it here.
#
# FILE PLACEMENT:
# Put your actual audio files (like .ogg, .mp3, .wav) inside the `game/audio/` directory.

init -1:
    # MUSIC (Background Music - BGM)
    # Usage example: play music bgm_station fadein 2.0
    # To stop: stop music fadeout 1.5
    define bgm_station = "audio/station_ambience.ogg"
    define bgm_ending_hopeful = "audio/ending_hopeful.ogg"
    define bgm_ending_ambiguous = "audio/ending_ambiguous.ogg"
    define bgm_ending_revelation = "audio/ending_revelation.ogg"

    # SOUND EFFECTS (SFX)
    # Usage example: play sound sfx_train_approach
    # With fade: play sound sfx_train_loud fadein 0.5
    define sfx_train_approach = "audio/train_approach.ogg"
    define sfx_train_loud = "audio/train_approach_loud.ogg"
