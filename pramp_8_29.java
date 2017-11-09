

import java.io.*;
import java.util.*;

class Solution {

  static int shiftedArrSearch(int[] shiftArr, int num) {
    
      int shiftBorder = binaryBorderSearch(shiftArr);
    
    
    // Maybe you want to write your own test cases in the main function?
    // Try with [3,4,5,1,2] ?
   
    
       int searchL = 0, searchR = shiftArr.length - 1;
      if (num >= shiftArr[0]) {
          searchR = shiftBorder;
      } else {
          searchL = shiftBorder;
      }

      int res = binaryElementSearch(shiftArr, searchL, searchR, num); 
      if (shiftArr[res] != num) {
         return -1;
      } else {
        return res;
      }
  }
  
  private static int binaryBorderSearch(int[] shiftArr) {
      // should r = shiftArr.length -1?
      int l = 0, r = shiftArr.length - 1;
      while (l + 1 < r) {
        int m = (r + l) / 2;
        int cur = shiftArr[m];
        if (shiftArr[r] < shiftArr[m]) {
          l = m;
        } else {
          r = m;
        }
      }
    return l;
  }
  
  private static int binaryElementSearch(int[] arr, int lb, int rb, int num) {
    // are you using searchL or searchR here? 
    // I don't see you are using it :/ 
    // Go take a look at how you call your function 
    int l = lb, r = rb;
      while (l + 1 < r) {
        int m = (r + l) / 2;
        int cur = arr[m];
        if (arr[m] < num) {
          l = m + 1;
        } else  if (arr[m] > num) {
          r = m;
        } else {
          return m;
        }
      }
    return l;
  }

  public static void main(String[] args) {
    int[] test = new int[] {1, 2, 3, 4, 5, 0};
    // maybe you want to test your binaryBorderSearch first? see if it works
    // i looked at it several minutes ago) okey  one more time)
    System.out.println(shiftedArrSearch(test, 5));
  }

}
