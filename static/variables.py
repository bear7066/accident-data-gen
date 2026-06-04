"""static variables"""
# important frames appears in 1.5~3.5 seconds
TIME_PATTERN = (
    "The action begins around 1.5 seconds in and completes by 3.5 seconds. "
    "The first 1.5 seconds show the subject in their initial state," 
    "and the final 1.5 seconds show the resulting state after the action. "
)

CONSTRAINTS = (
    "Realistic human motion, realistic physics, single continuous shot,"
    "no cuts, no zooms, no slow motion, no text overlay, no subtitles,"
    "no watermark, no music, no gore, no graphic injury."
)


"""dynamic variables"""
# 2 elderly people, 2 child, 2 middle-aged, 2 young people 
PEOPLES = [
    "an elderly man in his 70s wearing a cardigan",
    "an elderly woman in her 70s with grey hair",
    "a school-aged boy in a hoodie and sneakers",
    "a child wearing a birthday party hat blowing a whistle",
    "a middle-aged man in casual clothes",
    "a middle-aged woman in a sweater and jeans",
    "a young adult man in a t-shirt and jeans",
    "a young adult woman in casual clothes",
]


# three kind of light
LIGHT = [
    "night vision with low-light",
    "dim evening lighting",
    "bright daylight",
]


# wide angle from corner, 
CAMERA_VIEWPOINT = [
    "CCTV security camera mounted high in the corner, wide angle, static",
    "ceiling-mounted surveillance camera looking down at an angle",
]


# low-resolution, classical, surveilance camera
CAMERA_QUALITY = [
    "low-resolution security footage with mild compression artifacts",
    "typical CCTV video with realistic sensor noise",
    "surveillance camera quality, slightly grainy",
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


# 6 independent scences
SCENES = {
    "Living room": [
        "a sofa and coffee table in the foreground, a TV mounted on the wall",
        "an armchair near a window, a rug on the wooden floor, a bookshelf against the wall",
        "minimal furniture with a single couch, a side table with a lamp, tiled flooring",
    ],
    "Medical": [
        "a patient bed with side rails, an IV stand beside it, pale green walls",
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
    "Subway Station": [
        "a subway platform with yellow tactile strips along the edge, a train arriving in the background, overhead signage",
        "an empty subway platform with tiled walls, advertisement panels, benches along the wall",
        "a crowded subway platform with passengers waiting, a digital arrival display, fluorescent lighting",
    ],
    "Subway carriage": [
        "the interior of a subway carriage with rows of side-facing seats, vertical handrails, overhead grab handles",
        "a subway carriage in motion with a few standing passengers holding onto poles, sliding doors visible at the end", 
        "an empty subway carriage with hard plastic seats, metal handrails, route map above the windows"
    ]
}
