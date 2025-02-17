import numpy as np
from manim import *


class Funcion1(Scene):

    def construct(self):

        # colores
        rojo = '#CC0000'
        gris = '#666666'
        azul = '#0000FF'
        blanco = '#FFFFFF'

        # fondo
        self.camera.background_color = blanco

        # Funcion a graficar
        eqn0 = MathTex(r'y=e^{kx}', color=azul).move_to(np.array([-5.5, 3.2, 0])
                                                        ).scale(1.5)

        # ejes
        ax = Axes(x_range=[-3, 3, 1], y_range=[-1, 2, 1], x_length=16, y_length=8,
                  axis_config={'include_tip': True}
                  ).move_to(np.array([0, 0, 0])).scale(1).set_color(gris)

        # Escribir
        self.play(Write(ax), Write(eqn0))

        # funcion inicial
        curva = ax.plot(lambda x: np.exp(-3 * x), color=rojo)

        # parámetro de animación
        t = ValueTracker(-3)

        # Valor visible
        d = DecimalNumber(-3)

        # actualizar a d
        d.add_updater(lambda z: z.set_value(t.get_value()))
        d.move_to(np.array([-5.1, 2, 0])).set_color(rojo)

        # actualizar la curva
        curva.add_updater(lambda z: z.become(ax.plot(lambda x: np.exp(t.get_value() * x),
                                                     color=rojo)))
        k = MathTex('k=', color=azul).move_to(np.array([-6.1, 2, 0]))

        self.play(Write(k), Write(d), Write(curva))
        self.play(t.animate.set_value(3), run_time=5)
        self.wait(3)
        self.play(t.animate.set_value(0), run_time=5)
        self.wait(3)
