def set_color(p):
    colormap = ['orange', 'b', 'g', 'c', 'm', 'y']

    if p.belong_to is not None:
        label = p.belong_to
        return colormap[label]
    else:
        return 'gray'
