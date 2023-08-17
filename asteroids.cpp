#include <vector>
using namespace std;
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        for (int i=0; i < asteroids.size()-1; i++){
            for (int j=1; j < asteroids.size(); j++){
                if (asteroids[i] > 0 && asteroids[j] > 0){
                    std::cout << "i > j: " << asteroids[i] << " " << asteroids[j] << endl;
                    ;
                }
                else if (asteroids[i] < 0 && asteroids[j] < 0){
                    std::cout << "i < j: " << asteroids[i] << " " << asteroids[j] << endl;
                    ;
                }
                else if (asteroids[j] < 0){
                    if (asteroids[i] < abs(asteroids[j])){
                        std::cout << "i < j delete i";
                        asteroids.erase(asteroids.begin()+i);
                        for (auto a: asteroids){
                            std::cout << a << " ";
                        }
                    }
                    else if (asteroids[i] > abs(asteroids[j])){
                        asteroids.erase(asteroids.begin()+j);
                        std::cout << "i > j delete j";
                        for (auto a: asteroids){
                            std::cout << a << " ";
                        }
                    }
                    else {
                        asteroids.erase(asteroids.begin()+j);
                        asteroids.erase(asteroids.begin()+i);
                        std::cout << "i == j delete both";
                        for (auto a: asteroids){
                            std::cout << a << " ";
                        }
                    }
                }
            }
        }
        return asteroids;
    }
};