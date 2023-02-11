// MORE COMPACT FORM OF THE CODE

// class Solution {
//     public int garbageCollection(String[] garbage, int[] travel) {
//         int[] counts = new int[26]; // store frequency of 'G', "M" and "P"
//         int[] distance = new int[3];// store distance traveled
        
//         String GMP = "GMP";// stores 'GMP' and used for inner loop iteration  and makes the code compact

//         int sum = 0;
//         for (int i = 0; i < garbage.length; i++) {

//             for (char c: garbage[i].toCharArray())// check their occurence
//                 counts[c - 'A']++;

//             for (int j = 0; j < 3; j++) {
//                 // handle G,M,P at a time, since j = 0, 1,2, G,M,P respectively
//                 char c = GMP.charAt(j);
//                 if (counts[c - 'A'] > 0) { // frequency > 0, so need to be added to sum
//                     sum += counts[c - 'A']; // added to sum
//                     counts[c - 'A'] = 0; // set freqency to zero, since it is added
//                     if (i > 0) { // if i > 0, added the distance traveled
//                         distance[j] += travel[i - 1]; // added the current and previos distances 
//                         sum += distance[j];
//                         distance[j] = 0;    // set distance to zero, since it is already added
//                     }
//                 } else if (i > 0) // if frequency ==0, store distance traveled for future
//                     distance[j] += travel[i - 1];
//             }
//         }

//         return sum;
//     }
// }


// HERE IS A MORE SIMPLER ONE 
class Solution {
    public int garbageCollection(String[] garbage, int[] travel) {
        // Here is how the code works with O(n) time complexity
        // for each string it does the following
        //  1, store the frequency
        //  2, if i > 0, store travel distance
        //  3, add travel distance and frequency
        //  4, set travel distance and frequency to zero

    	// Here is for garbage 'G', I copied Down for "M" and "P" as well
        /// THE SHORT VERSION IS COMMENTED ABOVE
        //       // for garbage - G
        //       if(counts['G' - 'A'] > 0){    // 'G' count is > 0, so add to sum
        //           sum +=  counts['G'- 'A'];  // 'G' count added to sum
        //           counts['G'- 'A'] = 0;      // set 'G' count to zero
        //           if( i > 0){        // if i > 0, it may need to travel to different house
        //               distance[0] += travel[i - 1]; // addeds the previos and current house distance
        //               sum += distance[0];
        //               distance[0] = 0;     // set the distance to zero
        //           }
        //       }else if( i > 0) /// if the frequency is zero, increase the travel distance
        //           distance[0] += travel[i - 1];


        int[] counts = new int[26]; // store frequency of 'G', "M" and "P"
        int[] distance = new int[3];// store distance traveled
        
        int sum = 0;        
        for(int i = 0;  i < garbage.length; i++ ){
            
            for(char c : garbage[i].toCharArray())
                counts[c - 'A']++;
            
            // for garbage - G
            if(counts['G' - 'A'] > 0){ 
                sum +=  counts['G'- 'A'];
                counts['G'- 'A'] = 0;
                if( i > 0){
                    distance[0] += travel[i - 1];
                    sum += distance[0];
                    distance[0] = 0;
                }
            }else if( i > 0) 
                distance[0] += travel[i - 1];
            
            // for garbage - P
            if(counts['P' - 'A'] > 0){
                sum +=  counts['P'- 'A'];
                counts['P'- 'A'] = 0;
                if( i > 0){
                    distance[1] += travel[i - 1];
                    sum += distance[1];
                    distance[1] = 0;
                }
            }else if( i > 0)
                distance[1] += travel[i - 1];

            // for garbage - L
            if(counts['M' - 'A'] > 0){
                sum +=  counts['M'- 'A'];
                counts['M'- 'A'] = 0; 
                if( i > 0){
                    distance[2] += travel[i - 1];
                    sum += distance[2];
                    distance[2] = 0;
                }
            }else if( i > 0)
                distance[2] += travel[i - 1];            
        }

        return sum;
    }
}
