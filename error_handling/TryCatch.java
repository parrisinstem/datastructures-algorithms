package error_handling;


public class TryCatch {

    public static int linearSearch(int[] searchList, int targetValue) {
        for (int i = 0; i < searchList.length; i++) {
            if (searchList[i] == targetValue) {
                return i;
            }
        }
        throw new IllegalArgumentException(targetValue + " not in list");
    }

    public static void main(String[] args) {
        int[] numberList = {10, 14, 19, 26, 27, 31, 33, 35, 42, 44};
        int targetNumber = 33;

        try {
            int result = linearSearch(numberList, targetNumber);
            System.out.println(result);
            System.out.println(linearSearch(numberList, 100));
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
