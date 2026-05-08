# game/routes/ending_B.rpy
# ============================================================
# THE LAST TRAIN HOME - ENDING B: "Stay Behind"
# ============================================================
# Acceptance/Growth Ending
#
# The player chooses to stay on the platform, not boarding the train.
# This represents acceptance of one's circumstances, choosing reflection
# over escape, and the wisdom that sometimes stillness is the answer.
#
# REQUIREMENTS:
#   - Any empathy level (affects interpretation)
#   - Must choose "Stay on the platform"
#
# THEMES:
#   - Acceptance and surrender
#   - Finding peace in place
#   - Growth through stillness
#   - Internal vs external change
# ============================================================

label ending_stay_behind:
    $ change_scene("ending_b")

    scene bg station_empty with fade
    stop music fadeout AUDIO_FADE_OUT_SPEED

    pause TEXT_PAUSE_MEDIUM

    "You hesitate."
    pause TEXT_PAUSE_SHORT
    "The doors close."
    pause TEXT_PAUSE_SHORT
    "The train leaves without you."
    pause TEXT_PAUSE_LONG

    "The station becomes silent again."
    pause TEXT_PAUSE_MEDIUM

    # ========================================================
    # ENDING VARIATION - Based on empathy level & reflection
    # ========================================================

    if empathy >= EMPATHY_THRESHOLD_HIGH:
        # High empathy: Conscious, enlightened choice
        "You're still here. But something shifted."
        pause TEXT_PAUSE_SHORT

        "The weight isn't crushing anymore. It's just... present."
        pause TEXT_PAUSE_MEDIUM

        thought "I don't have to run. The truth was always on the platform with me."

        pause TEXT_PAUSE_SHORT

        "You look at the bench where the stranger sat. It's empty now."
        pause TEXT_PAUSE_SHORT

        "Maybe they were never really there. Or maybe they're still here—"
        "in the quiet moments you finally let yourself feel."
        pause TEXT_PAUSE_LONG

        play music "audio/ending_ambiguous.ogg" fadein AUDIO_FADE_IN_SPEED volume AUDIO_BGM_VOLUME

        "Tomorrow, you might board a train. Or maybe you'll just sit. "
        pause TEXT_PAUSE_SHORT
        "Both are okay. Both are choices."
        pause TEXT_PAUSE_MEDIUM

        "You sit on the bench and breathe with the station."
        pause TEXT_PAUSE_SHORT
        "And for the first time, you're not waiting for something to happen."
        pause TEXT_PAUSE_SHORT
        "You're just... here."

    elif has_reflected:
        # Medium empathy: Thoughtful acceptance
        "You're still here. The weight is still here too."
        pause TEXT_PAUSE_SHORT

        "But something changed. The weight isn't dragging you down anymore."
        pause TEXT_PAUSE_MEDIUM

        "It's part of you. And accepting that..."
        pause TEXT_PAUSE_SHORT

        play music "audio/ending_ambiguous.ogg" fadein AUDIO_FADE_IN_SPEED volume AUDIO_BGM_VOLUME

        "...that makes it lighter."
        pause TEXT_PAUSE_LONG

        "You sit on the bench. The bench is still warm."
        pause TEXT_PAUSE_SHORT
        "The lights still hum. You're still breathing."
        pause TEXT_PAUSE_MEDIUM

        "Sometimes that's enough."

    else:
        # Low empathy: Uncertain, but present
        "Nothing has changed."
        pause TEXT_PAUSE_SHORT
        "The station is still empty. The bench is still cold."
        pause TEXT_PAUSE_LONG

        "But you're here. You made a choice. You stayed."
        pause TEXT_PAUSE_SHORT

        play music "audio/ending_ambiguous.ogg" fadein AUDIO_FADE_IN_SPEED volume AUDIO_BGM_VOLUME

        thought "Maybe that's what matters. Not the reasons. Just the fact that I stayed."

        pause TEXT_PAUSE_MEDIUM

        "You sit and wait for the next train, or maybe just for dawn."
        pause TEXT_PAUSE_SHORT
        "The uncertainty is still there. But so are you."

    pause TEXT_PAUSE_LONG

    # ========================================================
    # CLOSING NARRATION
    # ========================================================

    "The station ticks. Seconds pass. Hours maybe."
    pause TEXT_PAUSE_SHORT
    "Outside, the city never stops. But here, in this small space between platforms..."
    pause TEXT_PAUSE_MEDIUM

    "There's quiet. And in that quiet, something grows."
    pause TEXT_PAUSE_LONG

    scene black with fade

    pause TEXT_PAUSE_LONG

    "{color=#ffffff}END - THE LAST TRAIN HOME{/color}"
    "{color=#8ab4f8}Ending B: Stay Behind{/color}"

    pause TEXT_PAUSE_LONG

    jump end_game
