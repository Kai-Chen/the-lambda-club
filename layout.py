def line(ch, width):
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

if __name__ == '__main__':
    lines = [['*' * (2 * i - 1)] for i in range(1, 5)]
    t = lines[0]
    for i in lines[1:]:
        t = above(t, i)

    draw(t)
    draw(above(t, block('-', 4)))
