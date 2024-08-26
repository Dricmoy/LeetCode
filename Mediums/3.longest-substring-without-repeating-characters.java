package Mediums;
/*
 * @lc app=leetcode id=3 lang=java
 *
 * [3] Longest Substring Without Repeating Characters
 */

// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;

        for (int i = 0; i < s.length(); i++){
            StringBuilder cur_substring = new StringBuilder();
            for (int j = i; j < s.length(); j ++){
                if (cur_substring.indexOf(String.valueOf(s.charAt(j))) != -1){
                    break;
                }
                cur_substring.append(s.charAt(j));
            }
            if (maxLength < cur_substring.length()){
                maxLength = cur_substring.length();
            }
        }
        
        return maxLength;
    }
}
// @lc code=end

