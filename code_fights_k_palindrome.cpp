int isKPalDP(string str1, string str2, int m, int n)
{
    // Create a table to store results of subproblems
    int dp[m + 1][n + 1];
 
    // Fill dp[][] in bottom up manner
    for (int i = 0; i <= m; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            // If first string is empty, only option is to
            // remove all characters of second string
            if (i == 0)
                dp[i][j] = j; // Min. operations = j
 
            // If second string is empty, only option is to
            // remove all characters of first string
            else if (j == 0)
                dp[i][j] = i; // Min. operations = i
 
            // If last characters are same, ignore last character
            // and recur for remaining string
            else if (str1[i - 1] == str2[j - 1])
                dp[i][j] = dp[i - 1][j - 1];
 
            // If last character are different, remove it
            // and find minimum
            else
             dp[i][j] = 1 + min(dp[i - 1][j], // Remove from str1
                             dp[i][j - 1]); // Remove from str2
        }
    }
 
    return dp[m][n];
}
 
// Returns true if str is k palindrome.
bool kpalindrome(string str, int k)
{
    string revStr = str;
    reverse(revStr.begin(), revStr.end());
    int len = str.length();
 
    return (isKPalDP(str, revStr, len, len) <= k*2);
}