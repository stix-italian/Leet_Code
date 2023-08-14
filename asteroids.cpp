class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        for (int i=0; i < asteroids.size(); i++){
            for (int j=1; j < asteroids.size()-1; j++){
                if (asteroids[i] > 0 && asteroids[j] > 0){
                    ;
                }
                else if (asteroids[i] < 0 && asteroids[j] < 0){
                    ;
                }
                else if (asteroids[j] < 0){
                    if (asteroids[i] < abs(asteroids[j])){
                        asteroids.erase(asteroids.begin()+i);
                    }
                    else if (asteroids[i] > abs(asteroids[j])){
                        asteroids.erase(asteroids.begin()+j);
                    }
                    else {
                        asteroids.erase(asteroids.begin()+j);
                        asteroids.erase(asteroids.begin()+i);
                    }
                }
            }
        }
        return asteroids;
    }
};