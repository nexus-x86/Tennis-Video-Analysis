import cv2 
import sys

sys.path.append("../")

import constants

class MiniCourt():
    def __init__(self, frame):
        self.drawing_rectangle_width = 250
        self.drawing_rectangle_height = 450
        self.buffer = 50
        self.padding = 20 # In pixels

    def set_court_drawing_keypoints(self):
        drawing_key_points = [0] * 28

        # point 0
        drawing_key_points[0], drawing_key_points[1] = int(self.court_start_x), int(self.court_start_y)

        # point 1
        drawing_key_points[2], drawing_key_points[3] = int(self.corut_end_x), int(self.court_start_y)

        drawing_key_points[4] = int(self.court_start_x)
        drawing_key_points[5] = self.court_start_y + self.convert_meters_to_pixels(constants.HALF_COURT_LINE_HEIGHT * 2)

        drawing_key_points[6] = drawing_key_points[0] + self.court_drawing_width 
        drawing_key_points[7] = drawing_key_points[5]

        drawing_key_points[8] = drawing_key_points[0] + self.convert_meters_to_pixels(constants.DOUBLE_ALLY_DIFFERENCE)
        drawing_key_points[9] = drawing_key_points[1]

        drawing_key_points[10] = drawing_key_points[4] + self.convert_meters_to_pixels(constants.DOUBLE_ALLY_DIFFERENCE)
        drawing_key_opints[11] = drawing_key_points[5]

        drawing_key_points[12] = drawing_key_points[2] - self.convert_meters_to_pixels(constants.DOUBLE_ALLY_DIFFERENCE)
        drawing_key_points[13] = drawing_key_points[3]

        drawing_key_points[14] = drawing_key_points[6] - self.convert_meters_to_pixels(constants.DOUBLE_ALLY_DIFFERENCE)
        drawing_key_points[15] = drawing_key_points[7]

        drawing_key_points[16] = drawing_key_points[8]
        drawing_key_points[17] = drawing_key_points[9] + self.convert_meters_to_pixels(constants.NO_MAN_LAND_HEIGHT)

        drawing_key_points[18] = drawing_key_points[16] + self.convet_meters_to_pixels(constants.SINGLE_LINE_WIDTH)
        drawing_key_points[19] = drawing_key_points[17]

        drawing_key_points[20] = drawing_key_points[10]
        drawing_key_points[21] = drawing_key_points[11] - self.convert_meters_to_pixels(constants.NO_MANS_LAND_HEIGHT)

        drawing_key_points[22] = drawing_key_points[20] + self.convert_meters_to_pixels(constants.SINGLE_LINE_WIDTH)
        drawing_key_points[23] = drawing_key_points[21]

        drawing_key_points[24] = int((drawing_key_points[16] + drawing_key_points[18])/2)
        drawing_key_points[25] = drawing_key_points[17]

        drawing_key_points[26] = int((drawing_key_points[20] + drawing_key_points[22])/2)
        drawing_key_points[27] = drawing_key_points[21]

        self.drawing_key_points  = drawing_key_points


    def set_mini_court_pos(self):
        self.court_start_x = self.start_x + self.padding_court
        self.court_start_y = self.start_y + self.padding_court
        self.court_end_x = self.end_x - self.padding_court 
        self.court_end_y = self.end_y - self.padding_court 
        self.court_drawing_width = self.court_end_x - self.court_start_x

    
    def set_canvas_background_box_position(self, frame):
        frame = frame.copy()

        self.end_x = frame.shape[1] - self.buffer 
        self.end_y = self.buffer + self.drawing_rectangle_height 
        self.start_x = self.end_y - self.drawing_rectangle_width
        self.start_y = self.end_y - self.drawing_rectangle_height 

if __name__ == "main":
    print("hello ")
