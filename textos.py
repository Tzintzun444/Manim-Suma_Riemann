import numpy as np
from manim import *


class Leccion1(Scene):

    def construct(self):
        texto1 = Text('Hola Mundo')
        self.add(texto1)
        self.wait(3)


class Leccion2(Scene):

    def construct(self):
        texto2 = Text('Curso de Manim')
        self.add(texto2)
        self.wait(3)
        self.remove(texto2)
        self.wait(3)


class Leccion3(Scene):

    def construct(self):
        texto3 = Text('Curso de Manim')
        self.play(FadeIn(texto3))
        self.wait(3)
        self.play(FadeOut(texto3))
        self.wait(3)
        self.play(Write(texto3))
        self.wait(3)


class Leccion4(Scene):

    def construct(self):
        rejilla = NumberPlane()
        texto1 = Text('Lema').move_to(RIGHT+UP)
        self.add(rejilla)
        self.wait(5)
        texto2 = Text('Lema').move_to(LEFT+DOWN)
        self.add(texto1,texto2)
        self.wait(5)


class Leccion5(Scene):

    def construct(self):
        rejilla = NumberPlane()
        self.add(rejilla)
        texto1 = Text('A').move_to(RIGHT + LEFT)
        texto2 = Text('B').move_to(LEFT+  DOWN)
        texto3 = Text('C').move_to(LEFT * 2.5)
        texto4 = Text('D').move_to(DOWN * 3.2)
        self.add(texto1, texto2, texto3, texto4)
        self.wait(5)


class Leccion6(Scene):

    def construct(self):
        rejilla = NumberPlane()
        self.add(rejilla)
        texto1 = Text('A').move_to(np.array([1, 1, 0]))
        texto2 = Text('B').move_to(np.array([-1, -1, 0]))
        texto3 = Text('C').move_to(np.array([-2.5, 0, 0]))
        texto4 = Text('D').move_to(np.array([0, -3.2, 0]))
        self.add(texto1, texto2, texto3, texto4)
        self.wait(5)


class Leccion7(Scene):

    def construct(self):
        texto1 = Text('Curso de Manim').move_to(UP)
        texto2 = Text('Curso de Manim').move_to(DOWN)
        texto3 = Text('Primeros pasos').move_to(UP)
        self.play(FadeIn(texto1))
        self.wait(3)
        self.play(Transform(texto1, texto2))
        self.wait(3)
        self.play(Transform(texto1, texto3))
        self.wait(3)



