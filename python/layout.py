def line(ch, width=1):
    return [ch * width]

def block(ch, width, height = None):
    height = height or width
    return [ch * width for i in range(height)]

def width(elem):
    return len(elem[0])

def height(elem):
    return len(elem)

def draw(elem):
    for i in elem:
        print(i)

def above(a, b):
    top = widen(a, width(b))
    bottom = widen(b, width(a))
    return top + bottom

def beside(a, b):
    left = heighten(a, height(b))
    right = heighten(b, height(a))
    return list(t[0] + t[1] for t in zip(left, right))

def widen(elem, new_width):
    diff = new_width - width(elem)
    if diff <= 0:
        return elem
    else:
        h = height(elem)
        lpad = block(' ', diff // 2, h)
        rpad = block(' ', diff - width(lpad), h)
        return beside(beside(lpad, elem), rpad)

def heighten(elem, new_height):
    diff = new_height - height(elem)
    if diff <= 0:
        return elem
    else:
        w = width(elem)
        top = block(' ', w, diff // 2)
        bottom = block(' ', w, diff - height(top))
        return above(above(top, elem), bottom)

def spiral(num_edges, direction=0):
    corner = line('+')
    if num_edges == 1:
        return corner
    space = line(' ')
    sp = spiral(num_edges - 1, (direction + 3) % 4)
    vertical = block('|', 1, height(sp))
    horizontal = line('-', width(sp))
    if direction == 0:
        return above(beside(corner, horizontal), beside(sp, space))
    elif direction == 1:
        return beside(above(sp, space), above(corner, vertical))
    elif direction == 2:
        return above(beside(space, sp), beside(horizontal, corner))
    else:
        return beside(above(vertical, corner), above(space, sp))

if __name__ == '__main__':
    lines = [['*' * (2 * i - 1)] for i in range(1, 5)]
    t = lines[0]
    for i in lines[1:]:
        t = above(t, i)

    draw(t)
    draw(above(t, block('-', 4)))
    draw(spiral(20))
