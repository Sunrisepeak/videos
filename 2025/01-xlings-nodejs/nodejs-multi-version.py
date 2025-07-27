from manim import *

"""
Manim Community v0.18.1
manim -pql 2025/01-xlings-nodejs/nodejs-multi-version.py
manim -pqh 2025/01-xlings-nodejs/nodejs-multi-version.py
"""

def video_start(scene, mobject):

    logo_svg = SVGMobject(
        "2025/01-xlings-nodejs/imgs/xlings-logo.svg",
    )

    logo_text = VGroup(
        Tex(r"\textit{\underline{xlings}}"),
        Tex(r"\textit{+}", color=RED)
    ).arrange(RIGHT, buff=0.1).scale(0.8).to_corner(UP + LEFT)

    scene.play(Write(logo_svg), run_time=0.8)
    scene.bring_to_front(logo_svg)

    scene.play(
        Transform(logo_svg, logo_text),
        FadeIn(mobject),
    )

    return logo_svg, mobject

class NodejsMultiVersion(MovingCameraScene):
    def construct(self):

        nodejs_wininstall = ImageMobject(
            "2025/01-xlings-nodejs/imgs/nodejs-win-install.png",
        ).scale(1.5)

        logo, _ = video_start(self, nodejs_wininstall)

        tool_svg = SVGMobject("2025/01-xlings-nodejs/imgs/tool.svg")
        tool_svg.shift(RIGHT * 3)
        tool_title = Text("一键安装").scale(0.5).next_to(tool_svg, UP * 1.5)

        self.play(
            nodejs_wininstall.animate.scale(0.8).shift(LEFT * 3),
            FadeIn(tool_svg),
        )

        nodejs_wininstall_title = Text("手动下载安装").scale(0.5).next_to(nodejs_wininstall, UP * 1.5)

        self.play(
            FadeIn(nodejs_wininstall_title),
            FadeIn(tool_title),
            run_time = 0.5
        )

        self.wait(0.5)

        npm_versions = VGroup(
            Text("11.0.0"),
            Text("10.9.2"),
            Text("9.15.0"),
            Text("8.19.4"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.7)

        nodejs_versions = VGroup(
            Text("24.4.1"),
            Text("23.6.0"),
            Text("22.17.1"),
            Text("20.19.0")
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).scale(0.7)

        npm_versions.move_to(LEFT * 3)
        nodejs_versions.move_to(RIGHT * 3)

        npm_svg = SVGMobject("2025/01-xlings-nodejs/imgs/npm.svg")
        nodejs_svg = SVGMobject("2025/01-xlings-nodejs/imgs/nodejs-svgrepo-com.svg")

        npm_svg.scale(0.3).next_to(npm_versions, UP * 1.5)
        nodejs_svg.scale(0.5).next_to(nodejs_versions, UP * 1.5)

        self.play(
            FadeOut(nodejs_wininstall),
            FadeOut(tool_svg),
            ReplacementTransform(nodejs_wininstall_title, npm_svg),
            ReplacementTransform(tool_title, nodejs_svg),
        )

        self.play(
            Create(npm_versions),
            Create(nodejs_versions)
        )

        version_links = VGroup(
            Line(npm_versions[0].get_right(), nodejs_versions[1].get_left(), color=WHITE),
            Line(npm_versions[3].get_right(), nodejs_versions[2].get_left(), color=BLUE),
            Line(npm_versions[1].get_right(), nodejs_versions[3].get_left(), color=YELLOW),
            Line(npm_versions[0].get_right(), nodejs_versions[0].get_left(), color=PURE_RED),
            Line(npm_versions[2].get_right(), nodejs_versions[0].get_left(), color=PURPLE),
        )

        for i in range(2):
            self.play(Create(version_links[0]), run_time=0.25)
            for j in range(len(version_links) - 1):
                self.play(
                    FadeOut(version_links[j]),
                    Create(version_links[j + 1]),
                    run_time=0.25
                )
            if i == 0:
                self.play(FadeOut(version_links[4]), run_time=0.25)

        self.wait(0.5)

        # 1 - 安装
        section_1 = Text(
            "一键安装 xlings install",
            font="Microsoft YaHei",
            t2c = { "xlings install": YELLOW }
        )

        npm_svg.set_opacity(0)
        nodejs_svg.set_opacity(0)
        npm_versions.set_opacity(0)
        nodejs_versions.set_opacity(0)
        tmp_version_link = version_links[4].copy()
        version_links[4].set_opacity(0)

        self.play(ReplacementTransform(tmp_version_link, section_1))

        self.wait(0.5)

        section_1.set_opacity(0)
        self._play_video()

        self.wait(0.5)

        # 2 - 切换版本
        section_2 = Text(
            "切换版本 xlings use",
            font="Microsoft YaHei",
            t2c = { "xlings use": YELLOW }
        )

        self.play(Write(section_2), run_time = 1)

        self.wait(0.5)

        section_2.set_opacity(0)
        self._play_video()

        self.wait(0.5)

        # 3 - 卸载时版本自动切换
        section_3 = Text(
            "npm和nodejs版本自由组合",
            font="Microsoft YaHei",
            t2c = { "npm": YELLOW, "nodejs": YELLOW  }
        )

        self.play(Write(section_3), run_time = 1)

        self.wait(0.5)

        section_3.set_opacity(0)
        self._play_video()

        self.wait(0.5)

        # 4 - 卸载时版本自动切换
        section_4 = Text(
            "卸载时版本自动切换 xlings remove",
            font="Microsoft YaHei",
            t2c = { "xlings remove": YELLOW }
        )

        self.play(Write(section_4), run_time = 1)

        self.wait(0.5)

        section_4.set_opacity(0)
        self._play_video()

        self.wait(0.5)

        linux_svg = SVGMobject("2025/01-xlings-nodejs/imgs/linux.svg").scale(0.8)
        windows_svg = SVGMobject("2025/01-xlings-nodejs/imgs/windows.svg").scale(0.75)
        macos_svg = SVGMobject("2025/01-xlings-nodejs/imgs/macos.svg").scale(0.8)

        self.play(Write(linux_svg), run_time=1)

        self.play(windows_svg.animate.shift(LEFT * 3.5))
        self.play(macos_svg.animate.shift(RIGHT * 3.5))

        self.wait(0.5)

        # 5 - ending

        ending = VGroup(
            Text("一个抽象的包管理器", color=RED).scale(0.9),
            Tex(r"\textit{\underline{https://xlings.d2learn.org}}"),
        ).arrange(DOWN, buff=0.15).scale(0.8)

        self.play(
            FadeOut(linux_svg),
            FadeOut(windows_svg),
            FadeOut(macos_svg),
            Transform(logo, ending)
        )

        self.wait(1)

        self.play(FadeOut(logo), run_time=3)

    def _play_video(self):
        video_play_2 = Text("播放视频")
        self.add(video_play_2)
        self.wait(2)
        video_play_2.set_opacity(0)