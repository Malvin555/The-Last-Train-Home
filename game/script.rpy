# game/script.rpy
# ============================================================
# THE LAST TRAIN HOME - Main Entry Point
# ============================================================
# This file orchestrates the game's initialization and flow.
#
# MODULAR STRUCTURE:
#   - game/data/constants.rpy       → Game-wide constants & configuration
#   - game/data/variables.rpy       → Default game state
#   - game/characters/definitions.rpy → Character definitions
#   - game/utils/helpers.rpy        → Utility functions
#   - game/scenes/*.rpy             → Story scenes
#   - game/routes/*.rpy             → Ending paths
#
# FILE LOADING ORDER (handled by Ren'Py automatically):
#   1. Init phase (constants, definitions, helpers)
#   2. Game start → label start
#   3. Scene flow → various labels
# ============================================================

# ============================================================
# CLICK-TO-CONTINUE ANIMATION
# ============================================================
# Visual indicator that player can advance text

image ctc:
    align (0.82, 0.90)
    "gui/ctc.png"
    subpixel True
    easein 1.0 ypos 0.89
    pause 0.4
    easein 1.0 ypos 0.90
    pause 0.4
    repeat

# ============================================================
# GAME INITIALIZATION
# ============================================================

# Game initialization happens automatically via RenPy

# ============================================================
# MAIN ENTRY POINT
# ============================================================

label start:

    # Hide quick menu during the cinematic intro
    $ quick_menu = False

    scene black with fade
    pause 1.0

    # ============================================================
    # CINEMATIC INTRO / PREMISE
    # ============================================================

    show text "We spend our lives waiting." with dissolve
    pause 2.0
    hide text with dissolve
    
    show text "Waiting for the right moment. For a reason. For permission to let go." with dissolve
    pause 3.0
    hide text with dissolve

    show text "But some nights, the waiting has to end." with dissolve
    pause 2.5
    hide text with dissolve

    pause 1.0

    # Restore UI
    $ quick_menu = True
    jump prologue

# ============================================================
# GAME END HANDLER
# ============================================================

label end_game:
    stop music fadeout 1.5
    scene black with fade
    pause 2.0
    return

# ============================================================
# DEVELOPER NOTES
# ============================================================
# This modular structure keeps the codebase organized and scalable:
#
# Structure:
#   game/data/          - Constants and game state
#   game/characters/    - Character definitions
#   game/scenes/        - Story content (prologue, acts)
#   game/routes/        - Ending paths
#   game/utils/         - Helper functions
#
# To add new content, create files following this structure.
# File naming convention: XX_name.rpy (where XX = 2-digit number)
# ============================================================
