package OldBugs;

import org.junit.Test;
import static org.junit.Assert.*;

class BankAccount {
    private double _balance;

    public BankAccount(double balance) {
        _balance = balance;
    }

    public void deposit(double value) {
        _balance += value;
    }

    public void withdraw(double value) {
        _balance -= value;
    }

    public double getBalance() {
        return _balance;
    }
}

public class BankAccountTest {
    @Test
    public void testDeposit() {
        BankAccount bankAccount = new BankAccount(0);
        bankAccount.deposit(100);
        assertTrue("Deposit value should be added to the balance", bankAccount.getBalance() == 100);
    }

    @Test
    public void testWithdraw() {
        BankAccount bankAccount = new BankAccount(100);
        bankAccount.withdraw(100);
        assertTrue("Withdraw value should be substracted from the balance", bankAccount.getBalance() == 0);
    }
}
