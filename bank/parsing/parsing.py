import bs4
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from abc import ABC, abstractmethod
from typing import List
from models.bank_data_models import Cards, Credits, Insurance, Deposits
from custom_errors.pars_errors import ParsErrors
from loggs.loggers import logger_done_pars


class ParsBank(ABC):

    @staticmethod
    def get_soup_by_url(url: str) -> bs4.BeautifulSoup:
        """
        :param url - link to the page
        :return: object of bs4.BeautifulSoup class
        """
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            page = driver.page_source
            soup = BeautifulSoup(page, 'lxml')
            return soup
        except Exception as e:
            ParsErrors.write_to_log(e=e, text='parsing.py ParsBank.get_url()')

    @staticmethod
    def get_data(soup: bs4.BeautifulSoup,  class_name: str, tag_name: str) -> List[str]:
        """
        get data from soup object
        :param soup: soup object
        :param class_name: name of class
        :param tag_name: tag name
        :return: list of data
        """
        try:
            return soup.find_all(tag_name, class_=class_name)
        except Exception as e:
            ParsErrors.write_to_log(e=e, text='parsing.py ParsBank.get_data()')

    @staticmethod
    @abstractmethod
    def get_cards() -> List[Cards]:
        """
        Get cards from bank
        :return: list of instances of Cards class
        """
        pass

    @staticmethod
    @abstractmethod
    def get_credits() -> List[Credits]:
        """
        Get credits from bank
        :return list of instances of Credits class
        """
        pass

    @staticmethod
    @abstractmethod
    def get_insurance() -> List[Insurance]:
        """
        Get insurance from bank
        :return list of instances of Insurance class
        """
        pass

    @staticmethod
    @abstractmethod
    def get_deposits() -> List[Deposits]:
        """
        Get deposits from bank
        :return list of instances of Deposits class
        """
        pass


class AlfaBank(ParsBank):

    @staticmethod
    def get_cards() -> List[Cards]:
        url = 'https://www.alfabank.by/cards/'
        soup = ParsBank.get_soup_by_url(url)
        links = ParsBank.get_data(
            soup=soup,
            class_name='link-more link-more--indent-left gtm_button_details_categories',
            tag_name='a'
                )
        links = list(map(lambda x: x.get('href'), links))
        cards = []
        for link in links:
            href = url[:-7] + link
            soup = ParsBank.get_soup_by_url(href)
            try:
                info = ParsBank.get_data(
                    soup=soup,
                    class_name='item-text',
                    tag_name='div'
                )
                info = list(map(lambda x: x.text.strip(), info))
                instance = Cards(
                    bank='AlfaBank',
                    name=soup.find('h1', class_='page-top-section__title h0').text,
                    info=' '.join(info),
                    link=link,
                )
                logger_done_pars.info(f'AlfaBank.get_cards() - {instance.name}')
                cards.append(instance)
            except Exception as e:
                ParsErrors.write_to_log(e=e, text='parsing.py AlfaBank.get_cards()')
        return cards

    @staticmethod
    def get_credits() -> List[Credits]:
        url = 'https://www.alfabank.by/credits/'
        soup = ParsBank.get_soup_by_url(url)
        links = ParsBank.get_data(
            soup=soup,
            class_name='link-more link-more--indent-left gtm_button_details_categories',
            tag_name='a',
        )
        links = list(map(lambda x: x.get('href'), links))
        credit = []
        for link in links:
            href = url[:-9] + link
            soup = ParsBank.get_soup_by_url(href)
            try:
                info = ParsBank.get_data(
                    soup=soup,
                    class_name='benefits-secondary__text',
                    tag_name='div'
                )
                info = list(map(lambda x: x.text.strip(), info))
                instance = Credits(
                    bank='AlfaBank',
                    name=soup.find('h1', class_='page-top-section__title h0').text,
                    info=' '.join(info),
                    link=link,
                )
                credit.append(instance)
                logger_done_pars.info(f'AlfaBank.get_credits() - {instance.name}')
            except Exception as e:
                ParsErrors.write_to_log(e=e, text='parsing.py AlfaBank.get_credits()')
        return credit

    @staticmethod
    def get_insurance() -> List[Insurance]:
        url = 'https://www.alfabank.by/insurance/'
        soup = ParsBank.get_soup_by_url(url)
        links = ParsBank.get_data(
            soup=soup,
            class_name='link-more link-more--indent-left gtm_button_details_categories',
            tag_name='a',
        )
        links = list(map(lambda x: x.get('href'), links))
        insurance = []
        for link in links:
            href = url[:-11] + link
            soup = ParsBank.get_soup_by_url(href)
            try:
                info = ParsBank.get_data(
                    soup=soup,
                    class_name='item-text',
                    tag_name='div'
                )
                info1 = list(map(lambda x: x.text.strip(), info[:4]))
                for i in info[4:len(info)-6]:
                    buf_soup = BeautifulSoup(str(i), 'lxml')
                    info1.append(buf_soup.div.p.get_text(strip=True))
                info = info1
                instance = Insurance(
                    bank='AlfaBank',
                    name=soup.find('h1', class_='page-top-section__title h0').text,
                    info=' '.join(info),
                    link=link,
                    )
                insurance.append(instance)
                logger_done_pars.info(f'AlfaBank.get_insurance() - {instance.name}')
            except Exception as e:
                ParsErrors.write_to_log(e=e, text='parsing.py AlfaBank.get_insurance()')
        return insurance

    @staticmethod
    def get_deposits() -> List[Deposits]:
        url = 'https://www.alfabank.by/deposits/'
        soup = ParsBank.get_soup_by_url(url)
        links = ParsBank.get_data(
            soup=soup,
            class_name='link-more link-more--indent-left gtm_button_details_categories',
            tag_name='a',
        )
        links = list(map(lambda x: x.get('href'), links))
        deposits = []
        for link in links:
            href = url[:-10] + link
            soup = ParsBank.get_soup_by_url(href)
            try:
                info = ParsBank.get_data(
                    soup=soup,
                    class_name='benefits-secondary__text',
                    tag_name='div'
                )
                info = list(map(lambda x: x.text.strip(), info))
                instance = Deposits(
                    bank='AlfaBank',
                    name=soup.find('h1', class_='page-top-section__title h0').text,
                    info=' '.join(info),
                    link=link,
                )
                deposits.append(instance)
                logger_done_pars.info(f'AlfaBank.get_deposits() - {instance.name}')
            except Exception as e:
                ParsErrors.write_to_log(e=e, text='parsing.py AlfaBank.get_deposits()')
        return deposits


a = AlfaBank.get_deposits()
print(len(a))
