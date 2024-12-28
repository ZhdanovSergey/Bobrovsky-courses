package DateTime;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.time.ZoneId;
import java.time.ZonedDateTime;

// Лично я не вижу в коде-примере никаких не зависящих от языка проблем.
// ChatGpt подсказал мне, что в примере используется старое апи,
// которое использует системный часовой пояс и не является потокобезопасным.

// Исправленный пример с использованием нового апи java.time
public class DateExample {
    public static void main(String[] args) {
        String dateString = "2024-05-13 14:30:00";
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        try {
            // Парсим строку в LocalDateTime
            LocalDateTime localDateTime = LocalDateTime.parse(dateString, formatter);

            // Если нужно, можно преобразовать в ZonedDateTime с указанием часового пояса
            ZonedDateTime zonedDateTime = localDateTime.atZone(ZoneId.systemDefault());

            System.out.println("ZonedDateTime: " + zonedDateTime);
        } catch (DateTimeParseException e) {
            System.err.println("Ошибка при парсинге даты: " + e.getMessage());
        }
    }
}
