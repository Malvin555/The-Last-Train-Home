# game/00_data/backgrounds.rpy
# Background image definitions for "The Last Train Home"
# Place your background image files under `game/backgrounds/`.
# Example: `The Last Train Home/game/backgrounds/station_night.png`

# Use `image bg <name> = "backgrounds/<file>"` so scripts can do:
#   scene bg <name> with fade
#   or
#   show bg <name> with dissolve

init 20:
    # Primary station backgrounds (used in scenes)
    # Use im.Scale so the background is resized to the project's screen dimensions
    image bg station_night = im.Scale("images/backgrounds/station_night.png", config.screen_width, config.screen_height)
    image bg station_bench = im.Scale("images/backgrounds/station_bench.png", config.screen_width, config.screen_height)
    # If you don't have dedicated images for every named background yet,
    # you can point missing names at existing files as a temporary fallback.
    image bg station_platform = im.Scale("images/backgrounds/station_bench.png", config.screen_width, config.screen_height)
    image bg station_quiet = im.Scale("images/backgrounds/station_bench.png", config.screen_width, config.screen_height)
    image bg station_train = im.Scale("images/backgrounds/station_train.png", config.screen_width, config.screen_height)

    # Train / interior & ending backgrounds
    image bg train_interior = im.Scale("images/backgrounds/train_interior.png", config.screen_width, config.screen_height)
    image bg station_empty = im.Scale("images/backgrounds/station_empty.png", config.screen_width, config.screen_height)
    image bg station_light = im.Scale("images/backgrounds/station_light.png", config.screen_width, config.screen_height)

# GUIDELINES / USAGE
# - Major transitions: use `scene bg <name> with <transition>` to set or replace the background.
#   Use `scene` when you want to clear the screen and set the background for a new beat.
# - Minor adjustments: use `show bg <name> with <transition>` to layer a background while keeping other
#   layer contents (rare for backgrounds, more common for overlay effects).
# - Character placement: after `scene bg ...`, place characters using `show <char> <expression> at <pos>`.
#   Example:
#       scene bg station_bench with dissolve
#       show stranger neutral at left with moveinleft
#       show malvin neutral at right
#
# SUGGESTED STORY MAPPING (where to change background in your current scripts):
# - Prologue (intro + first sighting)
#   * At start: `scene bg station_night with fade`
#   * When noticing the figure on the bench: `scene bg station_bench with dissolve`
#   * When the rails start to hum / train approaches: `scene bg station_train with fade` or add train sounds
# - Act One
#   * When entering the main platform: `scene bg station_platform with fade`
#   * Later when emptying out: `scene bg station_quiet with dissolve`
# - Act Two
#   * When train is arriving or you are on train: `scene bg station_train` or `scene bg train_interior`
# - Endings
#   * Emotional / final scenes: `scene bg train_interior`, `scene bg station_empty`, or `scene bg station_light`
#
# TRANSITION TIPS:
# - Use `with fade` for big cuts, `with dissolve` for softer emotional shifts.
# - Combine short pauses with transitions for weight: `pause 0.6; scene bg ... with dissolve`.
# - For flashbacks or memory overlays, consider using `show expression` (semi-transparent overlays) or
#   a separate `image flashback` that you `show` on top of the background.
#
# FILE LOCATION NOTE:
# - Put the actual PNGs in `The Last Train Home/game/backgrounds/` so the paths above resolve.
# - Filenames and tag names must match exactly (case-sensitive on Linux).
#
# EXAMPLE (short snippet to paste into a label):
#   scene bg station_night with fade
#   play music "audio/station_ambience.ogg" fadein 2.0
#   narrator "The platform is empty at this hour."
#   pause 1.0
#   scene bg station_bench with dissolve
#   show stranger neutral at left with moveinleft
#   narrator "Their eyes are fixed on the rails ahead..."
