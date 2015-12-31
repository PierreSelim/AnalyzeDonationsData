# AnalyzeDonationsData
Code to analyze Fundraising data from CiviCRM

Usage
-----

```python
import analyzedonations as an

analyzer = an.DonationsAnalyzer.from_frcivicrm_dump("Recherche_de_contribution_CiviCRM-2014-2015.csv")

print "count: {0} sum: {1} mean: {2}".format(analyzer.count_contribution(),
                                             analyzer.sum_total_amount(),
                                             analyzer.mean_total_amount())
print "count {0} sum: {1} mean: {2}".format(analyzer.count_lastweek_contribution(),
                                             analyzer.sum_lastweek_total_amount(),
                                             analyzer.mean_last_week_total_amount())
```
