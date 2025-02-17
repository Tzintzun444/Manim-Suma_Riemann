from manim import *

# Configuración para que el video sea para teléfonos
altura_original = config.pixel_height
config.pixel_height = config.pixel_width
config.pixel_width = altura_original

config.frame_width = config.frame_height * (9 / 16)
FRAME_HEIGHT = config.frame_height
FRAME_WIDTH = config.frame_width


# Clase de la animación
class Integral1(Scene):

    def construct(self):

        # rejilla = NumberPlane()
        # self.add(rejilla)

        # Pregunta de bienvenida
        bienvenida = Text('Alguna vez te has preguntado').move_to(UP * 2).scale(0.5)
        pregunta = Text('¿1 + 1 = 2?').scale(1.2)
        self.play(Write(bienvenida), run_time=0.5)
        self.wait(1)
        self.play(Write(pregunta), run_time=1.5)
        self.wait(1)
        self.play(Uncreate(bienvenida),
                  Uncreate(pregunta), run_time=0.5)
        self.wait(0.5)

        # Introducción al video
        titulo1 = Text('La integral').move_to(UP * 2).scale(0.85)
        titulo2 = titulo1.copy().move_to(UP * 2.5)
        integral1 = MathTex(r'A=\int_{a}^{b} f(x)\,dx')
        integral2 = integral1.copy()

        self.play(Write(titulo1),
                  Write(integral1), run_time=1)
        self.wait(1)

        # Datos iniciales
        datos1 = MathTex(r'f:[a,b]').move_to(UP + LEFT * 1.25).scale(0.75)
        datos2 = MathTex(r'f(a) \to f(b)').move_to(UP + RIGHT).scale(0.75)

        self.play(Transform(integral1, datos1),
                  Transform(integral2, datos2),
                  Transform(titulo1, titulo2), run_time=3)
        self.wait(3)

        subintervalos = MathTex(
            r'a=x_0<x_1<x_2<...<x_n=b'
        ).scale(0.6)

        self.play(Write(subintervalos), run_time=4)
        self.wait(4)

        particion_subint = MathTex(r'[x_{i-1}, x_i]').move_to(UP)
        longitud_subint = MathTex(r'x_i-x_{i-1}=\Delta x_i>0').scale(0.75)
        self.play(Transform(integral1, particion_subint),
                  Transform(integral2, particion_subint),
                  Transform(subintervalos, longitud_subint), run_time=5)
        self.wait(10)

        punto_muestra = MathTex(
            r'c_i \hspace{0.1cm} / \hspace{0.1cm} c_i \in [x_{i-1}, x_i]'
                                ).move_to(UP * 1.5)
        funcion_muestra = MathTex(r'f(c_i)').scale(1.5)
        self.play(
            Transform(integral2, punto_muestra),
            Transform(integral1, punto_muestra),
            run_time=4
        )
        self.wait(4)
        self.play(Transform(subintervalos, funcion_muestra),
                  run_time=2)
        self.wait(2)

        # Creación de la gráfica, puntos y el área bajo la curva
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

        # definición de la función
        funcion = lambda x: x ** (1 / 3) + 0.5 * x ** (1 / 2) + 2

        # creación de la curva
        curva0 = ax.plot(funcion,
                         color=BLUE, x_range=[0, 7.5])

        self.play(Uncreate(integral1), Uncreate(integral2))
        self.play(Transform(subintervalos, ax),
                  Write(punto_a), Write(punto_b))
        self.wait(1)
        self.play(Write(curva0))
        self.wait(2)

        subdivisions = [2, 5, 10, 20, 50, 100]
        prev_rectangles = None

        # Área de cada i-ésimo rectángulo
        area_base = MathTex(r'A_{i}= f(c_i) \cdot \Delta x_i'
                            ).move_to(DOWN * 3)
        # Área aproximada bajo la curva
        area_aprox = MathTex(r'A\approx S_n=\sum_{i=1}^{n}{f(c_i) \cdot \Delta x_i}'
                             ).move_to(DOWN * 3).scale(0.8)

        # Dibuja los rectángulos bajo la curva
        for n in subdivisions:
            # Calcular ancho de cada rectángulo
            dx = (b - a) / n

            # Crear rectángulos de Riemann
            rectangles = ax.get_riemann_rectangles(
                curva0, x_range=[a, b],
                dx=dx, fill_opacity=0.8
            )

            if prev_rectangles:
                self.play(
                    Transform(prev_rectangles, rectangles),
                    Transform(area_base, area_aprox))
                self.wait(1)
            else:
                self.play(
                    Write(rectangles),
                    Write(area_base), run_time=3
                )
                self.wait(3)
                prev_rectangles = rectangles

        self.wait(1)

        # Obtención del área bajo la curva
        area1 = ax.get_area(curva0, x_range=(0, 7), opacity=0.8)
        self.play(Uncreate(prev_rectangles), run_time=2)
        self.play(Write(area1), run_time=1)
        self.wait(2)

        # Replicación de la gráfica para moverla hacia arriba
        ax2 = ax.copy()
        punto_a2 = punto_a.copy()
        punto_b2 = punto_b.copy()
        curva1 = curva0.copy()
        area2 = area1.copy()
        titulo3 = Text('Suma de Riemann').move_to(UP * 2.4).scale(0.85)

        # Agrupación de la gráfica en un solo objeto
        grafica1 = VGroup(subintervalos, punto_a,
                          punto_b, curva0,
                          area1, titulo1)
        grafica2 = VGroup(ax2, punto_a2,
                          punto_b2, curva1,
                          area2, titulo3)
        grafica2.shift(UP * 0.75).scale(0.9)

        # Anima el movimiento de la gráfica
        for valor1, valor2 in zip(grafica1, grafica2):
            self.play(Transform(valor1, valor2),
                      run_time=0.5)
        self.wait(0.5)

        # Nomenclatura de la suma de Riemann
        tendencias = MathTex(r'n \to \infty, \hspace{0.2cm} \Delta x_i \to 0'
                             ).move_to(DOWN * 1.5).scale(0.8)
        suma_riemann1 = MathTex(
            r'A=',
            r'\lim_{n \to \infty} {\sum_{i=1}^{n}',
            r'{f(c_i)',
            r'\cdot',
            r'\Delta x_i}}'
        ).move_to(DOWN * 2.5).scale(0.8)
        self.play(Write(tendencias),
                  Transform(area_base, suma_riemann1),
                  run_time=2)
        self.wait(1)

        # Definición formal de la suma de Riemann
        definicion_inicial = MathTex(
            r'f(x):[a,b], \hspace{0.1cm} P = \{x_1,x_2,...,x_n\}'
        ).move_to(UP * 2).scale(0.6)

        definicion_media = MathTex(
            r'c_i \in [x_{i-1}, x_i]'
        ).move_to(UP * 1).scale(0.9)

        area_aprox1 = MathTex(
            r'S_n=',
            r'\sum_{i=1}^{n}',
            r'{f(c_i)',
            r'\cdot',
            r'\Delta x_i}'
        ).move_to(DOWN * 0.25).scale(0.8)

        suma_riemann2 = suma_riemann1.copy().move_to(DOWN * 0.25).scale(1)
        grafica1 = VGroup(subintervalos, punto_a,
                          punto_b, curva0, area1)

        # Animación final de la suma de Riemann
        self.play(Transform(titulo1, titulo3),
                  run_time=2)
        self.wait(2)
        self.play(Transform(grafica1, definicion_inicial),
                  run_time=3)
        self.wait(3)
        self.play(Write(definicion_media), run_time=2)
        self.wait(2)
        self.play(Write(area_aprox1), run_time=2)
        self.wait(2)
        self.play(Transform(area_base, suma_riemann2),
                  Transform(tendencias, suma_riemann2),
                  Transform(area_aprox1, suma_riemann2),
                  run_time=2)
        self.wait(2)

        # Escritura de la parte final de la integral
        integral = MathTex(
            r'A=', r'\int_{a}^{b}', r'f(x)', r'\,dx'
        ).move_to(UP * 1.5).scale(0.9)
        titulo_integral = Text('La integral').move_to(UP * 3)

        self.play(Uncreate(grafica1),
                  Uncreate(definicion_media))
        self.wait(2)
        self.play(Transform(titulo1, titulo_integral),
                  run_time=3)
        self.wait(3)

        # Transformación a pasos de la suma de Riemann a la notación de la integral
        self.play(Transform(suma_riemann2[1], integral[1]),
                  run_time=3)
        self.wait(3)
        self.play(Transform(suma_riemann2[2], integral[2]))
        self.wait(2)
        self.play(Transform(suma_riemann2[4], integral[3]),
                  run_time=2)
        self.wait(3)
        self.play(Transform(suma_riemann2[0], integral[0]),
                  run_time=2)
        self.wait(1)
        self.play(Uncreate(area_base),
                  Uncreate(tendencias),
                  Uncreate(area_aprox1))
        self.wait(1)

        # Creación y dibujo final de la gráfica con el resultado final
        ax2 = Axes(
            x_range=[-1, 8, 1],
            y_range=[0, 6, 1],
            x_length=4.3,
            y_length=3.4,
            axis_config={"include_tip": True}
        )
        punto_a3 = MathTex(r'a').move_to(ax2.coords_to_point(a, -0.6))
        punto_b3 = MathTex(r'b').move_to(ax2.coords_to_point(b, -0.6))
        curva2 = ax.plot(funcion,
                         color=BLUE,
                         x_range=[0, 7.5])
        area3 = ax.get_area(curva2, x_range=(0, 7),
                            opacity=0.8)
        grafica0 = VGroup(ax2, punto_a3,
                          punto_b3, curva2, area3
                          ).move_to(DOWN * 1.2).scale(0.85)

        self.play(Write(grafica0),
                  run_time=1.5)
        self.wait(1)

        # Animación final de resalte de la integral y su gráfica
        rect1 = SurroundingRectangle(integral, color=RED)
        rect2 = SurroundingRectangle(grafica0, color=RED)
        self.play(Write(rect1),
                  Write(rect2), run_time=2)
        self.wait(1)

        # Desaparición final
        self.play(Uncreate(titulo_integral),
                  Uncreate(suma_riemann2),
                  Uncreate(grafica0),
                  FadeOut(rect1),
                  FadeOut(rect2),
                  Uncreate(titulo1))
        self.wait(1)
