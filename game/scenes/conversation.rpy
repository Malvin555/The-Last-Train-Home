# game/scenes/conversation.rpy

label choice_openness:
    menu:
        "Yes. I believe people can change.":
            $ empathy += 2
            p "Yes. I think... given the right moment, anyone can."
            s "Interesting. Most people already decided that for themselves."
            "Their voice is soft. Not dismissive. Just... observant."
            
        "I'm not sure. It's complicated.":
            $ empathy += 1
            p "I don't know. Some things stay with us. Some don't."
            s "Honest. At least you're not pretending to have it figured out."
            
        "Stay silent.":  
            $ empathy += 0
            "You say nothing. The silence stretches, but it's not uncomfortable."
            s "...Fair enough. Silence speaks too."
    
    pause 1.0
    s "Do you regret anything in your life?"
    jump choice_regret

label choice_regret:
    menu:
        "Yes. More than I'd like to admit.":
            $ empathy += 1
            $ regret_accepted = True
            p "Yes. Some days, the weight feels heavier than others."
            s "That means you still care. That's not a bad thing."
            "They finally look at you. Their eyes hold something familiar."
            
        "No. I try not to dwell on it.":
            $ empathy += 0
            $ regret_accepted = False
            p "I try to look forward. Dwelling doesn't change the past."
            s "Forward is good. Just don't forget what brought you here."
            
        "I'd rather not say.":
            $ empathy += 0
            $ regret_accepted = False
            p "Some things are mine to carry."
            s "Understood. You'll know when you're ready to put them down."
    
    $ has_reflected = True
    pause 1.5
    "A deep sound echoes through the station. The rails begin to hum."
    return