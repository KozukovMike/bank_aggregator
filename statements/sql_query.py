sql_bank = """
    SELECT * 
    FROM bank;
"""

sql_deposit = """
    SELECT deposit.name, info, link, deposit.id, bank_id,  bank.name AS bank_name
    FROM deposit INNER JOIN bank 
    ON deposit.bank_id = bank.id;
    """

sql_card = """
    SELECT card.name, info, link, card.id, bank_id, bank.name AS bank_name
    FROM card INNER JOIN bank
    ON card.bank_id = bank.id;
    """

sql_credit = """
    SELECT credit.name, info, link, credit.id, bank_id, bank.name AS bank_name
    FROM credit INNER JOIN bank
    ON credit.bank_id = bank.id;
    """

sql_insurance = """
    SELECT insurance.name, info, link, insurance.id, bank_id, bank.name AS bank_name
    FROM insurance INNER JOIN bank
    ON insurance.bank_id = bank.id;
    """