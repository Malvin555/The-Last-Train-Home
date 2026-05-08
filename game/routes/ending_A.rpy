# game/routes/ending_A.rpy
# ============================================================
# THE LAST TRAIN HOME - ENDING A: "Move Forward"
# ============================================================
# Romantic/Connected Ending
#
# The player boards the train, leaving the platform behind.
# This represents acceptance and the choice to move forward,
# carrying their pain and growth with them.
#
# REQUIREMENTS:
#   - Any empathy level (affects the tone of reflection)
#   - Must choose "Board the train"
#
# THEMES:
#   - Movement and change
#   - Letting go and moving on
#   - Hope tempered with reality
# ============================================================

label ending_move_forward:
    $ change_scene("ending_a")

    scene bg train_interior with fade
    stop music fadeout AUDIO_FADE_OUT_SPEED

    pause TEXT_PAUSE_MEDIUM

    "The doors close behind you."
    pause TEXT_PAUSE_SHORT
    "The stranger is gone."
    pause TEXT_PAUSE_LONG

    "The train begins to move."
    pause TEXT_PAUSE_SHORT

    # ========================================================
    # ENDING VARIATION - Based on empathy level
    # ========================================================

    if empathy >= EMPATHY_THRESHOLD_HIGH:
        # High empathy: Deep understanding reached
        "You understand now. The train was never about distance."
        pause TEXT_PAUSE_SHORT
        "It was about letting go."
        pause TEXT_PAUSE_MEDIUM

        "You realize the stranger wasn't guiding you somewhere new—"
        "they were helping you understand what you already knew."
        pause TEXT_PAUSE_SHORT

        thought "The version of myself that was ready to move forward was waiting. It was always waiting."
        pause TEXT_PAUSE_LONG

        "You finally feel light. Not because the past disappeared,"
        "but because you chose to carry it differently."
        pause TEXT_PAUSE_MEDIUM

        play music "audio/ending_hopeful.ogg" fadein AUDIO_FADE_IN_SPEED volume AUDIO_BGM_VOLUME

        "The tracks hum beneath you, carrying you forward."
        pause TEXT_PAUSE_SHORT
        "You lean back against the seat and breathe."
        pause TEXT_PAUSE_LONG

        "It's not a clean break. But it's a start."
        pause TEXT_PAUSE_SHORT
        "And for the first time in a long time, that feels enough."

    elif regret_accepted:
        # Medium empathy: Acknowledged regret
        "The seats are empty around you."
        pause TEXT_PAUSE_SHORT
        "You lean back, breathing out a breath you didn't know you were holding."
        pause TEXT_PAUSE_LONG

        "Moving forward doesn't mean forgetting. It means making room."
        pause TEXT_PAUSE_SHORT
        "For the past. For the future. For yourself."
        pause TEXT_PAUSE_MEDIUM

        play music "audio/ending_hopeful.ogg" fadein AUDIO_FADE_IN_SPEED volume AUDIO_BGM_VOLUME

        "The train carries you through the night."
        pause TEXT_PAUSE_SHORT
        "And this time, the darkness doesn't feel like an ending."
        pause TEXT_PAUSE_MEDIUM

        "It feels like the space between what was and what could be."

    else:
        # Low empathy: Uncertain but moving
        "The train pulls away from the platform."
        pause TEXT_PAUSE_SHORT
        "You watch the station shrink behind the glass—the bench, the lights, the stranger."
        pause TEXT_PAUSE_LONG

        "It's not a clean break. Maybe there's no such thing."
        pause TEXT_PAUSE_SHORT

        thought "Maybe the point isn't to break. Maybe it's to choose."

        play music "audio/ending_hopeful.ogg" fadein AUDIO_FADE_IN_SPEED volume AUDIO_BGM_VOLUME

        pause TEXT_PAUSE_LONG

        "You made a choice. You're on the train."
        pause TEXT_PAUSE_SHORT
        "That has to be enough."

    pause TEXT_PAUSE_LONG

    # ========================================================
    # CLOSING NARRATION
    # ========================================================

    "The lights of the city blur past. Then trees. Then darkness and stars."
    pause TEXT_PAUSE_MEDIUM
    "The train carries you forward into whatever comes next."
    pause TEXT_PAUSE_LONG

    scene black with fade

    pause TEXT_PAUSE_LONG

    "{color=#ffffff}END - THE LAST TRAIN HOME{/color}"
    "{color=#8ab4f8}Ending A: Move Forward{/color}"

    pause TEXT_PAUSE_LONG

    jump end_game
