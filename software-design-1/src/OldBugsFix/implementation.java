package OldBugsFix;

import javax.xml.bind.ValidationException;

class BankAccount {
    private double _balance;

    public BankAccount(double balance) throws ValidationException {
        if (balance < 0) {
            throw new ValidationException("Initial balance could not be negative");
        }

        _balance = balance;
    }

    public void deposit(double value) throws ValidationException {
        if (value < 0) {
            throw new ValidationException("Deposit value could not be negative");
        }

        _balance += value;
    }

    public void withdraw(double value) throws Exception {
        if (value < 0) {
            throw new ValidationException("Withdraw value could not be negative");
        }

        if (value > _balance) {
            throw new Exception("Withdraw value could not be more than current balance");
        }

        _balance -= value;
    }

    public double getBalance() {
        return _balance;
    }
}
