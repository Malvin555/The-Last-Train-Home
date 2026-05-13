# game/routes/ending_C.rpy
# ============================================================
# THE LAST TRAIN HOME - ENDING C: "The Truth"
# ============================================================
# Revelation/Transcendent Ending
#
# The player asks "Who are you?" - the deepest question.
# The stranger reveals themselves as a reflection—the version of the
# player that already understood the answer. This is the "true" ending,
# unlocked only through maximum empathy.
#
# REQUIREMENTS:
#   - Empathy >= CHOICE_EMPATHY_GATE (3)
#   - Must ask: "Who are you?"
#   - This choice is only available to players who've built enough connection
#
# THEMES:
#   - Self-discovery and self-recognition
#   - The stranger as internal reflection
#   - Transcendence of fear through understanding
#   - Integration of shadow-self
# ============================================================

label ending_truth:
    $ change_scene("ending_c")

    scene bg station_light with fade
    stop music fadeout AUDIO_FADE_OUT_SPEED

    pause TEXT_PAUSE_LONG

    show malvin surprised at left with dissolve

    "You step forward and ask the question that matters most:"
    pause TEXT_PAUSE_SHORT

    p "Who are you?"

    pause TEXT_PAUSE_LONG

    # ========================================================
    # THE REVEAL - The Stranger's True Nature
    # ========================================================

    show stranger contemplative at right with dissolve

    s "I'm what you avoid every night before sleep."
    pause TEXT_PAUSE_MEDIUM

    s "I'm the moment before you make a choice. I'm the part of you that already knows the answer."
    pause TEXT_PAUSE_LONG

    "The lights on the platform flicker."
    pause TEXT_PAUSE_SHORT

    "Then they brighten."

    pause TEXT_PAUSE_LONG

    # ========================================================
    # ENDING VARIATION - Based on deeper reflection
    # ========================================================

    if empathy >= EMPATHY_THRESHOLD_HIGH and has_reflected:
        # Full enlightenment: Player fully integrated the truth
        "The platform begins to dissolve into soft white light."
        scene white with Dissolve(4.0)
        pause TEXT_PAUSE_MEDIUM

        show malvin contemplative
        "You understand now. The stranger isn't a guide. They're a mirror."
        pause TEXT_PAUSE_SHORT
        "Not to show you someone else, but to show you yourself."
        pause TEXT_PAUSE_LONG

        "The version of you that moved on was waiting. Not to replace you."
        pause TEXT_PAUSE_SHORT
        "To walk beside you."
        pause TEXT_PAUSE_MEDIUM

        thoughts "I didn't meet a stranger. I finally listened to myself."

        pause TEXT_PAUSE_LONG

        "The stranger steps toward the train."
        pause TEXT_PAUSE_SHORT

        show stranger smile
        s "You don't have to follow me. But I'm not going anywhere you don't want to go."
        pause TEXT_PAUSE_MEDIUM

        "They extend their hand."
        pause TEXT_PAUSE_MEDIUM

        show malvin happy
        p "Come with me. Both of us. The one I was and the one I'm becoming."

        pause TEXT_PAUSE_SHORT

        s "Yes. That's exactly right."

        play music bgm_ending_revelation fadein AUDIO_FADE_IN_SPEED volume AUDIO_BGM_VOLUME

        pause TEXT_PAUSE_LONG

        "As their hand touches yours, everything becomes light."
        pause TEXT_PAUSE_SHORT
        "Not white. Not darkness. Just... understanding."
        pause TEXT_PAUSE_LONG

        "You step onto the train together—but you realize you're not leaving anything behind."
        pause TEXT_PAUSE_SHORT
        "You're bringing it all with you. And that's okay."

    elif has_reflected:
        # Partial enlightenment: Player understands but hesitates
        "The platform dissolves slowly."
        scene white with Dissolve(4.0)
        pause TEXT_PAUSE_SHORT
        "The stranger becomes less distinct. Less 'them' and more... you."
        pause TEXT_PAUSE_LONG

        "Recognition hits like a quiet wave."
        pause TEXT_PAUSE_SHORT

        show malvin contemplative
        thoughts "It was always me. The part that was ready. The part that could heal."

        pause TEXT_PAUSE_MEDIUM

        play music bgm_ending_revelation fadein AUDIO_FADE_IN_SPEED volume AUDIO_BGM_VOLUME

        "The train doors open again. One last time."
        pause TEXT_PAUSE_MEDIUM

        show stranger neutral
        s "You don't have to board. But you know you can."
        pause TEXT_PAUSE_SHORT
        s "That's the point. You know you can. And that changes everything."

        pause TEXT_PAUSE_LONG

        "You step forward. Toward the train. Toward yourself."
        pause TEXT_PAUSE_MEDIUM

        "The platform goes white."
        scene white with Dissolve(3.0)

    else:
        # Minimum enlightenment: Confrontation with possibility
        "The light is too bright. You want to close your eyes."
        pause TEXT_PAUSE_SHORT

        "But you don't."
        pause TEXT_PAUSE_LONG

        show malvin angry
        thoughts "This is what I've been avoiding. Not the stranger. Myself."

        pause TEXT_PAUSE_MEDIUM

        play music bgm_ending_revelation fadein AUDIO_FADE_IN_SPEED volume AUDIO_BGM_VOLUME

        "The stranger's face changes. Becomes... more familiar."
        pause TEXT_PAUSE_SHORT

        show stranger neutral
        s "I'm not here to convince you. I'm here because you called. And you're here because part of you answered."

        pause TEXT_PAUSE_LONG

        "The train and the platform and the stranger all shimmer."
        pause TEXT_PAUSE_SHORT

        "And you realize: they're all the same thing. Projections. Waiting."
        pause TEXT_PAUSE_MEDIUM

        "Waiting for you to choose."

        pause TEXT_PAUSE_LONG

        "You step toward the light."
        pause TEXT_PAUSE_SHORT
        "Not because you're sure."
        pause TEXT_PAUSE_SHORT
        "But because you're ready to find out."
        scene white with Dissolve(3.0)

    pause TEXT_PAUSE_LONG

    # ========================================================
    # CLOSING NARRATION - The Transcendence
    # ========================================================

    scene white with Dissolve(5.0)

    pause TEXT_PAUSE_LONG

    "Everything goes white."
    pause TEXT_PAUSE_LONG

    "When it clears, you're standing on a train platform that looks exactly like the one you left."
    pause TEXT_PAUSE_SHORT

    "But nothing is the same."
    pause TEXT_PAUSE_SHORT

    "The stranger is gone."
    pause TEXT_PAUSE_SHORT
    "Or maybe you finally understand—they never left."
    pause TEXT_PAUSE_SHORT
    "You were just ready to see it."

    pause TEXT_PAUSE_LONG

    centered "{color=#ffffff}END - THE LAST TRAIN HOME{/color}"
    centered "{color=#8ab4f8}Ending C: The Truth{/color}"
    centered "{color=#d4a574}You finally saw yourself.{/color}"

    pause TEXT_PAUSE_LONG

    jump end_game
