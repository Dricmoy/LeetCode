class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        auto count = 0, check = 0, remcount = 0;
        for (int i = 0; i < mat.size(); i++){
            for (int j = 0; j < mat[0].size(); j++){
                if (mat[i][j] == 1){
                    count ++;
                    check = 0;

                    for (int x = 0; x < mat[0].size(); x++ ){
                        if (mat[i][x] == 1){
                            if (j != x){
                                remcount++;
                                check++;
                                break;
                            }
                        }
                    }

                    if (!check){
                        for (int x = 0; x < mat.size(); x++){
                            if (mat[x][j] == 1){
                                if (i != x){
                                    remcount++;
                                    break;
                                }
                            }
                        }
                    }

                }
            }
        }
        return count - remcount;
    }
};


//Forgot to use break at first, debugged using remcount, seems to offer more performance, probably a fluke. Used the var check, to avoid unnecessary looping