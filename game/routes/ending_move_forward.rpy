# game/routes/01_ending_move_forward.rpy
# ENDING A: "Move Forward"
# The player boards the train.
# Represents: Growth, acceptance, forward momentum
# Tone: Bittersweet, hopeful, transformative

label ending_move_forward:
    scene black with fade
    stop music fadeout 1.5
    pause 1.0

    scene bg train_interior with fade
    play music "audio/ending_hopeful.ogg" fadein 2.0 volume MUSIC_VOLUME_DEFAULT

    narrator "The doors close behind you."
    narrator "A soft hiss. Finality."
    pause 1.5

    # ============================================================
    # STRANGER REFLECTION - Based on affinity
    # ============================================================

    if affinity_stranger >= AFFECTION_HIGH:
        narrator "You look back through the window."
        narrator "The stranger is still there on the platform."
        narrator "They're smiling. Not sad. Just... knowing."
        pause 2.0

        narrator "You understand now: they were never meant to follow."
        narrator "They were meant to help you realize you could go alone."
        pause 1.5

        s "Take care of yourself. Please."
        pause 1.0
        narrator "Their voice reaches you somehow, across the distance."

    elif affinity_stranger >= AFFECTION_MEDIUM:
        narrator "You glimpse them on the platform as the train pulls away."
        narrator "They're watching. There's no judgment in their eyes."
        narrator "Only understanding."
        pause 1.5

        narrator "You realize: this isn't goodbye. This is just... a different kind of hello."
        pause 1.0

    else:
        narrator "You don't look back."
        narrator "Some trains are meant to be boarded alone."
        pause 1.5

        narrator "But somewhere deep down, you're grateful you weren't truly alone when you made the choice."
        pause 1.0

    pause 1.5

    # ============================================================
    # JOURNEY NARRATION
    # ============================================================

    narrator "The train moves through the night."
    narrator "Tunnel after tunnel. City lights flickering past."
    pause 1.5

    narrator "You should feel relief. Or sadness. Or something."
    narrator "Instead, you feel something quieter."
    narrator "Lighter."
    pause 1.0

    # ============================================================
    # REFLECTION ON GROWTH
    # ============================================================

    if regret_accepted:
        narrator "You think about your regrets now. The ones you mentioned to the stranger."
        narrator "They don't feel lighter exactly. But different."
        pause 1.0

        narrator "They feel like they belong to someone you were, not someone you are."
        pause 1.5

        narrator "And maybe that's what moving forward means: carrying your past without letting it carry you."
        pause 1.0

    elif vulnerability_shown:
        narrator "You think about what you shared on that platform."
        narrator "Your fears. Your uncertainty. Your desperate, human need to be understood."
        pause 1.0

        narrator "The stranger saw that. And didn't look away."
        pause 1.5

        narrator "That changes you. You didn't think it would, but it does."
        pause 1.0

    else:
        narrator "You think about what you didn't say on that platform."
        narrator "The words that stayed trapped inside."
        pause 1.0

        narrator "Maybe on the next journey, you'll find those words."
        narrator "Maybe on the journey after that."
        pause 1.5

        narrator "That's okay. Moving forward doesn't mean moving perfectly."
        pause 1.0

    pause 2.0

    # ============================================================
    # FINAL IMAGE & MESSAGE
    # ============================================================

    scene bg train_window_dawn with dissolve
    pause 1.0

    narrator "The sky outside changes color."
    narrator "From night to the soft gray of almost-dawn."
    pause 1.5

    narrator "You realize: you never asked where this train was going."
    narrator "And somehow, that's exactly right."
    pause 1.0

    narrator "The destination matters less than the journey."
    narrator "And for the first time in a long time, you're actually traveling it."

    pause 2.0

    # ============================================================
    # ENDING CREDITS ROLL
    # ============================================================

    scene black with fade
    pause 1.0

    centered "THE END"
    pause 1.0

    centered "Thank you for boarding."
    pause 3.0

    return
