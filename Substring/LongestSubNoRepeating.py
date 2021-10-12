# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

''' Pseude code
Sol 1: O(n^2): Window Sliding: update entire set from the new start-idx to the new end-idx
Sol 2: O(n):  Window Sliding but when updating unique_set by using del the item by key
'''

testcase = ['abcafg', ' ', 'au', "abcabcbb", "pwwkew"];
expected_result = [5, 1, 2, 3, 3];

class Sol1:
    def solve(self, s):
        string_len = len(s);
        if (string_len <= 1):   
            return string_len;
        max_len = 0;
        unique_set = {};
        start_idx = 0;
        end_idx = 0;
        
        for idx in range(0, string_len):
            item = s[idx];
            if (item in unique_set):
                existing_idx = unique_set[item];
                unique_set.clear();
                start_idx = existing_idx + 1;
                if (start_idx == idx):
                    unique_set[item] = idx;
                else:
                    # the next lines will cause O(n^2) time complexity
                    for index in range(start_idx, end_idx + 2):
                        unique_set[s[index]] = index;
            else:
                unique_set[item] = idx;
            end_idx = idx;
            new_len = end_idx - start_idx + 1;
            if (new_len > max_len):
                max_len = new_len;
        return max_len;


class Sol2:
    def solve(self, s):
        string_len = len(s);
        if (string_len <= 1):   
            return string_len;
        max_len = 0;
        unique_set = {};
        start_idx = 0;
        end_idx = 0;

        for idx in range(0, string_len):
            item = s[idx];
            if (item in unique_set):
                existing_idx = unique_set[item];
                old_start_idx = start_idx;
                start_idx = existing_idx + 1;
                if (start_idx == idx):
                    unique_set.clear();
                else:
                    # unique_set = {key:unique_set[key] for key in unique_set if unique_set[key] >= start_idx};
                    # -> worse than
                    for del_key in range(old_start_idx, start_idx):
                        del unique_set[s[del_key]];
            unique_set[item] = idx;
            end_idx = idx;
            new_len = end_idx - start_idx + 1;
            if (new_len > max_len):
                max_len = new_len;
        return max_len;

print(testcase)
result = [Sol2().solve(item) for item in testcase];
print('result', result)
print('Expect', expected_result)