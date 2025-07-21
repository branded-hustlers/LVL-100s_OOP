public class Switch {
    public static void main(String[] args) {

        int number = 1;

        String day = "monday";
        /*
         FALL THROUGH
         */
        String result = switch(day.toUpperCase()){
            case "MONDAY" ->
                "today is monday";

            case "TUESDAY" ->
                "today is tuesday";

            case "WEDNESDAY" ->
                "today is wednesday";

            case "THURSDAY" ->
                "today is thursday";

            default ->
                " ";

        };
        System.out.println("value in result: " + result);

    }
}