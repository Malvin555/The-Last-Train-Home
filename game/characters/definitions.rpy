# game/characters/definitions.rpy
# Character definitions for "The Last Train Home"
# All character objects defined here for consistency and maintainability

# ============================================================
# PLAYER CHARACTER
# ============================================================
# The protagonist - represented as "You" throughout the game
# Customizable based on player choices and personality

define p = Character(
    NAME_PLAYER,
    color=COLOR_PLAYER,
    ctc="ctc",
    ctc_position="fixed",
    what_prefix="\"",
    what_suffix="\"",
    kind=adv
)

# ============================================================
# THE STRANGER
# ============================================================
# Main NPC - mysterious figure on the train platform
# Represents introspection, growth, and hidden truths
# Personality: Observant, thoughtful, slightly cryptic

define s = Character(
    NAME_STRANGER,
    color=COLOR_STRANGER,
    ctc="ctc",
    ctc_position="fixed",
    what_prefix="\"",
    what_suffix="\"",
    kind=adv
)

# ============================================================
# NARRATOR / NARRATIVE VOICE
# ============================================================
# Omniscient narrator for descriptive passages and thoughts
# Used for scene descriptions and emotional beats

define narrator = Character(
    None,
    color=COLOR_NARRATOR,
    ctc="ctc",
    ctc_position="fixed",
    kind=adv
)

# ============================================================
# ALTERNATIVE NARRATOR (for inner thoughts/italicized passages)
# ============================================================
# Used for introspective moments and philosophical reflections

define thoughts = Character(
    None,
    color="#d4a574",  # Warm tan for intimate thoughts
    ctc="ctc",
    ctc_position="fixed",
    kind=adv
)

# ============================================================
# SYSTEM CHARACTER (for meta-commentary, optional)
# ============================================================
# Used sparingly for game messages or UI notifications

define system = Character(
    "[System]",
    color=COLOR_SYSTEM,
    ctc="ctc",
    ctc_position="fixed",
    kind=adv
)
