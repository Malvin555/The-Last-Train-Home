# game/data/variables.rpy
# Global game variables and tracking systems

# ============================================================
# RELATIONSHIP & AFFECTION TRACKING
# ============================================================

# Protagonist affection/connection levels with stranger
default affinity_stranger = 0          # Main relationship tracker (0-8)

# Emotional state flags
default has_reflected = False           # Whether player has opened up emotionally
default regret_accepted = False         # Whether player accepts their past
default vulnerability_shown = False     # Whether player showed vulnerability

# ============================================================
# STORY PROGRESSION & STATE
# ============================================================

default game_state = STATE_INTRO        # Current act/scene
default ending_type = None              # Which ending was achieved
default total_choices_made = 0          # For tracking playtime/engagement

# ============================================================
# CHARACTER KNOWLEDGE & DISCOVERY
# ============================================================

default knows_stranger_name = False     # Does player know the stranger's name?
default stranger_backstory_revealed = 0 # How much of their story is known (0-3)
default connection_depth = 0            # How deeply connected (0-5)

# ============================================================
# PLAYER CHOICES & PERSONALITY TRAITS
# ============================================================

default personality_honest = 0          # Honesty/openness score
default personality_hopeful = 0         # Hopefulness/optimism score
default personality_guarded = 0         # Guardedness/caution score

# ============================================================
# MISC FLAGS
# ============================================================

default first_conversation_done = False # Tracks prologue completion
default final_choice_made = False       # Tracks if final decision has been made
