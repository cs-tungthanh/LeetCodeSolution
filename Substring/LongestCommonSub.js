const maxCommon = ([head1,...tail1], [head2,...tail2], len = 0) => {
    if ( typeof head1 === 'undefined' || typeof head2 === 'undefined' ) {
         return len;
    }
    if ( head1 === head2 ) {
      return maxCommon( tail1, tail2, len+1 );
    }
    const firstBranch = maxCommon( tail1, [head2, ...tail2], 0 );
    const secondBranch = maxCommon([head1,...tail1], tail2, 0 );
    return Math.max( ...[len, firstBranch, secondBranch ] );
}
// a magnitude of n! * m! steps,
/*******
Explanation:
We will use an optional len argument to store the number of character matches 
    before the current iteration of maxCommon was called.
We will use recursion to process the strings.
If any of the strings have a length of 0, either head1, or head2 becomes undefined. 
    This is our exit condition for the recursion, and we return len, i.e. the number 
    of matching characters right before one of the strings became empty.
If both strings are non-empty, and the heads match, we recursively call maxCommon 
    on the tails of the strings, and increase the length of the counter of the 
    preceding common substring sequence by 1.
If the heads don’t match, we remove one character from either the first string or 
    from the second string, and calculate their maxCommon score, with len initialized 
    to 0 again. The longest string may either be in one of these branches, 
    or it is equal to len, counting the matches preceding the current strings [head1,...tail1] and [head2,...tail2].

// testcase
('123', '1')
('11111', '11f111g')
('11111', '11f111g')
// expected output
1
3
2
*******/

