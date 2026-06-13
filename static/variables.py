"""static variables"""
# important frames appears in 1.5~3.5 seconds
TIME_PATTERN = (
    "The action begins around 1.5 seconds in and completes by 3.5 seconds. "
    "The first 1.5 seconds show the subject in their initial state, " 
    "and the final 1.5 seconds show the resulting state after the action. "
)

CONSTRAINTS = (
    "Realistic human motion, realistic physics, single continuous shot, "
    "no cuts, no zooms, no slow motion, no text overlay, no subtitles, "
    "no watermark, no music, no gore, no graphic injury, "
    "normal color video only, no night vision, no infrared look, no green tint, "
    "no monochrome security-camera filter."
)


"""dynamic variables"""
# 2 elderly people, 2 child, 2 middle-aged, 2 young people 
PEOPLES = [
    "an elderly man in his 70s wearing a cardigan",
    "an elderly woman in her 70s with grey hair",
    "a school-aged boy in a hoodie and sneakers",
    "a child",
    "a middle-aged man in casual clothes",
    "a middle-aged woman in a sweater and jeans",
    "a young adult man in a t-shirt and jeans",
    "a young adult woman in casual clothes",
]


# three kind of light
LIGHT = [
    "normal warm indoor lighting",
    "neutral indoor lighting",
    "bright daylight",
]


# wide angle from corner, 
CAMERA_VIEWPOINT = [
    "CCTV security camera mounted high in the corner, wide angle, static",
    "ceiling-mounted surveillance camera looking down at an angle",
]


# low-resolution, classical, surveilance camera
CAMERA_QUALITY = [
    "normal-color low-resolution security footage with mild compression artifacts",
    "typical color CCTV video with realistic sensor noise",
    "normal-color surveillance camera quality, slightly grainy",
]


PERSON_POSITION = [
    "the person is centered in the middle of the frame",             
    "the person is positioned near the edge of the frame",           
    "the person is in the far background, occupying a small area",   
]


BLOCK = [
    "no blocked, the person's full body is visible throughout",      
    "the person's lower body is partially hidden behind furniture",  
    "the person is briefly occluded by an object passing in front",  
]


ACTION_POSITION = {
    "fall_slip_wet_floor": [
        "the person is centered or near-center and large enough for foot motion to be visible",
    ],
    "fall_from_chair": [
        "the person and the chair are centered or near-center, both clearly visible before and during the fall",
    ],
    "fall_from_bed": [
        "the person and the bed edge are centered or near-center, both clearly visible before and during the fall",
    ],
    "fall_from_wheelchair": [
        "the person and the wheelchair are centered or near-center, both clearly visible before and during the fall",
    ],
    "fall_down_stairs": [
        "the person is centered on the stair steps and occupies enough image area for the tumble to be clear",
    ],
    "fall_while_carrying_object": [
        "the person and the carried object are centered or near-center, both clearly visible before and during the fall",
    ],
    "collapse_with_wall_slide": [
        "the person and the supporting wall or furniture are centered or near-center and clearly visible",
    ],
    "collapse_stumble_loss_of_motor_control": [
        "the person is centered or near-center and large enough for stumbling steps to be visible",
    ],
    "accident_crowd_jostle": [
        "the target person is centered or near-center, with the surrounding crowd visible around them",
    ],
    "accident_collision_with_stationary_object": [
        "the person and the stationary object are centered or near-center, both clearly visible before impact",
    ],
    "hn_sit_down_floor": [
        "the person and clear floor or mat area are centered or near-center, with the full controlled lowering motion visible",
    ],
    "hn_lie_down_floor": [
        "the person and clear floor or mat area are centered or near-center, with the full controlled lying-down motion visible",
    ],
    "hn_stand_up_from_floor": [
        "the person and clear floor or mat area are centered or near-center, with the full controlled stand-up motion visible",
    ],
    "hn_stand_up_from_chair": [
        "the person and chair are centered or near-center, both clearly visible before and during the stand-up motion",
    ],
    "hn_bend_over_pick_up": [
        "the person and the object on the floor are centered or near-center, both clearly visible",
    ],
    "hn_squat_tie_shoes": [
        "the person, shoes, and hands are centered or near-center, all clearly visible",
    ],
    "hn_yoga_floor_pose": [
        "the person is centered on a mat or clear floor area, large enough for the yoga pose to be recognizable",
    ],
    "hn_stretching_floor": [
        "the person is centered on a mat or clear floor area, large enough for the stretching pose to be recognizable",
    ],
    "hn_situp_from_floor": [
        "the person is centered on a mat or clear floor area, lying face-up at the start with the full torso curl-up motion visible",
    ],
    "hn_play_with_child_floor": [
        "the adult and child are centered or near-center, both clearly visible on the floor play area",
    ],
}


ACTION_VISIBILITY = {
    "fall_slip_wet_floor": [
        "no occlusion; the person's full body, both feet, and floor contact are visible throughout",
    ],
    "fall_from_chair": [
        "no occlusion; the person's full body, the chair, and the chair-to-floor fall path are visible throughout",
    ],
    "fall_from_bed": [
        "no occlusion; the person's full body, the bed edge, and the bed-to-floor fall path are visible throughout",
    ],
    "fall_from_wheelchair": [
        "no occlusion; the person's full body, the wheelchair, and the wheelchair-to-floor fall path are visible throughout",
    ],
    "fall_down_stairs": [
        "no occlusion; the person's full body, feet, and multiple stair steps are visible throughout",
    ],
    "fall_while_carrying_object": [
        "no occlusion; the person's full body, hands, feet, and carried object are visible throughout",
    ],
    "collapse_with_wall_slide": [
        "no occlusion; the person's full body and contact with the wall or furniture are visible throughout",
    ],
    "collapse_stumble_loss_of_motor_control": [
        "no occlusion; the person's full body and feet are visible throughout",
    ],
    "accident_crowd_jostle": [
        "no occlusion of the target person; the target person and nearby crowd contacts remain visible",
    ],
    "accident_collision_with_stationary_object": [
        "no occlusion; the person's full body and the stationary object are visible before and during impact",
    ],
    "hn_sit_down_floor": [
        "no occlusion; the person's full body and the floor contact are visible throughout the controlled sit-down",
    ],
    "hn_lie_down_floor": [
        "no occlusion; the person's full body and the mat or clear floor area are visible throughout the controlled lie-down",
    ],
    "hn_stand_up_from_floor": [
        "no occlusion; the person's full body, hands, feet, and floor contact are visible throughout the controlled stand-up",
    ],
    "hn_stand_up_from_chair": [
        "no occlusion; the person's full body, feet, and chair are visible throughout the controlled stand-up",
    ],
    "hn_bend_over_pick_up": [
        "no occlusion; the person's full body, hands, feet, and the picked-up object are visible throughout",
    ],
    "hn_squat_tie_shoes": [
        "no occlusion; the person's full body, shoes, hands, and shoelace area are visible throughout",
    ],
    "hn_yoga_floor_pose": [
        "no occlusion; the person's full body and mat or clear floor area are visible throughout the yoga pose",
    ],
    "hn_stretching_floor": [
        "no occlusion; the person's full body and extended arms or legs are visible throughout the stretch",
    ],
    "hn_situp_from_floor": [
        "no occlusion; the person's full body, face-up starting posture, bent knees or extended legs, and sit-up torso motion are visible throughout",
    ],
    "hn_play_with_child_floor": [
        "no occlusion; the adult, child, and floor play interaction are visible throughout",
    ],
}


HARD_NEGATIVE_POSITION = [
    "the person is centered or near-center and large enough for the controlled action to be visible",
]


HARD_NEGATIVE_VISIBILITY = [
    "no occlusion; the person's full body, hands, feet, and controlled motion are visible throughout",
]


HARD_NEGATIVE_CONSTRAINTS = (
    "This is a hard negative, not a fall event: no falling, no collapse, no stumble, "
    "no distress, no injury behavior, no sudden uncontrolled drop, and no post-fall state. "
    "The subject remains calm and intentionally controls the entire motion. "
    "The final pose must clearly look like ordinary exercise, rest, play, or daily activity."
)


EXTRA_CONSTRAINTS_BY_ACTION = {
    "fall_slip_wet_floor": (
        "The wet or slippery patch must be visible before the fall, and the foot sliding on that patch must be the direct cause of the fall."
    ),
    "fall_from_chair": (
        "The chair or stool must be visible before, during, and after the fall; do not show a bed, wheelchair, or generic standing fall as the main cause."
    ),
    "fall_from_bed": (
        "The person must start seated on the bed edge with hips on the mattress, not standing beside it and not lying in the middle of the bed. The feet, bed edge, slide off the edge, body leaving the mattress, and final landing fully on the floor beside the bed must all be visible."
    ),
    "fall_from_wheelchair": (
        "The person must start seated in the wheelchair, and the wheelchair must remain visible as the person falls out beside it."
    ),
    "fall_down_stairs": (
        "The person must start on the stair steps and fall down multiple steps; do not place the fall mainly on a flat platform or landing."
    ),
    "fall_while_carrying_object": (
        "The carried object must be obvious and remain visible before the loss of balance; the fall must happen while carrying it."
    ),
    "collapse_with_wall_slide": (
        "The body must remain in contact with the wall, railing, or furniture during the downward slide."
    ),
    "collapse_stumble_loss_of_motor_control": (
        "There must be no visible obstacle, collision, or slippery patch; the fall comes from uncoordinated stumbling."
    ),
    "accident_crowd_jostle": (
        "The crowd contact must be visible and must cause the fall; do not show an isolated person falling alone."
    ),
    "accident_collision_with_stationary_object": (
        "The fixed object must be visible before impact, and the impact must directly cause the fall."
    ),
    "hn_situp_from_floor": (
        "This label means sit-up only: the person must start lying face-up on their back, then intentionally curl the torso upward into a seated position. Do not show pushups, planks, face-down exercise, crawling, rolling, or any prone position."
    ),
}


# 6 independent scences
SCENES = {
    "Living room": [
        "a sofa and coffee table in the foreground, a TV mounted on the wall",
        "an armchair near a window, a rug on the wooden floor, a bookshelf against the wall",
        "minimal furniture with a single couch, a side table with a lamp, tiled flooring",
    ],
    "Medical": [
        "a patient bed with side rails, an IV stand beside it, off-white walls",
        "a hospital waiting area with rows of plastic chairs, a reception counter, and overhead fluorescent lights",
        "a hospital corridor with handrails along the walls, doors to patient rooms, vinyl flooring",
    ],
    "Bedroom": [
        "a single bed with a nightstand and lamp, a wardrobe against the wall",
        "a double bed with the covers messy, clothes draped over a chair, a dresser with a mirror",
        "a tidy bedroom with a made bed, a rug at the foot of the bed, curtains drawn halfway",
    ],
    "Bathroom": [
        "a sink with a mirror above, a bathtub with a shower curtain, tiled walls and floor",
        "a small bathroom with a toilet, a sink, and a non-slip bath mat on the floor",
        "an accessible bathroom with grab bars near the toilet and shower, tiled flooring",
    ],
    "Bed area": [
        "a bedroom with a bed edge clearly visible, open floor space beside the bed, and no other furniture blocking the fall path",
        "a hospital room with a patient bed edge clearly visible, side rails lowered, and open floor space beside the bed",
        "a simple bedroom where the bed fills the center of the frame and the floor beside the bed is fully visible",
    ],
    "Chair seating area": [
        "a living room with one clearly visible chair or stool in the center and open floor space around it",
        "a hospital waiting area with one clearly visible chair in the foreground and the floor around it unobstructed",
        "a subway carriage with one clearly visible seat and open floor space directly in front of it",
    ],
    "Wheelchair area": [
        "a hospital room with a clearly visible wheelchair in the center and open floor space beside it",
        "a clinic corridor with a clearly visible wheelchair and no people blocking the view",
        "a living room with a clearly visible wheelchair beside a couch and open floor space around it",
    ],
    "Wet floor area": [
        "a corridor with a shiny wet patch on the floor and a small caution sign nearby",
        "a bathroom with a visible puddle or wet reflective patch on the tile floor",
        "a subway platform with a visible wet reflective patch on the floor, away from the platform edge",
    ],
    "Object carrying path": [
        "a clear corridor where the person carries a box or bag through the center of the frame",
        "a living room with open floor space where the person carries a laundry basket or tray",
        "a hospital corridor where the person carries a visible box, tray, or bag while walking",
    ],
    "Controlled floor activity": [
        "a living room with a yoga mat or clear rug area on the floor, away from furniture edges",
        "a bedroom with a clear floor mat beside the bed and no obstacles around the person",
        "a quiet exercise room with a mat centered in the frame and open floor space around it",
    ],
    "Controlled chair activity": [
        "a living room with one stable chair centered in the frame and open floor space around it",
        "a hospital waiting area with a single clearly visible chair and no crowd blocking the view",
        "a bedroom corner with one stable chair centered in the frame and clear floor around it",
    ],
    "Child play floor": [
        "a living room floor with a small child, toys clearly visible, and an adult sitting or kneeling nearby",
        "a playroom-like floor area with toys spread out, a small child visible, and an adult interacting calmly",
        "a bedroom floor with a small child and toys visible, with an adult sitting or kneeling nearby",
    ],
    "Subway Station": [
        "a subway platform with yellow tactile strips along the edge, a train arriving in the background, overhead signage",
        "an empty subway platform with tiled walls, advertisement panels, benches along the wall",
        "a crowded subway platform with passengers waiting, a digital arrival display, fluorescent lighting",
    ],
    "Subway stairs": [
        "a subway stairway connecting the platform and concourse, with visible steps filling the center of the frame and metal handrails on both sides",
        "a stairwell inside a subway station, with the person already on the steps before the fall, railings visible, and the landing at the bottom in view",
        "a downward flight of subway stairs beside the platform, with multiple steps clearly visible and no flat platform area dominating the frame",
    ],
    "Subway carriage": [
        "the interior of a subway carriage with rows of side-facing seats, vertical handrails, overhead grab handles",
        "a subway carriage in motion with a few standing passengers holding onto poles, sliding doors visible at the end", 
        "an empty subway carriage with hard plastic seats, metal handrails, route map above the windows"
    ]
}


SCENE_BY_ACTION = {
    "fall_slip_wet_floor": ["Wet floor area"],
    "fall_from_bed": ["Bed area"],
    "fall_from_chair": ["Chair seating area"],
    "fall_from_wheelchair": ["Wheelchair area"],
    "fall_down_stairs": ["Subway stairs"],
    "fall_while_carrying_object": ["Object carrying path"],
    "hn_sit_down_floor": ["Controlled floor activity"],
    "hn_lie_down_floor": ["Controlled floor activity"],
    "hn_stand_up_from_floor": ["Controlled floor activity"],
    "hn_stand_up_from_chair": ["Controlled chair activity"],
    "hn_bend_over_pick_up": ["Controlled floor activity"],
    "hn_squat_tie_shoes": ["Controlled floor activity"],
    "hn_yoga_floor_pose": ["Controlled floor activity"],
    "hn_stretching_floor": ["Controlled floor activity"],
    "hn_situp_from_floor": ["Controlled floor activity"],
    "hn_play_with_child_floor": ["Child play floor"],
    # Disabled with `accident_step_off_edge` in action_label.py.
    # "accident_step_off_edge": ["Subway Station"],
}
