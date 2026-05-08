# The Last Train Home - Improved Project Structure

## Overview
This is a professional, modular Ren'Py visual novel with improved story depth, character affection systems, and multiple meaningful endings.

## 🎯 What's New in v2.0

### Story Improvements
- **Better Pacing**: Split into clear acts with smooth transitions
- **Character Development**: The stranger evolves based on player choices and affinity level
- **Emotional Depth**: Multiple dialogue branches with genuine consequences
- **Rich Narration**: Detailed descriptions that set mood without being verbose
- **Three Distinct Endings**:
  - **Move Forward** - Hopeful growth and acceptance
  - **Stay Behind** - Contemplative peace and stillness
  - **The Truth** - Mystical revelation and self-discovery

### Code Organization
- **Modular Structure**: Each component has its own file
- **Constants System**: Easy to balance and tweak game values
- **Clean Naming**: All files follow the `XX_name.rpy` convention
- **Separation of Concerns**: Characters, scenes, routes, and data are separate

## 📁 Project Structure

```
The Last Train Home/
├── game/
│   ├── script.rpy                 # Main entry point
│   ├── options.rpy                # Game configuration
│   ├── screens.rpy                # UI screens
│   ├── gui.rpy                    # GUI customization
│   │
│   ├── data/                      # Game state and configuration
│   │   ├── constants.rpy          # All game constants
│   │   └── variables.rpy          # Default game variables
│   │
│   ├── characters/                # Character definitions
│   │   └── definitions.rpy        # All character objects
│   │
│   ├── scenes/                    # Story scenes
│   │   ├── 01_prologue.rpy        # Prologue: First meeting
│   │   ├── 02_act_one.rpy         # Act One: Deepening connection
│   │   └── 03_act_two.rpy         # Act Two/Climax: Final choice
│   │
│   ├── routes/                    # Ending paths
│   │   ├── 01_ending_move_forward.rpy
│   │   ├── 02_ending_stay_behind.rpy
│   │   └── 03_ending_truth.rpy
│   │
│   ├── utils/                     # Utility functions (empty, for future use)
│   │
│   ├── images/                    # Image assets (backgrounds, sprites)
│   ├── audio/                     # Audio assets (music, SFX)
│   ├── Font/                      # Custom fonts
│   └── gui/                       # GUI assets
```

## 🎮 Game Flow

```
START
  ↓
PROLOGUE (01_prologue.rpy)
  ├─ Stranger introduces themselves
  ├─ Player makes first choices
  └─ Affinity tracker: 0-2 points
  ↓
ACT ONE (02_act_one.rpy)
  ├─ Stranger opens up
  ├─ Player demonstrates vulnerability
  └─ Affinity tracker: 0-4 more points
  ↓
CLIMAX (03_act_two.rpy)
  ├─ Train arrives
  ├─ Final conversation varies by affinity
  └─ Player chooses path:
      ├─ Board the train
      ├─ Stay on platform
      └─ Ask stranger's identity
  ↓
ENDING (routes/*.rpy)
  ├─ Ending A: Move Forward
  ├─ Ending B: Stay Behind
  └─ Ending C: The Truth
  ↓
END
```

## 🎛️ Game Systems

### Affinity System (affinity_stranger)
Tracks connection between player and stranger. Affects:
- Dialogue variations
- Ending content
- Stranger's emotional responses
- Unlocked story paths

**Thresholds**:
- 0-2: Acquaintance
- 3-4: Friend
- 5-6: Confidant
- 7-8: Deep connection

### Personality Tracking
- **personality_honest**: Open, vulnerable responses
- **personality_hopeful**: Optimistic, forward-looking answers
- **personality_guarded**: Reserved, self-protective choices

### Emotional Flags
- `has_reflected`: Player opened up emotionally
- `regret_accepted`: Player acknowledged past regrets
- `vulnerability_shown`: Player shared something personal
- `knows_stranger_name`: Player asked stranger's identity

## 📝 Writing Guidelines

### Dialogue Structure
```renpy
s "Main character speaks."
pause 0.5
p "Player responds."
pause 1.0
narrator "Narrative description happens."
```

### Choices with Consequences
```renpy
menu:
    "Honest option":
        $ affinity_stranger += 2
        p "Character text."
        s "Response."
    
    "Guarded option":
        $ personality_guarded += 1
        p "Character text."
```

### Scene Organization
- Use section comments: `# ============================================================`
- Group related content logically
- Always include fallback dialogue for low-affinity paths

## 🛠️ How to Expand the Story

### Adding a New Scene
1. Create `game/scenes/04_scene_name.rpy`
2. Define label: `label scene_name:`
3. Update previous scene to `jump scene_name`
4. Add any new variables to `data/variables.rpy`

### Adding a New Character
1. Define character in `game/characters/definitions.rpy`
2. Add color constant to `data/constants.rpy`
3. Use in dialogue: `your_char "Text here"`

### Creating New Endings
1. Create `game/routes/04_ending_name.rpy`
2. Define label: `label ending_name:`
3. Add menu option in climax scene
4. Reference in `data/variables.rpy`

## 🎨 Customization Points

### Change Colors
Edit `game/data/constants.rpy`:
```python
define COLOR_STRANGER = "#8ab4f8"  # Change this color
```

### Adjust Affinity Thresholds
Edit `game/data/constants.rpy`:
```python
define AFFECTION_HIGH = 6  # Change this value
```

### Modify Music Settings
Edit `game/data/constants.rpy`:
```python
define MUSIC_VOLUME_DEFAULT = 0.6  # Change volume
```

## 🚀 Development Tips

### Testing Multiple Endings
Jump directly to climax scene:
```renpy
label test_climax:
    $ affinity_stranger = 7  # Set high affinity
    jump act_two
```

### Viewing All Content
Set high affinity values in Python console:
```
$ affinity_stranger = 8
$ has_reflected = True
```

### Debugging Choices
Add this to any scene to see current values:
```renpy
narrator "[affinity_stranger = [affinity_stranger]]"
```

## 🎵 Audio Requirements

The game expects these audio files in `game/audio/`:
- `station_ambience.ogg` - Main ambient music
- `train_approach.ogg` - Train arriving sound
- `train_approach_loud.ogg` - Train arrival climax
- `ending_hopeful.ogg` - Move Forward ending
- `ending_acceptance.ogg` - Stay Behind ending
- `ending_revelation.ogg` - The Truth ending

## 📸 Image Requirements

The game expects these backgrounds in `game/images/`:
- `bg_station_night.png`
- `bg_station_bench.png`
- `bg_station_platform.png`
- `bg_station_quiet.png`
- `bg_station_train.png`
- `bg_station_empty.png`
- `bg_station_light.png`
- `bg_train_interior.png`
- `bg_train_window_dawn.png`

And a character sprite in `game/images/`:
- `stranger_neutral.png` (or define in script)

## ✅ Quality Checklist

Before release, ensure:
- [ ] All audio files are present and play correctly
- [ ] All backgrounds are properly named and exist
- [ ] All three endings can be reached
- [ ] Affinity system works (choices increase values)
- [ ] Dialogue flows naturally
- [ ] Music fades smooth and aren't jarring
- [ ] No syntax errors (test in Ren'Py)

## 📖 File Naming Convention

All `.rpy` files follow this format: `XX_name.rpy`
- `XX` = 2-digit number (01, 02, 03, etc.)
- `name` = descriptive file name
- **Example**: `01_prologue.rpy`, `02_act_one.rpy`

⚠️ **Important**: Filenames must NOT start with '00' as Ren'Py reserves those for its own files.

## 💡 Tips for Better Stories

1. **Use Pauses**: Strategic pauses create emotional weight
   ```renpy
   narrator "Something important happened."
   pause 2.0  # Let the player feel it
   ```

2. **Branch Content Meaningfully**: Every choice should matter
   ```renpy
   if affinity_stranger >= AFFECTION_HIGH:
       s "You mean something to me."
   else:
       s "I barely know you."
   ```

3. **Show, Don't Tell**: Let narration convey emotion
   ```renpy
   narrator "Their eyes grew distant."  # Better than "they felt sad"
   ```

4. **Use Whitespace**: In narration, breaks improve readability
   ```renpy
   narrator "First thought."
   pause 1.0
   narrator "Second thought, different topic."
   ```

## 🐛 Troubleshooting

### Game won't start
- Check for syntax errors in `.rpy` files
- Ensure `label start:` exists in `script.rpy`
- Delete `.rpyc` compiled files and rebuild

### Choices don't affect story
- Check that variables are being modified: `$ variable_name += 1`
- Verify if/elif conditions match variable values
- Test in debug mode: `$ variable_name = 10`

### Music cuts off abruptly
- Use `fadeout` parameter: `stop music fadeout 1.5`
- Check audio file length isn't too short
- Ensure audio format is supported (OGG preferred)

## 📚 Additional Resources

- Ren'Py Documentation: https://www.renpy.org/doc/html/
- Visual Novel Writing Tips: https://www.wattpad.com/writing/visual-novel
- Ren'Py Community: https://lemmasoft.renai.us/

---

**Version**: 2.0  
**Last Updated**: 2024  
**Status**: Production Ready
