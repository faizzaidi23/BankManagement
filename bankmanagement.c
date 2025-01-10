#include <stdio.h>
#include <string.h>

#define MAX_ACCOUNTS 100

typedef struct {
    int accountNumber;
    char accountHolder[50];
    float balance;
} BankAccount;

BankAccount accounts[MAX_ACCOUNTS];
int accountCount = 0;

void createAccount() {
    if (accountCount < MAX_ACCOUNTS) {
        printf("Enter Account Number: ");
        scanf("%d", &accounts[accountCount].accountNumber);
        
        printf("Enter Account Holder Name: ");
        scanf("%s", accounts[accountCount].accountHolder);
        
        printf("Enter Initial Balance: ");
        scanf("%f", &accounts[accountCount].balance);
        
        printf("Account created successfully.\n");
        accountCount++;
    } else {
        printf("Account limit reached. Cannot create new account.\n");
    }
}

void displayAccounts() {
    if (accountCount == 0) {
        printf("No accounts available.\n");
    } else {
        printf("\nList of Bank Accounts:\n");
        for (int i = 0; i < accountCount; i++) {
            printf("Account Number: %d\n", accounts[i].accountNumber);
            printf("Account Holder: %s\n", accounts[i].accountHolder);
            printf("Balance: %.2f\n\n", accounts[i].balance);
        }
    }
}

void deposit() {
    int accountNumber;
    float amount;
    printf("Enter Account Number to deposit into: ");
    scanf("%d", &accountNumber);

    for (int i = 0; i < accountCount; i++) {
        if (accounts[i].accountNumber == accountNumber) {
            printf("Enter amount to deposit: ");
            scanf("%f", &amount);
            if (amount > 0) {
                accounts[i].balance += amount;
                printf("Deposit successful. New balance: %.2f\n", accounts[i].balance);
            } else {
                printf("Invalid deposit amount.\n");
            }
            return;
        }
    }
    printf("Account number not found.\n");
}

void withdraw() {
    int accountNumber;
    float amount;
    printf("Enter Account Number to withdraw from: ");
    scanf("%d", &accountNumber);

    for (int i = 0; i < accountCount; i++) {
        if (accounts[i].accountNumber == accountNumber) {
            printf("Enter amount to withdraw: ");
            scanf("%f", &amount);
            if (amount > 0 && amount <= accounts[i].balance) {
                accounts[i].balance -= amount;
                printf("Withdrawal successful. New balance: %.2f\n", accounts[i].balance);
            } else if (amount > accounts[i].balance) {
                printf("Insufficient balance.\n");
            } else {
                printf("Invalid withdrawal amount.\n");
            }
            return;
        }
    }
    printf("Account number not found.\n");
}

int main() {
    int choice;
    do {
        printf("\nBank Management System\n");
        printf("1. Create Account\n");
        printf("2. Display All Accounts\n");
        printf("3. Deposit Money\n");
        printf("4. Withdraw Money\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                createAccount();
                break;
            case 2:
                displayAccounts();
                break;
            case 3:
                deposit();
                break;
            case 4:
                withdraw();
                break;
            case 5:
                printf("Exiting... Thank you for using the bank management system.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 5);

    return 0;
}
