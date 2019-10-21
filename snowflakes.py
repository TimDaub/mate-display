    #for i in range(0, d.h):
    #    spawn = randint(0, 1)
    #    if spawn:
    #       flakes.append([randint(1, d.h - 1), randint(1, d.w - 1)])

    #    for flake in flakes:
    #        flake[1] += 1
    #        d.set_pixel(flake[0], flake[1] % 2, color)

    #    sleep_us(randint(100000, 300000))
    #    d.clear()


    #flakes = []
    #for i in range(0, 20):
    #    spawn = randint(0, 5)
    #    if spawn:
    #       flakes.append([randint(0, d.w), 0])

    #    for flake in flakes:
    #        try:
    #            d.set_pixel(flake[0] + flake[1] % 2, flake[1], color)
    #        except Exception:
    #            pass
    #        flake[1] += 1
    #    sleep_us(500000)
    #    d.clear()
