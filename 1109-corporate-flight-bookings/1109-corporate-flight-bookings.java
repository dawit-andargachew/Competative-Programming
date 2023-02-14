class Solution {
    public int[] corpFlightBookings(int[][] booking, int n) {
        
        // booking[i][0] = starting row
        // booking[i][1] = endign row
        int[] flight = new int[n];// array to be returned

        for(int i =0; i < booking.length; i++){

            // since the array is 0-based index, we need to substract 1 from each index
            int start = booking[i][0] - 1;
            int end = booking[i][1] - 1;

            while( start <= end)// start and end are inclusive
                flight[start++] += booking[i][2];
        }

        return flight;
    }
}