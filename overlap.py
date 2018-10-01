import math


def get_overlap_area(box1, box2):
    """Finds overlap area if the two boxes overlap each other

    :param box1: Coordinates in the format of diagonal points.
        top-left and bottom-right OR top-right and bottom-left.
        Ex. [(100,50),(300,150)]
    :type box1: list

    :param box2: Coordinates in the format of diagonal points.
        top-left and bottom-right OR top-right and bottom-left.
        Ex. [(100,50),(300,150)]
    :type box2: list

    :return: Returns the overlap area
    :rtype: int
    """
    box1_x1, box1_y1 = box1[0]
    box1_x2, box1_y2 = box1[1]

    box2_x1, box2_y1 = box2[0]
    box2_x2, box2_y2 = box2[1]
    # Calculate min and max x,y for box 1
    min_x1, max_x1 = min(box1_x1, box1_x2), max(box1_x1, box1_x2)
    min_y1, max_y1 = min(box1_y1, box1_y2), max(box1_y1, box1_y2)

    # Calculate min and max x,y for box 2
    min_x2, max_x2 = min(box2_x1, box2_x2), max(box2_x1, box2_x2)
    min_y2, max_y2 = min(box2_y1, box2_y2), max(box2_y1, box2_y2)

    # Check x overlap using min-x and max-x of both boxes
    x_overlap = max(0, min(max_x1, max_x2) - max(min_x1, min_x2))
    # Check y overlap using min-y and max-y of word against min-y and max-y of box
    y_overlap = max(0, min(max_y1, max_y2) - max(min_y1, min_y2))

    overlapArea = x_overlap * y_overlap
    return overlapArea


def distance_c_boxes(box1, box2):
    """Finds distance between centers of two boxes

    :param box1: Coordinates in the format of diagonal points.
        top-left and bottom-right OR top-right and bottom-left.
        Ex. [(100,50),(300,150)]
    :type box1: list

    :param box2: Coordinates in the format of diagonal points.
        top-left and bottom-right OR top-right and bottom-left.
        Ex. [(100,50),(300,150)]
    :type box2: list

    :return: Returns the distance
    :rtype: float
    """
    box1_x1, box1_y1 = box1[0]
    box1_x2, box1_y2 = box1[1]

    box2_x1, box2_y1 = box2[0]
    box2_x2, box2_y2 = box2[1]
    # center of box1
    cent_x1 = (box1_x1 + box1_x2) / 2
    cent_y1 = (box1_y1 + box1_y2) / 2
    # center of box2
    cent_x2 = (box2_x1 + box2_x2) / 2
    cent_y2 = (box2_y1 + box2_y2) / 2

    distance = math.sqrt((cent_x2 - cent_x1) ** 2 + (cent_y2 - cent_y1) ** 2)
    return distance


def test():
    box1 = [(100, 50), (300, 150)]
    box2 = [(100, 50), (300, 150)]
    overlap_area = get_overlap_area(box1, box2)
    distance = distance_c_boxes(box1, box2)
    print(f'Overlap area is {overlap_area}')
    print(f'Distance between the centers of two boxes is {distance}')


if __name__ == '__main__':
    test()
