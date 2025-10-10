import colorgram
new_list = []
colors = colorgram.extract('/Users/hossein/python/day18/200430102527-01-damien-hirst-severed-spots.jpg', 10)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    new_list.append(new_color)

print(new_list)