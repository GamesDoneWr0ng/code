from manim import *

down = 2

position1 = -0.17
angle1 = -0.40

class CartpoleMobject(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.cart = Rectangle(color=RED, height=1, width=2)
        self.cart.set_fill(ManimColor((112,56,105)), opacity=1)
        self.cart.shift(DOWN*down)

        self.pole = Line(start=self.cart.get_top(), end=self.cart.get_top() + UP * 3)
        self.pole.stroke_width = 15

        self.track = Line(start=7*LEFT+DOWN*down, end=7*RIGHT+DOWN*down)
        self.track.z_index = -1

        self.add(self.cart)
        self.add(self.pole)
        self.add(self.track)

    def observation(self):
        obs = VGroup()

        middle = DashedLine(self.cart.get_top(), self.cart.get_top()+UP*6)
        obs.add(middle)

        angle = Angle(self.pole, middle, 1)
        obs.add(angle)

        theta = MathTex(r"\boldsymbol{\theta}")
        theta.move_to(self.cart.get_top() + RIGHT*np.sin(-angle1/2) * 1.5 + UP*np.cos(angle1/2) * 1.5)
        print(theta.animation_override_for(FadeIn))
        obs.add(theta)

        text = VGroup(Tex(r"Pole angle"),
                      Tex(r"Angular velocity"),
                      Tex(r"Cart position"),
                      Tex(r"Cart velocity")
                      )
        text.arrange(DOWN)
        text.to_corner(UP+LEFT)
        obs.add(text)

        angleVelocity = CurvedArrow(self.pole.get_end(), rotate_vector(self.pole.get_end()-self.pole.get_start(), -PI/6) + self.pole.get_start(), angle=-PI/6)
        obs.add(angleVelocity)

        thetaDot = MathTex(r"\dot{\boldsymbol{\theta}}")
        thetaDot.move_to(rotate_vector(self.pole.get_end()-self.pole.get_start(), -PI/5) + self.pole.get_start())
        obs.add(thetaDot)

        distance = Arrow(start=self.cart.get_center()+DOWN+LEFT*7, 
                         end=self.cart.get_center()+DOWN
                         )
        x = MathTex(r"\boldsymbol{x}")
        x.move_to(self.cart.get_center()+DOWN+RIGHT/2)
        obs.add(distance)
        obs.add(x)

        speed = Arrow(start=self.cart.get_corner(DL),
                      end=self.cart.get_corner(DL)+LEFT*2
                      )
        
        xDot = MathTex(r"\dot{\boldsymbol{x}}")
        xDot.move_to(self.cart.get_corner(DL)+LEFT*2.5)
        obs.add(speed)
        obs.add(xDot)

        obs.set_color(BLUE)
        obs[0].set_color(WHITE)
        return obs


class CartpoleScene(Scene):
    def construct(self):
        cartpole = CartpoleMobject()

        self.play(Create(cartpole, lag_ratio=1, run_time=5))

        # Update cart position
        cart_move_animation = ApplyMethod(cartpole.cart.shift, 5*position1*RIGHT)
        pole_move_amimation = ApplyMethod(cartpole.pole.set_points_smoothly, [cartpole.cart.get_top() + 5*position1*RIGHT, cartpole.cart.get_top()+5*position1*RIGHT + -RIGHT*np.sin(angle1) * 3 + UP*np.cos(angle1) * 3])

        self.play(cart_move_animation, pole_move_amimation, run_time=2)

        # Render observation
        obs = cartpole.observation()
        self.play(Create(obs[0]))
        self.play(DrawBorderThenFill(obs[1]))
        self.play(Write(obs[2]), Write(obs[3][0]))

        self.play(Wait(1))
        self.play(Create(obs[4]))
        self.play(Write(obs[5]), Write(obs[3][1]))

        self.play(Wait(1))
        self.play(Create(obs[6]))
        self.play(Write(obs[7]), Write(obs[3][2]))

        self.play(Wait(1))
        self.play(Create(obs[8]))
        self.play(Write(obs[9]), Write(obs[3][3]))

        self.wait(2)
        self.play(FadeOut(obs))

        # Update cart position
        cart_move_animation = ApplyMethod(cartpole.cart.shift, -15*position1*RIGHT)
        pole_move_amimation = ApplyMethod(cartpole.pole.set_points_smoothly, 
                                          [cartpole.cart.get_top() -15*position1*RIGHT, 
                                           cartpole.cart.get_top() -15*position1*RIGHT +UP*3])

        self.play(cart_move_animation, pole_move_amimation, run_time=2)

        self.wait(2)
        self.play(FadeOut(cartpole))

        normalCart = MathTex(r"N_c=(m_c+m_p)g-m_pl(\ddot{\theta}sin\theta+\dot{\theta}^2cos\theta)")
        thetaDoubleDot = MathTex(r"\ddot{\theta}=\frac{gsin\theta+cos\theta*\{\frac{-F-m_pl\dot{\theta}^2[sin\theta+\mu_csgn(N_c\dot{x})cos\theta]}{m_c+m_p}+\mu_cgsgn(N_c\dot{x})\}-\frac{\mu_p\dot{\theta}}{m_pl}}{l\{\frac{4}{3}-\frac{m_pcos\theta}{m_c+m_p}[cos\theta-\mu_csgn(N_c\dot{x})]\}}")
        xDoubleDot = MathTex(r"\ddot{x}=\frac{F+m_pl(\dot{\theta}^2sin\theta-\ddot{\theta}cos\theta)-\mu_cN_csgn(N_c\dot{x})}{m_c+m_p}")
        thetaDoubleDot.scale(0.75)

        formulas = VGroup()
        formulas.add(normalCart)
        formulas.add(thetaDoubleDot)
        formulas.add(xDoubleDot)
        formulas.arrange(DOWN)

        self.play(Write(formulas), run_time=10)

        self.wait(2)