import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'cyan'
    points = []
    shapes = []
    running = True
    instrument = "pencil"
    desk_open = False
    font = pygame.font.SysFont(None, 24)

    button_rect = pygame.Rect(0, 25, 80, 25)
    button_circ = pygame.Rect(90, 25, 80, 25)
    button_sq = pygame.Rect(180, 25, 80, 25)
    button_rt = pygame.Rect(270, 25, 80, 25)
    button_et = pygame.Rect(360, 25, 80, 25)
    button_rh = pygame.Rect(450, 25, 80, 25)

    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_e:
                    instrument = "eraser"
                elif event.key == pygame.K_p:
                    instrument = "pencil"
                elif event.key == pygame.K_i:
                    if desk_open == True:
                        desk_open = False
                    else:
                        desk_open = True
                
                if event.key == pygame.K_1:
                    mode = 'red'
                elif event.key == pygame.K_2:
                    mode = 'green'
                elif event.key == pygame.K_3:
                    mode = 'blue'
                elif event.key == pygame.K_4:
                    mode = 'yellow'
                elif event.key == pygame.K_5:
                    mode = 'white'
                elif event.key == pygame.K_6:
                    mode = 'purple'
                elif event.key == pygame.K_7:
                    mode = 'cyan'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if desk_open:
                    if button_rect.collidepoint(event.pos):
                        instrument = "rectangle"
                        desk_open = False
                    if button_circ.collidepoint(event.pos):
                        instrument = "circle"
                        desk_open = False
                    if button_sq.collidepoint(event.pos):
                        instrument = "square"
                        desk_open = False
                    if button_rt.collidepoint(event.pos):
                        instrument = "right_triangle"
                        desk_open = False
                    if button_et.collidepoint(event.pos):
                        instrument = "equilateral_triangle"
                        desk_open = False
                    if button_rh.collidepoint(event.pos):
                        instrument = "rhombus"
                        desk_open = False

                elif event.button == 1:
                    if instrument == "rectangle":
                        shapes.append(("rectangle", event.pos))
                    elif instrument == "circle":
                        shapes.append(("circle", event.pos))
                    elif instrument == "square":
                        shapes.append(("square", event.pos))
                    elif instrument == "right_triangle":
                        shapes.append(("right_triangle", event.pos))
                    elif instrument == "equilateral_triangle":
                        shapes.append(("equilateral_triangle", event.pos))
                    elif instrument == "rhombus":
                        shapes.append(("rhombus", event.pos))
                    elif instrument == "eraser":
                        eraseAtPosition(event.pos, points, shapes, radius)
                    else:
                        radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                if instrument == "pencil":
                    position = event.pos
                    points = points + [position]
                    points = points[-256:]
                elif instrument == "eraser":
                    eraseAtPosition(event.pos, points, shapes, radius)
                
        screen.fill((0, 0, 0))
        if desk_open:
            pygame.draw.rect(screen, (200, 200, 200), button_rect)
            pygame.draw.rect(screen, (200, 200, 200), button_circ)
            pygame.draw.rect(screen, (200, 200, 200), button_sq)
            pygame.draw.rect(screen, (200, 200, 200), button_rt)
            pygame.draw.rect(screen, (200, 200, 200), button_et)
            pygame.draw.rect(screen, (200, 200, 200), button_rh)

            screen.blit(font.render("Rect", True, (0, 0, 0)),
                    (button_rect.x + 5, button_rect.y + 3))

            screen.blit(font.render("Circle", True, (0, 0, 0)),
                    (button_circ.x + 5, button_circ.y + 3))
            
            screen.blit(font.render("Square", True, (0, 0, 0)),
                    (button_sq.x + 5, button_sq.y + 3))

            screen.blit(font.render("Rt", True, (0, 0, 0)),
                    (button_rt.x + 5, button_rt.y + 3))
            
            screen.blit(font.render("Et", True, (0, 0, 0)),
                    (button_et.x + 5, button_et.y + 3))

            screen.blit(font.render("Rhombus", True, (0, 0, 0)),
                    (button_rh.x + 5, button_rh.y + 3))


        for shape in shapes:
            shape_type, pos = shape
            if shape_type == "rectangle":
                drawRectangle(screen, pos, mode)
            elif shape_type == "circle":
                drawCircle(screen, pos, mode)
            elif shape_type == "square":
                drawSquare(screen, pos, mode)
            elif shape_type == "right_triangle":
                drawRightTriangle(screen, pos, mode)
            elif shape_type == "equilateral_triangle":
                drawEquilateralTriangle(screen, pos, mode)
            elif shape_type == "rhombus":
                drawRhombus(screen, pos, mode)
                
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def eraseAtPosition(pos, points, shapes, radius):
    erase_radius = radius * 2
    i = 0
    while i < len(points):
        point = points[i]
        distance = ((point[0] - pos[0]) ** 2 + (point[1] - pos[1]) ** 2) ** 0.5
        if distance < erase_radius:
            points.pop(i)
        else:
            i += 1
    
    i = 0
    while i < len(shapes):
        shape_type, shape_pos = shapes[i]
        distance = ((shape_pos[0] - pos[0]) ** 2 + (shape_pos[1] - pos[1]) ** 2) ** 0.5
        if distance < erase_radius:
            shapes.pop(i)
        else:
            i += 1


def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'white':
        color = (c2, c2, c2)
    elif color_mode == 'cyan':
        color = (c1, c2, c2)
    elif color_mode == 'purple':
        color = (c2, c1, c2)
    elif color_mode == 'black':
        color = (0, 0, 0)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRightTriangle(screen, pos, color_mode):
    x, y = pos
    color1 = getColor(color_mode)

    p1 = (x, y + 30)
    p2 = (x + 50, y + 30)
    p3 = (x, y - 30)

    pygame.draw.polygon(screen, color1, [p1, p2, p3], 0)

def drawEquilateralTriangle(screen, pos, color_mode):
    x, y = pos
    color = getColor(color_mode)

    p1 = (x - 50, y + 30)
    p2 = (x + 50, y + 30)
    p3 = (x, y - 30)

    pygame.draw.polygon(screen, color, [p1, p2, p3], 0)

def drawRhombus(screen, pos, color_mode):
    x, y = pos
    color = getColor(color_mode)

    p1 = (x, y - 30)
    p2 = (x + 50, y + 30)
    p3 = (x, y + 80)
    p4 = (x - 50, y + 30)

    pygame.draw.polygon(screen, color, [p1, p2, p3, p4], 0)

def drawRectangle(screen, pos, color_mode):
    rect_x = pos[0] - 50
    rect_y = pos[1] - 30
    rect_width = 100
    rect_height = 60
    
    color = getColor(color_mode)
    pygame.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_height))

def drawSquare(screen, pos, color_mode):
    sq_x = pos[0] - 50
    sq_y = pos[1] - 30
    sq_width = 50
    sq_height = 50
    
    color = getColor(color_mode)
    pygame.draw.rect(screen, color, (sq_x, sq_y, sq_width, sq_height))

def drawCircle(screen, pos, color_mode):
    center_x = pos[0]
    center_y = pos[1]
    radius = 40
    
    color = getColor(color_mode)
    pygame.draw.circle(screen, color, (center_x, center_y), radius)

def getColor(color_mode):
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    elif color_mode == 'yellow':
        return (255, 255, 0)
    elif color_mode == 'white':
        return (255, 255, 255)
    elif color_mode == 'cyan':
        return (0, 255, 255)
    elif color_mode == 'purple':
        return (255, 0, 255)
    elif color_mode == 'black':
        return (0, 0, 0)

main()