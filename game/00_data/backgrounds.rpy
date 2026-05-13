# game/00_data/backgrounds.rpy
# Background image definitions for "The Last Train Home"

init 20:
    # Primary station backgrounds
    image bg station_night = im.Scale("images/backgrounds/station_night.jpg", config.screen_width, config.screen_height)
    image bg station_bench = im.Scale("images/backgrounds/station_bench.jpg", config.screen_width, config.screen_height)
    image bg station_platform = im.Scale("images/backgrounds/station_bench.jpg", config.screen_width, config.screen_height)
    image bg station_quiet = im.Scale("images/backgrounds/station_bench.jpg", config.screen_width, config.screen_height)
    image bg station_train = im.Scale("images/backgrounds/station_train.jpg", config.screen_width, config.screen_height)
    image bg station_early_train = im.Scale("images/backgrounds/station_early_train.jpg", config.screen_width, config.screen_height)

    # Train / interior & ending backgrounds
    image bg train_interior = im.Scale("images/backgrounds/train_interior.jpg", config.screen_width, config.screen_height)
    image bg station_empty = im.Scale("images/backgrounds/station_empty.jpg", config.screen_width, config.screen_height)
    image bg station_light = im.Scale("images/backgrounds/station_light.jpg", config.screen_width, config.screen_height)

    # Pure color backgrounds
    image white = Solid("#ffffff")
