import numpy as np


def combine(picture, background, show_progress=False):

    picture_height, picture_width, _ = picture.shape

    background_height, background_width, _ = background.shape

    assert background_height >= picture_height and background_width >= picture_width, "Background image dimensions must be equal to or greater than picture dimensions"

    new_picture = np.zeros([picture_height, picture_width, 3], dtype=np.uint8)

    for h in range(picture_height):
        if(show_progress):
            print(f' progress {int((h/picture_height)*100)}%', end="\r")

        for w in range(picture_width):

            picture_pixel = picture[h, w]
            (p_red, p_green, p_blue) = picture_pixel

            is_picture_pixel_green = p_green > 40 and p_green > 1.4 * \
                p_red and p_green > 1.4 * p_blue

            background_pixel = background[h, w]

            selected_pixel = background_pixel if is_picture_pixel_green else picture_pixel

            new_picture[h, w] = selected_pixel

    return new_picture
