from manim import *
import random
import math

########### Sets of constellations #############

class vday(Scene):
    def construct(self):
        yay = Tex("This too me many, many hours", font_size = 50, color = BLUE).shift(UP)
        yay2 = Tex("It was all worth it :)", font_size = 50, color = BLUE)
        yay3 = Tex("Happy Valentine's Day!!!", font_size = 70, color = RED)
        yay2.next_to(yay, DOWN)
        yay3.next_to(yay2, DOWN)

        graph = ImplicitFunction(
            lambda x, y: (x**2+(5*y/4-math.sqrt(math.fabs(x)))**2) - 1,
            color=RED
        ).shift(DOWN*3)
        heartEq = MathTex("x^2 + (\\frac{5y}{4}-\\sqrt{\\abs{x}})^2 = 1", font_size = 40).next_to(graph, RIGHT, buff = 0.5)

        self.play(Write(yay))
        self.wait()
        self.play(Write(yay2))
        self.wait()
        self.play(Write(yay3))
        self.wait()
        self.play(Create(graph), run_time = 5)
        self.play(FadeIn(heartEq))
        self.wait(10)


        

class StarsAndAliens1(Scene):
    def construct(self):
        plane = NumberPlane()
        pic = ImageMobject("normalSkyPic.png")
        self.add(pic)

        for i in range(6):
            alien = Circle(radius = 0.5, color = TEAL_A).move_to(plane.c2p(random.randint(-6,6), random.randint(-3,3)))
            self.play(Broadcast(alien, focal_point = alien.get_center()))
            self.wait(random.randint(2,5))

        for n in range(6):
            ss = Dot(color = YELLOW, radius = 0.03).move_to(plane.c2p(random.randint(-6,6), random.randint(-5,5))).set_opacity(0)
            b = TracedPath(ss.get_center, dissipating_time = 0.5, stroke_opacity = [1,0], stroke_color = YELLOW)

            self.add(b)
            self.play(ss.animate.move_to(plane.c2p(random.randint(-6,6), random.randint(-5,5))))
            self.wait(random.randint(2,5))

        ar = Aries().scale(0.75).shift(LEFT*3)
        ta = Taurus().scale(0.75).shift(LEFT*3)
        ge = Gemini().scale(0.75).shift(LEFT*3)
        arDesc = zodiacDesc("Aries: ", "March 21 - April 19", "Sagittarius, Leo and Aries", "The Ram").to_edge(UR, buff = 1).scale(0.75)
        taDesc = zodiacDesc("Taurus: ", "April 20 - May 20", "Virgo, Capricorn and Taurus", "The Bull").to_edge(UR, buff = 1).scale(0.75)
        geDesc = zodiacDesc("Gemini: ", "May 20 - June 20", "Aquarius, Libra Gemini", "The Twins").to_edge(UR, buff = 1).scale(0.75)


        self.play(FadeIn(ar), run_time = 5)
        self.wait()
        self.play(FadeIn(arDesc))
        self.wait(5)
        self.play(FadeOut(ar), FadeOut(arDesc))
        self.wait(5)

        self.play(FadeIn(ta), run_time = 5)
        self.wait()
        self.play(FadeIn(taDesc))
        self.wait(5)
        self.play(FadeOut(ta), FadeOut(taDesc))
        self.wait(5)

        self.play(FadeIn(ge), run_time = 5)
        self.wait()
        self.play(FadeIn(geDesc))
        self.wait(5)
        self.play(FadeOut(ge), FadeOut(geDesc))
        self.wait(5)


class StarsAndAliens2(Scene):
    def construct(self):
        plane = NumberPlane()
        pic = ImageMobject("galaxySkyPic2.png")
        self.add(pic)

        for i in range(6):
            alien = Circle(radius = 0.5, color = TEAL_A).move_to(plane.c2p(random.randint(-6,6), random.randint(-3,3)))
            self.play(Broadcast(alien, focal_point = alien.get_center()))
            self.wait(random.randint(2,5))

        for n in range(6):
            ss = Dot(color = YELLOW, radius = 0.03).move_to(plane.c2p(random.randint(-6,6), random.randint(-5,5))).set_opacity(0)
            b = TracedPath(ss.get_center, dissipating_time = 0.5, stroke_opacity = [1,0], stroke_color = YELLOW)

            self.add(b)
            self.play(ss.animate.move_to(plane.c2p(random.randint(-6,6), random.randint(-5,5))))
            self.wait(random.randint(2,5))

        ca = Cancer().scale(0.75).shift(LEFT*3)
        le = Leo().scale(0.75).shift(LEFT*3)
        vi = Virgo().scale(0.75).shift(LEFT*3)
        caDesc = zodiacDesc("Cancer: ", "June 21 - July 22", "Pisces, Scorpio and Cancer", "The Crab").to_edge(UR, buff = 1).scale(0.75)
        leDesc = zodiacDesc("Leo: ", "July 23 - August 22", "Aries, Leo and Sagittarius", "The Lion").to_edge(UR, buff = 1).scale(0.75)
        viDesc = zodiacDesc("Virgo: ", "August 23 - September 22", "Scorpio, Capricorn and Cancer", "The Virgin").to_edge(UR, buff = 1).shift(RIGHT*1.5).scale(0.75)

        self.play(FadeIn(ca), run_time = 5)
        self.wait()
        self.play(FadeIn(caDesc))
        self.wait(5)
        self.play(FadeOut(ca), FadeOut(caDesc))
        self.wait(5)

        self.play(FadeIn(le), run_time = 5)
        self.wait()
        self.play(FadeIn(leDesc))
        self.wait(5)
        self.play(FadeOut(le), FadeOut(leDesc))
        self.wait(5)

        self.play(FadeIn(vi), run_time = 5)
        self.wait()
        self.play(FadeIn(viDesc))
        self.wait(5)
        self.play(FadeOut(vi), FadeOut(viDesc))
        self.wait(5)

class StarsAndAliens3(Scene):
    def construct(self):
        plane = NumberPlane()
        pic = ImageMobject("nebulaSkyPic.png")
        self.add(pic)

        for i in range(6):
            alien = Circle(radius = 0.5, color = TEAL_A).move_to(plane.c2p(random.randint(-6,6), random.randint(-3,3)))
            self.play(Broadcast(alien, focal_point = alien.get_center()))
            self.wait(random.randint(2,5))

        for n in range(6):
            ss = Dot(color = YELLOW, radius = 0.03).move_to(plane.c2p(random.randint(-6,6), random.randint(-5,5))).set_opacity(0)
            b = TracedPath(ss.get_center, dissipating_time = 0.5, stroke_opacity = [1,0], stroke_color = YELLOW)

            self.add(b)
            self.play(ss.animate.move_to(plane.c2p(random.randint(-6,6), random.randint(-5,5))))
            self.wait(random.randint(2,5))

        li = Libra().scale(0.75).shift(LEFT*4)
        sc = Scorpius().scale(0.75).shift(LEFT*3)
        sa = Sagittarius().scale(0.75).shift(LEFT*3)
        liDesc = zodiacDesc("Libra: ", "September 23 - October 22", "Gemini, Aquarius, Other Libras", "The Scales").to_edge(UR, buff = 1).scale(0.75)
        scDesc = zodiacDesc("Scorpius: ", "October 23 - November 21", "Cancer and Pisces", "The Scorpion").to_edge(UR, buff = 1).scale(0.75)
        saDesc = zodiacDesc("Sagittarius: ", "November 22 - December 21", "Sagittarius, Aries and Leo", "The Archer").to_edge(UR, buff = 1).scale(0.75)

        self.play(FadeIn(li), run_time = 5)
        self.wait()
        self.play(FadeIn(liDesc))
        self.wait(5)
        self.play(FadeOut(li), FadeOut(liDesc))
        self.wait(5)

        self.play(FadeIn(sc), run_time = 5)
        self.wait()
        self.play(FadeIn(scDesc))
        self.wait(5)
        self.play(FadeOut(sc), FadeOut(scDesc))
        self.wait(5)

        self.play(FadeIn(sa), run_time = 5)
        self.wait()
        self.play(FadeIn(saDesc))
        self.wait(5)
        self.play(FadeOut(sa), FadeOut(saDesc))
        self.wait(5)


class StarsAndAliens4(Scene):
    def construct(self):
        plane = NumberPlane()
        pic = ImageMobject("galaxySkyPic.png")
        self.add(pic)

        for i in range(6):
            alien = Circle(radius = 0.5, color = TEAL_A).move_to(plane.c2p(random.randint(-6,6), random.randint(-3,3)))
            self.play(Broadcast(alien, focal_point = alien.get_center()))
            self.wait(random.randint(2,5))

        for n in range(6):
            ss = Dot(color = YELLOW, radius = 0.03).move_to(plane.c2p(random.randint(-6,6), random.randint(-5,5))).set_opacity(0)
            b = TracedPath(ss.get_center, dissipating_time = 0.5, stroke_opacity = [1,0], stroke_color = YELLOW)

            self.add(b)
            self.play(ss.animate.move_to(plane.c2p(random.randint(-6,6), random.randint(-5,5))))
            self.wait(random.randint(2,5))

        ca = Capricorn().scale(0.75).shift(LEFT*3)
        aq = Aquarius().scale(0.75).shift(LEFT*3)
        pi = Pisces().scale(0.75).shift(LEFT*3)
        caDesc = zodiacDesc("Capricorn: ", "December 22 - January 19", "Virgo, Taurus and Pisces", "The Goat").to_edge(UR, buff = 1).scale(0.75)
        aqDesc = zodiacDesc("Aquarius: ", "January 20 - Febuary 18", "Cancer and Pisces", "The Water Carrier").to_edge(UR, buff = 1).scale(0.75)
        piDesc = zodiacDesc("Pisces: ", "Febuary 19 - March 20", "Sagittarius, Aries and Leo", "The Fishes").to_edge(UR, buff = 1).scale(0.75)

        self.play(FadeIn(ca), run_time = 5)
        self.wait()
        self.play(FadeIn(caDesc))
        self.wait(5)
        self.play(FadeOut(ca), FadeOut(caDesc))
        self.wait(5)

        self.play(FadeIn(aq), run_time = 5)
        self.wait()
        self.play(FadeIn(aqDesc))
        self.wait(5)
        self.play(FadeOut(aq), FadeOut(aqDesc))
        self.wait(5)

        self.play(FadeIn(pi), run_time = 5)
        self.wait()
        self.play(FadeIn(piDesc))
        self.wait(5)
        self.play(FadeOut(pi), FadeOut(piDesc))
        self.wait(5)


########### Collections of pictures ############

class normalSkyPic(Scene):
    def construct(self):
        p = NumberPlane().set_opacity(0)
        a = BackgroundStars(stars = 3000)
        
        b = Stars(stars = 250)
        self.add(p, a, b)

class nebulaSkyPic(Scene):
    def construct(self):
        p = NumberPlane().set_opacity(0)
        a = BackgroundStars(stars = 3000)
        pic = ImageMobject("galaxy.png").scale(0.250).move_to(p.c2p(3,1))
        b = Stars(stars = 150)
        self.add(p, a, pic, b)

class galaxySkyPic(Scene):
    def construct(self):
        p = NumberPlane().set_opacity(0)
        a = BackgroundStars(stars = 3000)
        pic = ImageMobject("galaxy.png").scale(0.250).move_to(p.c2p(-2,2))
        b = Stars(stars = 150)
        self.add(p, a, pic, b)

class galaxySkyPic2(Scene):
    def construct(self):
        p = NumberPlane().set_opacity(0)
        a = BackgroundStars(stars = 3000)
        pic = ImageMobject("galaxy2.png").scale(1.8).move_to(p.c2p(0,0))
        b = Stars(stars = 150)
        self.add(p, a, pic, b)       


################# ZODIACS ##################
class zdTest(Scene):
    def construct(self):
        p = NumberPlane()
        a = zodiacDesc("Aries:","March 21 - April 19", "Sagittarius, Leo and Aries", "The Ram")
        a.scale(0.5)
        self.add(p,a)

class zodiacDesc(VGroup):
    def __init__(self, name: str, dates: str, comp: str, sym: str, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.dates = dates
        self.comp = comp
        self.sym = sym
        self.name = name

        Name = Tex(name, font_size = 70, color = BLUE)
        Dates = Tex("- Dates: " + dates, font_size = 40).next_to(Name, DOWN, buff = 0.5)
        Compatibility = Tex(" - Compatible Signs: " + comp, font_size = 40).next_to(Dates, DOWN, buff = 0.5)
        Symbol = Tex(" - Symbol: " + sym, font_size = 40).next_to(Compatibility, DOWN, buff = 0.5)

        self.add(Name, Dates, Compatibility, Symbol)

class Aries(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [-3.75, 0, 1.6, 1.8]
        ycoords = [0.9, 0, -0.75, -1.75]
        vg = VGroup()
        lvg = VGroup()
        for n in range(4):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
        

        
        lvg.add(l1,l2,l3)
        self.add(lvg)

class Gemini(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [0.6, 0, 1.23, 2.1, 2.45, 2.8, 1.8, -0.6, -.45, 0.3, 1.5, 1.125, -1.125, -1.45, -1.55, -1.1]
        ycoords = [0.65, 0, -0.95, -1.375, -1.375, -19/16, -1.75, -0.5, -23/16, -29/16, -2.5, -3.125, -.675, -17/15, -0.25, 5/16]
        vg = VGroup()
        lvg = VGroup()
        for n in range(16):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[5].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[2].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[10].get_center(), vg[11].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[10].get_center(), vg[12].get_center()).set_color(WHITE).set_opacity(0.6)
        l9 = Line(vg[9].get_center(), vg[10].get_center()).set_color(WHITE).set_opacity(0.6)
        l10 = Line(vg[3].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l11 = Line(vg[8].get_center(), vg[13].get_center()).set_color(WHITE).set_opacity(0.6)
        l12 = Line(vg[13].get_center(), vg[9].get_center()).set_color(WHITE).set_opacity(0.6)
        l13 = Line(vg[2].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
        l14 = Line(vg[13].get_center(), vg[14].get_center()).set_color(WHITE).set_opacity(0.6)
        l15 = Line(vg[13].get_center(), vg[15].get_center()).set_color(WHITE).set_opacity(0.6)
        

        
        lvg.add(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11, l12, l13, l14, l15)
        self.add(lvg)

class Leo(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [7/8, 9/16, -1/16, 0, 9/16, 0.75, -23/16, -2.75, -1.75]
        ycoords = [7/8, 9/8, 0.5, 0, -.25, -15/16, -9/8, -1.5, -7/16]
        vg = VGroup()
        lvg = VGroup()
        for n in range(9):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[5].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[6].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[7].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[8].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
        l9 = Line(vg[0].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        

        
        lvg.add(l1,l2,l3,l4,l5,l6,l7,l8,l9)
        self.add(lvg)

class Libra(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [-9/8, -7/8, -3/8, 0, 13/16, 31/16, 11/8, 0, 1/8]
        ycoords = [1.75, 1.25, 1.5, 1.75, 23/8, 2, 5/16, 0, -7/8]
        vg = VGroup()
        lvg = VGroup()
        for n in range(9):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[5].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[6].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[7].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[8].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
        l9 = Line(vg[5].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        

        
        lvg.add(l1,l2,l3,l4,l5,l6,l7,l8,l9)
        self.add(lvg)

class Sagittarius(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [-1/8, -0.5, -0.25, 5/16, 0, 0.25, 7/8, 15/16, 15/8, 1.25, 3/16, 0.25, -5/8, -35/32, -37/32, -49/16, -51/16, -11/16]
        ycoords = [2, 1.75, 1, 7/8, 0, -3/8, -9/8, -7/16, 0, -1.75, -19/8, -1.75, -5/8, -1.75, -39/16, -3/8, -23/16, -1/16]
        vg = VGroup()
        lvg = VGroup()
        for n in range(18):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[5].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[5].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[6].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[7].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l9 = Line(vg[8].get_center(), vg[9].get_center()).set_color(WHITE).set_opacity(0.6)
        l10 = Line(vg[9].get_center(), vg[10].get_center()).set_color(WHITE).set_opacity(0.6)
        l11 = Line(vg[10].get_center(), vg[11].get_center()).set_color(WHITE).set_opacity(0.6)
        l12 = Line(vg[11].get_center(), vg[12].get_center()).set_color(WHITE).set_opacity(0.6)
        l13 = Line(vg[12].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l14 = Line(vg[6].get_center(), vg[13].get_center()).set_color(WHITE).set_opacity(0.6)
        l15 = Line(vg[13].get_center(), vg[14].get_center()).set_color(WHITE).set_opacity(0.6)
        l16 = Line(vg[14].get_center(), vg[15].get_center()).set_color(WHITE).set_opacity(0.6)
        l17 = Line(vg[14].get_center(), vg[16].get_center()).set_color(WHITE).set_opacity(0.6)
        l18 = Line(vg[16].get_center(), vg[17].get_center()).set_color(WHITE).set_opacity(0.6)
        l19 = Line(vg[16].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
        l20 = Line(vg[0].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        

        
        lvg.add(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11, l12, l13, l14, l15, l16, l17, l18, l19, l20)
        self.add(lvg)

class Aquarius(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [2.1, .4, -1.2, 0, 1, -1, -1.4, -1.45, -0.5, -.25, 0.6, 1.55]
        ycoords = [2.4, 1.5, 0.6, 0, 0.1, -.125, -.25, -.75, -2, -1.5, -1.4, -1.8]
        vg = VGroup()
        lvg = VGroup()
        for n in range(12):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[3].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[6].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[7].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[8].get_center(), vg[9].get_center()).set_color(WHITE).set_opacity(0.6)
        l9 = Line(vg[9].get_center(), vg[10].get_center()).set_color(WHITE).set_opacity(0.6)
        l10 = Line(vg[10].get_center(), vg[11].get_center()).set_color(WHITE).set_opacity(0.6)
        l11 = Line(vg[11].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)

        
        lvg.add(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11)
        self.add(lvg)

class Taurus(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [-23/8, -1, -1/8, 0, 15/16, 37/16, 2.5, 2.75, 0.25, 0.75, -3/8, -3.5]
        ycoords = [39/16, 11/8, 3/8, 0, -9/16, -7/16, -15/16, -11/8, -1.25, -1.75, 0, 17/16]
        vg = VGroup()
        lvg = VGroup()
        for n in range(12):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[5].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[6].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[7].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[5].get_center(), vg[9].get_center()).set_color(WHITE).set_opacity(0.6)
        l9 = Line(vg[9].get_center(), vg[10].get_center()).set_color(WHITE).set_opacity(0.6)
        l10 = Line(vg[4].get_center(), vg[11].get_center()).set_color(WHITE).set_opacity(0.6)
        l11 = Line(vg[11].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
        

        
        lvg.add(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11)
        self.add(lvg)

class Cancer(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [-1.5, -3/8, 0, 15/8, 47/16, 1/8]
        ycoords = [17/8, 11/16, 0, -5/8, -17/16, -29/16]
        vg = VGroup()
        lvg = VGroup()
        for n in range(6):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[3].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
       
    
        
        lvg.add(l1,l2,l3,l4,l5)
        self.add(lvg)


class Virgo(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [-1, -5/8, 0, 17/16, 21/8, 45/16, -23/16, -2.25, -2.675]
        ycoords = [2.5, 7/8, 0, 1/8, 5/8, 13/8, -13/16, -2, 1/8]
        vg = VGroup()
        lvg = VGroup()
        for n in range(9):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[5].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[3].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[7].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[7].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
       
    
        
        lvg.add(l1,l2,l3,l4,l5, l6, l7, l8)
        self.add(lvg)

class Scorpius(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [2.5, 1.75, 21/8, 2.25, 1.25, 0.75, 0, -0.75, -21/16, -17/8, -39/16, -1.75]
        ycoords = [2, 1.25, 11/8, 11/16, 9/8, 13/16, 0, -23/16, -11/8, -19/16, -9/16, -1/8]
        vg = VGroup()
        lvg = VGroup()
        for n in range(12):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[2].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[2].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[5].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[6].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[7].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[8].get_center(), vg[9].get_center()).set_color(WHITE).set_opacity(0.6)
        l9 = Line(vg[9].get_center(), vg[10].get_center()).set_color(WHITE).set_opacity(0.6)
        l10 = Line(vg[10].get_center(), vg[11].get_center()).set_color(WHITE).set_opacity(0.6)
        l11 = Line(vg[11].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
       
    
        
        lvg.add(l1,l2,l3,l4,l5, l6, l7, l8, l9, l10, l11)
        self.add(lvg)


class Capricorn(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [23/8, 41/16, 17/8, 9/8, 11/16, -1/8, -1, -37/16, -27/16, -13/16, 0]
        ycoords = [1, 3/8, -1/8, -1.75, -33/16, -25/16, -17/16, 3/8, .25, 1/8, 0]
        vg = VGroup()
        lvg = VGroup()
        for n in range(11):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[5].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[6].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[7].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[8].get_center(), vg[9].get_center()).set_color(WHITE).set_opacity(0.6)
        l9 = Line(vg[9].get_center(), vg[10].get_center()).set_color(WHITE).set_opacity(0.6)
        l10 = Line(vg[10].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
        l11 = Line(vg[0].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        
       
    
        
        lvg.add(l1,l2,l3,l4,l5, l6, l7, l8, l9, l10, l11)
        self.add(lvg)

class Pisces(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)
        p = NumberPlane()

        

        xcoords = [-7/8, -9/16, -11/16, -9/8, -21/16, -1.75, -19/8, -1.75, -0.5, 0, 1.5, 35/16, 2.5, 23/8, 41/16, 17/8]
        ycoords = [43/16, 23/8, 35/16, 25/16, 17/16, 3/8, -7/16, -0.25, 1/16, 0, -1/8, -0.25, -1/8, -0.5, -13/16, -0.75]
        vg = VGroup()
        lvg = VGroup()
        for n in range(16):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)
        
        
        vg[:].set_color(WHITE)
        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[1].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[5].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[6].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[7].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l9 = Line(vg[8].get_center(), vg[9].get_center()).set_color(WHITE).set_opacity(0.6)
        l10 = Line(vg[9].get_center(), vg[10].get_center()).set_color(WHITE).set_opacity(0.6)
        l11 = Line(vg[10].get_center(), vg[11].get_center()).set_color(WHITE).set_opacity(0.6)
        l12 = Line(vg[11].get_center(), vg[12].get_center()).set_color(WHITE).set_opacity(0.6)
        l13 = Line(vg[12].get_center(), vg[13].get_center()).set_color(WHITE).set_opacity(0.6)
        l14 = Line(vg[13].get_center(), vg[14].get_center()).set_color(WHITE).set_opacity(0.6)
        l15 = Line(vg[14].get_center(), vg[15].get_center()).set_color(WHITE).set_opacity(0.6)
        l16 = Line(vg[15].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)
        l17 = Line(vg[0].get_center(), vg[12].get_center()).set_color(WHITE).set_opacity(0.6)
        
       
    
        
        lvg.add(l1,l2,l3,l4,l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17)
        self.add(lvg)








########## EXTRAS ###########


class Pegasus(VGroup):
    def __init__(self, **kwargs):
        VGroup.__init__(self, **kwargs)

        p = NumberPlane()

        xcoords = [2, 0.75, 0, 0.35, 0.75, 2.1, 3, -2.25, -2.55, 0, 1, 2.4, 3.5]
        ycoords = [2.75, 2.4, 2, 1.5, 1.35, 1.8, 2, 2, 0, 0, -0.75, -1.25, -0.5]
        vg = VGroup()
        lvg = VGroup()
        for n in range(13):
            star = Dot(point = p.c2p(xcoords[n-1], ycoords[n-1]), radius = 0.05, color = WHITE)
            vg.add(star)
            glowDot = GlowDot(rad = 1.5, opacity = 270)
            glowDot.move_to(star.get_center())
            self.add(glowDot)
            self.add(star)

        l1 = Line(vg[1].get_center(), vg[2].get_center()).set_color(WHITE).set_opacity(0.6)
        l2 = Line(vg[2].get_center(), vg[3].get_center()).set_color(WHITE).set_opacity(0.6)
        l3 = Line(vg[3].get_center(), vg[4].get_center()).set_color(WHITE).set_opacity(0.6)
        l4 = Line(vg[4].get_center(), vg[5].get_center()).set_color(WHITE).set_opacity(0.6)
        l5 = Line(vg[5].get_center(), vg[6].get_center()).set_color(WHITE).set_opacity(0.6)
        l6 = Line(vg[6].get_center(), vg[7].get_center()).set_color(WHITE).set_opacity(0.6)
        l7 = Line(vg[3].get_center(), vg[8].get_center()).set_color(WHITE).set_opacity(0.6)
        l8 = Line(vg[8].get_center(), vg[9].get_center()).set_color(WHITE).set_opacity(0.6)
        l9 = Line(vg[9].get_center(), vg[10].get_center()).set_color(WHITE).set_opacity(0.6)
        l10 = Line(vg[3].get_center(), vg[10].get_center()).set_color(WHITE).set_opacity(0.6)
        l11 = Line(vg[10].get_center(), vg[11].get_center()).set_color(WHITE).set_opacity(0.6)
        l12 = Line(vg[11].get_center(), vg[12].get_center()).set_color(WHITE).set_opacity(0.6)
        l13 = Line(vg[12].get_center(), vg[0].get_center()).set_color(WHITE).set_opacity(0.6)

        lvg.add(l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13)
        self.add(lvg)


class GlowDot(VGroup):
    def __init__(self, rad: float = 1.0, opacity: int = 250, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.rad = rad
        self.opacity = opacity

        for n in range(60):
            glowCircle = Circle(radius=rad*(1.002**(n**2))/400, stroke_opacity=0, fill_color=YELLOW,fill_opacity=0.2-n/opacity)
            self.add(glowCircle)


class Stars(VGroup):
    def __init__(self, stars : int = 2, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.stars = stars

        plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.5
            }
        )

        for n in range(self.stars):
            
            star = Dot(point = plane.c2p(random.uniform(-7,7), random.uniform(-4,4)), radius = random.uniform(0.005,0.05), fill_opacity = random.uniform(0.1,0.75))
            if random.randint(0,100) % 4 == 0:
                gd = GlowDot(rad = 0.5, opacity = 250)
                gd.move_to(star.get_center())
                self.add(gd, star)



class BackgroundStars(VGroup):
    def __init__(self, stars : int = 2, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.stars = stars


        plane = NumberPlane(
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 4,
                "stroke_opacity": 0.5
            }, 
            x_range = (-112/9, 112/9),
            y_range = (-16,16),
            x_length = 150,
            y_length = 150
        )
        
        one = rgb_to_color(hex_to_rgb("#ffd27d"))
        two = rgb_to_color(hex_to_rgb("#ffa371"))
        three = rgb_to_color(hex_to_rgb("#a6a8ff"))
        four = rgb_to_color(hex_to_rgb("#fffa86"))
        five = rgb_to_color(hex_to_rgb("#a87bff"))
        colors = [one, two, three, four, five]

        for n in range(self.stars):
            star = Dot(color = random.choice(colors), point = plane.c2p(random.uniform(-7,7), random.uniform(-4,4)), radius = random.uniform(0.005,0.05), fill_opacity = random.uniform(0.1,0.75))
            
            self.add(star)
        self.scale(0.25)
        


class test(Scene):
    def construct(self):
        testBSky = BackgroundStars(stars = 3000)
        testSky = Stars(stars = 150)

        #def create_glow(vmobject, rad=1, col=YELLOW):
        #glow_group = VGroup()
        #for idx in range(60):
            #new_circle = Circle(radius=rad*(1.002**(idx**2))/400, stroke_opacity=0, fill_color=col,
            #fill_opacity=0.2-idx/300).move_to(vmobject)
            #glow_group.add(new_circle)
        #return glow_group

        self.add(testBSky)
        self.add(testSky)
        


class pictureTest(Scene):
    def construct(self):
        plane = NumberPlane()
        pic = ImageMobject("test_ManimCE_v0.12.0")

        alien = Circle(radius = 0.5, color = TEAL_A).move_to(plane.c2p(-2,1))
        alien2 = Circle(radius = 0.5, color = TEAL_A).move_to(plane.c2p(1,-2))


        ss = Dot(color = YELLOW, radius = 0.03).set_opacity(0)
        #ss2 = Dot(color = YELLOW, radius = 0.03, opacity = 0).next_to(pic, DOWN)
        b = TracedPath(ss.get_center, dissipating_time = 0.5, stroke_opacity = [0,1], stroke_color = YELLOW)
        
        ar = Aries().scale(0.75).shift(LEFT*3)
        #aqtitle = Tex("Aquarius", color = BLUE, font_size = 50).to_edge(UP, buff = 1).to_edge(RIGHT, buff = 2)
        #aqbox = Rectangle(color = BLACK, height = 5, width = 4, stroke_color = WHITE).set_opacity(0.5).next_to(aqtitle, DOWN)
        #aqdesc = Tex("-January 20th - 18 Febuary", font_size = 25).move_to(aqbox.get_center()).shift(UP*1.5)

        ge = Gemini().scale(0.75).shift(LEFT*3)
        le = Leo().scale(0.75).shift(LEFT*3)
        li = Libra().scale(0.75).shift(LEFT*3)
        sa = Sagittarius().scale(0.75).shift(LEFT*3)
        aq = Aquarius().scale(0.75).shift(LEFT*3)
        ta = Taurus().scale(0.75).shift(LEFT*3)
        can = Cancer().scale(0.75).shift(LEFT*3)
        vi = Virgo().scale(0.75).shift(LEFT*3)
        sc = Scorpius().scale(0.75).shift(LEFT*3)
        cap = Capricorn().scale(0.75).shift(LEFT*3)
        pi = Pisces().scale(0.75).shift(LEFT*3)
        zodiacs = VGroup(ar, ge, le, li, sa, aq, ta, can, vi, sc, cap, pi)

        self.add(pic, ss, b)
        self.wait(5)

        for i in range(12):
            self.add(zodiacs[i])
            self.wait(2)
            self.remove(zodiacs[i])
            self.wait(2)
        
        self.add(zodiacs[0])
        self.wait(2)
        self.remove(zodiacs[0])
        self.wait(2)

        #self.add(aqtitle)
        #self.add(aqbox, aqdesc)
        self.wait(1)


class StarsAndAliens(Scene):
    def construct(self):
        plane = NumberPlane()
        pic = ImageMobject("test_ManimCE_v0.12.0")
        self.add(pic)

        for i in range(6):
            alien = Circle(radius = 0.5, color = TEAL_A).move_to(plane.c2p(random.randint(-6,6), random.randint(-3,3)))
            self.play(Broadcast(alien, focal_point = alien.get_center()))
            self.wait(random.randint(2,5))

        for n in range(6):
            ss = Dot(color = YELLOW, radius = 0.03).move_to(plane.c2p(random.randint(-6,6), random.randint(-5,5))).set_opacity(0)
            b = TracedPath(ss.get_center, dissipating_time = 0.5, stroke_opacity = [1,0], stroke_color = YELLOW)

            self.add(b)
            self.play(ss.animate.move_to(plane.c2p(random.randint(-6,6), random.randint(-5,5))))
            self.wait(random.randint(2,5))




class nebula(Scene):
    def construct(self):
        plane = NumberPlane()
        pic = ImageMobject("nebulaSkyPic.png").scale(0.250).move_to(plane.c2p(3,1))
        test = BackgroundStars(stars = 3000)
        self.add(pic)
        self.add(test)
        self.play(FadeIn(Aries()), run_time = 5)
        self.wait()
        