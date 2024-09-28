from manim import *

"""
python3 2024/d2learn-logo/d2learn_logo.py
manim -pql 2024/d2learn-logo/d2learn_logo.py D2LearnLogo
"""

class D2LearnLogo(Scene):
    def construct(self):
        start_text = Text("用二进制为核心设计logo?")
        self.wait(0.5)
        self.play(Write(start_text))
        title = VGroup(
            Text("从"),Text("名字").set_color(RED),
            Text("到"), Text("二进制").set_color(BLUE),
        ).arrange(buff=0).to_edge(UP)

        self.wait(0.5)
        self.play(ReplacementTransform(start_text, title))
        
        d2learn_text = Text("d2learn").set_color(RED).shift(LEFT * 3)
        title_1 = title[1].copy()
        self.wait(0.5)
        self.play(Transform(title_1, d2learn_text))
        binary_text = Text("01..101").set_color(BLUE).shift(RIGHT * 3)
        self.wait(0.5)
        self.play(Transform(d2learn_text, binary_text))
        
        self.wait(1)

        ascii_table_text = Text("ASCII编码表")

        self.play(ReplacementTransform(
            VGroup(title_1, binary_text, d2learn_text),
            ascii_table_text
        ))

        ascii_table = ImageMobject("2024/d2learn-logo/ascii_table.png").scale(0.5)
        ascii_table.set_color(YELLOW)

        self.wait(0.5)
        self.play(
            FadeOut(ascii_table_text),
            FadeIn(ascii_table),
            Transform(title, Text("d2learn").to_edge(UP))
        )

        d2learn_alpha = VGroup(
            Text("d").set_color(RED),
            Text("2").set_color(RED),
            Text("l").set_color(RED),
            Text("e").set_color(RED),
            Text("a").set_color(RED),
            Text("r").set_color(RED),
            Text("n").set_color(RED),
        ).arrange(buff=0).to_edge(UP).set_color(WHITE)

        select_box = d2learn_alpha[0].copy()
        self.wait(0.5)
        self.play(Transform(select_box, Circle().move_to(RIGHT * 2.66 + UP * 0.38).scale(0.2)))

        self.wait(0.5)
        self.play(Transform(select_box, Text("01100100").set_color(BLUE)))

        self.wait(0.5)
        self.play(FadeOut(ascii_table), select_box.animate.set_opacity(0.5))
        self.wait(0.5)
        self.play(FadeOut(select_box), run_time=0.5)

        d2learn_binary = VGroup(
            # 'd'
            VGroup(Text("0"), Text("1"), Text("1"), Text("0"), Text("0"), Text("1"), Text("0"), Text("0"))
                .arrange(buff=0.1).set_color(BLUE).shift(LEFT * 4 + UP).scale(0.6),
            # '2'
            VGroup(Text("0"), Text("0"), Text("1"), Text("1"), Text("0"), Text("0"), Text("1"), Text("0"))
                .arrange(buff=0.1).set_color(BLUE).shift(LEFT * 1.5 + UP).scale(0.6),
            # 'l'
            VGroup(Text("0"), Text("1"), Text("1"), Text("0"), Text("1"), Text("1"), Text("0"), Text("0"))
                .arrange(buff=0.1).set_color(BLUE).shift(RIGHT * 1.5 + UP).scale(0.6),
            # 'e'
            VGroup(Text("0"), Text("1"), Text("1"), Text("0"), Text("0"), Text("1"), Text("0"), Text("1"))
                .arrange(buff=0.1).set_color(BLUE).shift(RIGHT * 4 + UP).scale(0.6),
            # 'a'
            VGroup(Text("0"), Text("1"), Text("1"), Text("0"), Text("0"), Text("0"), Text("0"), Text("1"))
                .arrange(buff=0.1).set_color(BLUE).shift(LEFT * 2.5 + DOWN).scale(0.6),
            # 'r'
            VGroup(Text("0"), Text("1"), Text("1"), Text("1"), Text("0"), Text("0"), Text("1"), Text("0"))
                .arrange(buff=0.1).set_color(BLUE).shift(DOWN).scale(0.6),
            # 'n'
            VGroup(Text("0"), Text("1"), Text("1"), Text("0"), Text("1"), Text("1"), Text("1"), Text("0"))
                .arrange(buff=0.1).set_color(BLUE).shift(RIGHT * 2.5, DOWN).scale(0.6),
        )

        for i in range(7):
            self.play(Transform(d2learn_alpha[i], d2learn_binary[i]))

        for i in range(7):
            d2learn_binary[i].arrange(buff=0.2)
        d2learn_binary.arrange(DOWN, buff=0.1, aligned_edge=LEFT).scale(1.5)

        self.wait(0.5)
        self.play(ReplacementTransform(d2learn_alpha, d2learn_binary))

        self.wait()

        d2learnLogoMap = [
            [0,1,1,0,0,1,0,0], # d
            [0,0,1,1,0,0,1,0], # 2
            [0,1,1,0,1,1,0,0], # l
            [0,1,1,0,0,1,0,1], # e
            [0,1,1,0,0,0,0,1], # a
            [0,1,1,1,0,0,1,0], # r
            [0,1,1,0,1,1,1,0]  # n
        ]

        def generate_logo():
            for i in range(7):
                for j in range(8):
                    if d2learnLogoMap[i][j] == 1:
                        self.play(FadeToColor(d2learn_binary[i][j], WHITE), run_time=0.15)
                    else:
                        d2learn_binary[i][j].set_opacity(0)

        generate_logo()
        
        self.wait(0.5)
        self.play(FadeOut(d2learn_binary))

if __name__ == "__main__":
    scene = D2LearnLogo()
    scene.render()