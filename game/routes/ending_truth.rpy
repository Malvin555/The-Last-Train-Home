# game/routes/03_ending_truth.rpy
# ENDING C: "The Truth"
# The player asks the stranger's identity.
# Represents: Revelation, connection, transcendence
# Tone: Mystical, intimate, transformative

label ending_truth:
    scene black with fade
    stop music fadeout 1.5
    pause 1.0

    scene bg station_train with fade
    play music "audio/ending_revelation.ogg" fadein 2.0 volume 0.8

    narrator "Time seems to slow."
    pause 1.0

    narrator "You hear yourself ask the question you've been holding since the moment you saw them."
    pause 1.5

    # ============================================================
    # THE ASKING
    # ============================================================

    p "Who are you?"
    pause 2.0

    narrator "The station falls silent."
    narrator "Even the train seems to pause."
    pause 1.5

    show stranger neutral at center with dissolve

    s "That's the question, isn't it?"
    pause 1.0
    s "Who am I?"
    pause 1.5

    # ============================================================
    # THE REVELATION - Multiple layers of truth
    # ============================================================

    if affinity_stranger >= AFFECTION_HIGH:
        s "I'm what you've been searching for."
        pause 1.0
        s "Not a person. Not a guide."
        pause 0.5
        s "I'm the part of you that already knows the answers."

        narrator "The stranger's features shimmer slightly. Or maybe the station does."
        narrator "It's hard to tell which is real and which is reflection."

        pause 1.5

        s "I'm the conversation you've been trying to have with yourself for years."
        pause 1.0
        s "And now we've finally had it."

        pause 2.0

    elif affinity_stranger >= AFFECTION_MEDIUM:
        s "I'm someone who's been waiting."
        pause 1.0
        s "For a long time. At many stations."
        pause 0.5
        s "Waiting for people like you. People who still ask questions."

        narrator "Their form seems to become less distinct. More ethereal."

        pause 1.5

        s "I'm the voice that echoes in empty places."
        s "The presence that reminds you: you're not alone."
        pause 1.0
        s "Even when you feel like you are."

        pause 1.5

    else:
        s "I'm what you see when you finally look in the mirror."
        pause 1.0
        s "All the potential you've been ignoring."
        pause 0.5
        s "All the strength you forgot you had."

        pause 1.5

        s "I've always been here."
        s "You're only now learning to see me."

        pause 1.5

    # ============================================================
    # THE DEEPER TRUTH
    # ============================================================

    s "Do you want to know the real answer?"
    pause 1.5
    s "I'm what you will become if you have the courage to be honest."
    pause 1.0
    s "If you choose vulnerability over armor."
    pause 0.5
    s "If you choose growth over comfort."

    pause 2.0

    # ============================================================
    # THE TRANSFORMATION
    # ============================================================

    narrator "Something shifts."
    narrator "The stranger's boundaries blur with the station."
    narrator "The station blurs with the night."
    narrator "And you—you blur with all of it."

    pause 2.0

    narrator "For a moment, there is no distinction."
    narrator "No self and other. No stranger and known."
    narrator "Just understanding. Pure and complete."

    pause 2.0

    if vulnerability_shown:
        narrator "You see every moment you were brave."
        narrator "Every time you let someone see you. Really see you."
        narrator "And you understand: that was the whole point."
        pause 1.5

    elif has_reflected:
        narrator "You see the journey you've been on."
        narrator "Every question you asked yourself. Every moment of doubt."
        narrator "And you realize: the stranger was always there—inside you."
        pause 1.5

    else:
        narrator "You see yourself."
        narrator "Not as you are now, but as you're becoming."
        narrator "A version of you that's brave. That's whole."
        pause 1.5

    # ============================================================
    # RETURN TO CLARITY
    # ============================================================

    scene bg station_train with dissolve
    pause 1.0

    narrator "The station sharpens into focus."
    narrator "You're standing on the platform."
    narrator "The train waits. The doors are still open."

    pause 1.5

    show stranger neutral at center with dissolve

    s "Now do you understand?"
    pause 1.0

    s "The last train isn't about leaving or staying."
    s "It's about becoming."

    pause 1.5

    if affinity_stranger >= AFFECTION_HIGH:
        s "And you've already begun."
        pause 1.0
        s "So board, or stay. It doesn't matter."
        pause 0.5
        s "You're not running anymore. You're choosing."

        p "Thank you."
        pause 0.5
        s "Thank yourself. I'm just a mirror."

    else:
        s "The only question now is: what will you do with that knowledge?"
        pause 1.5

        p "I... I don't know."
        pause 1.0
        s "Then you're exactly where you need to be."

    pause 2.0

    # ============================================================
    # THE CHOICE REMAINS
    # ============================================================

    narrator "The train waits."
    narrator "The platform remains."
    narrator "And you—you are finally, completely whole."

    pause 1.0

    narrator "Not because all your problems are solved."
    narrator "But because you understand them now. You accept them."

    pause 1.5

    narrator "And that is its own kind of boarding."
    narrator "Its own kind of journey."

    pause 2.0

    # ============================================================
    # FINAL IMAGE: TRANSCENDENCE
    # ============================================================

    scene black with dissolve
    pause 1.0

    narrator "The station dissolves into white."
    narrator "Light without source. Understanding without words."

    pause 2.0

    narrator "And when the light fades..."
    pause 1.0

    narrator "You are finally home."

    pause 2.0

    scene black with fade
    pause 1.0

    centered "THE END"
    pause 1.0

    centered "You were always home."
    pause 1.0

    centered "You just needed to remember."
    pause 3.0

    return
