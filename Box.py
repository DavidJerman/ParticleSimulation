class Box:
    TIME_SCALE = 3

    def __init__(self, max_x, max_y, n=10):
        self.max_x = max_x
        self.max_y = max_y
        self.num_of_particles = n
        self.particles = []

    def add_particle(self, new_particle):
        if new_particle.hit_wall():
            return
        for particle in self.particles:
            if particle.hit(new_particle):
                return
        self.particles.append(new_particle)

    def update(self):
        for particle in self.particles:
            for temp_particle in self.particles:
                particle.collide(temp_particle)
            particle.update(self.TIME_SCALE)

    def draw(self, win):
        for particle in self.particles:
            particle.draw(win)
