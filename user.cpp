#include <iostream>
#include <fstream>
#include <string>
#include <curl>

extern "C" {
    #include "instaloader.h"
}

int main() {
    std::string username;
    std::cout << "Enter username: ";
    std::cin >> username;

    Instaloader instaloader;
    instaloader__context context;
    instaloader__context_init(&context);
    instaloader__profile profile;
    instaloader__profile_init(&profile);

    if (instaloader__profile_from_username(&context, &profile, username.c_str())) {
        std::cout << "Profile not found or private." << std::endl;
        return 1;
    }

    CURL *curl;
    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, profile.profile_pic_url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, NULL);

        std::string filename = username + ".jpg";
        std::ofstream photo(filename, std::ios::binary);
        if (photo.is_open()) {
            curl_easy_setopt(curl, CURLOPT_WRITEDATA, &photo);
            curl_easy_perform(curl);
            photo.close();
            std::cout << "Profile picture saved as " << filename << std::endl;
        } else {
            std::cerr << "Unable to open file." << std::endl;
            return 1;
        }
        curl_easy_cleanup(curl);
    } else {
        std::cerr << "Failed to initialize curl." << std::endl;
        return 1;
    }

    std::cout << "Followers: " << profile.followers << std::endl;

    return 0;
}
