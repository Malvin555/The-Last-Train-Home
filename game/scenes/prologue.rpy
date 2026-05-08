# game/scenes/01_prologue.rpy
# PROLOGUE: "The Last Train Home"
# Introduction to the world, the setting, and the stranger
# Establishes tone: melancholic yet hopeful, introspective

label prologue:
    scene black with fade
    pause 1.0

    # ============================================================
    # OPENING NARRATION - Set the mood
    # ============================================================

    scene bg station_night with fade
    play music "audio/station_ambience.ogg" fadein 2.0 volume MUSIC_VOLUME_DEFAULT

    narrator "The platform is empty at this hour."
    narrator "Or perhaps it was always empty, and you're only now noticing."
    pause 1.5

    narrator "Fluorescent lights hum overhead, casting everything in pale blue."
    narrator "A single announcement board flickers: <i>Last train departing—23:47</i>"
    pause 1.0

    narrator "You're not sure why you came here tonight."
    narrator "But here you are."
    pause 2.0

    # ============================================================
    # STRANGER INTRODUCTION
    # ============================================================

    scene bg station_bench with dissolve

    narrator "That's when you notice the figure on the bench."
    narrator "They don't move. Haven't moved, probably, for a while."
    pause 1.0

    show stranger neutral at left with moveinleft

    narrator "Their eyes are fixed on the rails ahead, as if waiting for something."
    narrator "Or someone."
    pause 1.5

    # ============================================================
    # FIRST DIALOGUE - The stranger speaks first
    # ============================================================

    pause 2.0
    s "You have the look of someone searching."
    pause 1.0
    s "Not for a train, I think. Something else."

    menu:
        "Turn to face them.":
            p "I... wasn't aware it was that obvious."
            s "It's not. Most people don't have it. But you do."
            $ affinity_stranger += 1
            $ personality_honest += 1

        "Ignore them.":
            narrator "You pretend not to hear. But you do."
            narrator "You always do."
            s "That's fine. Not everyone wants to be seen."
            $ personality_guarded += 1

        "Mirror their question.":
            p "Aren't we all searching for something?"
            s "There it is. A philosopher on the platform."
            pause 0.5
            s "No—not quite. Someone running from something, maybe. But phrasing it as searching."
            $ affinity_stranger += 1
            $ personality_honest += 1

    pause 1.5

    # ============================================================
    # DEEPER CONVERSATION - The stranger probes
    # ============================================================

    s "Do you ever wonder if people can really change?"
    pause 1.0
    s "Or do they just... carry themselves forward, the same as always?"

    menu:
        "Yes. I believe people can change.":
            $ affinity_stranger += 2
            $ personality_honest += 1
            p "Yes. I think... given the right moment, anyone can change."
            s "Interesting. You sound like you're trying to convince yourself."
            pause 0.5
            s "Or maybe you're speaking from experience."
            $ has_reflected = True

        "I'm not sure. It's complicated.":
            $ affinity_stranger += 1
            $ personality_honest += 1
            p "I don't think it's that simple. Some things stay with us. Some don't."
            s "Honest. At least you're not pretending to have it figured out."
            pause 0.5
            s "That's rarer than you'd think."
            $ has_reflected = True

        "Stay silent.":
            p "..."
            pause 1.5
            s "That's a valid answer too."
            s "Sometimes silence says more than words."
            narrator "They don't seem disappointed by your silence. Just... understanding."

        "Ask them first.":
            p "Do you think people can change?"
            pause 1.0
            s "A good deflection. I like that about you already."
            s "No, I think... people don't change. They just finally become who they were all along."
            $ affinity_stranger += 1

    pause 2.0

    # ============================================================
    # DEEPER QUESTION - Moving toward vulnerability
    # ============================================================

    s "Do you regret anything in your life?"
    pause 1.0
    s "Not just the small things. The big choices."

    menu:
        "Yes. More than I'd like to admit.":
            $ affinity_stranger += 2
            $ regret_accepted = True
            $ vulnerability_shown = True
            p "Yes. Some days, the weight feels heavier than other days."
            pause 1.0
            s "That means you still care. That's important."
            pause 0.5
            s "A lot of people just go numb."
            narrator "For the first time, the stranger looks at you directly."
            narrator "There's something in their eyes. Recognition, maybe."

        "No. I try not to dwell on it.":
            $ personality_guarded += 1
            p "I try to focus on what's ahead, not what's behind."
            pause 0.5
            s "That's a defense mechanism, you know. Nothing wrong with it."
            s "But running gets tiring eventually."

        "I'd rather not say.":
            p "Some things are mine to carry."
            pause 1.0
            s "Fair enough. You don't owe me your story."
            pause 0.5
            s "But maybe you owe it to yourself."
            $ personality_guarded += 1

        "Everyone has regrets.":
            p "Doesn't everyone? Regret is part of being human."
            pause 0.5
            s "Some people carry it. Others learn to put it down."
            s "The question is: which are you?"
            $ affinity_stranger += 1

    pause 2.0

    # ============================================================
    # ATMOSPHERE BUILD - Train approaching
    # ============================================================

    narrator "The rails begin to hum."
    narrator "Deep. Resonant. Unmistakable."
    pause 1.5

    s "It's coming."
    pause 1.0
    s "Your last train."

    # ============================================================
    # TRANSITION TO NEXT ACT
    # ============================================================

    pause 1.0
    $ first_conversation_done = True
    jump act_one
