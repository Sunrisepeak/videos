add_repositories("speak-repos git@github.com:Sunrisepeak/speak-repos.git")
add_requires("hanim")

target("d2learn-logo")
    set_kind("binary")
    add_packages("hanim")
    add_files("main.cpp")