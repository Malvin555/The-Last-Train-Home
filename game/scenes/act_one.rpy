# game/scenes/02_act_one.rpy
# ACT ONE: "The Waiting"
# The stranger and protagonist wait for the train
# Relationship deepens through shared vulnerability and connection

label act_one:
    scene bg station_platform with fade
    pause 1.0

    # ============================================================
    # TRANSITION NARRATION
    # ============================================================

    narrator "The train is late."
    narrator "It happens sometimes. The announcement board promises it will arrive in 15 minutes."
    pause 1.5

    narrator "You should probably sit. But instead, you stand. Waiting."
    pause 1.0

    # ============================================================
    # STRANGER OFFERS CONVERSATION
    # ============================================================

    show stranger neutral at right with dissolve
    show malvin neutral at left with dissolve

    s "You're not going to sit?"
    p "I... guess I'm too restless."

    pause 1.0
    s "That's nerves. The train always makes people nervous."
    s "Even when they want to board it."

    pause 1.5

    # ============================================================
    # MOMENT OF CONNECTION - Stranger opens up slightly
    # ============================================================

    show stranger contemplative
    s "I've been coming here for a long time, you know."
    pause 0.5
    s "To this platform. This station."
    pause 1.0
    s "Every night, I ask myself the same question: am I leaving, or am I staying?"

    menu:
        "How long has it been?":
            $ affinity_stranger += 1
            $ connection_depth += 1
            show malvin neutral
            p "How long have you been doing this?"
            pause 0.5
            show stranger sad
            s "I lost count. That's probably not a good sign."
            pause 1.0
            show stranger contemplative
            s "But you get comfortable in purgatory. That's the real trap."
            $ vulnerability_shown = True

        "Why don't you just choose?":
            $ affinity_stranger += 1
            show malvin angry
            p "Why not just make a decision? Pick one."
            pause 1.0
            show stranger neutral
            s "If only it were that simple."
            s "The hardest choices aren't between good and bad. They're between two different versions of yourself."

        "I think I understand.":
            $ affinity_stranger += 2
            $ has_reflected = True
            show malvin sad
            p "I think... I understand that feeling."
            pause 1.0
            show stranger smile
            s "I know you do. That's why I'm telling you."
            pause 0.5
            s "Most people don't have that capacity for understanding."
            narrator "There's warmth in the stranger's eyes now. Not judgment. Just recognition."
            $ vulnerability_shown = True

    pause 2.0

    # ============================================================
    # SHARING STORIES - Deeper conversation
    # ============================================================

    s "Can I ask you something? And you can refuse. I won't be offended."
    pause 0.5
    p "Go ahead."

    s "Why are you really here?"
    s "Not at this station. Here. In this life. Right now, in this moment."

    menu:
        "I don't know anymore.":
            $ affinity_stranger += 2
            $ regret_accepted = True
            show malvin sad
            p "I... honestly don't know anymore."
            pause 1.0
            p "I thought I was headed somewhere. But now? I can't remember where."
            pause 1.5
            show stranger smile
            s "That's the first honest thing most people say."
            s "Admitting you're lost. It's terrifying and liberating at the same time."
            $ connection_depth += 2

        "Because I'm running from something.":
            $ affinity_stranger += 1
            $ personality_guarded += 1
            show malvin angry
            p "Because I'm running from... I'm not even sure anymore."
            pause 1.0
            show stranger neutral
            s "The thing about running is, you can't ever outrun yourself."
            s "You just end up tired."
            pause 0.5
            show stranger smile
            s "But at least you're moving. That's something."
            $ connection_depth += 1

        "Because I'm looking for something.":
            $ affinity_stranger += 1
            $ personality_honest += 1
            show malvin neutral
            p "Because I'm searching. For meaning, purpose, redemption—I'm not sure which."
            pause 1.0
            show stranger smile
            s "Now that's admirable. Most people give up searching."
            s "They settle. They compromise. They forget."
            pause 0.5
            show stranger contemplative
            s "But you? You're still asking questions."
            $ connection_depth += 1

    pause 1.5

    # ============================================================
    # SHARED MOMENT - The platform grows quieter
    # ============================================================

    scene bg station_quiet with dissolve

    show stranger neutral at right
    show malvin neutral at left
    
    narrator "The platform has emptied out."
    narrator "It's just you and the stranger now."
    narrator "Just two people waiting for a train that hasn't come yet."
    pause 1.5

    show stranger smile
    s "You know what I love about train stations?"
    p "What?"

    pause 0.5
    s "They're the only place in the world where waiting is acceptable."
    show stranger contemplative
    s "Where you can stand still, say nothing, and it's perfectly fine."
    pause 1.0
    s "You're not expected to be productive. You're not expected to have it figured out."
    s "You're just... here."

    pause 2.0

    narrator "There's a strange peace in those words."
    narrator "Permission, almost. To simply exist for a moment."

    pause 1.5

    # ============================================================
    # STRANGER'S OFFER OF UNDERSTANDING
    # ============================================================

    show stranger neutral
    s "Whatever you decide to do—whether you board or stay—I want you to know something."
    pause 1.0
    s "You're not alone in feeling lost. In feeling uncertain."
    pause 0.5
    show stranger smile
    s "The people who pretend to have it figured out? They're just better at lying."

    menu:
        "Thank you.":
            $ affinity_stranger += 1
            show malvin happy
            p "Thank you. For... understanding."
            pause 1.0
            show stranger contemplative
            s "Understanding is the one thing I can offer. It's all I have."
            $ connection_depth += 1

        "Does it ever get easier?":
            $ affinity_stranger += 1
            show malvin sad
            p "Does it ever get easier? The not knowing?"
            pause 1.5
            show stranger neutral
            s "No. But you get stronger. And that's different."
            pause 0.5
            show stranger stern
            s "Easier means avoiding the pain. Stronger means choosing to face it anyway."
            $ has_reflected = True
            $ connection_depth += 1

        "What about you? Are you alone?":
            $ affinity_stranger += 2
            show malvin neutral
            p "Are you alone? In all of this?"
            pause 2.0
            show stranger contemplative
            s "I am. But I think... I'm less alone now."
            pause 0.5
            show stranger smile
            narrator "The stranger looks at you then—really looks at you."
            narrator "And you realize: this is a moment that matters."
            $ vulnerability_shown = True
            $ connection_depth += 2

    pause 2.0

    # ============================================================
    # TRAIN ANNOUNCEMENT - Act climax
    # ============================================================

    play sound sfx_train_approach fadein 1.0

    narrator "The rails begin to vibrate."
    narrator "A sound in the distance. Growing closer."
    pause 1.5

    s "It's here."
    pause 1.0

    $ game_state = STATE_CLIMAX
    jump act_two
