from manim import *


altura_original = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = altura_original

config.frame_width = config.frame_height * (9 / 16)
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


class SumaRiemann1(Scene):

    def construct(self):

        rejilla = NumberPlane()
        self.add(rejilla)

        bienvenida = Text('Alguna vez te has preguntado').move_to(UP * 2).scale(0.5)
        pregunta = Text('¿1 + 1 = 2?').scale(1.2)
        self.play(Write(bienvenida))
        self.wait(2)
        self.play(Write(pregunta))
        self.wait(2)
        self.play(Uncreate(bienvenida), Uncreate(pregunta), run_time=0.75)
        self.wait(1)

        # titulo = Text('Suma de Riemann').move_to(UP * 2).scale(0.75)
        # suma_riemann = MathTex(r'\lim_{n \to \infty} {\sum_{i=1}^{n}{f(c_i) \cdot \Delta x_i}}'
        #                        )

        titulo1 = Text('La integral').move_to(UP * 2).scale(0.85)
        titulo2 = titulo1.copy().move_to(UP * 2.5)
        integral1 = MathTex(r'A=\int_{a}^{b} f(x)\,dx')
        integral2 = integral1.copy()

        self.play(Write(titulo1), Write(integral1))
        self.wait(3)

        datos1 = MathTex(f'f:[a,b]').move_to(UP + LEFT * 1.25).scale(0.75)
        datos2 = MathTex(r'f(a) \to f(b)').move_to(UP + RIGHT).scale(0.75)

        self.play(Transform(integral1, datos1), Transform(integral2, datos2),
                  Transform(titulo1, titulo2))
        self.wait(2)

        subintervalos = MathTex(
            r'a=x_0<x_1<x_2<...<x_n=b'
        ).scale(0.6)

        self.play(Write(subintervalos))
        self.wait(2)

        particion_subint = MathTex(r'[x_{i-1}, x_i]').move_to(UP)
        longitud_subint = MathTex(r'x_i-x_{i-1}=\Delta x_i>0').scale(0.75)
        self.play(Transform(integral1, particion_subint),
                  Transform(integral2, particion_subint),
                  Transform(subintervalos, longitud_subint))
        self.wait(2)

        punto_muestra = MathTex(
            r'c_i \hspace{0.1cm} / \hspace{0.1cm} c_i \in [x_{i-1}, x_i]'
                                ).move_to(UP * 1.5)
        funcion_muestra = MathTex(r'f(c_i)').scale(1.5)
        self.play(
            Transform(integral2, punto_muestra),
            Transform(integral1, punto_muestra),
        )
        self.wait(2)
        self.play(Transform(subintervalos, funcion_muestra))
        self.wait(2)

        azul = '#001D6E'
        ax = Axes(
            x_range=[-1, 8, 1],
            y_range=[-1, 6, 1],
            x_length=4.3,
            y_length=3.4,
            axis_config={"include_tip": True}
        )
        punto_a = MathTex(r'a').move_to(ax.coords_to_point(1, -0.9))
        punto_b = MathTex(r'b').move_to(ax.coords_to_point(6, -0.9))
        self.play(Uncreate(integral1), Uncreate(integral2))
        self.play(Transform(subintervalos, ax))
        self.play(Write(punto_a), Write(punto_b), run_time=1.5)
        self.wait(2)

        curva0 = ax.plot(lambda x: x**(1/3) + 0.5*x**(1/2) + 2,
                         color=BLUE, x_range=[0, 7.5])
        self.play(Write(curva0), run_time=1.5)
        self.wait(2)
