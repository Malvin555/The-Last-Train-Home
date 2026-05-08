label train_arrival:
    scene bg station_train with fade
    play sound "audio/train_approach.ogg" fadein 1.0
    
    "The train slows to a stop. Doors slide open with a soft hiss."
    show stranger neutral at center with dissolve  # 🔧 Fixed: Use dissolve/fade for center
    
    s "This is your last chance." 
    
    menu:
        "Board the train.":
            jump ending_move_forward
        "Stay on the platform.":
            jump ending_stay_behind
        "Ask: 'Who are you?'":
            $ has_asked_identity = True
            jump ending_truth