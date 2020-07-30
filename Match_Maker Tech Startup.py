import numpy as np
import fetchmaker
from scipy.stats import binom_test
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from scipy.stats import chi2_contingency


print(np.mean(fetchmaker.get_tail_length('rottweiler')))
print(np.std(fetchmaker.get_tail_length('rottweiler')))






# Binomial Test

whippet_rescue = fetchmaker.get_is_rescue('whippet')
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)

pval_binom = binom_test( num_whippet_rescues, num_whippets, 0.08)
if pval_binom < 0.05:
  print('\nWhippets are significantly more likely to be rescue.')
elif pval_binom > 0.05:
  print('\nWhippets are significantly less likely to be rescue. Null hypothesis is True')

#### Whippets are significantly less likely to be rescue. Null hypothesis is True







# ANOVA Test

fstat, pval_anova = f_oneway((fetchmaker.get_weight("whippet")), (fetchmaker.get_weight("pitbull")), (fetchmaker.get_weight("terrier")))
if pval_anova < 0.05:
  print('\nThere is a significant difference in weights among these 3 Dogs. Lets proceed to Tukey\'s HSD')
elif pval_anova > 0.05:
  print('\nThese Dogs has no difference in weights. Just a random error.\n')

#### There is a significant difference in weights among these 3 Dogs. Lets proceed to Tukey's HSD






## Tukey's HSD

dogs = np.concatenate([(fetchmaker.get_weight("whippet")), (fetchmaker.get_weight("terrier")), (fetchmaker.get_weight("pitbull"))])

labels = ['whippet'] * len((fetchmaker.get_weight("whippet"))) + ['terrier'] * len((fetchmaker.get_weight("terrier"))) + ['pitbull'] * len((fetchmaker.get_weight("pitbull")))

sig_result = pairwise_tukeyhsd(dogs, labels, 0.05)
print(sig_result)

####  Pitbull, terrier Differ from each other
####  Pitbull, Whippet don't Differ from each other
####  Terrier, Whippet Differ from each other








# Chi2- Test

poodle_colors = fetchmaker.get_color("poodle") 
shihtzu_colors = fetchmaker.get_color("shihtzu") 

shitzu_brown = np.count_nonzero(shihtzu_colors == "brown" )
shitzu_black =np.count_nonzero(shihtzu_colors == "black" )
shitzu_gold =np.count_nonzero(shihtzu_colors == "gold" )
shitzu_grey =np.count_nonzero(shihtzu_colors == "grey" )
shitzu_white =np.count_nonzero(shihtzu_colors == "white" )


poodle_brown =np.count_nonzero(poodle_colors == "brown" )
poodle_black =np.count_nonzero(poodle_colors == "black" )
poodle_gold =np.count_nonzero(poodle_colors == "gold" )
poodle_grey =np.count_nonzero(poodle_colors == "grey" )
poodle_white =np.count_nonzero(poodle_colors == "white" )


color_table = [[poodle_black, shitzu_black],
               [poodle_brown, shitzu_brown],
               [poodle_gold, shitzu_gold],
               [poodle_grey, shitzu_grey],
               [poodle_white, shitzu_white]
               ]

chi2, pval_chi2, dof, expected = chi2_contingency(color_table)

print(pval_chi2)

#### 0.00530240829324

#### poodle"s and "shihtzu"s have significantly different color breakdowns.
