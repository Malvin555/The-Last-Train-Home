# game/data/variables.rpy

# ============================================================
# RELATIONSHIP & AFFECTION TRACKING
# ============================================================
default empathy = 0                     # Main relationship tracker
default affinity_stranger = 0           # Legacy tracker (keep if used elsewhere)
default stranger_relationship_tier = 0
default openness_level = 0
default connection_depth = 0            

# Emotional state flags
default has_reflected = False           
default regret_accepted = False         
default vulnerability_shown = False     
default has_asked_identity = False

# ============================================================
# STORY PROGRESSION & STATE
# ============================================================
default current_scene = "prologue"
default game_state = STATE_INTRO        
default scenes_visited = []
default game_completion_percent = 0.0
default ending_type = None              
default total_choices_made = 0          

# ============================================================
# CHARACTER KNOWLEDGE & DISCOVERY
# ============================================================
default knows_stranger_name = False     
default stranger_backstory_revealed = 0 
default stranger_dialogue_seen = {}
default choice_history = {}

# ============================================================
# PLAYER CHOICES & PERSONALITY TRAITS
# ============================================================
default personality_honest = 0          
default personality_hopeful = 0         
default personality_guarded = 0         

# ============================================================
# MISC FLAGS
# ============================================================
default first_conversation_done = False 
default final_choice_made = False       

# ============================================================
# DEBUG & CONFIG
# ============================================================
define DEBUG_MODE = True
define DEBUG_UNLOCK_ALL_CHOICES = False