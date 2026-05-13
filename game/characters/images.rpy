# game/characters/images.rpy

init 10:
    # CUSTOM POSITION PADDING
    # This prevents characters from sticking to the very edges of the screen
    transform left:
        xalign 0.15
        yalign 1.0

    transform right:
        xalign 0.85
        yalign 1.0

    # =========================================================================
    # HOW TO FIX DIFFERENT SIZES:
    # If a character is too big or too small, change the `zoom` number below!
    # Examples:
    #   zoom=0.8  -> Makes the image 20% smaller
    #   zoom=1.2  -> Makes the image 20% bigger
    #   zoom=1.0  -> Default size
    # You can use different zooms for different characters to make them match.
    # =========================================================================

    # PLAYER (MALVIN) expressions
    image malvin neutral = Transform("images/characters/malvin/neutral.png", zoom=0.55)
    image malvin happy = Transform("images/characters/malvin/happy.png", zoom=0.55)
    image malvin contemplative = Transform("images/characters/malvin/contemplative.png", zoom=0.8)
    image malvin sad = Transform("images/characters/malvin/sad.png", zoom=0.55)
    image malvin surprised = Transform("images/characters/malvin/surprised.png", zoom=0.55)
    image malvin angry = Transform("images/characters/malvin/angry.png", zoom=0.55)

    # STRANGER expressions
    image stranger neutral = Transform("images/characters/stranger/neutral.png", zoom=0.9)
    image stranger smile = Transform("images/characters/stranger/smile.png", zoom=0.5)
    image stranger contemplative = Transform("images/characters/stranger/contemplative.png", zoom=0.5)
    image stranger stern = Transform("images/characters/stranger/stern.png", zoom=0.5)
    image stranger surprised = Transform("images/characters/stranger/surprised.png", zoom=0.5)

    # LYNETTE expressions
    image lynette neutral = Transform("characters/lynette/neutral.png", zoom=0.5)
    image lynette smile = Transform("characters/lynette/smile.png", zoom=0.5)
    image lynette sad = Transform("characters/lynette/sad.png", zoom=0.5)
    image lynette angry = Transform("characters/lynette/angry.png", zoom=0.5)
    image lynette thinking = Transform("characters/lynette/thinking.png", zoom=0.5)

# USAGE EXAMPLES (commented)
# show stranger neutral at left with moveinleft
# show stranger smile at left with dissolve
# show malvin surprised at right with moveinright
# show lynette sad at center with dissolve

# SUGGESTED MAPPINGS TO STORY BEATS (guidelines)
# - PROLOGUE:
#   * When the stranger is first visible: show stranger neutral (already used).
#   * When the stranger teases/softens: show stranger smile.
#   * When the stranger reveals something weighty or looks inward: show stranger contemplative at center.
# - PLAYER (MALVIN) REACTIONS:
#   * Honest confession / vulnerability: show malvin sad -> malvin contemplative -> malvin relieved/happy.
#   * Defensive / guarded choices: show malvin neutral or angry depending on tone.
# - LYNETTE:
#   * Warm or affectionate beats: show lynette smile.
#   * Private pain or reflection: show lynette thinking or sad.
