#include <vector>

#include "hanim.h"


using namespace hanim;

const static int THICKNESS_240P = 1;
const static int THICKNESS_480P = 2;
const static int THICKNESS_1080P = 4;

const static int THICKNESS = THICKNESS_480P; // THICKNESS_1080P;

static std::vector<std::vector<bool>> d2learnLogoMap {
    {0,1,1,0,0,1,0,0}, // d
    {0,0,1,1,0,0,1,0}, // 2
    {0,1,1,0,1,1,0,0}, // l
    {0,1,1,0,0,1,0,1}, // e
    {0,1,1,0,0,0,0,1}, // a
    {0,1,1,1,0,0,1,0}, // r
    {0,1,1,0,1,1,1,0}  // n
};

struct D2LearnLogo : public Scene {
    virtual void timeline() override {
        auto logo = PixelPanel();
        logo.stroke_color(HColor::BLACK);
        logo.scale(2);
        //play(Create(logo));
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 8; j++) {
                if (d2learnLogoMap[i][j]) {
                    play(FillColor(logo[i][j], HColor::WHITE), 5);
                } else {
                    play(FadeOut(logo[i][j]), 5);
                }
            }
        }

        play(FillColor(logo[7][0], HColor::RED), 10);
        play(FillColor(logo[7][1], HColor::ORANGE), 10);
        play(FillColor(logo[7][2], HColor::YELLOW), 10);
        play(FillColor(logo[7][3], HColor::GREEN), 10);
        play(FillColor(logo[7][4], HColor::CYAN), 10);
        play(FillColor(logo[7][5], HColor::BLUE), 10);
        play(FillColor(logo[7][6], HColor::PURPLE), 10);
        play(FillColor(logo[7][7], HColor::WHITE), 10);
    }
};

struct D2LearnLogoColor : public Scene {
    virtual void timeline() override {
        auto logo = PixelPanel();
        logo.stroke_color(HColor::BLACK);
        logo.fill_color(HColor::BLACK);
        logo.scale(3);

        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 8; j++) {
                if (d2learnLogoMap[i][j]) {
                    logo[i][j].fill_color(HColor::WHITE);
                }
            }
        }

        play(FadeIn(logo));

        auto toCyan = HAnimGroup();
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 8; j++) {
                if (d2learnLogoMap[i][j]) {
                    toCyan.add(FillColor(logo[i][j], HColor::CYAN));
                }
            }
        }

        play(toCyan);

        auto logo_border = Grid(2, 2, 0.25);
        logo_border.scale(3);
        play(DrawBorder(logo_border));

        auto border1 = Rectangle(logo[0][0].get_center(), logo[7][7].get_center());
        border1.shift({0.375, 0.375, 0});
        border1.stroke_color(HColor::PURPLE);
        border1.thickness(THICKNESS * 1.35);
        play(FadeIn(border1));
        play(FadeOut(border1), 40);
        border1.stroke_opacity(1);
        play(FadeIn(border1), 40);
        play(FadeOut(border1), 40);

        auto bottom_border = Rectangle(
            logo[7][0].clone().shift({-0.375, -0.375, 0}).get_center(),
            logo[7][7].clone().shift({0.375, 0.375, 0}).get_center()
        );
        bottom_border.stroke_color(HColor::PURPLE);
        bottom_border.thickness(THICKNESS * 1.35);

        play(Transform(border1, bottom_border));
        play(FadeOut(border1), 40);
        border1.stroke_opacity(1);
        play(FadeIn(border1), 40);
        play(FadeOut(border1), 40);

        auto red = Circle().fill_color(HColor::RED).stroke_opacity(0);
        red.move_to(HPos::LEFT * 5);
        red.shift(HPos::UP * 3);
        red.scale(0.2);

        auto orange = red.clone().fill_color(HColor::ORANGE).shift(HPos::DOWN * 1);
        auto yellow = red.clone().fill_color(HColor::YELLOW).shift(HPos::DOWN * 2);
        auto green = red.clone().fill_color(HColor::GREEN).shift(HPos::DOWN * 3);
        auto cyan = red.clone().fill_color(HColor::CYAN).shift(HPos::DOWN * 4);
        auto blue = red.clone().fill_color(HColor::BLUE).shift(HPos::DOWN * 5);
        auto purple = red.clone().fill_color(HColor::PURPLE).shift(HPos::DOWN * 6);
        
        play(DrawBorder(red), 30);
        play(DrawBorder(orange), 30);
        play(DrawBorder(yellow), 30);
        play(DrawBorder(green), 30);
        play(DrawBorder(cyan), 30);
        play(DrawBorder(blue), 30);
        play(DrawBorder(purple), 30);

        play(HAnimGroup(
            Transform(red, logo[7][0].clone().fill_color(HColor::RED)),
            Transform(orange, logo[7][1].clone().fill_color(HColor::ORANGE)),
            Transform(yellow, logo[7][2].clone().fill_color(HColor::YELLOW)),
            Transform(green, logo[7][3].clone().fill_color(HColor::GREEN)),
            Transform(cyan, logo[7][4].clone().fill_color(HColor::CYAN)),
            Transform(blue, logo[7][5].clone().fill_color(HColor::BLUE)),
            Transform(purple, logo[7][6].clone().fill_color(HColor::PURPLE))
        ));

        logo[7][0].fill_color(HColor::RED);
        logo[7][1].fill_color(HColor::ORANGE);
        logo[7][2].fill_color(HColor::YELLOW);
        logo[7][3].fill_color(HColor::GREEN);
        logo[7][4].fill_color(HColor::CYAN);
        logo[7][5].fill_color(HColor::BLUE);
        logo[7][6].fill_color(HColor::PURPLE);

        wait(30);

        auto target_color = logo[7][7].clone().fill_color(HColor::WHITE);
        play(HAnimGroup(
            Transform(red, target_color),
            Transform(orange, target_color),
            Transform(yellow, target_color),
            Transform(green, target_color),
            Transform(cyan, target_color),
            Transform(blue, target_color),
            Transform(purple, target_color)
        ));

        red.opacity(0);
        orange.opacity(0);
        yellow.opacity(0);
        green.opacity(0);
        cyan.opacity(0);
        blue.opacity(0);
        purple.opacity(0);

        logo[7][7].color(HColor::WHITE);

        wait(30);

    }
};

int main() {
    hanim::HEngine::default_config1();
    //hanim::HEngine::set_window_size(320, 240);
    //hanim::HEngine::default_config2();
    hanim::HEngine::recorder_file_name("d2learn-logo");
    hanim::HEngine::render(D2LearnLogo());
    //hanim::HEngine::render(D2LearnLogoColor());
    hanim::HEngine::save_frame_to_img("d2learn-logo.png");
    return 0;
}