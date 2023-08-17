#include <vector>
using namespace std;
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        for (int i=0; i < asteroids.size()-1; i++){
            cout << "i is: " << i << endl;
            for (auto a: asteroids){
                        std::cout << a << " ";
                    }
                    cout << "end of starting vector." << endl;
            if (asteroids[i] > 0 && asteroids[i+1] > 0){
                std::cout << "both are positive no collision " << asteroids[i] << " " << asteroids[i+1] << endl;
                ;
            }
            else if (asteroids[i] < 0 && asteroids[i+1] < 0){
                std::cout << "both are negative no collision " << asteroids[i] << " " << asteroids[i+1] << endl;
                ;
            }
            else if (asteroids[i+1] < 0){
                if (asteroids[i] < abs(asteroids[i+1])){
                    std::cout << "i < i+1 delete i" << endl;
                    asteroids.erase(asteroids.begin()+i);
                    for (auto a: asteroids){
                        std::cout << a << " ";
                    }
                    cout << endl;
                }
                else if (asteroids[i] > abs(asteroids[i+1])){
                    asteroids.erase(asteroids.begin()+i+1);
                    std::cout << "i > i+1 delete i+1" << endl;
                    for (auto a: asteroids){
                        std::cout << a << " ";
                    }
                    cout << endl;
                }
                else {
                    asteroids.erase(asteroids.begin()+i+1);
                    asteroids.erase(asteroids.begin()+i);
                    std::cout << "i == i+1 delete both" << endl;
                    for (auto a: asteroids){
                        std::cout << a << " ";
                    }
                    cout << endl;
                }
            }
        }
        return asteroids;
    }
};