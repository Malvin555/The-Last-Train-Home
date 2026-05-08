# game/routes/02_ending_stay_behind.rpy
# ENDING B: "Stay Behind"
# The player chooses not to board the train.
# Represents: Acceptance, stillness, peace with uncertainty
# Tone: Contemplative, bittersweet, introspective

label ending_stay_behind:
    scene black with fade
    stop music fadeout 1.5
    pause 1.0

    scene bg station_empty with fade
    play music "audio/ending_acceptance.ogg" fadein 2.0 volume MUSIC_VOLUME_DEFAULT

    narrator "You don't move."
    narrator "The doors slide open. They slide closed."
    pause 1.5

    narrator "The train pulls away."
    narrator "And you stay."
    pause 2.0

    # ============================================================
    # THE STRANGER'S REACTION
    # ============================================================

    show stranger neutral at center with dissolve

    if affinity_stranger >= AFFECTION_HIGH:
        s "I thought you might stay."
        pause 1.0
        s "Not because you're afraid to leave."
        s "But because you're curious about what staying means."
        pause 1.5

        p "Does it matter? It's done now."
        pause 1.0

        s "Maybe. Or maybe this is just the beginning."
        pause 0.5
        s "Staying can be the bravest choice of all."

    elif affinity_stranger >= AFFECTION_MEDIUM:
        s "You stayed."
        pause 1.5
        s "That takes courage, you know. In a different way than leaving does."
        pause 1.0

        p "Does it?"
        pause 0.5
        s "Most people think the only way to find yourself is to run."
        s "But sometimes you have to plant roots to grow."

    else:
        s "You're still here."
        pause 2.0
        s "The night keeps everyone, in the end."
        pause 1.0
        s "But what matters is how you spend it."

    pause 1.5

    # ============================================================
    # THE PLATFORM TRANSFORMS
    # ============================================================

    scene bg station_quiet with dissolve
    pause 1.0

    narrator "The station is quiet again."
    narrator "But it's a different quiet than before."
    pause 1.5

    narrator "It's not empty. It's peaceful."
    pause 1.0

    # ============================================================
    # REFLECTION ON CHOICE
    # ============================================================

    if has_reflected:
        narrator "You stand on the platform—the same one where you arrived."
        narrator "But you're not the same person."
        pause 1.0

        narrator "The night has changed you. The stranger has changed you."
        pause 1.5

        narrator "You realize: growth isn't always about going forward."
        narrator "Sometimes it's about standing still and finally understanding where you are."

    elif vulnerability_shown:
        narrator "You feel lighter than you did an hour ago."
        narrator "Not because the weight is gone, but because you set it down for a moment."
        narrator "And it felt good."
        pause 1.5

        narrator "You know it will be waiting for you in the morning. But right now, you get to rest."

    else:
        narrator "You're still uncertain. Maybe more so than before."
        narrator "But the uncertainty feels different now."
        narrator "Less like drowning. More like floating."
        pause 1.5

        narrator "It's not comfort. But it's something."

    pause 2.0

    # ============================================================
    # THE STRANGER'S FAREWELL
    # ============================================================

    show stranger neutral at left with dissolve

    if affinity_stranger >= AFFECTION_HIGH:
        s "Will you stay a little longer?"
        p "I... yes. I think I will."
        pause 1.0

        s "Good. I'd like that."
        pause 0.5
        s "Not because we have anything left to say."
        s "But because sometimes the best conversations are the quiet ones."

        narrator "And so you do. You stay."
        narrator "Not forever. But for tonight, you stay."

    elif affinity_stranger >= AFFECTION_MEDIUM:
        s "The next train comes in about an hour."
        pause 1.0
        s "If you ever want to board it, you know where to find me."
        pause 0.5
        p "And if I don't?"
        pause 1.0
        s "Then I'll be here anyway. Waiting. As I always am."

    else:
        s "You can stay as long as you need."
        pause 1.0
        s "I'm not going anywhere."

        p "How long have you been waiting?"
        pause 1.5
        s "How long will you?"

    pause 2.0

    # ============================================================
    # FINAL IMAGE: THE PLATFORM AT PEACE
    # ============================================================

    scene bg station_night with fade
    pause 1.0

    narrator "The station lights are warm now."
    narrator "Or maybe they always were. You're only now noticing."
    pause 1.5

    narrator "Outside, the city sleeps."
    narrator "But here on the platform, you're awake."
    narrator "Truly awake, for the first time in a long time."
    pause 1.0

    narrator "And that's enough."

    pause 2.0

    # ============================================================
    # ENDING MESSAGE
    # ============================================================

    scene black with fade
    pause 1.0

    centered "THE END"
    pause 1.0

    centered "The train will come again tomorrow."
    pause 1.0

    centered "But for tonight, you stay."
    pause 3.0

    return
