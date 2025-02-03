from manim import *


class Grafica1(Scene):

    def construct(self):

        cielo = '#C4DDFF'
        azul = '#001D6E'
        rojo = '#B20600'

        self.camera.background_color = cielo
        ax = Axes(x_range=[-1, 14, 1],
                  y_range=[-3.5, 3.5, 1],
                  x_length=9,
                  y_length=3,
                  axis_config={"include_tip": True},
                  # x_axis_config = {"numbers_to_include": [3.14, 6.28, 9.42, 12.56]}
                  )
        p1 = MathTex(r'\pi', color=azul).move_to(ax.coords_to_point(PI, -0.5))
        p2 = MathTex(r'2\pi', color=azul).move_to(ax.coords_to_point(2 * PI, -0.5))
        p3 = MathTex(r'3\pi', color=azul).move_to(ax.coords_to_point(3 * PI, -0.5))
        p4 = MathTex(r'4\pi', color=azul).move_to(ax.coords_to_point(4 * PI, -0.5))

        ax.set_color(azul)
        self.play(Write(ax), Write(p1), Write(p2), Write(p3), Write(p4))
        self.wait(3)
        curva0 = ax.plot(lambda x: np.sin(x), color=rojo, x_range=[0, 4 * PI])
        curva1 = curva0.copy()
        curva2 = ax.plot(lambda x: 3 * np.sin(x), color=rojo, x_range=[0, 4 * PI])
        curva3 = ax.plot(lambda x: 0.5 * np.sin(x), color=rojo, x_range=[0, 4 * PI])
        eqn0 = MathTex(r'y=\sin{x}', color=azul).move_to(UP * 2.5).scale(2)
        eqn1 = eqn0.copy()
        eqn2 = MathTex(r'y=3\sin{x}', color=azul).move_to(UP * 2.5).scale(2)
        eqn3 = MathTex(r'y=0.5\sin{x}', color=azul).move_to(UP * 2.5).scale(2)
        self.play(Write(curva1), Write(eqn1))
        self.play(Transform(curva1, curva2), Transform(eqn1, eqn2), run_time=2)
        self.wait(2)
        self.play(Transform(curva1, curva3), Transform(eqn1, eqn3), run_time=2)
        self.wait(2)
        self.play(Transform(curva1, curva0), Transform(eqn1, eqn0), run_time=2)
        self.wait(2)
