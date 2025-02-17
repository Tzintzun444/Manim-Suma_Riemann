from manim import *


class Leccion12(Scene):

    def construct(self):
        eqn0 = MathTex("2x^2+6x+7=0").move_to(UP * 3)
        eqn1 = MathTex("x=\\frac{-b \\pm  \\sqrt{b^2-4ac}}{2a}").move_to(UP * 1.5)
        eqn2 = MathTex(r"x=\frac{-b \pm  \sqrt{b^2-4ac}}{2a}")
        eqn3 = MathTex(r"\left(\begin{array}{cc} 1 & 2 \\ 3 & 4 \end{array}\right)").move_to(DOWN * 2)

        self.play(Write(eqn0))
        self.wait(3)
        self.play(Write(eqn1))
        self.wait(3)
        self.play(Write(eqn2))
        self.wait(3)
        self.play(Write(eqn3))
        self.wait(3)


class Leccion13(Scene):

    def construct(self):
        eqn0 = MathTex("2x^2+6x+7=0").move_to(UP).scale(1.5)
        eqn1 = MathTex("2x^2", "+6x", "+7", "=0").move_to(DOWN).scale(1.5)
        self.play(Write(eqn0))
        self.wait(3)
        self.play(Write(eqn1[0]))
        self.wait(1)
        self.play(Write(eqn1[1]))
        self.wait(1)
        self.play(Write(eqn1[2]))
        self.wait(1)
        self.play(Write(eqn1[3]))


class Leccion14(Scene):

    def construct(self):
        color1 = '#0F2C67'
        color2 = '#CD1818'
        color3 = '#F3950D'
        color4 = '#F4E185'
        eqn0 = MathTex("2x^2+6x+7=0").move_to(UP).scale(1.5)
        eqn1 = MathTex("\\frac{a}{b}").move_to(DOWN * 0.5)
        eqn2 = MathTex(r"{-b \pm \sqrt{b^2-4ac}}", r"\over", r"{2a}",
                       color=color4).move_to(DOWN * 2)
        eqn2[1].set_color(color3)
        eqn2[2].set_color(color2)
        self.play(Write(eqn0))
        self.wait(2)

        self.play(Write(eqn1))
        self.wait(2)

        self.play(Write(eqn2[0]))
        self.wait(1)

        self.play(Write(eqn2[1]))
        self.wait(1)

        self.play(Write(eqn2[2]))
        self.wait(3)


class Leccion15(Scene):

    def construct(self):
        color1 = '#0F2C67'
        color2 = '#CD1818'
        color3 = '#F3950D'
        color4 = '#F4E185'

        self.camera.background_color = color1

        eqn0 = MathTex("x=", "2.5").move_to(UP * 2 + LEFT * 2).scale(1.5)
        eqn1 = MathTex("x=", "1.5").move_to(UP * 2 + RIGHT * 2).scale(1.5)
        eqn2= MathTex(
            "z=(", "2.5", ")^2+(", "1.5", ")^2"
        ).move_to(DOWN).scale(1.5)

        eqn0.set_color(color3)
        eqn1.set_color(color2)

        self.play(Write(eqn0))
        self.wait(1)
        self.play(Write(eqn1))
        self.wait(3)
        self.play(Write(eqn2[0]), Write(eqn2[2]), Write(eqn2[4]))
        self.wait(3)
        self.play(Transform(eqn0[1], eqn2[1]),
                  Transform(eqn1[1], eqn2[3]))
        self.wait(3)
