# game/scenes/03_act_two.rpy
# ACT TWO / CLIMAX: "The Last Train"
# The train arrives. Final moment of choice.
# Everything the player and stranger built comes to this moment.

label act_two:
    scene black with fade
    pause 1.0

    scene bg station_train with fade
    play sound sfx_train_loud fadein 0.5

    narrator "The train pulls into the station."
    narrator "It's long. Dark. Patient."
    narrator "The doors slide open with a hiss of compressed air."
    pause 2.0

    # ============================================================
    # FINAL CONVERSATION BEFORE THE CHOICE
    # ============================================================

    show stranger neutral at right with dissolve
    show malvin neutral at left with dissolve

    pause 1.0
    s "This is it."
    pause 1.0
    s "The last train."

    show malvin sad
    p "Is it really the last one? Or just... another one?"
    pause 1.0
    show stranger contemplative
    s "Does the distinction matter?"
    pause 0.5
    s "If you don't board, you might board the next one. Or the one after."
    pause 0.5
    s "Or maybe you'll just stay on the platform forever, waiting."

    pause 1.5

    # ============================================================
    # MOMENTS BEFORE THE FINAL CHOICE
    # ============================================================

    # BRANCH: Different dialogue based on affinity level
    if affinity_stranger >= AFFECTION_HIGH:
        show stranger smile
        s "But here's what I know: whatever you choose, it'll be the right choice."
        pause 0.5
        s "Because you'll be choosing it consciously."
        pause 1.0
        s "Not out of fear. Not out of habit."
        pause 1.0
        s "You've thought about it. You've questioned it. You've felt it."
        pause 0.5
        s "And that—that's what makes it real."

        narrator "The stranger reaches out. Their hand hovers near yours."
        narrator "They don't touch. But they could."

        pause 2.0

    elif affinity_stranger >= AFFECTION_MEDIUM:
        show stranger neutral
        s "I can't make this choice for you. And honestly? I wouldn't want to."
        pause 1.0
        s "This is yours alone."
        pause 0.5
        s "But know that either way, you won't be invisible. You won't be forgotten."
        pause 1.0
        s "I see you. That's real."

        pause 2.0

    else:
        show stranger stern
        s "You know what the difference is between staying and leaving?"
        pause 1.0
        s "It's not the distance. It's the intention behind it."
        pause 1.0
        s "So before you decide, ask yourself: what am I running from? And what am I running toward?"

        pause 2.0

    # ============================================================
    # THE FINAL CHOICE - Three distinct paths
    # ============================================================

    s "So what will it be?"
    pause 1.0

    menu:
        "Board the train and move forward.":
            $ ending_type = "move_forward"
            $ final_choice_made = True
            jump ending_move_forward

        "Stay on the platform.":
            $ ending_type = "stay_behind"
            $ final_choice_made = True
            jump ending_stay_behind

        "Ask: 'Who are you?'":
            $ ending_type = "truth"
            $ knows_stranger_name = True
            $ final_choice_made = True
            jump ending_truth
