package SynchronizationMechanisms;

import java.util.concurrent.CompletableFuture;

// Использование CompletableFuture для параллельной обработки нескольких шагов заказа и объединения результатов.

class Order {
    private final String orderId;

    public Order(String orderId) {
        this.orderId = orderId;
    }

    public String getOrderId() {
        return orderId;
    }
}

public class CompletableFutureExample {
    public static void main(String[] args) {
        Order order = new Order("12345");

        CompletableFuture<Void> orderProcessing = CompletableFuture.supplyAsync(() -> {
            // Имитируем проверку наличия товара
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                throw new IllegalStateException(e);
            }
            System.out.println("Checked inventory for order " + order.getOrderId());
            return true; // Предположим, что товар есть
        }).thenApply(inStock -> {
            if (inStock) {
                // Имитируем обработку платежа
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    throw new IllegalStateException(e);
                }
                System.out.println("Processed payment for order " + order.getOrderId());
                return true; // Платеж успешен
            } else {
                System.out.println("Order " + order.getOrderId() + " cannot be processed due to out of stock.");
                return false;
            }
        }).thenCompose(paymentSuccessful -> {
            if (paymentSuccessful) {
                // Имитируем доставку
                return CompletableFuture.supplyAsync(() -> {
                    try {
                        Thread.sleep(2000);
                    } catch (InterruptedException e) {
                        throw new IllegalStateException(e);
                    }
                    System.out.println("Order " + order.getOrderId() + " has been delivered.");
                    return true;
                });
            } else {
                return CompletableFuture.completedFuture(false);
            }
        }).thenAccept(deliverySuccessful -> {
            if (deliverySuccessful) {
                System.out.println("Order processing completed successfully.");
            } else {
                System.out.println("Order processing failed.");
            }
        });

        System.out.println("Order processing started...");
        orderProcessing.join(); // Блокируем выполнение до завершения обработки заказа
    }
}