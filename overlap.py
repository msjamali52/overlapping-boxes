import math

# Box1 co-ordinates
box1_x1, box1_y1 = (300,50)
box1_x2, box1_y2 = (100,150)

# Box2 co-ordinates
box2_x1, box2_y1 = (300,50)
box2_x2, box2_y2 = (100,150)


# Calculate min and max x,y for box 1
min_x1 = min(box1_x1,box1_x2)
max_x1 = max(box1_x1,box1_x2)
min_y1 = min(box1_y1,box1_y2)
max_y1 = max(box1_y1,box1_y2)

# Calculate min and max x,y for box 2
min_x2 = min(box2_x1,box2_x2)
max_x2 = max(box2_x1,box2_x2)
min_y2 = min(box2_y1,box2_y2)
max_y2 = max(box2_y1,box2_y2)


# Check x overlap using min-x and max-x of both boxes
x_overlap = max(0, min(max_x1, max_x2) - max(min_x1, min_x2))
# Check y overlap using min-y and max-y of word against min-y and max-y of box
y_overlap = max(0, min(max_y1, max_y2) - max(min_y1, min_y2))

# Calculate overlap area using overlapping width and height
overlapArea = x_overlap * y_overlap
if overlapArea != 0:
    print('Boxes are overlapping with each other, overlap area is ',overlapArea,' pixels')
else:
    # find distance between centers of both boxes

    # center of box1
    cent_x1 = (box1_x1 + box1_x2) / 2
    cent_y1 = (box1_y1 + box1_y2) / 2

    # center of box2
    cent_x2 = (box2_x1 + box2_x2) / 2
    cent_y2 = (box2_y1 + box2_y2) / 2

    distance = math.sqrt((cent_x2 - cent_x1) ** 2 + (cent_y2 - cent_y1) ** 2)
    print('Distance between centers of two boxes is ',distance,' pixels')