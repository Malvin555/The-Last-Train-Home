# game/data/constants.rpy
# Game-wide constants, colors, and configuration

# COLOR PALETTE
define COLOR_PLAYER = "#e6e6e6"      # Light gray for player text
define COLOR_STRANGER = "#8ab4f8"    # Soft blue for stranger
define COLOR_ALEX = "#ff9999"        # Warm red for Alex
define COLOR_NARRATOR = "#ffffff"    # White for narrator
define COLOR_SYSTEM = "#ffeb3b"      # Yellow for system messages

# CHARACTER NAMES (for easy reference and consistency)
define NAME_PLAYER = "Malvin"
define NAME_STRANGER = "Stranger"
define NAME_ALEX = "Alex"

# GAME STATES (for tracking player progress)
define STATE_INTRO = 0
define STATE_ACT_ONE = 1
define STATE_ACT_TWO = 2
define STATE_CLIMAX = 3
define STATE_ENDING = 4

# AFFECTION THRESHOLDS (for branching endings)
define AFFECTION_MIN = 0
define AFFECTION_LOW = 2
define AFFECTION_MEDIUM = 4
define AFFECTION_HIGH = 6
define AFFECTION_MAX = 8

# AUDIO SETTINGS
define MUSIC_VOLUME_DEFAULT = 0.6
define MUSIC_VOLUME_CLIMAX = 0.7
define SOUND_VOLUME_DEFAULT = 0.8
