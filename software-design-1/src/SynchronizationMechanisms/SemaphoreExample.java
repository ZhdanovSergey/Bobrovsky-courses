package SynchronizationMechanisms;

import java.util.concurrent.Semaphore;

// Использование Semaphore для управления доступом к принтеру

class Printer {
    private final Semaphore semaphore = new Semaphore(2); // Доступ только для 2 потоков

    public void printDocument(String document) {
        try {
            semaphore.acquire();
            System.out.printf("%s is printing document: %s%n", Thread.currentThread().getName(), document);
            Thread.sleep(2000); // Имитируем время печати
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            System.out.printf("%s has finished printing document: %s%n", Thread.currentThread().getName(), document);
            semaphore.release();
        }
    }
}

public class SemaphoreExample {
    public static void main(String[] args) {
        Printer printer = new Printer();
        for (int i = 1; i <= 5; i++) {
            String doc = "Document " + i;
            new Thread(() -> printer.printDocument(doc)).start();
        }
    }
}