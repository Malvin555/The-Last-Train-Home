# script.rpy
# Main entry point for "The Last Train Home"
# Handles initialization, audio setup, and routes to the first scene.
# Keeps logic minimal. All characters, variables, and story flow live in modular files.

# CTC Animation (Click-to-Continue)
image ctc:
    align (0.82, 0.90)
    "gui/ctc.png"
    subpixel True
    easein 1.0 ypos 0.89
    pause 0.4
    easein 1.0 ypos 0.90
    pause 0.4
    repeat

# NOTE: 
# - Character definitions → system/characters.rpy
# - Default variables    → system/variables.rpy
# - Story flow           → scenes/ & routes/

label start:
    $ quick_menu = True

    # Fade from black
    scene black with fade

    # Start ambient audio (replace with your actual BGM file)
    play music "audio/station_ambience.ogg" fadein 2.0 volume 0.6

    # Route to the modular prologue
    jump prologue


label end_game:
    stop music fadeout 2.0
    scene black with fade
    $ renpy.pause(2)
    return