import io

from PIL import Image, ImageDraw

from .lambdas import flatten_grid, filter_odd_numbers, md5, get_color, get_random_string, get_random_color


class Identicon:
    bg = '#f0f0f0'

    def __init__(self, key=None, rand=False):
        if not key:
            self.hash = md5(get_random_string())
            self.color = get_color(self.hash)
        else:
            self.hash = md5(key)
            self.color = get_random_color() if rand else get_color(self.hash)
        self.image = self.build_identicon()

    def build_identicon(self):
        grid = self.build_grid(self.hash)
        flat_grid = flatten_grid(grid)
        filtered_grid = filter_odd_numbers(flat_grid)
        pixel_map = self.build_pixel_map(filtered_grid)
        image = self.draw_image(pixel_map, filtered_grid)
        return image

    def show(self):
        self.image.show()

    def byte_array(self):
        byte_array = io.BytesIO()
        self.image.save(byte_array, format='PNG')
        return byte_array.getvalue()

    def build_grid(self, hash):
        # cut off 2 front bytes to make hash even 30 bytes
        hash_30 = hash[2:]
        # split the hash into 5 lists of 6 bytes each,
        # each 6 bytes split into 3 hex numbers converted to int
        temp_list = [[int(hash_30[j:j + 2], 16) for j in range(i, i + 6, 2)]
                     for i in range(0, 30, 6)]
        # now we create a "mirror" effect in each of thsoe 5 lists
        # ([1, 2, 3] becomes [1, 2, 3, 2, 1])
        grid = list(map(lambda l: l + [l[1], l[0]], temp_list))
        return grid

    def build_pixel_map(self, filtered_grid):
        pixel_map = []
        for i, v in enumerate(filtered_grid):
            horizontal = ((i % 5) * 50) + 20
            vertical = ((i // 5) * 50) + 20
            top_left = (horizontal, vertical)
            bottom_right = (horizontal + 50, vertical + 50)
            pixel_map.append((top_left, bottom_right))
        return pixel_map

    def draw_image(self, pixel_map, filtered_grid):
        img = Image.new("RGB", (290, 290), self.bg)
        draw = ImageDraw.Draw(img)
        for grid_val, area in zip(filtered_grid, pixel_map):
            if grid_val:
                draw.rectangle(area, fill=self.color)
        return img
