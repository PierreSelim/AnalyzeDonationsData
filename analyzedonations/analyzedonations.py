# -*- coding: utf-8 -*-
"""Analyze donation module."""

import pandas as pd
import datetime as dt

FR_TRANSLATIONS = {
    u'Statut de la contribution': 'contribution_status',
    u'Titre de la campagne': 'campaign_title',
    u'Identifiant de la campagne': 'compaign_id',
    u'Origine de la contribution': 'contribution_origin',
    u'Mode de paiement': 'payment_mode',
    u'Montant des frais': 'tax_amount',
    u'Montant net': 'net_amonunt',
    u'Montant total': 'total_amount',
    u'Identifiant de contribution': 'contribution_id'
}


class DonationsAnalyzer(object):
    """Donations Analzer."""

    def __init__(self, dataframe):
        """Constructor.

        Args:
            dataframe (pd.core.DataFrame): dataframe to analyze.
        """
        self.dataframe = dataframe
        self.year = dataframe.index[0].year
        # last week of december
        dec_25 = dt.datetime(self.year, 12, 25)
        jan_1 = dt.datetime(self.year + 1, 1, 1)
        start_lastweek = self.dataframe.index.searchsorted(dec_25)
        end_lastweek = self.dataframe.index.searchsorted(jan_1)
        self.last_week = dataframe.ix[start_lastweek:end_lastweek]

    @classmethod
    def from_frcivicrm_dump(cls, filename):
        """DonationsAnalyzer from a dump of CiviCRM"""
        data_frame = pd.read_csv(filename,
                                 parse_dates=['Date de réception'],
                                 dayfirst=True,
                                 index_col=['Date de réception'])
        data_frame.rename(columns=FR_TRANSLATIONS, inplace=True)
        data_frame.rename(index={'Date de réception': 'receive_date'},
                          inplace=True)
        return cls(data_frame)

    @staticmethod
    def __count_contribution__(dataframe):
        """Count contribution on a given dataframe"""
        return dataframe['contribution_id'].count()

    @staticmethod
    def __sum_total_amount__(dataframe):
        """Sum of total amount for each contribution"""
        return dataframe['total_amount'].sum()

    @staticmethod
    def __mean_total_amount__(dataframe):
        """Mean of total amount"""
        return dataframe['total_amount'].mean()

    def count_contribution(self):
        """Count of the contributions"""
        return DonationsAnalyzer.__count_contribution__(self.dataframe)

    def sum_total_amount(self):
        """Sum of the total amount of each contribution"""
        return DonationsAnalyzer.__sum_total_amount__(self.dataframe)

    def mean_total_amount(self):
        """Mean of the total amount of each contribution"""
        return DonationsAnalyzer.__mean_total_amount__(self.dataframe)

    def count_lastweek_contribution(self):
        """Count contributions made between Dec 25th and Dec 31st (included)"""
        return DonationsAnalyzer.__count_contribution__(self.last_week)

    def sum_lastweek_total_amount(self):
        """Sum of total amount between Dec 25th and Dec 31st (included)"""
        return DonationsAnalyzer.__sum_total_amount__(self.last_week)

    def mean_last_week_total_amount(self):
        """Mean of total amount between Dec 25th and Dec 31st (included)"""
        return DonationsAnalyzer.__mean_total_amount__(self.last_week)
