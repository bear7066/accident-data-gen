ACTION_LABELS ={
    # fall: 10
    "fall_forward": {
        "category": "fall_direction",
        "description": "person falls forward and uses hands/arms/knees to break the impact, landing on front of the body",
    },
    "fall_face_first": {
        "category": "fall_direction",
        "description": "person falls straight forward without breaking the fall with hands, landing face or torso first on the floor",
    },
    "fall_backward": {
        "category": "fall_direction",
        "description": "person loses balance and falls straight backward, landing on the back or buttocks",
    },
    "fall_sideways_left": {
        "category": "fall_direction",
        "description": "person falls directly to the left side, landing on the left shoulder, hip, or thigh",
    },
    "fall_sideways_right": {
        "category": "fall_direction",
        "description": "person falls directly to the right side, landing on the right shoulder, hip, or thigh",
    },
    "fall_diagonal_forward_left": {
        "category": "fall_direction",
        "description": "person falls obliquely toward the front-left, landing on the front-left side of the body",
    },
    "fall_diagonal_forward_right": {
        "category": "fall_direction",
        "description": "person falls obliquely toward the front-right, landing on the front-right side of the body",
    },
    "fall_rotational": {
        "category": "fall_direction",
        "description": "person's body twists or spins along the vertical axis during the descent, landing in a contorted or tangled position",
    },


    # fall by some objects: 10    
    "fall_slip_wet_floor": {
        "category": "fall_cause",
        "description": "person walks onto a wet, icy, or slippery surface, losing traction and triggering a fall",
    },
    "fall_trip_obstacle": {
        "category": "fall_cause",
        "description": "person's foot catches on a distinct object or uneven surface on the floor, triggering a trip and fall",
    },
    "fall_trip_own_feet": {
        "category": "fall_cause",
        "description": "person missteps or trips over their own feet/legs while walking, losing stability and falling",
    },
    "fall_lose_balance_standing": {
        "category": "fall_cause",
        "description": "person is in a stationary standing position, suddenly loses balance without external locomotion, and falls",
    },
    "fall_from_chair": {
        "category": "fall_cause",
        "description": "person transitioning from or sitting on a chair/stool loses stability and falls to the floor",
    },
    "fall_from_bed": {
        "category": "fall_cause",
        "description": "person rolls off, slips from, or loses balance at the edge of a bed and falls to the floor",
    },
    "fall_from_wheelchair": {
        "category": "fall_cause",
        "description": "person slides, tips, or falls out from a wheelchair onto the ground",
    },
    "fall_down_stairs": {
        "category": "fall_cause",
        "description": "person loses footing or balance while ascending or descending stairs, tumbling down the steps",
    },
    "fall_while_carrying_object": {
        "category": "fall_cause",
        "description": "person carrying an object loses stability, drops or holds the object, and falls",
    },
    "fall_while_turning": {
        "category": "fall_cause",
        "description": "person initiates an abrupt change of direction or pivot while moving, loses balance, and falls",
    },


    # Medical: 8
    "collapse_sudden_drop": {
        "category": "medical_collapse",
        "description": "person suddenly loses muscle tone and drops straight down vertically to the floor, with no protective extension of arms or legs",
    },
    "collapse_slow_slump": {
        "category": "medical_collapse",
        "description": "person gradually weakens, sways, and slowly slumps or crumples down onto the floor over a few seconds",
    },
    "collapse_with_clutching_body": {
        "category": "medical_collapse",
        "description": "person clutches a specific body part (e.g., chest, head, stomach) in apparent distress or pain immediately before or during the collapse",
    },
    "collapse_with_wall_slide": {
        "category": "medical_collapse",
        "description": "person leans against a wall or furniture for support, then slowly slides downward into a seated or prone position on the floor",
    },
    "collapse_with_stiffening_and_shaking": {
        "category": "medical_collapse",
        "description": "person's body stiffens abruptly, falls rigidly to the floor, followed by visible convulsive movements or shaking of limbs",
    },
    "collapse_with_unilateral_weakness": {
        "category": "medical_collapse",
        "description": "person exhibits sudden asymmetric movement, dragging or sagging on one side of the body, drifting toward that side before falling",
    },
    "collapse_post_transition": {
        "category": "medical_collapse",
        "description": "person successfully transitions from sitting/lying to standing, but sways and collapses within seconds of reaching the upright position",
    },
    "collapse_stumble_loss_of_motor_control": {
        "category": "medical_collapse",
        "description": "person is walking or moving normally, then suddenly experiences a loss of motor coordination, stumbles aimlessly without an external trip/slip obstacle, and falls",
    },

    # accident: 6
    "accident_door_collision": {
        "category": "accident",
        "description": "person collides with a moving door (either swinging open or closing), causing them to lose balance and fall",
    },
    "accident_falling_object_hit": {
        "category": "accident",
        "description": "an object drops from an elevated position, strikes the person, and directly causes them to fall down",
    },
    "accident_one_on_one_collision": {
        "category": "accident",
        "description": "person collides directly with exactly one other moving individual (1-on-1 impact), causing at least one person to fall",
    },
    "accident_crowd_jostle": {
        "category": "accident",
        "description": "person is surrounded by a dense, moving group of people (crowd) and falls due to multi-directional pushing or crowding",
    },
    "accident_collision_with_stationary_object": {
        "category": "accident",
        "description": "person walks or runs directly into a fixed, stationary object (e.g., wall, table, pillar), bounces back or trips, and falls",
    },
    "accident_step_off_edge": {
        "category": "accident",
        "description": "person steps past the edge of an elevated platform, curb, or ledge into empty space, losing footing and falling downward",
    },

    
    # post fall 6: the action after falling 
    "post_fall_motionless": {
        "category": "post_fall",
        "description": "person lies motionless on the floor after a fall, not moving at all",
    },
    "post_fall_struggling_to_get_up": {
        "category": "post_fall",
        "description": "person on the floor after a fall tries repeatedly to push themselves up but fails",
    },
    "post_fall_crawling_for_help": {
        "category": "post_fall",
        "description": "person who has fallen crawls slowly across the floor, reaching for support or help",
    },
    "post_fall_calling_for_help": {
        "category": "post_fall",
        "description": "person lying on the floor after a fall raises an arm and waves for help",
    },
    "post_fall_rolling_in_pain": {
        "category": "post_fall",
        "description": "person on the floor curls up or rolls slightly, clearly in pain after a fall",
    },
    "post_fall_unconscious": {
        "category": "post_fall",
        "description": "person lies face-down or on their side on the floor, completely still and unresponsive",
    },

    # hard negative(10): action similar to accident, fall...
    "hn_sit_down_floor": {
        "category": "hard_negative",
        "description": "person calmly and deliberately sits down on the floor in a controlled motion to rest or read",
    },
    "hn_lie_down_floor": {
        "category": "hard_negative",
        "description": "person deliberately lies down on the floor or on a yoga mat in a controlled motion to relax",
    },
    "hn_stand_up_from_floor": {
        "category": "hard_negative",
        "description": "person who was sitting or lying on the floor calmly stands up in a normal, controlled manner",
    },
    "hn_stand_up_from_chair": {
        "category": "hard_negative",
        "description": "person stands up from a chair normally without stumbling or losing balance",
    },
    "hn_bend_over_pick_up": {
        "category": "hard_negative",
        "description": "person bends at the waist to pick up an object from the floor, then straightens back up",
    },
    "hn_squat_tie_shoes": {
        "category": "hard_negative",
        "description": "person squats or crouches down to tie their shoelaces, then stands back up",
    },
    "hn_yoga_floor_pose": {
        "category": "hard_negative",
        "description": "person performs a yoga pose on the floor such as child's pose, plank, or downward dog",
    },
    "hn_stretching_floor": {
        "category": "hard_negative",
        "description": "person stretches their body while sitting or lying on the floor in a controlled exercise",
    },
    "hn_pushup_situp": {
        "category": "hard_negative",
        "description": "person does pushups or situps on the floor as exercise",
    },
    "hn_play_with_child_floor": {
        "category": "hard_negative",
        "description": "an adult sits or lies on the floor playing with a small child, moving in a relaxed way",
    },
}
