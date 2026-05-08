label prologue:
    scene bg station_night with fade
    play music "audio/station_ambience.ogg" fadein 2.0 volume 0.6
    
    "The platform is quiet. Only the hum of fluorescent lights and the distant wind keep you company."
    "The announcement board flickers: <i>Last train departing soon.</i>"
    
    scene bg station_bench with dissolve
    "A figure sits on the bench nearby. They don't look at you. Not yet."
    
    pause 1.5
    show stranger neutral at left with moveinleft
    
    s "..."
    pause 2.0
    s "Do you think people can really change?"
    
    call choice_openness
    jump train_arrival