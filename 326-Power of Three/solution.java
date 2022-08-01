class solution {
    public boolean isPowerOfThree(int n) {
      if (n % 3 != 0 && n != 1)
            return false;

        int remainder;
        while (n > 1) {
            remainder = n % 3;
            if (remainder != 0)
                return false;

            n = n / 3;
        }

        if (n == 1)
            return true;
        else
            return false;
    }
}