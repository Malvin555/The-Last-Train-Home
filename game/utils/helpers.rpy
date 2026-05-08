# game/utils/helpers.rpy
# ============================================================
# THE LAST TRAIN HOME - Utility Helpers & Functions
# ============================================================
# Common functions used throughout the game for:
#   - Relationship management
#   - Dialogue branching
#   - Scene transitions
#   - Game state queries
# ============================================================

init python:
    # ========================================================
    # RELATIONSHIP SYSTEM FUNCTIONS
    # ========================================================

    def update_empathy(points, reason=""):
        """
        Add empathy points and update relationship tier.

        Args:
            points (int): Number of empathy points to add
            reason (str): Optional description of why points were awarded
        """
        global empathy, stranger_relationship_tier

        empathy += points

        # Update relationship tier based on empathy threshold
        if empathy >= EMPATHY_THRESHOLD_HIGH:
            stranger_relationship_tier = REL_TIER_SOULMATE
        elif empathy >= EMPATHY_THRESHOLD_MID:
            stranger_relationship_tier = REL_TIER_CONFIDANT
        elif empathy >= EMPATHY_THRESHOLD_LOW:
            stranger_relationship_tier = REL_TIER_FRIEND
        else:
            stranger_relationship_tier = REL_TIER_ACQUAINTANCE

        if DEBUG_MODE:
            print(f"[EMPATHY] +{points} {reason} (Total: {empathy}, Tier: {stranger_relationship_tier})")

    def get_relationship_tier_name(tier):
        """
        Get human-readable name for relationship tier.

        Args:
            tier (int): Relationship tier constant

        Returns:
            str: Tier name
        """
        tier_names = {
            REL_TIER_STRANGER: "Stranger",
            REL_TIER_ACQUAINTANCE: "Acquaintance",
            REL_TIER_FRIEND: "Friend",
            REL_TIER_CONFIDANT: "Confidant",
            REL_TIER_SOULMATE: "Soulmate"
        }
        return tier_names.get(tier, "Unknown")

    def has_enough_empathy(required_level):
        """
        Check if player has sufficient empathy for choice.

        Args:
            required_level (int): Minimum empathy required

        Returns:
            bool: True if player meets requirement
        """
        return empathy >= required_level

    def mark_dialogue_seen(dialogue_key):
        """
        Mark a dialogue line as seen in conversation history.

        Args:
            dialogue_key (str): Key identifying the dialogue
        """
        global stranger_dialogue_seen
        if dialogue_key in stranger_dialogue_seen:
            stranger_dialogue_seen[dialogue_key] = True

    def has_dialogue_seen(dialogue_key):
        """
        Check if player has already seen this dialogue.

        Args:
            dialogue_key (str): Key identifying the dialogue

        Returns:
            bool: True if dialogue was seen before
        """
        return stranger_dialogue_seen.get(dialogue_key, False)

    # ========================================================
    # CHOICE & BRANCHING FUNCTIONS
    # ========================================================

    def can_unlock_choice(empathy_required=0, topics_required=None):
        """
        Determine if a choice should be available to the player.

        Args:
            empathy_required (int): Minimum empathy needed
            topics_required (list): Topics that must be discussed

        Returns:
            bool: True if choice should be available
        """
        # Check empathy gate
        if empathy < empathy_required and not DEBUG_UNLOCK_ALL_CHOICES:
            return False

        # Check topic gates (if any)
        if topics_required:
            # Example: Check if certain conversations happened
            pass

        return True

    def record_choice(choice_label, player_choice):
        """
        Record player's choice for story tracking.

        Args:
            choice_label (str): Label identifying the choice point
            player_choice (str): The choice the player made
        """
        global choice_history
        choice_history[choice_label] = player_choice

        if DEBUG_MODE:
            print(f"[CHOICE] {choice_label}: {player_choice}")

    # ========================================================
    # SCENE MANAGEMENT FUNCTIONS
    # ========================================================

    def change_scene(new_scene):
        """
        Update current scene and track progress.

        Args:
            new_scene (str): Scene identifier from constants
        """
        global current_scene, scenes_visited, game_completion_percent

        current_scene = new_scene
        if new_scene not in scenes_visited:
            scenes_visited.append(new_scene)

        # Update completion percentage (rough estimate)
        total_scenes = 4  # prologue, act1, act2, climax
        game_completion_percent = (len(scenes_visited) / total_scenes) * 100

        if DEBUG_MODE:
            print(f"[SCENE] Now in: {new_scene} ({game_completion_percent:.0f}% complete)")

    def get_current_scene():
        """
        Get the current scene identifier.

        Returns:
            str: Current scene
        """
        return current_scene

    # ========================================================
    # STATE QUERY FUNCTIONS
    # ========================================================

    def is_player_open():
        """Check if player has been emotionally open."""
        return openness_level >= 2

    def is_player_thoughtful():
        """Check if player has engaged in self-reflection."""
        return has_reflected

    def has_player_acknowledged_regret():
        """Check if player has admitted to regrets."""
        return regret_accepted

    def is_special_ending_available():
        """Check if player can unlock the 'truth' ending."""
        return has_asked_identity and empathy >= EMPATHY_THRESHOLD_HIGH

    # ========================================================
    # UTILITY FUNCTIONS
    # ========================================================

    def pause_for_effect(seconds):
        """
        Create a dramatic pause in dialogue.
        Used in Ren'Py labels via: $ pause_for_effect(2.0)

        Args:
            seconds (float): Duration of pause
        """
        renpy.pause(seconds)

    def get_time_since_start():
        """
        Get elapsed time in seconds (approximate).

        Returns:
            int: Seconds since game start
        """
        # This would need to be tracked if you want accurate timing
        return renpy.get_game_runtime()

    def format_stat_display():
        """
        Format game statistics for debug display.

        Returns:
            str: Formatted stats string
        """
        stats = f"""
        === GAME STATS ===
        Empathy: {empathy}/{EMPATHY_THRESHOLD_HIGH}
        Tier: {get_relationship_tier_name(stranger_relationship_tier)}
        Honesty: {openness_level}/2
        Reflection: {'Yes' if has_reflected else 'No'}
        Scene: {current_scene}
        Completion: {game_completion_percent:.0f}%
        """
        return stats

    # ========================================================
    # DEBUG/DEVELOPMENT FUNCTIONS
    # ========================================================

    def debug_set_empathy(value):
        """
        DEVELOPMENT ONLY: Manually set empathy for testing.

        Args:
            value (int): Empathy value to set
        """
        global empathy
        empathy = value
        print(f"[DEBUG] Empathy set to {value}")

    def debug_unlock_all_endings():
        """
        DEVELOPMENT ONLY: Enable access to all ending paths.
        """
        global has_asked_identity, empathy
        has_asked_identity = True
        empathy = EMPATHY_THRESHOLD_HIGH
        print("[DEBUG] All endings unlocked")

    def debug_reset_game():
        """
        DEVELOPMENT ONLY: Reset all game state to defaults.
        """
        global empathy, has_reflected, regret_accepted, has_asked_identity
        global current_scene, scenes_visited, choice_history

        empathy = 0
        has_reflected = False
        regret_accepted = False
        has_asked_identity = False
        current_scene = SCENE_PROLOGUE
        scenes_visited = []
        choice_history = {}

        print("[DEBUG] Game state reset")
