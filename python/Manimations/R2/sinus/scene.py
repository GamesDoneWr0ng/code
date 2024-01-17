from manim import *

class SineWaveEmitter(Scene):
    def construct(self):
        # Create a circle and a dot
        circle = Circle(radius=2)
        circle.shift(LEFT*5)

        dot = Dot(circle.point_at_angle(0), color=RED)
        
        # ValueTracker for the angle
        angle_tracker = ValueTracker(0)

        # Update the dot's position to be on the circle's periphery
        dot.add_updater(lambda m: m.move_to(circle.point_at_angle(angle_tracker.get_value())))

        # Create the sine wave using ParametricFunction
        sine_wave = always_redraw(lambda:
            ParametricFunction(
                lambda t: np.array([
                    t-2,
                    2*np.sin(t),
                    0
                ]),
                t_range=np.array([0, angle_tracker.get_value(), 0.01]),
                color=BLUE
            )
        )

        # Add the circle, dot, and sine wave to the scene
        self.add(circle, dot, sine_wave)

        # Rotate the dot around the circle and emit the sine wave
        self.play(angle_tracker.animate.set_value(4 * PI), run_time=8, rate_func=linear)
        self.wait()
