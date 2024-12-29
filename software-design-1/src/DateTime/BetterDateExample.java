package DateTime;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class BetterDateExample {
    public static void main(String[] args) {
        String dateString = "2024-05-13T14:30:00";
        DateTimeFormatter formatter = DateTimeFormatter.ISO_LOCAL_DATE_TIME;
        LocalDateTime date = LocalDateTime.parse(dateString, formatter);
        System.out.println("Date: " + date);
    }
}