class Operation:
    def __init__(
            self,
            pk: int,
            date: str,
            state: str,
            operation_amount: dict,
            description: str,
            from_: str,
            to: str
    ):
        self.pk = pk
        self.date = date
        self.state = state
        self.operation_amount = operation_amount
        self.description = description
        if from_:
            self.from_ = self.convert_payment(from_)
        else:
            self.from_ = ''
        self.to = self.convert_payment(to)

    def convert_payment(self, payment):
        """
        Функция принимает номер банковского счета и карты, и маскирует его.
        :param payment: from_, to
        :return: **XXXX, XXXX XX** **** XXXX
        """
        if payment.startswith('Счет'):
            payment = payment.split()
            number_bank_check = payment[-1]
            return f"{' '.join(payment[:-1])} **{number_bank_check[-4:]}"
        else:
            payment = payment.split()
            number_card = payment[-1]
            return f"{' '.join(payment[:-1])} {number_card[:4]} {number_card[4:6]}** **** {number_card[12:]}"
