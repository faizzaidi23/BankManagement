#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct BankAccount {
    int accountNumber;
    char accountHolder[50];
    float balance;
    struct BankAccount* next;
} BankAccount;

BankAccount* head = NULL;

void createAccount() {
    BankAccount* newAccount = (BankAccount*)malloc(sizeof(BankAccount));
    if (!newAccount) {
        printf("Memory allocation failed.\n");
        return;
    }

    printf("Enter Account Number: ");
    scanf("%d", &newAccount->accountNumber);

    printf("Enter Account Holder Name: ");
    scanf("%s", newAccount->accountHolder);

    printf("Enter Initial Balance: ");
    scanf("%f", &newAccount->balance);

    newAccount->next = head;
    head = newAccount;

    printf("Account created successfully.\n");
}

void displayAccounts() {
    if (!head) {
        printf("No accounts available.\n");
        return;
    }

    printf("\nList of Bank Accounts:\n");
    BankAccount* current = head;
    while (current) {
        printf("Account Number: %d\n", current->accountNumber);
        printf("Account Holder: %s\n", current->accountHolder);
        printf("Balance: %.2f\n\n", current->balance);
        current = current->next;
    }
}

void deposit() {
    int accountNumber;
    float amount;
    printf("Enter Account Number to deposit into: ");
    scanf("%d", &accountNumber);

    BankAccount* current = head;
    while (current) {
        if (current->accountNumber == accountNumber) {
            printf("Enter amount to deposit: ");
            scanf("%f", &amount);
            if (amount > 0) {
                current->balance += amount;
                printf("Deposit successful. New balance: %.2f\n", current->balance);
            } else {
                printf("Invalid deposit amount.\n");
            }
            return;
        }
        current = current->next;
    }
    printf("Account number not found.\n");
}

void withdraw() {
    int accountNumber;
    float amount;
    printf("Enter Account Number to withdraw from: ");
    scanf("%d", &accountNumber);

    BankAccount* current = head;
    while (current) {
        if (current->accountNumber == accountNumber) {
            printf("Enter amount to withdraw: ");
            scanf("%f", &amount);
            if (amount > 0 && amount <= current->balance) {
                current->balance -= amount;
                printf("Withdrawal successful. New balance: %.2f\n", current->balance);
            } else if (amount > current->balance) {
                printf("Insufficient balance.\n");
            } else {
                printf("Invalid withdrawal amount.\n");
            }
            return;
        }
        current = current->next;
    }
    printf("Account number not found.\n");
}

void freeAccounts() {
    BankAccount* current = head;
    while (current) {
        BankAccount* temp = current;
        current = current->next;
        free(temp);
    }
    head = NULL;
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
                freeAccounts();
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 5);

    return 0;
}
