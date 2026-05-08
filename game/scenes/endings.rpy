label ending_move_forward:
    scene bg train_interior with fade
    stop music fadeout 1.5
    
    "The doors close behind you. The stranger is gone."
    
    if empathy >= 3:
        "You realize the train was never about distance. It was about letting go."
        "You finally feel light. Not because the past disappeared, but because you chose to carry it differently."
    elif regret_accepted:
        "The seats are empty. You lean back, breathing out a breath you didn't know you were holding."
        "Moving forward doesn't mean forgetting. It means making room."
    else:
        "The train pulls away. You watch the platform shrink behind the glass."
        "It's not a clean break. But it's a start."
        
    play music "audio/ending_hopeful.ogg" fadein 2.0 volume 0.5
    "You finally feel light."
    $ renpy.pause(2)
    return

label ending_stay_behind:
    scene bg station_empty with fade
    stop music fadeout 1.5
    
    "You hesitate. The doors close. The train leaves without you."
    "The station becomes silent again."
    
    if empathy >= 3:
        "You're still here. But something shifted. The weight isn't crushing anymore. It's just... present."
        "Tomorrow, you might board. Or maybe you'll just sit. Both are okay."
    else:
        "Nothing has changed. But something inside you feels heavier."
        "And yet, the bench is still warm. The lights still hum. You're still breathing."
        
    play music "audio/ending_ambiguous.ogg" fadein 2.0 volume 0.5
    $ renpy.pause(2)
    return

label ending_truth:
    scene bg station_light with fade
    stop music fadeout 1.5
    
    s "I'm what you avoid every night before sleep."
    pause 1.5
    "The lights flicker. The platform dissolves into soft white."
    
    if empathy >= 4:
        "You understand now. The stranger isn't a guide. They're the part of you that already healed."
        "You didn't meet them tonight. You finally listened."
    elif has_reflected:
        "The version of you that moved on was waiting. Not to replace you. To walk beside you."
        "The train fades into light. You step forward."
    else:
        "Recognition hits like a quiet wave. The stranger is you. Or the you that's ready to be."
        "The platform goes white. You don't feel fear. Just stillness."
        
    play music "audio/ending_revelation.ogg" fadein 2.0 volume 0.5
    "Everything goes white."
    $ renpy.pause(3)
    return