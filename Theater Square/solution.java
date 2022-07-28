class solution {

    public static int theater_square(int m, int n, int a) {
        int width = Math.round((float) m / a); // number of square needed for width
        int height = Math.round((float) n / a); // number of squares need for height

        // the total amount of squares need to cover the field is widht * height
        return width * height;
    }

    public static void main(String[] args) {
        
        // System.out.println("me is " + theater_square(300, 30, 4)); 

    }

}
