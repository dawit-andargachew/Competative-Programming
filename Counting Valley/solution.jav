class solution {

  public static int countingValleys(int steps, String path) {
      int seaLevel = 0;
      int valleyCount = 0;

      for (int i = 0; i < path.length(); i++) {
          if (path.charAt(i) == 'U') {
              // if (seaLevel == -1) // 1
              // valleyCount++;
              seaLevel++;
              if (seaLevel == 0) // 2
                  valleyCount++;

          } else if (path.charAt(i) == 'D') {
              // if (seaLevel ==-1) // 3
              // valleyCount++;
              seaLevel--;

              // if (seaLevel ==-1) //4
              // valleyCount++;
          }

      }

      return valleyCount;
  }

}
