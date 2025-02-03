from manim import *
from scipy.integrate import quad

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

        datos1 = MathTex(r'f:[a,b]').move_to(UP + LEFT * 1.25).scale(0.75)
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

        # rojo = '#B20600'
        a = 0
        b = 7
        ax = Axes(
            x_range=[-1, 8, 1],
            y_range=[0, 6, 1],
            x_length=4.3,
            y_length=3.4,
            axis_config={"include_tip": True}
        )
        punto_a = MathTex(r'a').move_to(ax.coords_to_point(a, -0.6))
        punto_b = MathTex(r'b').move_to(ax.coords_to_point(b, -0.6))

        self.play(Uncreate(integral1), Uncreate(integral2))
        self.play(Transform(subintervalos, ax))
        self.play(Write(punto_a), Write(punto_b), run_time=1.5)
        self.wait(2)

        funcion = lambda x: x**(1/3) + 0.5*x**(1/2) + 2
        curva0 = ax.plot(funcion,
                         color=BLUE, x_range=[0, 7.5])
        # area = ax.get_area(curva0, x_range=(0, 7), color=rojo, opacity=0.5)
        # area_valor = quad(funcion, 0, 7)

        # grafico = VGroup(ax, curva0)  # area

        self.play(Write(curva0), run_time=1.5)
        self.wait(1)
        # self.play(Write(area))
        # self.wait(2)

        subdivisions = [2, 5, 10, 20, 50, 100]
        prev_rectangles = None
        area_base = MathTex(r'A_{i}= f(c_i) \cdot \Delta x_i').move_to(DOWN * 3)
        area_aprox = MathTex(r'A\approx S_n=\sum_{i=1}^{n}{f(c_i) \cdot \Delta x_i}'
                             ).move_to(DOWN * 2.5).scale(0.8)

        for n in subdivisions:
            # Calcular ancho de cada rectángulo
            dx = (b - a) / n

            # Crear rectángulos de Riemann (muestreo por la derecha)
            rectangles = ax.get_riemann_rectangles(
                curva0,
                x_range=[a, b],
                dx=dx,
                # input_sample_type="right",
                # stroke_width=0.5,
                # color=rojo,
                fill_opacity=0.8
                )

            if prev_rectangles:
                self.play(
                    Transform(prev_rectangles, rectangles),
                    run_time=0.8
                )
                self.play(Transform(area_base, area_aprox))
                self.wait(1)
            else:
                self.play(
                    Write(rectangles),
                    Write(area_base),
                    run_time=1
                )
                self.wait(1)
                prev_rectangles = rectangles

        self.wait(2)
        area1 = ax.get_area(curva0, x_range=(0, 7), opacity=0.8)
        self.play(Uncreate(prev_rectangles), Write(area1), run_time=0.6)
        self.wait(2)

        ax2 = ax.copy()
        punto_a2 = punto_a.copy()
        punto_b2 = punto_b.copy()
        curva1 = curva0.copy()
        area2 = area1.copy()
        titulo3 = titulo2.copy()

        grafica1 = [subintervalos, punto_a, punto_b, curva0, area1, titulo1]
        grafica2 = VGroup(ax2, punto_a2, punto_b2, curva1, area2, titulo3)
        grafica2.shift(UP * 0.75).scale(0.9)

        for valor1, valor2 in zip(grafica1, grafica2):
            self.play(Transform(valor1, valor2), run_time=0.5)

        suma_riemann = MathTex(
            r'A=\lim_{n \to \infty} {\sum_{i=1}^{n}{f(c_i) \cdot \Delta x_i}}'
        ).move_to(DOWN * 2).scale(0.8)
        self.play(Transform(area_base, suma_riemann))
        self.wait(2)
