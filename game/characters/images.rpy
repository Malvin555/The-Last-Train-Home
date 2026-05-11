# game/characters/images.rpy

init 10:
    # PLAYER (MALVIN) expressions
    image malvin neutral = "characters/malvin/neutral.png"
    image malvin happy = "characters/malvin/happy.png"
    image malvin sad = "characters/malvin/sad.png"
    image malvin surprised = "characters/malvin/surprised.png"
    image malvin angry = "characters/malvin/angry.png"

    # STRANGER expressions
    image stranger neutral = "characters/stranger/neutral.png"
    image stranger smile = "characters/stranger/smile.png"
    image stranger contemplative = "characters/stranger/contemplative.png"
    image stranger stern = "characters/stranger/stern.png"
    image stranger surprised = "characters/stranger/surprised.png"

    # LYNETTE expressions
    image lynette neutral = "characters/lynette/neutral.png"
    image lynette smile = "characters/lynette/smile.png"
    image lynette sad = "characters/lynette/sad.png"
    image lynette angry = "characters/lynette/angry.png"
    image lynette thinking = "characters/lynette/thinking.png"

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
