from random import Random
from action_label import ACTION_LABELS
from variables import (
    TIME_PATTERN,
    CONSTRAINTS,
    PEOPLES,
    LIGHT,
    CAMERA_VIEWPOINT,
    CAMERA_QUALITY,
    PERSON_POSITION,
    BLOCK,
    ACTION_POSITION,
    ACTION_VISIBILITY,
    HARD_NEGATIVE_POSITION,
    HARD_NEGATIVE_VISIBILITY,
    HARD_NEGATIVE_CONSTRAINTS,
    EXTRA_CONSTRAINTS_BY_ACTION,
    SCENES,
    SCENE_BY_ACTION,
)


def _pool_for_action(
    action_label: str,
    category: str,
    action_pool: dict[str, list[str]],
    hard_negative_pool: list[str],
    default_pool: list[str],
) -> list[str]:
    if action_label in action_pool:
        return action_pool[action_label]
    if category == "hard_negative":
        return hard_negative_pool
    return default_pool


def build_prompt(action_label: str, seed: int | None = None, duration: int = 5) -> str:
    prompt = ""
    rng = Random(seed)
    action = ACTION_LABELS[action_label]
    category = action["category"]
    time_pattern = TIME_PATTERN
    constraints = CONSTRAINTS
    people = rng.choice(PEOPLES) 
    light = rng.choice(LIGHT)
    camera_viewpoint = rng.choice(CAMERA_VIEWPOINT)
    camera_quality = rng.choice(CAMERA_QUALITY)
    position_pool = _pool_for_action(
        action_label,
        category,
        ACTION_POSITION,
        HARD_NEGATIVE_POSITION,
        PERSON_POSITION,
    )
    visibility_pool = _pool_for_action(
        action_label,
        category,
        ACTION_VISIBILITY,
        HARD_NEGATIVE_VISIBILITY,
        BLOCK,
    )
    person_position = rng.choice(position_pool)
    block = rng.choice(visibility_pool)
    scene_pool = SCENE_BY_ACTION.get(action_label, list(SCENES.keys()))
    scene = rng.choice(scene_pool) # pick up scence type
    scene_desc = rng.choice(SCENES[scene]) # access corresponded desc
    extra_constraints = []
    if action_label in EXTRA_CONSTRAINTS_BY_ACTION:
        extra_constraints.append(EXTRA_CONSTRAINTS_BY_ACTION[action_label])
    if category == "hard_negative":
        extra_constraints.append(HARD_NEGATIVE_CONSTRAINTS)
    label_constraints = " ".join(extra_constraints)
    label_constraints_line = (
        f"\n      Label-specific constraints: {label_constraints}"
        if label_constraints
        else ""
    )
   

    prompt = f"""
      Create a {duration}-second realistic video.
      Timing: {time_pattern}
      Constraints: {constraints}{label_constraints_line}

      Camera: {camera_viewpoint}. {camera_quality}. The camera is completely static throughout.
      Scene: {scene}. {scene_desc}.
      Lighting: {light}.
      Subject: {people}.
      Position: {person_position}.
      Visibility: {block}.
      Action: {action["description"]}.
    """
    return prompt


if __name__ == '__main__':
    print(build_prompt("fall_from_chair"))
