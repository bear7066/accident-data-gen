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
    SCENES,
)

def build_prompt(action_label: str, seed: int | None = None, duration: int = 5) -> str:
    prompt = ""
    rng = Random(seed)
    action = ACTION_LABELS[action_label]
    time_pattern = TIME_PATTERN
    constraints = CONSTRAINTS
    people = rng.choice(PEOPLES) 
    light = rng.choice(LIGHT)
    camera_viewpoint = rng.choice(CAMERA_VIEWPOINT)
    camera_quality = rng.choice(CAMERA_QUALITY)
    person_position = rng.choice(PERSON_POSITION)
    block = rng.choice(BLOCK)
    scene = rng.choice(list(SCENES.keys())) # pick up scence type
    scene_desc = rng.choice(SCENES[scene]) # access corresponded desc
   

    prompt = f"""
      Create a {duration}-second realistic video.
      Timing: {time_pattern}
      Constraints: {constraints}

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
