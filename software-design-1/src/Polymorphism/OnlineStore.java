package Polymorphism;

interface PaymentMethod {
    void processPayment(double amount);
}

class CreditCardPayment implements PaymentMethod {
    @Override
    public void processPayment(double amount) {
        System.out.println("Обработка платежа кредитной картой на сумму: $" + amount);
    }
}

class PayPalPayment implements PaymentMethod {
    @Override
    public void processPayment(double amount) {
        System.out.println("Обработка платежа через PayPal на сумму: $" + amount);
    }
}

class BitcoinPayment implements PaymentMethod {
    @Override
    public void processPayment(double amount) {
        System.out.println("Обработка платежа биткойнами на сумму: $" + amount);
    }
}

class OnlineStore {
    private PaymentMethod paymentMethod;

    public OnlineStore(PaymentMethod paymentMethod) {
        this.paymentMethod = paymentMethod;
    }

    public void process(double amount) {
        paymentMethod.processPayment(amount);
    }
}

class Main {
    public static void main(String[] args) {
        OnlineStore storeWithCreditCard = new OnlineStore(new CreditCardPayment());
        OnlineStore storeWithPayPal = new OnlineStore(new PayPalPayment());
        OnlineStore storeWithBitcoin = new OnlineStore(new BitcoinPayment());

        storeWithCreditCard.process(100.0);
        storeWithPayPal.process(200.0);
        storeWithBitcoin.process(300.0);
    }
}