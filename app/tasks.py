from datetime import datetime, timedelta

from models import Payment

PURCHASE_TIME_LIMIT = 60


def fill_file_with_hw():
    with open("file.txt", "w") as file:
        for line in range(1, 1001):
            file.write("Hello World\n")


def check_payment():
    new_payment_list = Payment.select().where(Payment.status == "new")

    for payment in new_payment_list:
        payment_lifetime = payment.date + timedelta(seconds=PURCHASE_TIME_LIMIT)
        print(payment_lifetime, payment.status)
        if payment_lifetime < datetime.now():
            payment.status = "not_paid"
            payment.save()


def issue_paid_item(payment_id):
    paid_payment = Payment.get_by_id(payment_id)
    paid_payment.is_issued = True
    paid_payment.save()


if __name__ == "__main__":
    fill_file_with_hw()
