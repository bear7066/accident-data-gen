ACTION_LABELS ={
    # different fall
    # "fall_forward": {
    #     "category": "fall_direction",
    #     "description": "person falls forward and uses hands/arms/knees to break the impact, landing on front of the body",
    # },
    # "fall_face_first": {
    #     "category": "fall_direction",
    #     "description": "person falls straight forward without breaking the fall with hands, landing face or torso first on the floor",
    # },
    # "fall_backward": {
    #     "category": "fall_direction",
    #     "description": "person loses balance and falls straight backward, landing on the back or buttocks",
    # },
    # "fall_sideways_left": {
    #     "category": "fall_direction",
    #     "description": "person falls directly to the left side, landing on the left shoulder, hip, or thigh",
    # },
    # "fall_sideways_right": {
    #     "category": "fall_direction",
    #     "description": "person falls directly to the right side, landing on the right shoulder, hip, or thigh",
    # },
    # "fall_diagonal_forward_left": {
    #     "category": "fall_direction",
    #     "description": "person falls obliquely toward the front-left, landing on the front-left side of the body",
    # },
    # "fall_diagonal_forward_right": {
    #     "category": "fall_direction",
    #     "description": "person falls obliquely toward the front-right, landing on the front-right side of the body",
    # },
    # "fall_rotational": {
    #     "category": "fall_direction",
    #     "description": "person's body twists or spins along the vertical axis during the descent, landing in a contorted or tangled position",
    # },


    # fall by some objects: 10    
    # "fall_slip_wet_floor": {
    #     "category": "fall_cause",
    #     "description": "person clearly steps onto a visible wet, shiny, or slippery patch on the floor; one or both feet slide out, the body loses traction, and the person falls to the floor",
    # },
    # Disabled after QC: cues are often not visible enough to separate from generic falls.
    # "fall_trip_obstacle": {
    #     "category": "fall_cause",
    #     "description": "person's foot catches on a distinct object or uneven surface on the floor, triggering a trip and fall",
    # },
    # "fall_trip_own_feet": {
    #     "category": "fall_cause",
    #     "description": "person missteps or trips over their own feet/legs while walking, losing stability and falling",
    # },
    # "fall_lose_balance_standing": {
    #     "category": "fall_cause",
    #     "description": "person is in a stationary standing position, suddenly loses balance without external locomotion, and falls",
    # },
    "fall_from_chair": {
        "category": "fall_cause",
        "description": "person starts seated on a clearly visible chair or stool; while shifting weight or starting to stand, the chair remains visible as the person loses stability and falls from the chair to the floor",
    },
    "fall_from_bed": {
        "category": "fall_cause",
        "description": "person starts sitting on the visible edge of the bed with hips on the mattress and both feet hanging off or touching the floor beside the bed; the person's center of mass slips past the bed edge, the body leaves the mattress, and the person lands fully on the floor beside the bed",
    },
    "fall_from_wheelchair": {
        "category": "fall_cause",
        "description": "person starts seated in a clearly visible wheelchair; the wheelchair stays visible as the person slides, tips, or falls out of it and lands on the floor next to the wheelchair",
    },
    # "fall_down_stairs": {
    #     "category": "fall_cause",
    #     "description": "person starts on the stair steps, loses footing while ascending or descending, and visibly tumbles down multiple steps rather than merely falling on a flat landing or platform",
    # },
    # "fall_while_carrying_object": {
    #     "category": "fall_cause",
    #     "description": "person walks while carrying a clearly visible object such as a box, bag, tray, or laundry basket; the object stays visible as the person loses stability, drops or clutches it, and falls",
    # },
    # Disabled after QC: turning cue is not consistently clear.
    # "fall_while_turning": {
    #     "category": "fall_cause",
    #     "description": "person initiates an abrupt change of direction or pivot while moving, loses balance, and falls",
    # },


    # Medical: 8
    # Disabled after generation/QC: missing or visually weak medical-specific cues.
    # "collapse_sudden_drop": {
    #     "category": "medical_collapse",
    #     "description": "person suddenly loses muscle tone and drops straight down vertically to the floor, with no protective extension of arms or legs",
    # },
    # "collapse_slow_slump": {
    #     "category": "medical_collapse",
    #     "description": "person gradually weakens, sways, and slowly slumps or crumples down onto the floor over a few seconds",
    # },
    # "collapse_with_clutching_body": {
    #     "category": "medical_collapse",
    #     "description": "person clutches a specific body part (e.g., chest, head, stomach) in apparent distress or pain immediately before or during the collapse",
    # },
    # "collapse_with_wall_slide": {
    #     "category": "medical_collapse",
    #     "description": "person visibly leans against a wall, handrail, or furniture for support, keeps contact with it, then slowly slides downward into a seated or prone position on the floor",
    # },
    # "collapse_with_stiffening_and_shaking": {
    #     "category": "medical_collapse",
    #     "description": "person's body stiffens abruptly, falls rigidly to the floor, followed by visible convulsive movements or shaking of limbs",
    # },
    # "collapse_with_unilateral_weakness": {
    #     "category": "medical_collapse",
    #     "description": "person exhibits sudden asymmetric movement, dragging or sagging on one side of the body, drifting toward that side before falling",
    # },
    # "collapse_post_transition": {
    #     "category": "medical_collapse",
    #     "description": "person successfully transitions from sitting/lying to standing, but sways and collapses within seconds of reaching the upright position",
    # },
    # "collapse_stumble_loss_of_motor_control": {
    #     "category": "medical_collapse",
    #     "description": "person is walking normally with no visible obstacle, then shows sudden loss of motor coordination with irregular steps, swaying, and aimless stumbling before falling",
    # },

    # accident: 6
    # Disabled after generation/QC: accident mechanism is missing or hard to verify.
    # "accident_door_collision": {
    #     "category": "accident",
    #     "description": "person collides with a moving door (either swinging open or closing), causing them to lose balance and fall",
    # },
    # "accident_falling_object_hit": {
    #     "category": "accident",
    #     "description": "an object drops from an elevated position, strikes the person, and directly causes them to fall down",
    # },
    # "accident_one_on_one_collision": {
    #     "category": "accident",
    #     "description": "person collides directly with exactly one other moving individual (1-on-1 impact), causing at least one person to fall",
    # },
    # "accident_crowd_jostle": {
    #     "category": "accident",
    #     "description": "person is visibly surrounded by a dense moving crowd; repeated body contact or pushing from nearby people causes the person to lose balance and fall",
    # },
    # "accident_collision_with_stationary_object": {
    #     "category": "accident",
    #     "description": "person walks or runs directly into a clearly visible fixed object such as a wall, table, bench, or pillar, bounces back or trips from the impact, and falls",
    # },
    # "accident_step_off_edge": {
    #     "category": "accident",
    #     "description": "person steps past the edge of an elevated platform, curb, or ledge into empty space, losing footing and falling downward",
    # },

    
    # post fall 6: the action after falling 
    # "post_fall_motionless": {
    #     "category": "post_fall",
    #     "description": "person is already on the floor after a fall and remains motionless for the whole clip, with no attempt to sit, crawl, or stand",
    # },
    # "post_fall_struggling_to_get_up": {
    #     "category": "post_fall",
    #     "description": "person is already on the floor after a fall and repeatedly tries to push up with arms or knees but fails to stand",
    # },
    # "post_fall_crawling_for_help": {
    #     "category": "post_fall",
    #     "description": "person is already on the floor after a fall and slowly crawls across the floor, reaching toward a wall, furniture, doorway, or other support",
    # },
    # duplicate
    # "post_fall_calling_for_help": {
    #     "category": "post_fall",
    #     "description": "person lying on the floor after a fall raises an arm and waves for help",
    # },
    # "post_fall_rolling_in_pain": {
    #     "category": "post_fall",
    #     "description": "person is already on the floor after a fall and curls up, rolls slightly, or clutches the body in apparent pain without standing up",
    # },
    # hard to distinguish from purely fall
    # "post_fall_unconscious": {
    #     "category": "post_fall",
    #     "description": "person lies face-down or on their side on the floor, completely still and unresponsive",
    # },

    # hard negative(10): action similar to accident, fall...
    # "hn_sit_down_floor": {
    #     "category": "hard_negative",
    #     "description": "person calmly and deliberately lowers themself from standing to a seated position on the floor, using controlled balance and showing no stumble, collapse, or distress",
    # },
    # "hn_lie_down_floor": {
    #     "category": "hard_negative",
    #     "description": "person deliberately kneels or sits first, then lies down on the floor or a yoga mat in a slow controlled motion to relax, with no sudden drop or injury behavior",
    # },
    # "hn_stand_up_from_floor": {
    #     "category": "hard_negative",
    #     "description": "person begins in a relaxed seated or exercise pose on the floor and calmly stands up in a normal controlled manner, without struggling or appearing injured",
    # },
    # "hn_stand_up_from_chair": {
    #     "category": "hard_negative",
    #     "description": "person begins seated on a clearly visible chair and stands up normally in one controlled motion without stumbling, falling, or losing balance",
    # },
    # "hn_bend_over_pick_up": {
    #     "category": "hard_negative",
    #     "description": "person bends at the waist to pick up a clearly visible small object from the floor, grasps it, and straightens back up in a controlled motion",
    # },
    # "hn_squat_tie_shoes": {
    #     "category": "hard_negative",
    #     "description": "person squats or crouches beside their clearly visible shoes, uses both hands near the shoelaces, then stands back up in a controlled motion",
    # },
    # "hn_yoga_floor_pose": {
    #     "category": "hard_negative",
    #     "description": "person deliberately performs a recognizable yoga pose on a mat or clear floor area, such as child's pose, plank, or downward dog, with smooth controlled movement",
    # },
    # "hn_stretching_floor": {
    #     "category": "hard_negative",
    #     "description": "person performs a clear stretching exercise while sitting or lying on the floor, extending arms or legs deliberately with calm controlled movement",
    # },
    # "hn_situp_from_floor": {
    #     "category": "hard_negative",
    #     "description": "person starts lying flat on their back on a floor mat, calmly performs sit-up motions by curling the torso upward into a seated upright position, then returns to lying on the back; no pushups, no plank pose, no face-down exercise, no fall, collapse, or distress",
    # },
    # "hn_play_with_child_floor": {
    #     "category": "hard_negative",
    #     "description": "an adult and a clearly visible child sit or kneel on the floor together, playing calmly with toys or gestures in a relaxed controlled way",
    # },
    # "hn_near_fall_no_fall": {
    #     "category": "hard_negative",
    #     "description": "person briefly slips, trips, missteps, or sways as if about to fall, but quickly regains balance and remains standing or walking; the person never touches the floor, never collapses, and never enters a post-fall state",
    # },
}
